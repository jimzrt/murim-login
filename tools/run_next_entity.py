#!/usr/bin/env python3
"""Run the entity pass on the oldest finalized chapter not yet checked, and commit it."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from run_entity_pass import (
    commit_entity,
    entity_done,
    final_clean,
    refuse_live_locks,
    run_chapter,
    unexpected_paths,
)
from run_lock import hold_entity_lock
from run_next import changed_paths


def next_entity_chapter(dirty: list[str] | None = None) -> int | None:
    dirty_set = set(changed_paths() if dirty is None else dirty)
    for path in sorted((ROOT / "translations").glob("[0-9][0-9][0-9][0-9].md")):
        number = int(path.stem)
        if entity_done(number, dirty_set) or not final_clean(number, dirty_set):
            continue
        return number
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--no-commit", action="store_true", help="stop before the commit")
    args = parser.parse_args()
    refuse_live_locks()
    chapter = next_entity_chapter()
    if chapter is None:
        print("Nothing to check: every finalized chapter has been through the entity pass.", flush=True)
        return 0
    stray = [path for path in unexpected_paths(chapter, changed_paths()) if not path.startswith("reviews/entity/")]
    if stray:
        raise SystemExit("working tree has unexpected changes: " + ", ".join(stray))
    with hold_entity_lock(ROOT, holder="run_next_entity", chapter=chapter, stage="entity") as lock:
        if run_chapter(chapter):
            raise SystemExit(f"entity pass failed for chapter {chapter}")
        if args.no_commit:
            return 0
        lock.update(stage="committing")
        commit_entity(chapter, holder="run_next_entity")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
