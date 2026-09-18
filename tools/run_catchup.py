#!/usr/bin/env python3
"""One-shot quality catch-up: reset, audit 9-63, remaster 2-63 and 162-179.

When this finishes, resume the normal FIFOs:

    python tools/run_next.py
    python tools/run_next_mastering.py

Translation should continue from docs/STATE.md. Mastering should next pick 180
after chapters 1 and 64 are registered and 2-63 plus 162-179 are remastered.

Two remaster lanes run in parallel (2-63 and 162-179). Each lane is sequential
so prior-chapter mastered tails stay in the continuity packet. Git commits take
commit.lock and only stage that chapter's mastering paths.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from run_lock import hold_audit_locks, hold_commit_lock, hold_master_lock
from run_next import changed_paths, git
from run_next_mastering import next_mastering_chapter

try:
    from tools.mastering import command_reset_for_remaster, load_config, state_for
    from tools.workflow import (
        command_committed,
        command_master,
        incomplete_chapter,
        is_harness_artifact,
        master_allowed_paths,
        master_owns_path,
        paths,
    )
except ModuleNotFoundError:
    from mastering import command_reset_for_remaster, load_config, state_for
    from workflow import (
        command_committed,
        command_master,
        incomplete_chapter,
        is_harness_artifact,
        master_allowed_paths,
        master_owns_path,
        paths,
    )

KEEP_LIVE = list(range(2, 9))
AUDIT_START = 9
AUDIT_END = 63
AUDIT_CHAPTERS = list(range(AUDIT_START, AUDIT_END + 1))
FULL_RESET = list(range(9, 64)) + list(range(162, 180))
LANE_A = list(range(2, 64))
LANE_B = list(range(162, 180))
REGISTER_ONLY = [1, 64]
REMASTER = LANE_A + LANE_B
CATCHUP_CHAPTERS = sorted(set(KEEP_LIVE + FULL_RESET + REGISTER_ONLY))
PHASES = ("reset", "audit", "snapshot", "remaster", "register", "verify")
PROGRESS_PATH = ROOT / ".work" / "catchup.json"
FINISH_LOCK = threading.Lock()


def atomic_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    tmp = path.with_suffix(".json.tmp")
    tmp.write_text(text, encoding="utf-8")
    tmp.replace(path)


def load_progress() -> dict:
    if not PROGRESS_PATH.exists():
        return {
            "version": 1,
            "phase": "reset",
            "completed": [],
            "registered": [],
            "audit_committed": False,
        }
    value = json.loads(PROGRESS_PATH.read_text(encoding="utf-8"))
    value.setdefault("completed", [])
    value.setdefault("registered", [])
    value.setdefault("audit_committed", False)
    value.setdefault("phase", "reset")
    return value


def save_progress(progress: dict) -> None:
    atomic_json(PROGRESS_PATH, progress)


def catchup_owns_path(path: str, chapters: list[int] | None = None) -> bool:
    chapters = chapters if chapters is not None else CATCHUP_CHAPTERS
    if path.startswith("reviews/retrofit/"):
        return True
    return any(master_owns_path(path, number) for number in chapters)


def default_retries() -> int:
    return max(0, int(load_config().get("run_until_mastering_retries", 2)))


def default_retry_delay() -> float:
    return max(0.0, float(load_config().get("run_until_mastering_retry_delay_seconds", 30)))


def python_tool(*args: str) -> None:
    result = subprocess.run([sys.executable, str(ROOT / "tools" / args[0]), *args[1:]], cwd=ROOT)
    if result.returncode:
        raise SystemExit(f"{' '.join(args)} failed with exit code {result.returncode}")


def require_catchup_tree(chapters: list[int], *, resume: bool) -> None:
    try:
        git("rev-parse", "--verify", "HEAD")
        dirty = changed_paths()
    except subprocess.CalledProcessError as error:
        raise SystemExit(error.stderr.strip() or "project must be an initialized Git repository") from None
    in_flight = incomplete_chapter()
    if in_flight is not None:
        raise SystemExit(
            f"chapter {in_flight} has an in-flight translation transaction; "
            "finish or stop it before catch-up"
        )
    harness = [path for path in dirty if is_harness_artifact(path)]
    unexpected = [path for path in harness if not catchup_owns_path(path, chapters)]
    if unexpected:
        raise SystemExit("working tree has unexpected changes: " + ", ".join(unexpected))
    if not resume and harness:
        raise SystemExit(
            "working tree must be clean before catch-up; commit or stash existing changes"
        )


def next_state_chapter() -> int:
    try:
        from tools.run_next import next_chapter
    except ModuleNotFoundError:
        from run_next import next_chapter
    return next_chapter()


def phase_index(name: str) -> int:
    if name not in PHASES:
        raise SystemExit(f"unknown phase {name}; choose from {', '.join(PHASES)}")
    return PHASES.index(name)


def should_run(current: str, start: str) -> bool:
    return phase_index(current) >= phase_index(start)


def reset_chapters(*, dry_run: bool) -> None:
    print(f"Reset keep-live {KEEP_LIVE[0]}-{KEEP_LIVE[-1]}", flush=True)
    print(f"Reset restore {FULL_RESET[0]}-63 and 162-179", flush=True)
    if dry_run:
        return
    for number in KEEP_LIVE:
        command_reset_for_remaster(number, keep_translation=True)
    for number in FULL_RESET:
        command_reset_for_remaster(number, keep_translation=False)


def classify_audit_paths(dirty: list[str]) -> tuple[list[str], list[str]]:
    """Commit only 9-63 audit files; ignore other catch-up dirt; reject foreign harness files."""
    allowed: list[str] = []
    unexpected: list[str] = []
    for path in dirty:
        if not is_harness_artifact(path):
            continue
        if catchup_owns_path(path, AUDIT_CHAPTERS):
            allowed.append(path)
        elif catchup_owns_path(path):
            continue
        else:
            unexpected.append(path)
    return allowed, unexpected


def audit_verified() -> bool:
    path = ROOT / "reviews" / "retrofit" / f"{AUDIT_START:04d}-{AUDIT_END:04d}" / "state.json"
    if not path.exists():
        return False
    try:
        return json.loads(path.read_text(encoding="utf-8")).get("stage") == "VERIFIED"
    except (OSError, json.JSONDecodeError):
        return False


def audit_range(jobs: int, *, dry_run: bool) -> None:
    if dry_run:
        print(f"would audit chapters {AUDIT_START}-{AUDIT_END} with {jobs} jobs", flush=True)
        return
    if audit_verified():
        print(f"Audit {AUDIT_START}-{AUDIT_END} already VERIFIED", flush=True)
        return
    args = ["audit_range.py", "run", str(AUDIT_START), str(AUDIT_END), "--jobs", str(jobs)]
    with hold_audit_locks(ROOT, holder="run_catchup", chapter=AUDIT_START, stage="audit"):
        python_tool(*args)


def commit_audit(*, dry_run: bool) -> None:
    allowed, unexpected = classify_audit_paths(changed_paths())
    if unexpected:
        raise SystemExit("refusing to commit unexpected audit paths: " + ", ".join(unexpected))
    if dry_run:
        print(f"would commit audit ({len(allowed)} files)", flush=True)
        return
    if not allowed:
        print("Audit produced no file changes", flush=True)
        return
    with hold_commit_lock(ROOT, holder="run_catchup", chapter=AUDIT_START, stage="audit-commit"):
        git("add", "--", *allowed)
        git("commit", "-m", f"Audit chapters {AUDIT_START}-{AUDIT_END}", "--", *allowed, capture=False)
    print(f"Committed audit chapters {AUDIT_START}-{AUDIT_END}", flush=True)


def snapshot_audited(*, dry_run: bool) -> None:
    print(f"Re-snapshot audited chapters {AUDIT_START}-{AUDIT_END}", flush=True)
    if dry_run:
        return
    for number in range(AUDIT_START, AUDIT_END + 1):
        command_reset_for_remaster(number, keep_translation=True)


def primary_stage(number: int) -> str | None:
    state_path = paths(number)["state"]
    if not state_path.exists():
        return None
    try:
        return json.loads(state_path.read_text(encoding="utf-8")).get("stage")
    except (OSError, json.JSONDecodeError):
        return None


def commit_mastered_chapter(chapter: int, *, allow_empty: bool = False) -> None:
    transaction = json.loads(paths(chapter)["state"].read_text(encoding="utf-8"))
    if transaction.get("stage") != "MASTERED":
        raise SystemExit(f"workflow stopped at {transaction.get('stage')}; expected MASTERED")
    dirty = changed_paths()
    allowed = master_allowed_paths(chapter, dirty)
    unexpected = [
        path for path in dirty
        if is_harness_artifact(path) and not catchup_owns_path(path)
    ]
    if unexpected:
        raise SystemExit("refusing to commit unexpected paths: " + ", ".join(unexpected))
    ours = [path for path in dirty if path in allowed]
    with hold_commit_lock(ROOT, holder="run_catchup", chapter=chapter, stage="committing"):
        if ours:
            print(f"  ✓ commit     {len(ours)} files", flush=True)
            git("add", "--", *ours)
            git("commit", "-m", f"Master Chapter {chapter}", "--", *ours, capture=False)
        elif allow_empty:
            git("commit", "--allow-empty", "-m", f"Master Chapter {chapter}", capture=False)
            print("  ✓ commit     empty register", flush=True)
        elif git("log", "-1", "--pretty=%s") == f"Master Chapter {chapter}":
            print("  ✓ commit     already recorded", flush=True)
        else:
            raise SystemExit("workflow reached MASTERED without checkpointable changes")
        command_committed(chapter, "HEAD")
    print(f"Chapter {chapter}  mastered", flush=True)


def remaster_one(chapter: int, retries: int, delay: float) -> None:
    stage = primary_stage(chapter)
    if stage == "MASTERED_COMMITTED":
        return
    if stage == "MASTERED":
        with FINISH_LOCK:
            commit_mastered_chapter(chapter)
        return
    attempts = 1 + max(0, retries)
    last_error: BaseException | None = None
    for attempt in range(1, attempts + 1):
        try:
            if primary_stage(chapter) != "MASTERED":
                python_tool("mastering.py", "run", str(chapter))
            with FINISH_LOCK:
                if primary_stage(chapter) != "MASTERED":
                    command_master(chapter)
                commit_mastered_chapter(chapter)
            return
        except (SystemExit, subprocess.CalledProcessError) as error:
            last_error = error
            if attempt == attempts:
                break
            print(
                f"Chapter {chapter} remaster failed; retry {attempt}/{retries} after {delay:g}s",
                flush=True,
            )
            if delay > 0:
                time.sleep(delay)
    raise SystemExit(f"chapter {chapter} remaster failed: {last_error}")


def remaster_lane(name: str, chapters: list[int], progress: dict, retries: int, delay: float, *, dry_run: bool) -> list[int]:
    done = set(progress.get("completed") or [])
    remaining = [number for number in chapters if number not in done]
    print(f"{name}: {len(remaining)} chapter(s) {remaining[0] if remaining else '—'}–{remaining[-1] if remaining else '—'}", flush=True)
    if dry_run:
        for number in remaining:
            print(f"  would remaster {number}", flush=True)
        return []
    finished: list[int] = []
    for number in remaining:
        if primary_stage(number) == "MASTERED_COMMITTED":
            print(f"Chapter {number} already MASTERED_COMMITTED; skipping", flush=True)
        else:
            print(f"\n=== Remaster Chapter {number} ({name}) ===", flush=True)
            remaster_one(number, retries, delay)
        finished.append(number)
        with FINISH_LOCK:
            current = load_progress()
            completed = list(dict.fromkeys([*current.get("completed", []), number]))
            current["completed"] = completed
            current["phase"] = "remaster"
            save_progress(current)
    return finished


def register_existing(number: int, *, dry_run: bool) -> None:
    stage = primary_stage(number)
    if stage == "MASTERED_COMMITTED":
        print(f"Chapter {number} already MASTERED_COMMITTED", flush=True)
        return
    overlay = state_for(number)
    if overlay.get("stage") != "PROMOTED" or not overlay.get("qa_passed"):
        raise SystemExit(f"chapter {number}: register-only requires a PROMOTED overlay")
    print(f"Register existing master for chapter {number}", flush=True)
    if dry_run:
        return
    command_master(number)
    commit_mastered_chapter(number, allow_empty=True)


def verify_heads() -> None:
    translation_next = next_state_chapter()
    mastering_next = next_mastering_chapter()
    print(f"Next translation chapter (STATE.md): {translation_next}", flush=True)
    print(f"Next mastering FIFO chapter: {mastering_next}", flush=True)
    if mastering_next != 180:
        raise SystemExit(f"expected next mastering chapter 180, got {mastering_next}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--jobs", type=int, default=4, help="parallel audit block reviews")
    parser.add_argument("--lane-workers", type=int, default=2, help="1=serial lanes, 2=parallel 2-63 and 162-179")
    parser.add_argument("--from-phase", choices=PHASES, help="start at this phase (default: resume)")
    parser.add_argument(
        "--retries",
        type=int,
        default=None,
        help="extra remaster attempts per chapter after the first failure",
    )
    parser.add_argument("--retry-delay", type=float, default=None)
    args = parser.parse_args()
    retries = default_retries() if args.retries is None else max(0, args.retries)
    delay = default_retry_delay() if args.retry_delay is None else max(0.0, args.retry_delay)
    progress = load_progress()
    if progress.get("phase") == "done" and not args.from_phase:
        verify_heads()
        print("Catch-up already complete.", flush=True)
        return 0
    start = args.from_phase or progress.get("phase") or "reset"
    resume = PROGRESS_PATH.exists() or bool(progress.get("completed"))
    require_catchup_tree(CATCHUP_CHAPTERS, resume=resume or args.dry_run)
    workers = 1 if args.lane_workers < 2 else 2
    print(
        f"Catch-up from phase {start}; audit jobs={max(1, args.jobs)}; "
        f"lane workers={workers}",
        flush=True,
    )
    if args.dry_run:
        if should_run("reset", start):
            reset_chapters(dry_run=True)
        if should_run("audit", start):
            audit_range(max(1, args.jobs), dry_run=True)
            commit_audit(dry_run=True)
        if should_run("snapshot", start):
            snapshot_audited(dry_run=True)
        if should_run("remaster", start):
            remaster_lane("lane-a", LANE_A, progress, retries, delay, dry_run=True)
            remaster_lane("lane-b", LANE_B, progress, retries, delay, dry_run=True)
        if should_run("register", start):
            for number in REGISTER_ONLY:
                register_existing(number, dry_run=True)
        print("Dry run only; FIFO not verified.", flush=True)
        return 0

    with hold_master_lock(ROOT, holder="run_catchup", chapter=KEEP_LIVE[0], stage=start) as lock:
        if should_run("reset", start):
            lock.update(stage="reset")
            reset_chapters(dry_run=False)
            progress = load_progress()
            progress["phase"] = "audit"
            save_progress(progress)
        if should_run("audit", start):
            lock.update(stage="audit")
            audit_range(max(1, args.jobs), dry_run=False)
            commit_audit(dry_run=False)
            progress = load_progress()
            progress["phase"] = "snapshot"
            progress["audit_committed"] = True
            save_progress(progress)
        if should_run("snapshot", start):
            lock.update(stage="snapshot")
            snapshot_audited(dry_run=False)
            progress = load_progress()
            progress["phase"] = "remaster"
            save_progress(progress)
        if should_run("remaster", start):
            lock.update(stage="remaster")
            progress = load_progress()
            lanes = [("lane-a", LANE_A), ("lane-b", LANE_B)]
            if workers == 1:
                for name, chapters in lanes:
                    remaster_lane(name, chapters, progress, retries, delay, dry_run=False)
                    progress = load_progress()
            else:
                with ThreadPoolExecutor(max_workers=2) as executor:
                    futures = [
                        executor.submit(
                            remaster_lane, name, chapters, progress, retries, delay, dry_run=False
                        )
                        for name, chapters in lanes
                    ]
                    for future in as_completed(futures):
                        future.result()
            progress = load_progress()
            progress["phase"] = "register"
            save_progress(progress)
        if should_run("register", start):
            lock.update(stage="register")
            for number in REGISTER_ONLY:
                register_existing(number, dry_run=False)
                progress = load_progress()
                registered = list(dict.fromkeys([*progress.get("registered", []), number]))
                progress["registered"] = registered
                save_progress(progress)
            progress = load_progress()
            progress["phase"] = "verify"
            save_progress(progress)
        lock.update(stage="verify")
        verify_heads()
        progress = load_progress()
        progress["phase"] = "done"
        save_progress(progress)
    print(
        "Catch-up complete. Run python tools/run_next.py and python tools/run_next_mastering.py.",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
