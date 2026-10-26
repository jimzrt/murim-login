#!/usr/bin/env python3
"""Entity consistency pass over a range of finalized chapters.

Workers run the detector, escalation, apply, and QA for different chapters in
parallel. Git commits `Entity Chapter N` one chapter at a time. A failed
chapter stays uncommitted and the others continue.

    python tools/run_entity_pass.py 1 1191 --workers 3
    python tools/run_entity_pass.py 1 1191 --dry-run      # packets + prefilter, no model calls
    python tools/run_entity_pass.py 1 1191 --estimate     # cost/time from packet sizes
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from run_lock import (
    ADDRESS_LOCK_NAME,
    ENTITY_LOCK_ENV,
    FINAL_LOCK_NAME,
    LOCK_NAME,
    LOCK_LABELS,
    hold_commit_lock,
    hold_entity_lock,
    lock_is_live,
)
from run_next import changed_paths, commit_paths, git

try:
    from tools.entity_pass import (
        DRY_ROOT,
        dry_run_chapter,
        entity_owns_path,
        estimate,
        final_promoted,
        foreign_entity_paths,
        load_config,
        load_state,
        save_state,
        summary_markdown,
    )
    from tools.workflow import is_harness_artifact
except ModuleNotFoundError:
    from entity_pass import (
        DRY_ROOT,
        dry_run_chapter,
        entity_owns_path,
        estimate,
        final_promoted,
        foreign_entity_paths,
        load_config,
        load_state,
        save_state,
        summary_markdown,
    )
    from workflow import is_harness_artifact

BLOCKING_LOCKS = (FINAL_LOCK_NAME, LOCK_NAME, ADDRESS_LOCK_NAME)


def refuse_live_locks(root: Path = ROOT) -> None:
    live = [LOCK_LABELS[name] for name in BLOCKING_LOCKS if lock_is_live(root, name)]
    if live:
        raise SystemExit(
            "entity pass refuses to run while these locks are live: " + ", ".join(live)
            + ". Wait for them to finish (python tools/run_lock.py)."
        )


def entity_done(number: int, dirty: set[str]) -> bool:
    if load_state(number).get("stage") != "COMMITTED":
        return False
    return not any(entity_owns_path(path, number) for path in dirty)


def final_clean(number: int, dirty: set[str]) -> bool:
    if not final_promoted(number):
        return False
    prefix = f"reviews/final/{number:04d}/"
    return not any(path.startswith(prefix) for path in dirty)


def select_chapters(start: int, end: int, dirty: list[str] | None = None) -> tuple[list[int], list[str]]:
    if start < 0 or end < start:
        raise SystemExit("range must satisfy 0 <= START <= END")
    dirty_set = set(dirty or [])
    chosen: list[int] = []
    notes: list[str] = []
    for number in range(start, end + 1):
        if not (ROOT / "translations" / f"{number:04d}.md").is_file():
            notes.append(f"chapter {number}: no translation")
            continue
        if entity_done(number, dirty_set):
            continue
        if not final_clean(number, dirty_set):
            notes.append(f"chapter {number}: final touches not PROMOTED")
            continue
        chosen.append(number)
    return chosen, notes


def allowed_paths(number: int, dirty: list[str]) -> set[str]:
    return {path for path in dirty if entity_owns_path(path, number)}


def unexpected_paths(number: int, dirty: list[str]) -> list[str]:
    """Harness paths that are neither this chapter's nor owned by another queue."""
    try:
        from tools.final_touches import foreign_final_paths
        from tools.run_next import foreign_master_paths
    except ModuleNotFoundError:
        from final_touches import foreign_final_paths
        from run_next import foreign_master_paths
    allowed = allowed_paths(number, dirty)
    foreign = foreign_master_paths(dirty) | foreign_final_paths(dirty) | foreign_entity_paths(dirty)
    foreign.difference_update(allowed)
    return [
        path for path in dirty
        if path not in allowed and path not in foreign and is_harness_artifact(path)
    ]


def commit_entity(number: int, *, holder: str = "run_entity_pass") -> None:
    state = load_state(number)
    if state.get("stage") not in {"READY_TO_COMMIT", "COMMITTED"}:
        raise SystemExit(f"entity pass stopped at {state.get('stage')}; expected READY_TO_COMMIT")
    dirty = changed_paths()
    unexpected = unexpected_paths(number, dirty)
    if unexpected:
        raise SystemExit("refusing to commit unexpected paths: " + ", ".join(unexpected))
    if state.get("stage") != "COMMITTED":
        save_state(number, stage="COMMITTED")
        dirty = changed_paths()
    ours = sorted(allowed_paths(number, dirty))
    if not ours:
        print(f"Chapter {number}  entity: already recorded", flush=True)
        return
    with hold_commit_lock(ROOT, holder=holder, chapter=number, stage="committing"):
        commit_paths(ours, f"Entity Chapter {number}")
    applied = (state.get("counts") or {}).get("auto", 0)
    print(f"Chapter {number}  entity committed ({len(ours)} files, {applied} applied)", flush=True)


