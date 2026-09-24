#!/usr/bin/env python3
"""Parse and validate structured model responses."""

from __future__ import annotations

import json
import re

SEVERITIES = {"critical", "major", "minor"}
SEVERITY_RANK = {"critical": 3, "major": 2, "minor": 1}
DISPOSITIONS = {"applied", "rejected", "unresolved"}
ADDRESS_ENDPOINT = re.compile(
    r"(?=.*[가-힣])[가-힣0-9](?:[가-힣0-9]| [가-힣0-9])*"
)
PAREN_HANGUL = re.compile(r"\(([가-힣0-9](?:[가-힣0-9]| [가-힣0-9])*)\)")


def _strip_json_fence(text: str) -> str:
    fenced = re.fullmatch(r"```(?:json)?\s*(.*?)\s*```", text, re.DOTALL | re.IGNORECASE)
    if fenced:
        return fenced.group(1).strip()
    return text


def extract_reading_copy(raw: str, number: int) -> str:
    """Drop a short model preamble and return the English reading copy."""
    text = raw.strip()
    fenced = re.fullmatch(r"```(?:markdown|md)?\s*(.*?)\s*```", text, re.DOTALL | re.IGNORECASE)
    if fenced:
        text = fenced.group(1).strip()
    heading = f"# Chapter {number}"
    index = text.find(heading)
    if index < 0:
        raise ValueError(f"reading copy is missing {heading!r}")
    prefix = text[:index]
    if prefix.count("\n") > 2 or index > 400:
        raise ValueError(f"preamble before {heading!r} is too long to salvage")
    text = text[index:]
    return text if text.endswith("\n") else text + "\n"


def parse_json_object(raw: str) -> dict:
    """Parse the first JSON object, ignoring trailing looped or prose junk."""
    text = _strip_json_fence(raw.strip())
    if not text:
        raise ValueError("model did not return valid JSON: empty response")
    try:
        value = json.loads(text)
        if isinstance(value, dict):
            return value
    except json.JSONDecodeError:
        pass
    start = text.find("{")
    preview = repr(raw[:400])
    if start < 0:
        raise ValueError(f"model did not return valid JSON: {preview}")
    try:
        value, _end = json.JSONDecoder().raw_decode(text, start)
    except json.JSONDecodeError as error:
        raise ValueError(f"model did not return valid JSON: {error}\nPreview: {preview}") from None
    if not isinstance(value, dict):
        raise ValueError(f"model response must be one JSON object\nPreview: {preview}")
    return value


def validate_review(value: dict) -> dict:
    findings = value.get("findings")
    if not isinstance(findings, list):
        raise ValueError("review response requires a findings array")
    normalized: list[dict] = []
    seen: set[str] = set()
    required = ("id", "severity", "source", "current", "replacement", "defect", "rationale")
    for position, finding in enumerate(findings, 1):
        if not isinstance(finding, dict):
            raise ValueError(f"finding {position} must be an object")
        for key in required:
            if not isinstance(finding.get(key), str) or not finding[key].strip():
                raise ValueError(f"finding {position} requires nonempty {key}")
        identifier = finding["id"].strip()
        if identifier in seen:
            raise ValueError(f"duplicate finding id: {identifier}")
        seen.add(identifier)
        severity = finding["severity"].lower().strip()
        if severity not in SEVERITIES:
            raise ValueError(f"invalid severity for {identifier}: {severity}")
        confidence = finding.get("confidence")
        if not isinstance(confidence, (int, float)) or isinstance(confidence, bool) or not 0 <= confidence <= 1:
            raise ValueError(f"confidence for {identifier} must be between 0 and 1")
        if finding["current"] == finding["replacement"]:
            raise ValueError(f"finding {identifier} replacement must differ from current text")
        normalized.append({
            **finding,
            "id": identifier,
            "severity": severity,
            "confidence": float(confidence),
        })
    summary = value.get("summary", "No actionable findings" if not normalized else "")
    if not isinstance(summary, str):
        raise ValueError("review summary must be a string")
    return {"version": 1, "summary": summary.strip(), "findings": normalized}


