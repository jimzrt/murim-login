#!/usr/bin/env python3
"""Finalize a range of mastered chapters with parallel edits and serial commits.

Each worker runs the final-touches model and QA for a different chapter. Git
commits one finished chapter at a time. A failed chapter stays uncommitted.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from run_lock import hold_final_lock
from run_next_final import commit_final, final_done, mastering_done, translation_blocked

try:
    from tools.final_touches import load_config
except ModuleNotFoundError:
    from final_touches import load_config


def default_workers() -> int:
    return max(1, int(load_config().get("batch_workers", 3)))


def select_batch(start: int, end: int, dirty: list[str] | None = None) -> tuple[list[int], list[str]]:
    if start < 0 or end < 0:
        raise SystemExit("chapter numbers must be non-negative")
    if end < start:
        raise SystemExit("end chapter is before the start chapter")
    dirty_set = set(dirty or [])
    chosen: list[int] = []
    notes: list[str] = []
    for number in range(start, end + 1):
        if not (ROOT / "translations" / f"{number:04d}.md").is_file():
            notes.append(f"chapter {number}: no translation")
            continue
        if final_done(number, dirty_set):
            continue
        if not mastering_done(number):
            notes.append(f"chapter {number}: not mastered")
            continue
        blocked = translation_blocked(number)
        if blocked:
            notes.append(f"chapter {number}: still in translation or mastering")
            continue
        chosen.append(number)
    return chosen, notes


def run_chapter(number: int) -> int:
    command = [sys.executable, str(ROOT / "tools" / "final_touches.py"), "run", str(number)]
    return subprocess.run(command, cwd=ROOT).returncode


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("start", type=int, help="first chapter to finalize")
    parser.add_argument("end", nargs="?", type=int, help="last chapter to finalize; defaults to start")
    parser.add_argument(
        "--workers",
        type=int,
        default=None,
        help=f"parallel model calls (default: docs/final.json batch_workers, currently {default_workers()})",
    )
    parser.add_argument("--dry-run", action="store_true", help="print the chapter list and exit")
    args = parser.parse_args()
    end = args.start if args.end is None else args.end
    workers = default_workers() if args.workers is None else max(1, args.workers)
    chapters, notes = select_batch(args.start, end)
    for note in notes:
        print(note, flush=True)
    if not chapters:
        print(f"Nothing to finish in chapters {args.start}–{end}.", flush=True)
        return 0
    print(
        f"Final touches {chapters[0]}–{chapters[-1]}: {len(chapters)} chapter"
        f"{'s' if len(chapters) != 1 else ''}, {workers} worker{'s' if workers != 1 else ''}",
        flush=True,
    )
    if args.dry_run:
        for number in chapters:
            print(f"  would finish chapter {number}", flush=True)
        return 0

    failures: list[int] = []
    committed: list[int] = []
    commit_gate = threading.Lock()

    def finish(number: int) -> None:
        code = run_chapter(number)
        if code:
            print(f"Chapter {number} final touches failed with exit code {code}", flush=True)
            failures.append(number)
            return
        with commit_gate:
            try:
                commit_final(number)
            except SystemExit as exc:
                print(f"Chapter {number} commit failed: {exc}", flush=True)
                failures.append(number)
                return
        committed.append(number)

    with hold_final_lock(
        ROOT, holder="run_final_batch", chapter=chapters[0], stage="starting", until=end
    ) as lock:
        lock.update(stage=f"batch:{len(chapters)}")
        with ThreadPoolExecutor(max_workers=min(workers, len(chapters))) as pool:
            futures = [pool.submit(finish, number) for number in chapters]
            for future in as_completed(futures):
                future.result()
        lock.update(stage="finished" if not failures else "finished-with-failures")

    print(
        f"Finished {len(committed)} chapter{'s' if len(committed) != 1 else ''}; "
        f"{len(failures)} failed",
        flush=True,
    )
    if failures:
        print("Failed chapters: " + ", ".join(str(number) for number in sorted(failures)), flush=True)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
