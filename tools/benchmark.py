#!/usr/bin/env python3
"""Score accepted translations against the frozen Murim Login regression suite."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ITEMS_PATH = ROOT / "benchmark" / "items.jsonl"
REQUIRED_KEYS = ("id", "chapter", "category", "source", "constraint", "origin")


def _strings(value: object, label: str) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value] if value.strip() else []
    if not isinstance(value, list) or any(not isinstance(item, str) or not item.strip() for item in value):
        raise ValueError(f"{label} must be a string or an array of nonempty strings")
    return [item.strip() for item in value]


def load_items(path: Path | None = None) -> list[dict]:
    path = path or ITEMS_PATH
    items: list[dict] = []
    seen: set[str] = set()
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            item = json.loads(line)
        except json.JSONDecodeError as error:
            raise ValueError(f"{path}:{line_number}: invalid JSON: {error}") from None
        if not isinstance(item, dict):
            raise ValueError(f"{path}:{line_number}: item must be an object")
        missing = [key for key in REQUIRED_KEYS if key not in item]
        if missing:
            raise ValueError(f"{path}:{line_number}: missing {', '.join(missing)}")
        identifier = item["id"]
        if not isinstance(identifier, str) or not identifier.strip():
            raise ValueError(f"{path}:{line_number}: id must be a nonempty string")
        if identifier in seen:
            raise ValueError(f"duplicate benchmark id: {identifier}")
        seen.add(identifier)
        if not isinstance(item["chapter"], int) or isinstance(item["chapter"], bool) or item["chapter"] < 0:
            raise ValueError(f"{identifier}: chapter must be a non-negative integer")
        item["required"] = _strings(item.get("required"), f"{identifier}.required")
        item["forbidden"] = _strings(item.get("forbidden"), f"{identifier}.forbidden")
        items.append(item)
    return items


def contains(haystack: str, needle: str) -> bool:
    return needle.casefold() in haystack.casefold()


def score_item(item: dict, translation: str) -> dict:
    missing = [span for span in item["required"] if not contains(translation, span)]
    hits = [span for span in item["forbidden"] if contains(translation, span)]
    if not item["required"] and not item["forbidden"]:
        status = "unscored"
    elif missing or hits:
        status = "fail"
    else:
        status = "pass"
    return {
        "id": item["id"],
        "chapter": item["chapter"],
        "category": item["category"],
        "status": status,
        "missing_required": missing,
        "forbidden_hits": hits,
    }


def translation_path(number: int, root: Path | None = None) -> Path:
    return (root or ROOT) / "translations" / f"{number:04d}.md"


def score_items(
    items: list[dict],
    *,
    chapter: int | None = None,
    root: Path | None = None,
) -> dict:
    root = root or ROOT
    selected = [item for item in items if chapter is None or item["chapter"] == chapter]
    results: list[dict] = []
    missing_files: list[int] = []
    cache: dict[int, str] = {}
    for item in selected:
        path = translation_path(item["chapter"], root)
        if item["chapter"] not in cache:
            if not path.is_file():
                missing_files.append(item["chapter"])
                results.append({
                    "id": item["id"],
                    "chapter": item["chapter"],
                    "category": item["category"],
                    "status": "missing",
                    "missing_required": item["required"],
                    "forbidden_hits": [],
                })
                continue
            cache[item["chapter"]] = path.read_text(encoding="utf-8")
        results.append(score_item(item, cache[item["chapter"]]))
    counts = {"pass": 0, "fail": 0, "unscored": 0, "missing": 0}
    for result in results:
        counts[result["status"]] += 1
    return {
        "version": 1,
        "item_count": len(selected),
        "counts": counts,
        "missing_translations": sorted(set(missing_files)),
        "results": results,
    }


def format_report(report: dict) -> str:
    counts = report["counts"]
    lines = [
        f"Benchmark items: {report['item_count']}",
        f"Pass {counts['pass']}, fail {counts['fail']}, unscored {counts['unscored']}, missing {counts['missing']}",
    ]
    for result in report["results"]:
        if result["status"] == "pass":
            continue
        detail = result["status"]
        if result["missing_required"]:
            detail += "; missing " + " | ".join(result["missing_required"])
        if result["forbidden_hits"]:
            detail += "; forbidden " + " | ".join(result["forbidden_hits"])
        lines.append(f"{result['id']} ch{result['chapter']} {result['category']}: {detail}")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--chapter", type=int)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--items", type=Path)
    args = parser.parse_args()
    items = load_items(args.items) if args.items else load_items()
    report = score_items(items, chapter=args.chapter)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(format_report(report))
    if report["counts"]["fail"] or report["counts"]["missing"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