def _finding_rank(finding: dict) -> tuple[int, float]:
    severity = SEVERITY_RANK.get(str(finding.get("severity", "")), 0)
    confidence = finding.get("confidence", 0.0)
    if not isinstance(confidence, (int, float)) or isinstance(confidence, bool):
        confidence = 0.0
    return (severity, float(confidence))


def _collapse_overlapping_spans(
    spans: list[tuple[int, int, str, str, tuple[int, float]]],
) -> list[tuple[int, int, str, str]]:
    best_for_range: dict[tuple[int, int], tuple[int, int, str, str, tuple[int, float]]] = {}
    for span in spans:
        key = (span[0], span[1])
        current = best_for_range.get(key)
        if current is None or span[4] > current[4] or (
            span[4] == current[4] and span[3] < current[3]
        ):
            best_for_range[key] = span
    ordered = sorted(
        best_for_range.values(),
        key=lambda item: (-item[4][0], -item[4][1], -(item[1] - item[0]), item[0], item[3]),
    )
    kept: list[tuple[int, int, str, str, tuple[int, float]]] = []
    for span in ordered:
        if any(span[0] < other[1] and other[0] < span[1] for other in kept):
            continue
        kept.append(span)
    kept.sort(key=lambda item: item[0])
    return [(start, end, replacement, identifier) for start, end, replacement, identifier, _ in kept]


def apply_review_replacements(text: str, review: dict) -> str:
    spans: list[tuple[int, int, str, str, tuple[int, float]]] = []
    for finding in review["findings"]:
        old = finding["current"]
        replacement = re.sub(r"\s*\([^()\n]*[가-힣][^()\n]*\)", "", finding["replacement"])
        rank = _finding_rank(finding)
        starts = [match.start() for match in re.finditer(re.escape(old), text)]
        matched_old = old
        matched_replacement = replacement
        if not starts:
            candidates = []
            if "… " in old:
                candidates.append((old.replace("… ", "…"), replacement))
            if "…." in old:
                candidates.append((old.replace("….", "…"), replacement))
            candidates.append((f"*{old}*", replacement))
            if len(old) >= 2 and old.startswith("*") and old.endswith("*"):
                candidates.append((old[1:-1], replacement[1:-1] if replacement.startswith("*") and replacement.endswith("*") else replacement))
            if len(old) >= 2 and old[0] == "“" and old[-1] == "”":
                candidates.append((f"*{old[1:-1]}*", replacement))
                candidates.append((old[1:-1], replacement[1:-1] if replacement.startswith("“") and replacement.endswith("”") else replacement))
            for candidate, candidate_replacement in candidates:
                candidate_starts = [match.start() for match in re.finditer(re.escape(candidate), text)]
                if len(candidate_starts) == 1:
                    starts = candidate_starts
                    matched_old = candidate
                    matched_replacement = candidate_replacement
                    break
        if len(starts) != 1:
            punctuation_only = old.replace("...", "…") == replacement
            if punctuation_only and starts:
                spans.extend((start, start + len(old), replacement, finding["id"], rank) for start in starts)
                continue
            thought_formatting = (
                old.startswith("“") and old.endswith("”")
                and replacement == f"*{old[1:-1]}*"
            )
            if thought_formatting and starts:
                spans.extend((start, start + len(old), replacement, finding["id"], rank) for start in starts)
                continue
            paragraph_starts = [
                start for start in starts
                if (start == 0 or text[start - 2:start] == "\n\n")
                and (start + len(old) == len(text) or text[start + len(old):start + len(old) + 2] == "\n\n")
            ]
            paired_findings = [
                item for item in review["findings"]
                if item["current"] == old
                and re.sub(r"\s*\([^()\n]*[가-힣][^()\n]*\)", "", item["replacement"]) == replacement
            ]
            paired_sources = [item.get("source") for item in paired_findings]
            if (
                len(paragraph_starts) > 1
                and len(paragraph_starts) == len(paired_findings)
                and len(set(paired_sources)) == len(paired_sources)
            ):
                spans.extend(
                    (start, start + len(old), replacement, finding["id"], rank)
                    for start in paragraph_starts
                )
                continue
            if len(paragraph_starts) != 1:
                raise ValueError(f"finding {finding['id']} current text occurs {len(starts)} times")
            start = paragraph_starts[0]
        else:
            start = starts[0]
        spans.append((start, start + len(matched_old), matched_replacement, finding["id"], rank))
    collapsed = _collapse_overlapping_spans(spans)
    revised = text
    for start, end, replacement, _ in reversed(collapsed):
        revised = revised[:start] + replacement + revised[end:]
    return revised.rstrip() + "\n"


