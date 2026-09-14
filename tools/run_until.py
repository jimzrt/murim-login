#!/usr/bin/env python3
"""Run run_next.py sequentially until a target chapter, with bounded chapter retries."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from run_lock import hold_run_lock
from workflow import incomplete_chapter, project_config


def next_chapter() -> int:
    state = (ROOT / "docs" / "STATE.md").read_text(encoding="utf-8")
    match = re.search(r"^- Next chapter:\s*(\d+)\s*$", state, re.MULTILINE)
    if not match:
        raise SystemExit("docs/STATE.md has no exact '- Next chapter: N' line")
    return int(match.group(1))


def start_chapter() -> int:
    return incomplete_chapter() or next_chapter()


def planned_chapters(until: int) -> list[int]:
    if until < 0:
        raise SystemExit("until chapter must be a non-negative integer")
    start = start_chapter()
    if start > until:
        return []
    return list(range(start, until + 1))


def default_chapter_retries() -> int:
    return max(0, int(project_config().get("run_until_chapter_retries", 2)))


def run_next_chapter() -> int:
    command = [sys.executable, str(ROOT / "tools" / "run_next.py")]
    return subprocess.run(command, cwd=ROOT).returncode


def run_chapter_with_retries(chapter: int, retries: int, lock) -> int:
    attempts = 1 + max(0, retries)
    for attempt in range(1, attempts + 1):
        lock.update(chapter=chapter, stage=f"run_next:{attempt}/{attempts}")
        code = run_next_chapter()
        if code == 0:
            return 0
        if attempt == attempts:
            return code
        print(
            f"Chapter {chapter} failed with exit code {code}; "
            f"retry {attempt}/{retries} (resume same chapter)",
            flush=True,
        )
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("until", type=int, help="stop after this chapter is committed")
    parser.add_argument("--dry-run", action="store_true", help="print the plan and exit")
    parser.add_argument(
        "--retries",
        type=int,
        default=None,
        help=(
            "extra run_next attempts per chapter after the first failure "
            f"(default: docs/workflow.json run_until_chapter_retries, currently "
            f"{default_chapter_retries()})"
        ),
    )
    args = parser.parse_args()
    retries = default_chapter_retries() if args.retries is None else max(0, args.retries)
    chapters = planned_chapters(args.until)
    start = start_chapter()
    if not chapters:
        print(f"Nothing to do: next chapter is {start}, until is {args.until}", flush=True)
        return 0
    print(
        f"Until {args.until}: {len(chapters)} chapter{'s' if len(chapters) != 1 else ''} remaining "
        f"({chapters[0]}–{chapters[-1]}); {retries} chapter retr{'ies' if retries != 1 else 'y'} "
        f"after failure",
        flush=True,
    )
    if args.dry_run:
        for chapter in chapters:
            print(f"  would run chapter {chapter}", flush=True)
        return 0
    with hold_run_lock(
        ROOT, holder="run_until", chapter=chapters[0], stage="starting", until=args.until
    ) as lock:
        for index, chapter in enumerate(chapters, 1):
            current = start_chapter()
            if current != chapter:
                raise SystemExit(
                    f"next chapter is {current}, expected {chapter}; stopping before run_next"
                )
            print(f"\n=== Chapter {chapter} ({index}/{len(chapters)}) ===", flush=True)
            code = run_chapter_with_retries(chapter, retries, lock)
            if code:
                lock.update(stage="failed")
                print(
                    f"Chapter {chapter} failed with exit code {code} after {1 + retries} attempt"
                    f"{'' if retries == 0 else 's'}; stopping. "
                    f"Resume chapter {chapter}; do not start a later chapter until it is committed.",
                    flush=True,
                )
                return code
            leftover = incomplete_chapter()
            if leftover is not None:
                raise SystemExit(
                    f"run_next returned success but chapter {leftover} is still in progress"
                )
            advanced = next_chapter()
            if advanced != chapter + 1:
                raise SystemExit(
                    f"run_next returned success but next chapter is {advanced}, expected {chapter + 1}"
                )
            remaining = args.until - chapter
            if remaining:
                print(f"Chapter {chapter}: done; {remaining} remaining through {args.until}", flush=True)
            else:
                print(f"Chapter {chapter}: done; reached chapter {args.until}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
