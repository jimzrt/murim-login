#!/usr/bin/env python3
"""Exact-match address-pair and Korean danger-term ledgers."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ADDRESS_COLUMNS = (
    "Speaker", "Addressee", "Kinship", "Normal address", "Speech level", "Notes",
)
RISK_COLUMNS = ("Korean", "Category", "Constraint", "Forbidden English")
RISK_CATEGORIES = frozenset({
    "polysemy",
    "idiom",
    "slang",
    "kinship",
    "register",
    "zero_anaphora_pattern",
    "comedy",
    "murim_vs_hunter",
})
KOREAN_TERM = re.compile(r"[가-힣]+(?:\s+[가-힣]+)*")
KOREAN_NAME = re.compile(r"[가-힣]{2,}")
TABLE_ROW = re.compile(r"^\|(.*)\|\s*$")

ADDRESS_HEADER = """# Established Address Pairs

Exceptional speaker → addressee forms established in accepted chapters.
Injected only when both endpoints are present in the current chapter: the
Korean appears in the source, or belongs to a matched compact profile.
Overrides generic relationship prose in character profiles for this pair.

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
"""

RISK_HEADER = """# Korean Danger Register

Durable risky Korean terms. Injected only when the exact Korean appears in
the current chapter. These are constraints, not preferred glossary English;
`docs/NAMES.md` still wins on the same Korean key.

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
"""


def _cells(line: str) -> list[str] | None:
    match = TABLE_ROW.match(line.rstrip())
    if not match:
        return None
    return [cell.strip() for cell in match.group(1).split("|")]


def _is_separator(cells: list[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell or "") for cell in cells)


def _split_forbidden(value: str) -> list[str]:
    text = value.strip()
    if not text or text in {"-", "—"}:
        return []
    return [part.strip() for part in text.split(" / ") if part.strip()]


def load_address_pairs(path: Path | None = None) -> list[dict]:
    path = path or (ROOT / "docs" / "ADDRESS.md")
    if not path.is_file():
        return []
    pairs: list[dict] = []
    seen: set[tuple[str, str]] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        cells = _cells(line)
        if not cells or len(cells) < 5 or _is_separator(cells):
            continue
        speaker, addressee = cells[0], cells[1]
        if speaker == "Speaker" or not KOREAN_NAME.fullmatch(speaker) or not KOREAN_NAME.fullmatch(addressee):
            continue
        key = (speaker, addressee)
        if key in seen:
            raise ValueError(f"duplicate address pair: {speaker} -> {addressee}")
        seen.add(key)
        notes = cells[5] if len(cells) > 5 else ""
        pairs.append({
            "speaker": speaker,
            "addressee": addressee,
            "kinship": cells[2],
            "normal_address": cells[3],
            "speech_level": cells[4],
            "notes": notes,
            "row": line.rstrip(),
        })
    return pairs


def matching_address_pairs(
    source: str,
    endpoint_koreans: set[str],
    pairs: list[dict] | None = None,
) -> list[dict]:
    pairs = pairs if pairs is not None else load_address_pairs()

    def present(korean: str) -> bool:
        return korean in source or korean in endpoint_koreans

    return [pair for pair in pairs if present(pair["speaker"]) and present(pair["addressee"])]


def address_pairs_text(pairs: list[dict]) -> str:
    if not pairs:
        return "(No matching address pairs.)"
    header = "| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |\n| ------- | --------- | ------- | -------------- | ------------ | ----- |"
    return header + "\n" + "\n".join(item["row"] for item in pairs)


def format_address_row(item: dict) -> str:
    notes = item.get("notes", "")
    return (
        f"| {item['speaker']} | {item['addressee']} | {item['kinship']} | "
        f"{item['normal_address']} | {item['speech_level']} | {notes} |"
    )


def load_risks(path: Path | None = None) -> list[dict]:
    path = path or (ROOT / "docs" / "RISKS.md")
    if not path.is_file():
        return []
    risks: list[dict] = []
    seen: set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        cells = _cells(line)
        if not cells or len(cells) < 3 or _is_separator(cells):
            continue
        korean = cells[0]
        if korean == "Korean" or not KOREAN_TERM.fullmatch(korean):
            continue
        category = cells[1].strip()
        if category not in RISK_CATEGORIES:
            raise ValueError(f"invalid risk category for {korean}: {category}")
        if korean in seen:
            raise ValueError(f"duplicate risk key: {korean}")
        seen.add(korean)
        constraint = cells[2]
        forbidden = _split_forbidden(cells[3] if len(cells) > 3 else "")
        risks.append({
            "korean": korean,
            "category": category,
            "constraint": constraint,
            "forbidden": forbidden,
            "row": line.rstrip(),
        })
    return risks


def matching_risks(source: str, risks: list[dict] | None = None) -> list[dict]:
    risks = risks if risks is not None else load_risks()
    return [item for item in risks if item["korean"] in source]


def risks_text(entries: list[dict]) -> str:
    if not entries:
        return "(No matching risk notes.)"
    header = "| Korean | Category | Constraint | Forbidden English |\n| ------ | -------- | ---------- | ----------------- |"
    return header + "\n" + "\n".join(item["row"] for item in entries)
