#!/usr/bin/env python3
"""Corpus scanner: chapters whose English drifts from a ledger name.

For every chapter with both a Korean source and a reading copy, list ledger
proper names (people, sects, places, skills) whose Korean stands at a word
boundary in the source while the English uses a known wrong variant
(docs/NAME_VARIANTS.md), a similar non-ledger spelling, or omits a profiled
character entirely. Read-only; it never edits translations.

    python tools/name_drift.py                 # all chapters, Markdown to stdout
    python tools/name_drift.py 601 1191 --output report.md
    python tools/name_drift.py --json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTER_FILE = re.compile(r"^(\d{4})\.md$")

try:
    from tools.name_check import check_names, proper_name_entries
except ModuleNotFoundError:
    sys.path.insert(0, str(ROOT / "tools"))
    from name_check import check_names, proper_name_entries


def chapters(root: Path, start: int | None, end: int | None) -> list[int]:
    found: list[int] = []
    for path in (root / "translations").iterdir():
        match = CHAPTER_FILE.match(path.name)
        if not match:
            continue
        number = int(match.group(1))
        if start is not None and number < start or end is not None and number > end:
            continue
        if (root / "source" / f"{number:04d}.txt").is_file():
            found.append(number)
    return sorted(found)


def finalized(root: Path, number: int) -> bool:
    path = root / "reviews" / "final" / f"{number:04d}" / "state.json"
    try:
        state = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False
    return state.get("stage") == "PROMOTED" and bool(state.get("qa_passed"))


def scan(root: Path = ROOT, start: int | None = None, end: int | None = None) -> dict:
    entries = proper_name_entries(root)
    groups: dict[str, dict[tuple, list[int]]] = {
        "name_variant": defaultdict(list),
        "name_variant_suspect": defaultdict(list),
        "name_absent": defaultdict(list),
    }
    numbers = chapters(root, start, end)
    for number in numbers:
        source = (root / "source" / f"{number:04d}.txt").read_text(encoding="utf-8")
        translation = (root / "translations" / f"{number:04d}.md").read_text(encoding="utf-8")
        result = check_names(source, translation, entries)
        for finding in result["errors"] + result["warnings"]:
            details = finding["details"]
            key = (details["korean"], details["preferred"], tuple(details.get("found") or ()))
            groups[finding["code"]][key].append(number)
    report: dict = {"version": 1, "chapters_scanned": len(numbers), "groups": {}}
    for code, items in groups.items():
        rows = []
        for (korean, preferred, found), hits in sorted(items.items(), key=lambda pair: (-len(pair[1]), pair[0])):
            rows.append({
                "korean": korean,
                "preferred": preferred,
                "found": list(found),
                "chapters": hits,
                "pending_final": [number for number in hits if not finalized(root, number)],
            })
        report["groups"][code] = rows
    return report


TITLES = {
    "name_variant": (
        "Known wrong variants (blocking in final QA)",
        "Rows from `docs/NAME_VARIANTS.md` still present in the reading copy.",
    ),
    "name_variant_suspect": (
        "Suspected drift (final-QA warning)",
        "The preferred English is absent and a similar non-ledger spelling is used. "
        "Confirm against the source before adding a row to `docs/NAME_VARIANTS.md`.",
    ),
    "name_absent": (
        "Profiled names absent from the English (final-QA warning)",
        "A profiled character's Korean name (three or more syllables, or spaced) "
        "is in the source, but no word of the preferred English is in the reading copy.",
    ),
}


def _chapter_list(numbers: list[int]) -> str:
    return ", ".join(str(number) for number in numbers) or "—"


def render(report: dict) -> str:
    lines = [
        "# Name Drift Report",
        "",
        f"Chapters scanned: {report['chapters_scanned']}. "
        "“Pending” chapters have not been promoted by final touches yet.",
        "",
    ]
    for code, (title, blurb) in TITLES.items():
        rows = report["groups"].get(code, [])
        total = sum(len(row["chapters"]) for row in rows)
        lines += [f"## {title}", "", blurb, "", f"{len(rows)} names, {total} chapter hits.", ""]
        if not rows:
            lines += ["None.", ""]
            continue
        lines += [
            "| Korean | Preferred | Found | Chapters | Pending final |",
            "| ------ | --------- | ----- | -------- | ------------- |",
        ]
        for row in rows:
            found = "; ".join(row["found"]) or "—"
            lines.append(
                f"| {row['korean']} | {row['preferred']} | {found} | "
                f"{_chapter_list(row['chapters'])} | {_chapter_list(row['pending_final'])} |"
            )
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("start", type=int, nargs="?")
    parser.add_argument("end", type=int, nargs="?")
    parser.add_argument("--json", action="store_true", help="print JSON instead of Markdown")
    parser.add_argument("--output", type=Path, help="write the report to this path")
    args = parser.parse_args()
    report = scan(ROOT, args.start, args.end)
    text = json.dumps(report, ensure_ascii=False, indent=2) + "\n" if args.json else render(report)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
        print(args.output)
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
