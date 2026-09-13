#!/usr/bin/env python3
"""Validate the gapped Chapter 374 expedition and resume parked 374–375 progress."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise SystemExit(f"invalid JSON at {path}: {error}") from None
    if not isinstance(value, dict):
        raise SystemExit(f"{path} must contain one object")
    return value


def state_numbers() -> tuple[int, int]:
    text = (ROOT / "docs" / "STATE.md").read_text(encoding="utf-8")
    completed = re.search(r"^- Last completed:\s*(\d+)\s*$", text, re.MULTILINE)
    next_chapter = re.search(r"^- Next chapter:\s*(\d+)\s*$", text, re.MULTILINE)
    if not completed or not next_chapter:
        raise SystemExit("docs/STATE.md must contain exact Last completed and Next chapter lines")
    return int(completed.group(1)), int(next_chapter.group(1))


def translation_path(chapter: int) -> Path:
    return ROOT / "translations" / f"{chapter:04d}.md"


def parked_progress(config: dict) -> dict:
    parked = config.get("parked_progress")
    if not isinstance(parked, dict):
        raise SystemExit("docs/expedition.json must contain parked_progress")
    from_chapter = parked.get("from_chapter")
    through_chapter = parked.get("through_chapter")
    if not isinstance(from_chapter, int) or not isinstance(through_chapter, int):
        raise SystemExit("parked_progress from_chapter and through_chapter must be integers")
    if through_chapter < from_chapter:
        raise SystemExit("parked_progress through_chapter must be >= from_chapter")
    return parked


def check() -> dict:
    config = read_json(ROOT / "docs" / "expedition.json")
    required = {
        "version", "mode", "start_chapter", "seed_safe_through",
        "skipped_ranges", "canonical_anchor", "pages_repository",
        "pages_event", "release_tag",
    }
    missing = required - set(config)
    if missing:
        raise SystemExit("expedition config missing: " + ", ".join(sorted(missing)))
    if config["version"] != 1 or config["mode"] != "expedition":
        raise SystemExit("docs/expedition.json must be version 1 expedition mode")
    start = config["start_chapter"]
    seed = config["seed_safe_through"]
    if not isinstance(start, int) or not isinstance(seed, int) or start != seed + 1:
        raise SystemExit("start_chapter must be exactly seed_safe_through + 1")
    parked = parked_progress(config)
    completed, next_chapter = state_numbers()
    initial_state = completed == seed and next_chapter == start
    ongoing_state = completed >= start and next_chapter == completed + 1
    if not (initial_state or ongoing_state):
        raise SystemExit(
            f"expedition state must start at {seed}/{start} or advance sequentially "
            f"from Chapter {start}; found {completed}/{next_chapter}"
        )
    context = read_json(ROOT / "docs" / "CONTEXT.json")
    safe_through = context.get("safe_through")
    if not isinstance(safe_through, int) or safe_through < seed:
        raise SystemExit("CONTEXT.json safe_through must be at least the expedition seed")
    if start <= 0 or not (ROOT / "source" / f"{start:04d}.txt").is_file():
        raise SystemExit(f"missing source for expedition start chapter {start}")
    if not (ROOT / "docs" / "EXPEDITION.md").is_file() or not (ROOT / "docs" / "EXPEDITION_SEED.md").is_file():
        raise SystemExit("expedition instruction and seed files are required")
    for chapter in range(int(parked["from_chapter"]), int(parked["through_chapter"]) + 1):
        path = translation_path(chapter)
        if not path.is_file():
            raise SystemExit(f"missing parked translation: {path}")
    return {
        "mode": config["mode"],
        "start_chapter": start,
        "seed_safe_through": seed,
        "pages_repository": config["pages_repository"],
        "release_tag": config["release_tag"],
        "parked_from": parked["from_chapter"],
        "parked_through": parked["through_chapter"],
    }


def resume_parked() -> dict:
    config = read_json(ROOT / "docs" / "expedition.json")
    start = config["start_chapter"]
    parked = parked_progress(config)
    from_chapter = int(parked["from_chapter"])
    through_chapter = int(parked["through_chapter"])
    completed, next_chapter = state_numbers()
    if completed != from_chapter - 1 or next_chapter != from_chapter:
        raise SystemExit(
            f"resume-parked requires last completed {from_chapter - 1} and next "
            f"{from_chapter}; found {completed}/{next_chapter}"
        )
    for chapter in range(start, from_chapter):
        path = translation_path(chapter)
        if not path.is_file():
            raise SystemExit(f"catch-up translation missing: {path}")
    for chapter in range(from_chapter, through_chapter + 1):
        path = translation_path(chapter)
        if not path.is_file():
            raise SystemExit(f"parked translation missing: {path}")
    context_rel = parked.get("context")
    state_rel = parked.get("state")
    if not isinstance(context_rel, str) or not isinstance(state_rel, str):
        raise SystemExit("parked_progress must name context and state snapshot paths")
    context_src = ROOT / context_rel
    state_src = ROOT / state_rel
    if not context_src.is_file() or not state_src.is_file():
        raise SystemExit("parked CONTEXT/STATE snapshots are missing")
    shutil.copyfile(context_src, ROOT / "docs" / "CONTEXT.json")
    shutil.copyfile(state_src, ROOT / "docs" / "STATE.md")
    restored_completed, restored_next = state_numbers()
    if restored_completed != through_chapter or restored_next != through_chapter + 1:
        raise SystemExit("parked STATE.md does not resume immediately after parked_progress")
    return {
        "restored_completed": restored_completed,
        "restored_next": restored_next,
        "kept_translations": list(range(from_chapter, through_chapter + 1)),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    check_parser = sub.add_parser("check")
    check_parser.add_argument("--json", action="store_true")
    sub.add_parser("resume-parked")
    args = parser.parse_args()
    if args.command == "resume-parked":
        result = resume_parked()
        print(
            f"Restored parked progress: last completed {result['restored_completed']}; "
            f"next chapter {result['restored_next']}; kept "
            + ", ".join(f"{chapter:04d}" for chapter in result["kept_translations"])
        )
        return 0
    result = check()
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    else:
        print(
            f"Expedition valid: Chapter {result['start_chapter']} start; "
            f"seed safe through {result['seed_safe_through']}; "
            f"parked {result['parked_from']}–{result['parked_through']}; "
            f"Pages {result['pages_repository']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
