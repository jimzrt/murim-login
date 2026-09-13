#!/usr/bin/env python3
"""Validate the deliberately gapped Chapter 374 translation expedition."""

from __future__ import annotations

import argparse
import json
import re
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
    completed, next_chapter = state_numbers()
    if completed != seed or next_chapter != start:
        raise SystemExit(
            f"expedition state must be {seed} completed and {start} next; "
            f"found {completed} and {next_chapter}"
        )
    context = read_json(ROOT / "docs" / "CONTEXT.json")
    if context.get("safe_through") != seed:
        raise SystemExit("CONTEXT.json safe_through does not match expedition seed")
    if start <= 0 or not (ROOT / "source" / f"{start:04d}.txt").is_file():
        raise SystemExit(f"missing source for expedition start chapter {start}")
    if not (ROOT / "docs" / "EXPEDITION.md").is_file() or not (ROOT / "docs" / "EXPEDITION_SEED.md").is_file():
        raise SystemExit("expedition instruction and seed files are required")
    for chapter in (371, 372, 373):
        for path in (
            ROOT / "summaries" / "beats" / f"{chapter:04d}.md",
        ):
            if not path.is_file():
                raise SystemExit(f"missing source bridge artifact: {path}")
    return {
        "mode": config["mode"],
        "start_chapter": start,
        "seed_safe_through": seed,
        "pages_repository": config["pages_repository"],
        "release_tag": config["release_tag"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    check_parser = sub.add_parser("check")
    check_parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = check()
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    else:
        print(
            f"Expedition valid: Chapter {result['start_chapter']} start; "
            f"seed safe through {result['seed_safe_through']}; "
            f"Pages {result['pages_repository']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