def _nonempty_strings(value: object, label: str, *, allow_empty: bool = True) -> list[str]:
    if not isinstance(value, list) or (not allow_empty and not value):
        raise ValueError(f"{label} must be {'a nonempty ' if not allow_empty else 'an '}array")
    if any(not isinstance(item, str) or not item.strip() for item in value):
        raise ValueError(f"{label} must contain nonempty strings")
    return [item.strip() for item in value]


def _coerce_address_endpoint(value: str, extra: list[tuple[str, str]]) -> str:
    text = value.strip()
    if ADDRESS_ENDPOINT.fullmatch(text):
        return text
    parenthetical = PAREN_HANGUL.search(text)
    if parenthetical and ADDRESS_ENDPOINT.fullmatch(parenthetical.group(1)):
        return parenthetical.group(1)
    try:
        from tools.names import unique_korean_for_english
    except ModuleNotFoundError:
        from names import unique_korean_for_english
    resolved = unique_korean_for_english(text, extra)
    if resolved:
        return resolved
    raise ValueError("must be Korean")


def validate_durable_update(value: dict, number: int) -> dict:
    if value.get("chapter") != number:
        raise ValueError(f"durable update chapter must be {number}")
    beat = value.get("beat")
    if not isinstance(beat, dict):
        raise ValueError("durable update requires a beat object")
    normalized_beat = {
        "plot": _nonempty_strings(beat.get("plot"), "beat.plot", allow_empty=False),
        "continuity": _nonempty_strings(beat.get("continuity"), "beat.continuity"),
        "translation_decisions": _nonempty_strings(
            beat.get("translation_decisions", []), "beat.translation_decisions"
        ),
    }
    context = value.get("context")
    if not isinstance(context, dict):
        raise ValueError("durable update requires a context object")
    try:
        from tools.context import CONTEXT_REQUIRED_KEYS
    except ModuleNotFoundError:
        from context import CONTEXT_REQUIRED_KEYS
    missing = [key for key in CONTEXT_REQUIRED_KEYS if key not in context]
    if missing:
        raise ValueError("durable context missing " + ", ".join(missing))
    context = {key: context[key] for key in CONTEXT_REQUIRED_KEYS}
    names = value.get("names")
    if not isinstance(names, list):
        raise ValueError("durable update names must be an array")
    normalized_names = []
    for position, item in enumerate(names, 1):
        if not isinstance(item, dict):
            raise ValueError(f"name {position} must be an object")
        row = {}
        for key in ("korean", "english", "notes"):
            field = item.get(key)
            if not isinstance(field, str) or (key != "notes" and not field.strip()):
                raise ValueError(f"name {position} requires {key}")
            if "\n" in field or "|" in field:
                raise ValueError(f"name {position} {key} cannot contain a newline or pipe")
            row[key] = field.strip()
        normalized_names.append(row)
    address_pairs = value.get("address_pairs", [])
    if not isinstance(address_pairs, list):
        raise ValueError("durable update address_pairs must be an array")
    normalized_address = []
    seen_pairs: set[tuple[str, str]] = set()
    extra = [(row["korean"], row["english"]) for row in normalized_names]
    for position, item in enumerate(address_pairs, 1):
        if not isinstance(item, dict):
            raise ValueError(f"address pair {position} must be an object")
        row = {}
        for key in ("speaker", "addressee", "kinship", "normal_address", "speech_level", "notes"):
            field = item.get(key, "")
            if not isinstance(field, str):
                raise ValueError(f"address pair {position} requires {key}")
            if key != "notes" and not field.strip():
                raise ValueError(f"address pair {position} requires {key}")
            if "\n" in field or "|" in field:
                raise ValueError(f"address pair {position} {key} cannot contain a newline or pipe")
            row[key] = field.strip()
        try:
            row["speaker"] = _coerce_address_endpoint(row["speaker"], extra)
            row["addressee"] = _coerce_address_endpoint(row["addressee"], extra)
        except ValueError:
            raise ValueError(
                f"address pair {position} speaker and addressee must be Korean "
                "(Hangul required; Arabic digits allowed in titles like 1팀장)"
            ) from None
        key = (row["speaker"], row["addressee"])
        if key in seen_pairs:
            raise ValueError(f"duplicate address pair: {row['speaker']} -> {row['addressee']}")
        seen_pairs.add(key)
        normalized_address.append(row)
    profile_updates = value.get("profile_updates")
    if not isinstance(profile_updates, list):
        raise ValueError("durable update profile_updates must be an array")
    normalized_updates = []
    for position, item in enumerate(profile_updates, 1):
        if not isinstance(item, dict):
            raise ValueError(f"profile update {position} must be an object")
        path, current, replacement = (item.get(key) for key in ("path", "current", "replacement"))
        if not all(isinstance(field, str) and field.strip() for field in (path, current, replacement)):
            raise ValueError(f"profile update {position} requires path, current, and replacement")
        if current == replacement or "\n" in current or "\n" in replacement:
            raise ValueError(f"profile update {position} must replace one complete line")
        normalized_updates.append({
            "path": path.strip(),
            "current": current,
            "replacement": replacement,
        })
    creations = value.get("profile_creations")
    if not isinstance(creations, list):
        raise ValueError("durable update profile_creations must be an array")
    normalized_creations = []
    for position, item in enumerate(creations, 1):
        if not isinstance(item, dict):
            raise ValueError(f"profile creation {position} must be an object")
        normalized = {}
        for key in ("filename", "korean", "english", "role", "personality", "voice", "relationships"):
            field = item.get(key)
            if not isinstance(field, str) or not field.strip():
                raise ValueError(f"profile creation {position} requires {key}")
            normalized[key] = field.strip()
        normalized["aliases"] = _nonempty_strings(
            item.get("aliases"), f"profile creation {position} aliases"
        )
        normalized_creations.append(normalized)
    return {
        "version": 1,
        "chapter": number,
        "beat": normalized_beat,
        "context": context,
        "names": normalized_names,
        "address_pairs": normalized_address,
        "profile_updates": normalized_updates,
        "profile_creations": normalized_creations,
    }


