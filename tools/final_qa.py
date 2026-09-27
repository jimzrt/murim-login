"""Deterministic checks for the final-touches reading copy."""

from __future__ import annotations

import difflib
import re

FOOTNOTE_DEF = re.compile(r"^\[\^[^\]]+\]:")
FOOTNOTE_REF = re.compile(r"\[\^[^\]]+\]")
BAD_SYSTEM = re.compile(
    r"^(?:>\s*)?(?:\[\s*)?(?:\*\*)?\s*System(?:\s+(?:Message|Window))?\s*(?:\*\*)?(?:\s*\])?\s*$",
    re.IGNORECASE,
)
QUOTED_THOUGHT = re.compile(r"^\*[“\"].*[”\"]\*$")
SYSTEM_HEADING = "> **System**"
LENGTH_RATIO_MAX = 6.0


def _finding(code: str, message: str, **details: object) -> dict:
    return {"code": code, "message": message, "details": details}


def prose_body(text: str) -> str:
    kept: list[str] = []
    for line in text.splitlines():
        if FOOTNOTE_DEF.match(line.strip()):
            continue
        kept.append(FOOTNOTE_REF.sub("", line))
    return "\n".join(kept).strip()


def baseline_preserved(baseline: str, candidate: str) -> float:
    """Share of baseline prose still present after footnote lines are ignored."""
    base = prose_body(baseline)
    cand = prose_body(candidate)
    if not base:
        return 1.0
    matcher = difflib.SequenceMatcher(None, base, cand)
    matched = sum(block.size for block in matcher.get_matching_blocks())
    return matched / len(base)


def format_errors(text: str) -> list[dict]:
    errors: list[dict] = []
    if '"' in text:
        errors.append(_finding(
            "straight_quotes",
            "reading copy contains straight double quotes; speech uses curly quotes",
        ))
    lines = text.splitlines()
    for index, line in enumerate(lines):
        stripped = line.strip()
        if not stripped:
            continue
        line_no = index + 1
        if "└" in stripped and not stripped.startswith(">"):
            errors.append(_finding(
                "chat_format",
                "chat or comment line must be a blockquote beginning with └",
                line=line_no,
            ))
        if QUOTED_THOUGHT.match(stripped):
            errors.append(_finding(
                "thought_format",
                "direct thoughts are italics without quotation marks",
                line=line_no,
            ))
        if BAD_SYSTEM.match(stripped) and stripped != SYSTEM_HEADING:
            errors.append(_finding(
                "system_format",
                "System panel heading must be exactly '> **System**'",
                line=line_no,
            ))
        if stripped == SYSTEM_HEADING:
            cursor = index + 1
            saw_body = False
            while cursor < len(lines) and lines[cursor].strip():
                body = lines[cursor].strip()
                if not body.startswith(">"):
                    errors.append(_finding(
                        "system_format",
                        "System panel lines must stay inside the blockquote",
                        line=cursor + 1,
                    ))
                    break
                saw_body = True
                cursor += 1
            if not saw_body:
                errors.append(_finding(
                    "system_format",
                    "System panel is empty",
                    line=line_no,
                ))
    return errors


def assess(
    number: int,
    source: str,
    baseline: str,
    candidate: str,
    glossary: list[tuple[str, str]] | None = None,
    *,
    min_baseline_preserved: float = 0.8,
) -> dict:
    try:
        from tools.qa import run_qa
    except ModuleNotFoundError:
        from qa import run_qa
    qa = run_qa(number, source, candidate, glossary or [])
    errors: list[dict] = []
    warnings = list(qa.get("warnings") or [])
    for error in qa.get("errors") or []:
        if error.get("code") == "length_ratio":
            ratio = float((error.get("details") or {}).get("ratio") or 0)
            if ratio <= LENGTH_RATIO_MAX:
                warnings.append({
                    **error,
                    "message": "length grew within the final-touches footnote allowance",
                })
                continue
        errors.append(error)
    errors.extend(format_errors(candidate))
    preserved = baseline_preserved(baseline, candidate)
    metrics = dict(qa.get("metrics") or {})
    metrics["baseline_preserved"] = round(preserved, 3)
    if preserved < min_baseline_preserved:
        errors.append(_finding(
            "prose_drift",
            "the edit rewrote mastered prose instead of limiting itself to footnotes, format, and source repairs",
            baseline_preserved=round(preserved, 3),
            minimum=min_baseline_preserved,
        ))
    qa["errors"] = errors
    qa["warnings"] = warnings
    qa["metrics"] = metrics
    qa["passed"] = not errors
    return qa
