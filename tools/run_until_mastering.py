#!/usr/bin/env python3
"""Run run_next_mastering.py sequentially until a target chapter, with bounded retries."""

from __future__ import annotations

import argparse
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from run_lock import hold_master_lock
from run_next_mastering import (
    accepted_translation_numbers,
    needs_mastering,
    next_mastering_chapter,
)

try:
    from mastering import load_config
except ModuleNotFoundError:
    from tools.mastering import load_config


def planned_chapters(until: int) -> list[int]:
    if until < 0:
        raise SystemExit("until chapter must be a non-negative integer")
    current = next_mastering_chapter()
    if current is None or current > until:
        return []
    planned = [
        number
        for number in accepted_translation_numbers()
        if current <= number <= until and needs_mastering(number)
    ]
    if current <= until and needs_mastering(current) and current not in planned:
        planned.insert(0, current)
    return planned


def default_chapter_retries() -> int:
    return max(0, int(load_config().get("run_until_mastering_retries", 2)))


def default_retry_delay_seconds() -> float:
    return max(0.0, float(load_config().get("run_until_mastering_retry_delay_seconds", 30)))


def run_next_mastering_chapter() -> int:
    command = [sys.executable, str(ROOT / "tools" / "run_next_mastering.py")]
    return subprocess.run(command, cwd=ROOT).returncode


def run_chapter_with_retries(chapter: int, retries: int, delay_seconds: float, lock) -> int:
    attempts = 1 + max(0, retries)
    for attempt in range(1, attempts + 1):
        lock.update(chapter=chapter, stage=f"run_next_mastering:{attempt}/{attempts}")
        code = run_next_mastering_chapter()
        if code == 0:
            return 0
        if attempt == attempts:
            return code
        print(
            f"Chapter {chapter} mastering failed with exit code {code}; "
            f"retry {attempt}/{retries} after {delay_seconds:g}s (resume same chapter)",
            flush=True,
        )
        if delay_seconds > 0:
            time.sleep(delay_seconds)
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("until", type=int, help="stop after this chapter is mastered")
    parser.add_argument("--dry-run", action="store_true", help="print the plan and exit")
    parser.add_argument(
        "--retries",
        type=int,
        default=None,
        help=(
            "extra run_next_mastering attempts per chapter after the first failure "
            f"(default: docs/mastering.json run_until_mastering_retries, currently "
            f"{default_chapter_retries()})"
        ),
    )
    parser.add_argument(
        "--retry-delay",
        type=float,
        default=None,
        help=(
            "seconds to wait between chapter retries "
            f"(default: docs/mastering.json run_until_mastering_retry_delay_seconds, currently "
            f"{default_retry_delay_seconds():g})"
        ),
    )
    args = parser.parse_args()
    retries = default_chapter_retries() if args.retries is None else max(0, args.retries)
    delay = (
        default_retry_delay_seconds()
        if args.retry_delay is None
        else max(0.0, args.retry_delay)
    )
    chapters = planned_chapters(args.until)
    current = next_mastering_chapter()
    if not chapters:
        if current is None:
            print(f"Nothing to do: mastering queue is empty (until {args.until})", flush=True)
        else:
            print(
                f"Nothing to do: next mastering chapter is {current}, until is {args.until}",
                flush=True,
            )
        return 0
    print(
        f"Master until {args.until}: {len(chapters)} chapter{'s' if len(chapters) != 1 else ''} remaining "
        f"({chapters[0]}–{chapters[-1]}); {retries} chapter retr{'ies' if retries != 1 else 'y'} "
        f"after failure, {delay:g}s delay",
        flush=True,
    )
    if args.dry_run:
        for chapter in chapters:
            print(f"  would master chapter {chapter}", flush=True)
        return 0
    with hold_master_lock(
        ROOT, holder="run_until_mastering", chapter=chapters[0], stage="starting", until=args.until
    ) as lock:
        for index, chapter in enumerate(chapters, 1):
            current = next_mastering_chapter()
            if current != chapter:
                raise SystemExit(
                    f"next mastering chapter is {current}, expected {chapter}; "
                    "stopping before run_next_mastering"
                )
            print(f"\n=== Master Chapter {chapter} ({index}/{len(chapters)}) ===", flush=True)
            code = run_chapter_with_retries(chapter, retries, delay, lock)
            if code:
                lock.update(stage="failed")
                print(
                    f"Chapter {chapter} mastering failed with exit code {code} after "
                    f"{1 + retries} attempt{'' if retries == 0 else 's'}; stopping. "
                    f"Resume chapter {chapter}; do not start a later chapter until it is mastered.",
                    flush=True,
                )
                return code
            if needs_mastering(chapter):
                raise SystemExit(
                    f"run_next_mastering returned success but chapter {chapter} still needs mastering"
                )
            advanced = next_mastering_chapter()
            if advanced is not None and advanced <= chapter:
                raise SystemExit(
                    f"run_next_mastering returned success but next mastering chapter is still {advanced}"
                )
            remaining = len([n for n in chapters[index:] if needs_mastering(n)])
            if remaining:
                print(
                    f"Chapter {chapter}: mastered; {remaining} remaining through {args.until}",
                    flush=True,
                )
            else:
                print(f"Chapter {chapter}: mastered; reached chapter {args.until}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