def validate_dispositions(dispositions: object, review: dict) -> list[dict]:
    if not isinstance(dispositions, list):
        raise ValueError("response requires a dispositions array")
    expected = {finding["id"] for finding in review["findings"]}
    normalized: list[dict] = []
    seen: set[str] = set()
    for item in dispositions:
        if not isinstance(item, dict):
            raise ValueError("every disposition must be an object")
        identifier = item.get("finding_id")
        status = item.get("status")
        reason = item.get("reason")
        if identifier not in expected or identifier in seen:
            raise ValueError(f"unknown or duplicate disposition id: {identifier}")
        if status not in DISPOSITIONS:
            raise ValueError(f"invalid disposition for {identifier}: {status}")
        if not isinstance(reason, str) or not reason.strip():
            raise ValueError(f"disposition {identifier} requires a reason")
        seen.add(identifier)
        normalized.append({"finding_id": identifier, "status": status, "reason": reason.strip()})
    missing = expected.difference(seen)
    if missing:
        raise ValueError("missing dispositions: " + ", ".join(sorted(missing)))
    return normalized


def blocking_dispositions(review: dict, revision: dict) -> list[str]:
    severities = {finding["id"]: finding["severity"] for finding in review["findings"]}
    return [
        item["finding_id"]
        for item in revision["dispositions"]
        if item["status"] == "unresolved" and severities[item["finding_id"]] in {"critical", "major"}
    ]