def run_chapter(number: int) -> int:
    command = [sys.executable, str(ROOT / "tools" / "entity_pass.py"), "run", str(number)]
    env = os.environ.copy()
    env[ENTITY_LOCK_ENV] = str(os.getpid())
    return subprocess.run(command, cwd=ROOT, env=env).returncode


def dry_run(chapters: list[int], workers: int, out: Path | None) -> dict:
    cfg = load_config()
    records = [dry_run_chapter(number, cfg) for number in chapters]
    est = estimate(records, cfg, workers)
    summary = summary_markdown(records, est)
    target = out or DRY_ROOT
    target.mkdir(parents=True, exist_ok=True)
    (target / "summary.md").write_text(summary, encoding="utf-8")
    (target / "summary.json").write_text(
        json.dumps({"estimate": est, "chapters": records}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(summary, end="", flush=True)
    print(f"\nPackets and prefilter reports: {DRY_ROOT}\nSummary: {target / 'summary.md'}", flush=True)
    return est


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("start", type=int)
    parser.add_argument("end", nargs="?", type=int, help="defaults to start")
    parser.add_argument("--workers", type=int, default=None,
                        help="parallel chapters (default: docs/entity.json batch_workers)")
    parser.add_argument("--dry-run", action="store_true",
                        help="build packets and prefilter reports for every chapter in range; no model calls")
    parser.add_argument("--estimate", action="store_true", help="same as --dry-run; prints the cost/time estimate")
    parser.add_argument("--summary-dir", type=Path, help="where --dry-run writes summary.md/json")
    parser.add_argument("--no-commit", action="store_true", help="edit and QA, but leave chapters uncommitted")
    args = parser.parse_args()
    end = args.start if args.end is None else args.end
    cfg = load_config()
    workers = cfg["batch_workers"] if args.workers is None else max(1, args.workers)

    if args.dry_run or args.estimate:
        if end < args.start:
            raise SystemExit("end chapter is before the start chapter")
        chapters = [n for n in range(args.start, end + 1) if (ROOT / "translations" / f"{n:04d}.md").is_file()]
        dry_run(chapters, workers, args.summary_dir)
        return 0

    refuse_live_locks()
    git("rev-parse", "--verify", "HEAD")
    chapters, notes = select_chapters(args.start, end, changed_paths())
    for note in notes:
        print(note, flush=True)
    if not chapters:
        print(f"Nothing to check in chapters {args.start}–{end}.", flush=True)
        return 0
    stray = [path for number in chapters for path in unexpected_paths(number, changed_paths())
             if not path.startswith("reviews/entity/")]
    if stray:
        raise SystemExit("working tree has unexpected changes: " + ", ".join(sorted(set(stray))))
    print(f"Entity pass {chapters[0]}–{chapters[-1]}: {len(chapters)} chapters, {workers} workers", flush=True)

    failures: list[int] = []
    committed: list[int] = []
    commit_gate = threading.Lock()

    def finish(number: int) -> None:
        code = run_chapter(number)
        if code:
            print(f"Chapter {number} entity pass failed with exit code {code}", flush=True)
            failures.append(number)
            return
        if args.no_commit:
            return
        with commit_gate:
            try:
                commit_entity(number)
            except SystemExit as exc:
                print(f"Chapter {number} commit failed: {exc}", flush=True)
                failures.append(number)
                return
        committed.append(number)

    with hold_entity_lock(ROOT, holder="run_entity_pass", chapter=chapters[0], stage="starting", until=end) as lock:
        lock.update(stage=f"batch:{len(chapters)}")
        with ThreadPoolExecutor(max_workers=min(workers, len(chapters))) as pool:
            for future in as_completed([pool.submit(finish, number) for number in chapters]):
                future.result()
        lock.update(stage="finished" if not failures else "finished-with-failures")

    print(f"Committed {len(committed)}; {len(failures)} failed", flush=True)
    print(f"Human review: python tools/entity_pass.py report {args.start} {end}", flush=True)
    if failures:
        print("Failed chapters: " + ", ".join(str(n) for n in sorted(failures)), flush=True)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
