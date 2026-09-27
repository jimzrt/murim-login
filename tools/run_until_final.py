#!/usr/bin/env python3
"""Run run_next_final.py sequentially from the oldest unfinished chapter through a target."""

from __future__ import annotations

import argparse
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from run_lock import hold_final_lock

try:
    from tools.final_touches import load_config, load_state
    from tools.run_next_final import mastering_done, next_final_chapter, translation_numbers
except ModuleNotFoundError:
    from final_touches import load_config, load_state
    from run_next_final import mastering_done, next_final_chapter, translation_numbers


def needs_final(number: int) -> bool:
    state = load_state(number)
    if state.get("stage") == "PROMOTED" and state.get("qa_passed"):
        return False
    return mastering_done(number)


def planned_chapters(until: int) -> list[int]:
    if until < 0:
        raise SystemExit("until chapter must be a non-negative integer")
    current = next_final_chapter()
    if current is None or current > until:
        return []
    planned: list[int] = []
    for number in translation_numbers():
        if number < current or number > until:
            continue
        if load_state(number).get("stage") == "PROMOTED" and load_state(number).get("qa_passed"):
            continue
        if not mastering_done(number):
            break
        planned.append(number)
    if current not in planned and needs_final(current):
        planned.insert(0, current)
    return planned


def default_chapter_retries() -> int:
    return max(0, int(load_config().get("run_until_final_retries", 2)))


def default_retry_delay_seconds() -> float:
    return max(0.0, float(load_config().get("run_until_final_retry_delay_seconds", 30)))


def run_next_final_chapter() -> int:
    command = [sys.executable, str(ROOT / "tools" / "run_next_final.py")]
    return subprocess.run(command, cwd=ROOT).returncode


def run_chapter_with_retries(chapter: int, retries: int, delay_seconds: float, lock) -> int:
    attempts = 1 + max(0, retries)
    for attempt in range(1, attempts + 1):
        lock.update(chapter=chapter, stage=f"run_next_final:{attempt}/{attempts}")
        code = run_next_final_chapter()
        if code == 0:
            return 0
        if attempt == attempts:
            return code
        print(
            f"Chapter {chapter} final touches failed with exit code {code}; "
            f"retry {attempt}/{retries} after {delay_seconds:g}s (resume same chapter)",
            flush=True,
        )
        if delay_seconds > 0:
            time.sleep(delay_seconds)
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("until", type=int, help="stop after this chapter's final touches commit")
    parser.add_argument("--dry-run", action="store_true", help="print the plan and exit")
    parser.add_argument(
        "--retries",
        type=int,
        default=None,
        help=(
            "extra run_next_final attempts per chapter after the first failure "
            f"(default: docs/final.json run_until_final_retries, currently {default_chapter_retries()})"
        ),
    )
    parser.add_argument(
        "--retry-delay",
        type=float,
        default=None,
        help=(
            "seconds to wait between chapter retries "
            f"(default: docs/final.json run_until_final_retry_delay_seconds, currently "
            f"{default_retry_delay_seconds():g})"
        ),
    )
    args = parser.parse_args()
    retries = default_chapter_retries() if args.retries is None else max(0, args.retries)
    delay = default_retry_delay_seconds() if args.retry_delay is None else max(0.0, args.retry_delay)
    chapters = planned_chapters(args.until)
    current = next_final_chapter()
    if not chapters:
        if current is None:
            print(f"Nothing to do: final-touches queue is empty or waiting on mastering (until {args.until})", flush=True)
        else:
            print(
                f"Nothing to do: next final-touches chapter is {current}, until is {args.until}",
                flush=True,
            )
        return 0
    print(
        f"Final touches until {args.until}: {len(chapters)} chapter{'s' if len(chapters) != 1 else ''} remaining "
        f"({chapters[0]}–{chapters[-1]}); {retries} chapter retr{'ies' if retries != 1 else 'y'} "
        f"after failure, {delay:g}s delay",
        flush=True,
    )
    if args.dry_run:
        for chapter in chapters:
            print(f"  would finish chapter {chapter}", flush=True)
        return 0
    with hold_final_lock(
        ROOT, holder="run_until_final", chapter=chapters[0], stage="starting", until=args.until
    ) as lock:
        for index, chapter in enumerate(chapters, 1):
            current = next_final_chapter()
            if current != chapter:
                raise SystemExit(
                    f"next final-touches chapter is {current}, expected {chapter}; "
                    "stopping before run_next_final"
                )
            print(f"\n=== Final Chapter {chapter} ({index}/{len(chapters)}) ===", flush=True)
            code = run_chapter_with_retries(chapter, retries, delay, lock)
            if code:
                lock.update(stage="failed")
                print(
                    f"Chapter {chapter} final touches failed with exit code {code} after "
                    f"{1 + retries} attempt{'' if retries == 0 else 's'}; stopping. "
                    f"Resume chapter {chapter}; do not start a later chapter until it is finished.",
                    flush=True,
                )
                return code
            if needs_final(chapter):
                raise SystemExit(
                    f"run_next_final returned success but chapter {chapter} still needs final touches"
                )
            advanced = next_final_chapter()
            if advanced is not None and advanced <= chapter:
                raise SystemExit(
                    f"run_next_final returned success but next final-touches chapter is still {advanced}"
                )
            remaining = [item for item in chapters[index:] if needs_final(item)]
            if remaining:
                print(
                    f"Chapter {chapter}: finished; {len(remaining)} remaining through {args.until}",
                    flush=True,
                )
            else:
                print(f"Chapter {chapter}: finished; reached chapter {args.until}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
