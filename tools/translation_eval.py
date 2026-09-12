#!/usr/bin/env python3
"""Deterministic regression checks for chapter translation candidates."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# These source-grounded semantic controls accept ordinary wording variation.
# They reject known reversals without pinning the accepted translation's prose.
QUALITY_ANCHORS = (
    {
        "id": "internal_energy_realization",
        "required_patterns": (
            r"\bnever (?:used|had|possessed|handled)\b.{0,80}\b(?:anything|something|power|energy)\b",
            r"\bnot (?:as if|like) I(?:’|')ve ever (?:used|had)\b",
        ),
        "forbidden_patterns": (
            r"\bshould have (?:tried )?(?:using|used)\b.{0,60}\b(?:beginning|start)\b",
        ),
    },
    {
        "id": "counter_direction",
        "required_patterns": (
            r"\b(?:Successful attempts|Success Count)\s*:?\s*\((?:2|5|6) / 100\)",
        ),
        "forbidden_patterns": (
            r"\bRemaining (?:successful attempts|success count)\s*:?\s*\((?:2|5|6) / 100\)",
        ),
    },
    {
        "id": "idiom_function",
        "required_patterns": (
            r"\bonly know what something is like once you(?:’|')ve experienced it\b",
            r"\bonly someone who(?:’|')?d? eaten meat knew its taste\b",
            r"\bexperience (?:was|is) everything\b",
        ),
        "forbidden_patterns": (),
    },
    {
        "id": "inventory_command",
        "required_patterns": (r"[“\"]Acquire [Ii]tem[.”\"]",),
        "forbidden_patterns": (r"[“\"]Item Acquired[.”\"]",),
    },
    {
        "id": "gold_spoon_wordplay",
        "required_patterns": (r"\bgold(?:en)? spoon\b",),
        "forbidden_patterns": (),
    },
    {
        "id": "nickname_punchline",
        "required_patterns": (r"\bNight King\b",),
        "forbidden_patterns": (r"\b(?:Fire|Flame) King\b",),
    },
    {
        "id": "training_cave",
        "required_patterns": (r"\btraining cave\b",),
        "forbidden_patterns": (r"\btraining hall\b",),
    },
)


def _matches_any(patterns: tuple[str, ...], text: str) -> bool:
    return any(re.search(pattern, text, re.IGNORECASE | re.DOTALL) for pattern in patterns)


def evaluate_text(text: str) -> dict:
    checks = []
    for anchor in QUALITY_ANCHORS:
        required = _matches_any(anchor["required_patterns"], text)
        forbidden = _matches_any(anchor["forbidden_patterns"], text)
        checks.append({
            "id": anchor["id"],
            "required_present": required,
            "forbidden_present": forbidden,
            "passed": required and not forbidden,
        })
    return {
        "passed": all(item["passed"] for item in checks),
        "passed_checks": sum(item["passed"] for item in checks),
        "total_checks": len(checks),
        "checks": checks,
    }


def evaluate_path(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    result = evaluate_text(text)
    return {"path": str(path), **result}


def compare_paths(baseline: Path, candidates: list[Path]) -> dict:
    return {
        "version": 1,
        "baseline": evaluate_path(baseline),
        "candidates": [evaluate_path(path) for path in candidates],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("candidates", nargs="+", type=Path)
    parser.add_argument("--baseline", type=Path, default=ROOT / "translations" / "0010.md")
    args = parser.parse_args()
    result = compare_paths(args.baseline, args.candidates)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["baseline"]["passed"] and all(item["passed"] for item in result["candidates"]) else 1


if __name__ == "__main__":
    raise SystemExit(main())
