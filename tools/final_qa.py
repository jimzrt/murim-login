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
PANEL_HEADING = re.compile(r"^> \*\*[^*]+\*\*\s*$")
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


def _panel_heading_counts(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if PANEL_HEADING.match(stripped):
            counts[stripped] = counts.get(stripped, 0) + 1
    return counts


def _panel_label(line: str) -> str | None:
    match = PANEL_HEADING.match(line.strip())
    if not match:
        return None
    return match.group(0)[len("> **") : -len("**")].strip()


def _blockquote_has_label(line: str, label: str) -> bool:
    stripped = line.strip()
    if not stripped.startswith(">"):
        return False
    if stripped in {f"> **{label}**", f"> {label}"}:
        return True
    return re.search(r"\*\*" + re.escape(label) + r"(?:\*\*|:)", stripped) is not None


def missing_panel_headings(baseline: str, candidate: str) -> list[str]:
    """Bold blockquote labels in the mastered copy, such as `> **Warning**`.

    A chat rewrite keeps the label when the same bold name remains on a
    blockquote line, including `> └ **Name:** message`.
    """
    base = _panel_heading_counts(baseline)
    missing: list[str] = []
    for heading, count in base.items():
        label = _panel_label(heading)
        if label is None:
            continue
        found = sum(1 for line in candidate.splitlines() if _blockquote_has_label(line, label))
        if found < count:
            missing.append(heading)
    return missing


def _chat_titles(baseline: str) -> list[str]:
    """Panel lines that name a thread above later speaker labels."""
    lines = [line.strip() for line in baseline.splitlines()]
    titles: list[str] = []
    for index, line in enumerate(lines):
        if _panel_label(line) is None:
            continue
        for nxt in lines[index + 1 : index + 6]:
            if not nxt or nxt == ">":
                continue
            if _panel_label(nxt) is not None:
                titles.append(line)
            break
    return titles


def _system_panels(text: str) -> list[tuple[str, list[str]]]:
    """Each System panel with the prose line that introduces it."""
    lines = text.splitlines()
    panels: list[tuple[str, list[str]]] = []
    previous = ""
    index = 0
    while index < len(lines):
        if lines[index].strip() == SYSTEM_HEADING:
            block = [lines[index]]
            index += 1
            while index < len(lines):
                if lines[index].lstrip().startswith(">"):
                    block.append(lines[index])
                    index += 1
                    continue
                if (
                    lines[index].strip() == ""
                    and index + 1 < len(lines)
                    and lines[index + 1].lstrip().startswith(">")
                ):
                    block.append(lines[index])
                    index += 1
                    continue
                break
            panels.append((previous, block))
            continue
        if lines[index].strip() and not lines[index].lstrip().startswith(">"):
            previous = lines[index]
        index += 1
    return panels


def _panel_words(block: list[str]) -> set[str]:
    text = re.sub(r"[>*_#\[\]`]", " ", " ".join(block))
    return {word.lower() for word in re.findall(r"[A-Za-z]{4,}", text) if word.lower() != "system"}


def _panel_body(panel: list[str]) -> tuple[str, ...]:
    body: list[str] = []
    for line in panel:
        stripped = line.strip()
        if stripped in {SYSTEM_HEADING, ">", ""}:
            continue
        body.append(stripped)
    return tuple(body)


def _body_present(lines: list[str], body: tuple[str, ...]) -> bool:
    if not body:
        return False
    stripped = [line.strip() for line in lines]
    width = len(body)
    return any(tuple(stripped[index : index + width]) == body for index in range(len(stripped)))


def _restore_system_panels(baseline: str, lines: list[str]) -> list[str]:
    for previous, panel in _system_panels(baseline):
        if not previous or _body_present(lines, _panel_body(panel)):
            continue
        words = _panel_words(panel)
        try:
            anchor = lines.index(previous)
        except ValueError:
            continue
        insert_at = anchor + 1
        if insert_at < len(lines) and lines[insert_at].strip() == "":
            insert_at += 1
        if insert_at < len(lines):
            nxt = lines[insert_at].strip()
            shared = words & _panel_words([nxt])
            if nxt.startswith("*") and nxt.endswith("*") and len(shared) >= 2:
                del lines[insert_at]
                if insert_at < len(lines) and lines[insert_at].strip() == "":
                    del lines[insert_at]
        lines[insert_at:insert_at] = ["", *panel, ""]
    return lines


def normalize_reading_copy(baseline: str, candidate: str) -> str:
    """Keep the chapter heading as the only ATX heading and restore panel labels."""
    lines: list[str] = []
    for line in candidate.splitlines():
        match = re.match(r"^#{2,6}\s+(.+?)\s*$", line.strip())
        if match:
            lines.append(f"**{match.group(1).strip()}**")
            continue
        lines.append(line)
    lines = _restore_system_panels(baseline, lines)
    missing_titles = [
        title
        for title in _chat_titles(baseline)
        if not any(_blockquote_has_label(line, _panel_label(title) or "") for line in lines)
    ]
    if missing_titles:
        for index, line in enumerate(lines):
            if line.strip().startswith("> └"):
                lines[index:index] = missing_titles
                break
    text = "\n".join(lines)
    if candidate.endswith("\n"):
        text += "\n"
    return text


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
    missing_headings = missing_panel_headings(baseline, candidate)
    if missing_headings:
        errors.append(_finding(
            "panel_heading",
            "a document or panel heading from the mastered chapter was removed",
            headings=missing_headings,
        ))
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