def review_markdown(review: dict) -> str:
    if not review["findings"]:
        return "# Review\n\nNo actionable findings.\n"
    sections = ["# Review", "", review["summary"]]
    for finding in review["findings"]:
        chapter_line = [f"- **Chapter:** {finding['chapter']}"] if "chapter" in finding else []
        sections.extend([
            "", f"## {finding['id']} — {finding['severity'].title()}", "",
            *chapter_line,
            f"- **Confidence:** {finding['confidence']:.2f}",
            f"- **Source:** {finding['source']}",
            f"- **Current:** {finding['current']}",
            f"- **Defect:** {finding['defect']}",
            f"- **Replacement:** {finding['replacement']}",
            f"- **Rationale:** {finding['rationale']}",
        ])
    return "\n".join(sections).rstrip() + "\n"


def validate_range_review(value: dict, chapters: set[int]) -> dict:
    review = validate_review(value)
    for finding in review["findings"]:
        chapter = finding.get("chapter")
        if not isinstance(chapter, int) or isinstance(chapter, bool) or chapter not in chapters:
            raise ValueError(f"finding {finding['id']} has invalid chapter: {chapter}")
    return review


def validate_patchset(value: dict, review: dict) -> dict:
    patches = value.get("patches")
    if not isinstance(patches, list):
        raise ValueError("patch response requires a patches array")
    finding_by_id = {item["id"]: item for item in review["findings"]}
    normalized_patches: list[dict] = []
    covered: set[str] = set()
    for position, patch in enumerate(patches, 1):
        if not isinstance(patch, dict):
            raise ValueError(f"patch {position} must be an object")
        chapter = patch.get("chapter")
        finding_ids = patch.get("finding_ids")
        old = patch.get("old")
        new = patch.get("new")
        if not isinstance(chapter, int) or isinstance(chapter, bool):
            raise ValueError(f"patch {position} requires an integer chapter")
        if not isinstance(finding_ids, list) or not finding_ids:
            raise ValueError(f"patch {position} requires finding_ids")
        if any(identifier not in finding_by_id for identifier in finding_ids):
            raise ValueError(f"patch {position} references an unknown finding")
        if any(finding_by_id[identifier].get("chapter") != chapter for identifier in finding_ids):
            raise ValueError(f"patch {position} mixes findings from another chapter")
        if not isinstance(old, str) or not old:
            raise ValueError(f"patch {position} requires exact nonempty old text")
        if not isinstance(new, str) or old == new:
            raise ValueError(f"patch {position} requires different replacement text")
        covered.update(finding_ids)
        normalized_patches.append({"chapter": chapter, "finding_ids": finding_ids, "old": old, "new": new})
    dispositions = validate_dispositions(value.get("dispositions"), review)
    applied = {item["finding_id"] for item in dispositions if item["status"] == "applied"}
    if applied != covered:
        raise ValueError("applied dispositions must exactly match findings covered by patches")
    summary = value.get("summary", "")
    if not isinstance(summary, str):
        raise ValueError("patch summary must be a string")
    return {"version": 1, "summary": summary.strip(), "patches": normalized_patches, "dispositions": dispositions}
