#!/usr/bin/env python3
"""Address pass: render 소협 by context in finished chapters.

The pipeline once rendered 소협 one-for-one as “Young Hero X”. This pass fixes
only those address phrases, following `RULES.md` → Address: keep the formal,
deferential, and sarcastic uses; use the name between familiar peers and in
third-person reference; never attach it to a nickname unless the Korean does
so on purpose. No other edits.

Per chapter:

1. One model call (docs/address.json `model`) receives the Korean, the
   English, the rule, the matched address pairs from docs/ADDRESS.md, the
   compact character cards, and every “Young Hero” occurrence. It returns
   exact `current` → `replacement` spans with a reason and confidence.
2. Each finding must contain the address phrase, cite Korean with 소협 that is
   in the source, and edit only within a few characters of the phrase.
   Missing, repeated, overlapping, or out-of-window spans go to human review.
3. Confident findings are applied atomically; final QA must not gain an error.

State lives under reviews/address/NNNN/. Commit is separate
(run_address_pass.py).
"""

from __future__ import annotations

import argparse
import difflib
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "docs" / "address.json"
RULES_PATH = ROOT / "RULES.md"
ADDRESS_ROOT = ROOT / "reviews" / "address"
DRY_ROOT = ROOT / ".work" / "address-dry"

try:
    from tools.entity_pass import (
        HANGUL,
        FOOTNOTE_REF,
        apply_findings,
        call_model,
        changed_chars,
        entity_qa,
        final_promoted,
        packet_tokens,
    )
    from tools.entity_pass import load_state as load_entity_state
    from tools.final_qa import FOOTNOTE_DEF
    from tools.final_touches import matching_profiles, profiles_text
    from tools.mastering import atomic_json, atomic_text, current_source, exact_glossary, read_text, sha256_text
except ModuleNotFoundError:
    sys.path.insert(0, str(ROOT / "tools"))
    from entity_pass import (
        HANGUL,
        FOOTNOTE_REF,
        apply_findings,
        call_model,
        changed_chars,
        entity_qa,
        final_promoted,
        packet_tokens,
    )
    from entity_pass import load_state as load_entity_state
    from final_qa import FOOTNOTE_DEF
    from final_touches import matching_profiles, profiles_text
    from mastering import atomic_json, atomic_text, current_source, exact_glossary, read_text, sha256_text

USES = ("familiar", "third_person", "epithet")
IN_FLIGHT = {"PREPARED", "DETECTED", "READY_TO_COMMIT", "QA_FAILED", "FAILED"}
ENTITY_IN_FLIGHT = {"PREPARED", "DETECTED", "ESCALATED", "READY_TO_COMMIT", "QA_FAILED", "FAILED"}


def _squash(text: str) -> str:
    return re.sub(r"\s+", "", text)


def _span_lines(text: str, start: int, end: int) -> list[str]:
    line_start = text.rfind("\n", 0, start) + 1
    line_end = text.find("\n", end)
    return text[line_start: len(text) if line_end < 0 else line_end].splitlines()


def _save_metrics(path: Path, number: int, stage: str, metrics: dict) -> None:
    data = {"version": 1, "chapter": number, "stages": {}}
    if path.exists():
        data = json.loads(path.read_text(encoding="utf-8"))
        data.setdefault("stages", {})
    data["stages"][stage] = metrics
    atomic_json(path, data)


# ---------------------------------------------------------------- config


def load_config(path: Path = CONFIG_PATH) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if value.get("version") != 1:
        raise SystemExit("docs/address.json version must be 1")
    if not isinstance(value.get("model"), str) or not value["model"].strip():
        raise SystemExit("docs/address.json model must name a model")
    terms = value.get("terms")
    if not isinstance(terms, dict) or not terms or not all(
        isinstance(k, str) and HANGUL.search(k) and isinstance(v, str) and v.strip() for k, v in terms.items()
    ):
        raise SystemExit("docs/address.json terms must map Korean address words to their English phrase")
    for key, default in (("auto_apply_min_confidence", 0.8), ("min_baseline_preserved", 0.97)):
        number = float(value.get(key, default))
        if not 0 <= number <= 1:
            raise SystemExit(f"docs/address.json {key} must be between 0 and 1")
        value[key] = number
    value["timeout"] = int(value.get("timeout", 1800))
    value["model_retries"] = max(0, int(value.get("model_retries", 1)))
    value["packet_token_limit"] = int(value.get("packet_token_limit", 60000))
    value["max_changed_chars"] = int(value.get("max_changed_chars", 40))
    value["edit_window_chars"] = max(0, int(value.get("edit_window_chars", 24)))
    value["batch_workers"] = max(1, int(value.get("batch_workers", 3)))
    value.setdefault("estimate", {})
    return value


def phrase_pattern(cfg: dict) -> re.Pattern:
    phrases = sorted(set(cfg["terms"].values()), key=len, reverse=True)
    return re.compile(r"(?<![A-Za-z])(?:" + "|".join(re.escape(p) for p in phrases) + r")(?![A-Za-z])", re.IGNORECASE)


def chapter_paths(number: int, root: Path = ADDRESS_ROOT) -> dict[str, Path]:
    folder = root / f"{number:04d}"
    return {
        "root": folder,
        "state": folder / "state.json",
        "baseline": folder / "baseline.md",
        "packet": folder / "address-packet.md",
        "detect": folder / "detect.json",
        "result": folder / "result.json",
        "report": folder / "report.md",
        "qa": folder / "qa.json",
        "metrics": folder / "metrics.json",
        "log": folder / "omp" / "address.jsonl",
        "translation": ROOT / "translations" / f"{number:04d}.md",
    }


def load_state(number: int) -> dict:
    path = chapter_paths(number)["state"]
    if not path.exists():
        return {"version": 1, "chapter": number, "stage": "NOT_STARTED"}
    state = json.loads(path.read_text(encoding="utf-8"))
    return state if isinstance(state, dict) else {"version": 1, "chapter": number, "stage": "NOT_STARTED"}


def save_state(number: int, **fields: object) -> dict:
    state = load_state(number)
    state.update({"version": 1, "chapter": number, **fields})
    atomic_json(chapter_paths(number)["state"], state)
    return state


def address_owns_path(path: str, number: int) -> bool:
    return path == f"translations/{number:04d}.md" or path.startswith(f"reviews/address/{number:04d}/")


def active_address_chapters() -> list[int]:
    if not ADDRESS_ROOT.is_dir():
        return []
    found: list[int] = []
    for path in sorted(ADDRESS_ROOT.glob("[0-9][0-9][0-9][0-9]/state.json")):
        try:
            state = json.loads(path.read_text(encoding="utf-8"))
            number = int(path.parent.name)
        except (OSError, json.JSONDecodeError, ValueError):
            continue
        if state.get("stage") in IN_FLIGHT:
            found.append(number)
    return found


def foreign_address_paths(dirty: list[str]) -> set[str]:
    """Paths owned by the address queue."""
    active = set(active_address_chapters())
    return {
        path for path in dirty
        if path.startswith("reviews/address/") or any(address_owns_path(path, n) for n in active)
    }


def entity_in_flight(number: int) -> bool:
    return load_entity_state(number).get("stage") in ENTITY_IN_FLIGHT


def in_scope(source: str, cfg: dict) -> bool:
    return any(term in source for term in cfg["terms"])


# ---------------------------------------------------------------- packet


def rule_text(path: Path = RULES_PATH) -> str:
    """The `## Address` section of RULES.md, so drafts and this pass share one rule."""
    text = read_text(path)
    match = re.search(r"^## Address\n(.*?)(?=^## |\Z)", text, re.MULTILINE | re.DOTALL)
    if not match:
        raise SystemExit("RULES.md has no '## Address' section")
    return match.group(1).strip()


def occurrences(translation: str, cfg: dict) -> list[dict]:
    pattern = phrase_pattern(cfg)
    found = []
    for line_no, line in enumerate(translation.splitlines(), 1):
        for match in pattern.finditer(line):
            found.append({"line": line_no, "text": line.strip()})
            break
    return found


def korean_lines(source: str, cfg: dict) -> list[str]:
    return [line.strip() for line in source.splitlines() if any(term in line for term in cfg["terms"])]


def address_pairs(source: str, number: int) -> str:
    try:
        from tools.context import address_pairs_text, matched_address_pairs
        from tools.mastering import safe_profiles
    except ModuleNotFoundError:
        from context import address_pairs_text, matched_address_pairs
        from mastering import safe_profiles
    return address_pairs_text(matched_address_pairs(source, safe_profiles(source, number)))


SCHEMA = """{
  "summary": "one sentence",
  "uncertain": false,
  "uncertain_reason": "",
  "findings": [
    {
      "use": "familiar|third_person|epithet",
      "current": "exact unique English span containing the address phrase",
      "replacement": "the same span with only the address phrase changed",
      "korean": "exact Korean words with 소협 that this phrase renders",
      "speaker": "who says it, or narration",
      "addressee": "who is addressed or referred to",
      "present": false,
      "reason": "the speaker's relationship, and why this use is familiar, a third-person reference, or an epithet, not formal",
      "confidence": 0.0
    }
  ]
}"""


def build_packet(number: int, source: str, translation: str, cfg: dict, profiles: list[dict],
                 pairs: str, omitted: int = 0) -> str:
    terms = ", ".join(f"`{k}` → “{v}”" for k, v in cfg["terms"].items())
    leads = occurrences(translation, cfg)
    lead_text = "\n".join(f"- line {item['line']}: {item['text']}" for item in leads) or "(None.)"
    korean = "\n".join(f"- {line}" for line in korean_lines(source, cfg)) or "(None.)"
    return f"""# Address Pass — Chapter {number}

An earlier pipeline rendered {terms} one-for-one. Decide each English
occurrence listed below against the rule and the Korean scene, and report
only the ones that must change. Do not use tools. Return exactly one JSON
object with no Markdown fence, in this shape:

{SCHEMA}

Use an empty findings array when every occurrence is right.

## The rule

{rule_text()}

## How to decide

- Work out the speaker, the addressee, and their relationship from the Korean
  scene, the address pairs, and the cards. A first meeting, a stranger, an
  official, a servant, an innkeeper, an elder being courteous, a formal
  introduction, a stern or icy register, and sarcasm keep “Young Hero”.
- Korean name + 소협 often replaces “you”. If that person is the addressee,
  or is present and spoken about to their face (“진 소협의 활약”, “여기 있는
  진 소협”), it is second person: keep the honorific direct address. Never
  report it as `third_person`, and never rewrite “your …, Young Hero Jin”
  into a third-person name.
- The speaker decides, not the grammar: a deferential or formal speaker
  (official, guard, captain relaying orders, servant, merchant, stranger,
  rival keeping his distance, elder being polite) keeps “Young Hero X” even
  when referring to someone in the third person. Do not report those.
- Familiar friends, comrades, and companions who already know each other use
  the name (“Cheongpung”, “Gung Gibang”, the established short form) or
  “young sir” only when the address itself carries meaning. `use: familiar`.
- A familiar speaker referring to someone who is absent, or narration, uses
  the name. `use: third_person`. Name the speaker's relationship in `reason`.
- “Young Hero” attached to a nickname, place, or epithet is wrong unless the
  Korean does it on purpose. `use: epithet`.
- When unsure, leave it unchanged. Never report a formal or deferential use.
- Leave 대협, 소저, 공자, and every other honorific alone.

## Span rules

1. `current` is the shortest exact span of the English, copied character for
   character, that contains the address phrase and occurs exactly once in the
   chapter. Extend it with nearby words until it is unique. Never span more
   than one line.
2. `replacement` changes only the address phrase and its minimal grammatical
   surroundings: drop “Young Hero”, use the right name form, fix capitalization
   or a comma. Keep every other word, punctuation mark, italic marker, and
   footnote reference (`[^n]`) intact.
3. `korean` quotes the exact Korean words containing 소협 for this occurrence.
4. Set `confidence` honestly: 0.9+ only when the relationship is explicit in
   this chapter.
5. Set `present` to true when the person named is the addressee or is in
   the scene being spoken about to their face.
6. Set `uncertain` when the chapter has speakers or relationships you cannot
   resolve.

## English occurrences to decide

{lead_text}

## Korean lines with the address

{korean}

## Matched address pairs

{pairs}

## Character cards

{profiles_text(profiles, omitted)}

## Korean source

```text
{source.rstrip()}
```

## Current English — Chapter {number}

```markdown
{translation.rstrip()}
```
"""


def packet_for(number: int, inputs: dict, cfg: dict) -> str:
    kept = list(inputs["profiles"])
    while True:
        packet = build_packet(number, inputs["source"], inputs["translation"], cfg, kept,
                              inputs["pairs"], omitted=len(inputs["profiles"]) - len(kept))
        if packet_tokens(packet) <= cfg["packet_token_limit"]:
            return packet
        if not kept:
            raise SystemExit(f"address packet estimate {packet_tokens(packet)} exceeds limit {cfg['packet_token_limit']}")
        kept.pop()


def chapter_inputs(number: int, translation: str | None = None) -> dict:
    source = current_source(number)
    text = read_text(chapter_paths(number)["translation"]) if translation is None else translation
    return {
        "source": source,
        "translation": text,
        "glossary": exact_glossary(source),
        "profiles": matching_profiles(source),
        "pairs": address_pairs(source, number),
    }


# ------------------------------------------------------------- validation


def _confidence(value: object, label: str) -> float:
    if not isinstance(value, (int, float)) or isinstance(value, bool) or not 0 <= value <= 1:
        raise ValueError(f"{label} confidence must be a number between 0 and 1")
    return float(value)


def _finding(raw: object, label: str, cfg: dict) -> dict:
    if not isinstance(raw, dict):
        raise ValueError(f"{label} must be an object")
    for key in ("use", "current", "replacement", "korean", "reason"):
        if not isinstance(raw.get(key), str) or not raw[key].strip():
            raise ValueError(f"{label} requires nonempty {key}")
    use = raw["use"].strip().lower()
    if use not in USES:
        raise ValueError(f"{label} has invalid use {use!r}")
    if raw["current"] == raw["replacement"]:
        raise ValueError(f"{label} replacement must differ from current")
    if HANGUL.search(raw["replacement"]):
        raise ValueError(f"{label} replacement contains Hangul")
    return {
        "use": use,
        "current": raw["current"],
        "replacement": raw["replacement"],
        "korean": raw["korean"].strip(),
        "speaker": str(raw.get("speaker") or "").strip(),
        "addressee": str(raw.get("addressee") or "").strip(),
        "present": raw.get("present") if isinstance(raw.get("present"), bool) else None,
        "reason": raw["reason"].strip(),
        "confidence": _confidence(raw.get("confidence"), label),
    }


def _invalid_finding(raw: object, error: str) -> dict:
    value = raw if isinstance(raw, dict) else {}

    def text(key: str) -> str:
        return value[key] if isinstance(value.get(key), str) else ""

    confidence = value.get("confidence")
    return {
        "use": text("use").strip().lower() or "invalid",
        "current": text("current"),
        "replacement": text("replacement"),
        "korean": text("korean").strip(),
        "speaker": text("speaker").strip(),
        "addressee": text("addressee").strip(),
        "present": None,
        "reason": text("reason").strip() or "—",
        "confidence": float(confidence) if isinstance(confidence, (int, float)) and not isinstance(confidence, bool)
        and 0 <= confidence <= 1 else 0.0,
        "invalid": error,
    }


# A deferential or formal speaker keeps “Young Hero X” even in the third person.
DEFERENTIAL_SPEAKER = re.compile(
    r"\b(?:official|magistrate|guard|guards|captain|soldier|servant|maid|attendant|steward|butler|"
    r"merchant|shopkeeper|innkeeper|clerk|manager|supervisor|judge|examiner|herald|messenger|"
    r"stranger|passerby|onlooker|instructor|host|official's|elder|elders|lord|minister)\b",
    re.IGNORECASE,
)
SECOND_PERSON = re.compile(r"\b(?:you|your|yours|yourself)\b", re.IGNORECASE)


def validate_detection(value: dict, source: str, translation: str, cfg: dict) -> dict:
    findings = value.get("findings")
    if not isinstance(findings, list):
        raise ValueError("address response requires a findings array")
    uncertain = value.get("uncertain", False)
    if not isinstance(uncertain, bool):
        raise ValueError("uncertain must be true or false")
    normalized = []
    for position, raw in enumerate(findings, 1):
        try:
            item = _finding(raw, f"finding {position}", cfg)
        except ValueError as exc:
            # One malformed finding goes to human review; the valid ones still apply.
            item = _invalid_finding(raw, str(exc))
        item["id"] = f"A{position:02d}"
        item["span_count"] = translation.count(item["current"])
        item["evidence_found"] = _squash(item["korean"]) in _squash(source)
        normalized.append(item)
    summary = value.get("summary", "")
    reason = value.get("uncertain_reason", "")
    return {
        "version": 1,
        "uncertain": uncertain,
        "uncertain_reason": reason.strip() if isinstance(reason, str) else "",
        "summary": summary.strip() if isinstance(summary, str) else "",
        "findings": normalized,
    }


def edits_local(current: str, replacement: str, pattern: re.Pattern, window: int) -> bool:
    """Every edit lies within `window` characters of an address phrase in `current`."""
    phrases = [(m.start(), m.end()) for m in pattern.finditer(current)]
    if not phrases:
        return False
    matcher = difflib.SequenceMatcher(None, current, replacement, autojunk=False)
    for tag, i1, i2, _j1, _j2 in matcher.get_opcodes():
        if tag == "equal":
            continue
        if not any(start - window <= i1 and i2 <= end + window for start, end in phrases):
            return False
    return True


def screen(findings: list[dict], cfg: dict, translation: str) -> list[dict]:
    """Give every finding a status: auto or human, with a reason."""
    pattern = phrase_pattern(cfg)
    minimum = cfg["auto_apply_min_confidence"]
    for finding in findings:
        if finding.get("invalid"):
            finding.update(status="human", reason_status=f"invalid finding: {finding['invalid']}")
            continue
        current, replacement = finding["current"], finding["replacement"]
        count = translation.count(current)
        problem = ""
        third = finding["use"] == "third_person"
        if count == 0:
            problem = "current span is missing from the chapter"
        elif count > 1:
            problem = f"current span occurs {count} times"
        elif not pattern.search(current):
            problem = "current span has no address phrase"
        elif not any(term in finding["korean"] for term in cfg["terms"]):
            problem = "Korean evidence has no address word"
        elif not finding.get("evidence_found"):
            problem = "Korean evidence is not in the source"
        elif "\n" in current:
            problem = "span crosses a line"
        elif third and finding.get("present"):
            problem = "the person is present: name + 소협 is second person"
        elif third and SECOND_PERSON.search(current) and not SECOND_PERSON.search(replacement):
            problem = "span is second person: keep the honorific direct address"
        elif third and DEFERENTIAL_SPEAKER.search(finding.get("speaker", "")):
            problem = "deferential or formal speaker keeps the address in the third person"
        elif sorted(FOOTNOTE_REF.findall(current)) != sorted(FOOTNOTE_REF.findall(replacement)):
            problem = "replacement changes footnote references"
        elif changed_chars(current, replacement) > cfg["max_changed_chars"]:
            problem = f"edit changes more than {cfg['max_changed_chars']} characters"
        elif not edits_local(current, replacement, pattern, cfg["edit_window_chars"]):
            problem = "edit reaches beyond the address phrase"
        else:
            start = translation.index(current)
            if any(FOOTNOTE_DEF.match(line.strip()) for line in _span_lines(translation, start, start + len(current))):
                problem = "span touches a footnote definition"
            elif finding["confidence"] < minimum:
                problem = f"confidence {finding['confidence']:.2f} below {minimum:.2f}"
        finding.update(status="human" if problem else "auto", reason_status=problem)
    spans = []
    for finding in findings:
        if finding["status"] == "auto":
            start = translation.index(finding["current"])
            spans.append((start, start + len(finding["current"]), finding))
    for index, (start, end, finding) in enumerate(spans):
        for other_start, other_end, other in spans[index + 1:]:
            if start < other_end and other_start < end:
                for item in (finding, other):
                    item.update(status="human", reason_status="overlaps another finding")
    return findings


# ------------------------------------------------------------------ report


def report_markdown(number: int, findings: list[dict], detection: dict, applied: bool, cfg: dict,
                    baseline: str) -> str:
    lines = [f"# Address Pass — Chapter {number}", ""]
    lines.append(f"- Model: {detection.get('model') or cfg['model']}")
    lines.append(f"- Summary: {detection.get('summary') or '—'}")
    if detection.get("uncertain"):
        lines.append(f"- Uncertain: {detection.get('uncertain_reason') or 'yes'}")
    lines.append(f"- Occurrences: {len(phrase_pattern(cfg).findall(baseline))}")
    lines.append(f"- Applied: {'yes' if applied else 'no'}")
    lines.append("")
    for status, title in (("auto", "Applied"), ("human", "Needs human review"), ("reverted", "Reverted after review")):
        items = [item for item in findings if item["status"] == status]
        lines += [f"## {title} ({len(items)})", ""]
        if not items:
            lines += ["None.", ""]
            continue
        for item in items:
            lines.append(f"### {item['id']} · {item['use']} · {item['confidence']:.2f}")
            lines.append("")
            lines.append(f"- Current: “{item['current']}”")
            lines.append(f"- Replacement: “{item['replacement']}”")
            lines.append(f"- Korean: {item['korean']}")
            if item.get("speaker") or item.get("addressee"):
                lines.append(f"- Speaker → addressee: {item.get('speaker') or '?'} → {item.get('addressee') or '?'}")
            lines.append(f"- Why: {item['reason']}")
            if item.get("reason_status"):
                lines.append(f"- Status reason: {item['reason_status']}")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def diff_markdown(number: int, baseline: str, current: str, findings: list[dict]) -> str:
    """Changed lines, old and new, with the reason for each applied finding."""
    lines = [f"## Chapter {number}", ""]
    old, new = baseline.splitlines(), current.splitlines()
    matcher = difflib.SequenceMatcher(None, old, new, autojunk=False)
    changed = False
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            continue
        changed = True
        lines.append("```diff")
        lines += [f"- {line}" for line in old[i1:i2]]
        lines += [f"+ {line}" for line in new[j1:j2]]
        lines.append("```")
        lines.append("")
    if not changed:
        lines += ["No changes applied.", ""]
    auto = [item for item in findings if item["status"] == "auto"]
    human = [item for item in findings if item["status"] == "human"]
    if auto:
        lines += ["Applied:", ""]
        lines += [
            f"- **{item['id']}** {item['use']} ({item['confidence']:.2f}), "
            f"{item.get('speaker') or '?'} → {item.get('addressee') or '?'}: {item['reason']}"
            for item in auto
        ]
        lines.append("")
    if human:
        lines += ["Held for human review:", ""]
        lines += [
            f"- **{item['id']}** “{item['current']}” → “{item['replacement']}” — {item['reason']} "
            f"[{item.get('reason_status', '')}]"
            for item in human
        ]
        lines.append("")
    return "\n".join(lines)


# ------------------------------------------------------------- model call


def structured_call(number: int, paths: dict, cfg: dict, validate) -> dict:
    try:
        from tools.model_io import parse_json_object
    except ModuleNotFoundError:
        from model_io import parse_json_object
    model = cfg["model"]
    attempts = 1 + cfg["model_retries"]
    error = ""
    for attempt in range(1, attempts + 1):
        stage = "address" if attempt == 1 else f"address_retry_{attempt - 1}"
        output, metrics, call = call_model(
            paths["packet"], model, cfg["timeout"], paths["log"], label="address",
            hint=f"attempt {attempt}/{attempts}",
        )
        _save_metrics(paths["metrics"], number, stage, metrics)
        try:
            value = validate(parse_json_object(output))
        except ValueError as exc:
            error = str(exc)
            call.done(metrics, f"invalid JSON: {error[:80]}")
            continue
        call.done(metrics)
        value["model"] = model
        return value
    raise SystemExit(f"address pass for chapter {number} returned invalid JSON: {error}")


# --------------------------------------------------------------- pipeline


def dry_run_chapter(number: int, cfg: dict, out_root: Path = DRY_ROOT) -> dict:
    inputs = chapter_inputs(number)
    packet = packet_for(number, inputs, cfg)
    atomic_text(out_root / f"{number:04d}" / "address-packet.md", packet)
    return {
        "chapter": number,
        "packet_tokens": packet_tokens(packet),
        "korean": sum(inputs["source"].count(term) for term in cfg["terms"]),
        "english": len(phrase_pattern(cfg).findall(inputs["translation"])),
        "final_promoted": final_promoted(number),
    }


def command_run(number: int, cfg: dict | None = None, *, require_final: bool = True) -> dict:
    cfg = cfg or load_config()
    paths = chapter_paths(number)
    if not paths["translation"].exists():
        raise SystemExit(f"missing translation: translations/{number:04d}.md")
    if require_final and not final_promoted(number):
        raise SystemExit(f"chapter {number} has not been promoted by final touches")
    if entity_in_flight(number):
        raise SystemExit(f"chapter {number} has an uncommitted entity pass; finish it first")
    state = load_state(number)
    stage = state.get("stage", "NOT_STARTED")
    if stage == "COMMITTED":
        return state
    live = read_text(paths["translation"])
    if stage == "READY_TO_COMMIT":
        if sha256_text(live) != state.get("translation_sha256"):
            raise SystemExit(f"chapter {number} translation changed after the address edit; run reset {number}")
        return state
    if stage in {"QA_FAILED", "FAILED"}:
        raise SystemExit(f"chapter {number} address pass is {stage}; inspect reviews/address/{number:04d}/ and run reset {number}")

    try:
        from tools.progress import step
    except ModuleNotFoundError:
        from progress import step

    if stage == "NOT_STARTED":
        inputs = chapter_inputs(number, live)
        if not in_scope(inputs["source"], cfg):
            raise SystemExit(f"chapter {number} source has no configured address word")
        paths["root"].mkdir(parents=True, exist_ok=True)
        atomic_text(paths["baseline"], live)
        atomic_text(paths["packet"], packet_for(number, inputs, cfg))
        state = save_state(
            number, stage="PREPARED",
            baseline_sha256=sha256_text(live),
            source_sha256=sha256_text(inputs["source"]),
            model=cfg["model"],
        )
    baseline = read_text(paths["baseline"])
    if sha256_text(live) != state.get("baseline_sha256"):
        raise SystemExit(f"chapter {number} translation changed since the address pass began; run reset {number}")
    inputs = chapter_inputs(number, baseline)
    if sha256_text(inputs["source"]) != state.get("source_sha256"):
        raise SystemExit(f"chapter {number} source changed since the address pass began; run reset {number}")
    source = inputs["source"]

    if state["stage"] == "PREPARED":
        # Rebuild so a rerun (after a failed call or a rule change) uses the current rule.
        atomic_text(paths["packet"], packet_for(number, inputs, cfg))
        detection = structured_call(
            number, paths, cfg, lambda value: validate_detection(value, source, baseline, cfg),
        )
        atomic_json(paths["detect"], detection)
        state = save_state(number, stage="DETECTED")
    detection = json.loads(read_text(paths["detect"]))

    findings = screen([dict(item) for item in detection["findings"]], cfg, baseline)
    auto = [item for item in findings if item["status"] == "auto"]
    candidate = baseline
    applied = False
    if auto:
        try:
            candidate = apply_findings(baseline, auto)
        except ValueError as exc:
            for item in auto:
                item.update(status="human", reason_status=f"atomic apply blocked: {exc}")
            candidate = baseline
        else:
            qa = entity_qa(number, source, baseline, candidate, inputs["glossary"], cfg)
            atomic_json(paths["qa"], qa)
            if not qa["passed"]:
                messages = "; ".join(item.get("message", "") for item in qa["new_errors"])
                for item in auto:
                    item.update(status="human", reason_status=f"final QA failed: {messages}")
                atomic_json(paths["result"], {"version": 1, "chapter": number, "findings": findings})
                atomic_text(paths["report"], report_markdown(number, findings, detection, False, cfg, baseline))
                save_state(number, stage="QA_FAILED")
                raise SystemExit(f"address edit for chapter {number} failed final QA: {messages}")
            applied = True
    counts = {status: sum(1 for item in findings if item["status"] == status) for status in ("auto", "human")}
    atomic_json(paths["result"], {"version": 1, "chapter": number, "applied": applied, "counts": counts, "findings": findings})
    atomic_text(paths["report"], report_markdown(number, findings, detection, applied, cfg, baseline))
    if applied:
        atomic_text(paths["translation"], candidate)
    state = save_state(number, stage="READY_TO_COMMIT", applied=applied, counts=counts,
                       translation_sha256=sha256_text(candidate))
    step("address", "ready to commit", facts=[f"{counts['auto']} applied", f"{counts['human']} for review"])
    return state


def command_revert(number: int, ids: list[str], reason: str, cfg: dict | None = None) -> dict:
    """Undo applied findings after human review: replacement → current, exact and atomic."""
    cfg = cfg or load_config()
    paths = chapter_paths(number)
    state = load_state(number)
    if state.get("stage") not in {"READY_TO_COMMIT", "COMMITTED"} or not paths["result"].exists():
        raise SystemExit(f"chapter {number} has no finished address pass to revert")
    live = read_text(paths["translation"])
    if sha256_text(live) != state.get("translation_sha256"):
        raise SystemExit(f"chapter {number} translation changed after the address pass; revert by hand")
    result = json.loads(read_text(paths["result"]))
    findings = result.get("findings", [])
    by_id = {item["id"]: item for item in findings}
    chosen = []
    for identifier in ids:
        item = by_id.get(identifier)
        if item is None or item.get("status") != "auto":
            raise SystemExit(f"chapter {number}: {identifier} is not an applied finding")
        chosen.append({"id": identifier, "current": item["replacement"], "replacement": item["current"]})
    try:
        candidate = apply_findings(live, chosen)
    except ValueError as exc:
        raise SystemExit(f"chapter {number}: revert blocked: {exc}") from None
    source = current_source(number)
    qa = entity_qa(number, source, live, candidate, exact_glossary(source), cfg)
    if not qa["passed"]:
        messages = "; ".join(item.get("message", "") for item in qa["new_errors"])
        raise SystemExit(f"chapter {number}: revert failed final QA: {messages}")
    for identifier in ids:
        by_id[identifier].update(status="reverted", reason_status=reason)
    counts = {status: sum(1 for item in findings if item["status"] == status) for status in ("auto", "human", "reverted")}
    result.update(counts=counts, applied=counts["auto"] > 0)
    atomic_json(paths["result"], result)
    detection = json.loads(read_text(paths["detect"])) if paths["detect"].exists() else {}
    atomic_text(paths["report"], report_markdown(number, findings, detection, counts["auto"] > 0, cfg,
                                                 read_text(paths["baseline"])))
    atomic_text(paths["translation"], candidate)
    reverted = sorted(set(state.get("reverted", [])) | set(ids))
    return save_state(number, stage="READY_TO_COMMIT", counts=counts, reverted=reverted,
                      translation_sha256=sha256_text(candidate))


def command_reset(number: int) -> None:
    paths = chapter_paths(number)
    state = load_state(number)
    if state.get("stage") == "COMMITTED":
        raise SystemExit(f"chapter {number} address pass is committed; nothing to reset")
    if paths["baseline"].exists() and state.get("stage") in {"READY_TO_COMMIT", "QA_FAILED"}:
        live = read_text(paths["translation"])
        if sha256_text(live) == state.get("translation_sha256"):
            atomic_text(paths["translation"], read_text(paths["baseline"]))
    if paths["root"].exists():
        shutil.rmtree(paths["root"])
    print(f"Chapter {number}: address state removed")


# ---------------------------------------------------------------- estimate


def estimate(records: list[dict], cfg: dict, workers: int) -> dict:
    est = cfg.get("estimate") or {}
    rate = est.get("usd_per_1k_packet_tokens", [0.003, 0.0039])
    seconds = float(est.get("seconds_per_chapter", 40))
    tokens = sum(item["packet_tokens"] for item in records)
    count = len(records)
    return {
        "chapters": count,
        "korean_occurrences": sum(item["korean"] for item in records),
        "english_occurrences": sum(item["english"] for item in records),
        "not_final_promoted": sum(1 for item in records if not item["final_promoted"]),
        "packet_tokens_total": tokens,
        "packet_tokens_mean": round(tokens / count) if count else 0,
        "packet_tokens_max": max((item["packet_tokens"] for item in records), default=0),
        "model_calls": count,
        "usd": [round(tokens / 1000 * rate[0], 2), round(tokens / 1000 * rate[1], 2)],
        "workers": workers,
        "hours": round(count * seconds / max(1, workers) / 3600, 1),
    }


def summary_markdown(records: list[dict], est: dict, cfg: dict) -> str:
    lines = [
        "# Address Pass — Dry Run",
        "",
        f"Model: `{cfg['model']}` · terms: " + ", ".join(f"{k} → {v}" for k, v in cfg["terms"].items()),
        "",
        f"Chapters in scope: {est['chapters']} (not final-promoted: {est['not_final_promoted']}) · "
        f"Korean occurrences: {est['korean_occurrences']} · English occurrences: {est['english_occurrences']}",
        "",
        f"Packet tokens: total {est['packet_tokens_total']:,}, mean {est['packet_tokens_mean']:,}, "
        f"max {est['packet_tokens_max']:,}.",
        "",
        f"Estimate: {est['model_calls']} model calls (one per chapter, plus a retry only on invalid JSON), "
        f"${est['usd'][0]}–${est['usd'][1]}, about {est['hours']} h with {est['workers']} workers.",
        "",
        "| Chapter | 소협 | English | Packet tokens |",
        "| ------: | ---: | ------: | ------------: |",
        *[
            f"| {item['chapter']} | {item['korean']} | {item['english']} | {item['packet_tokens']:,} |"
            for item in sorted(records, key=lambda item: (-item["english"], item["chapter"]))[:40]
        ],
    ]
    return "\n".join(lines) + "\n"


def range_report(start: int, end: int) -> str:
    lines = [f"# Address Pass — Human Review {start}–{end}", ""]
    for number in range(start, end + 1):
        path = chapter_paths(number)["result"]
        if not path.exists():
            continue
        items = [item for item in json.loads(read_text(path)).get("findings", []) if item.get("status") == "human"]
        if not items:
            continue
        lines += [f"## Chapter {number}", ""]
        lines += [
            f"- **{item['id']}** {item['use']} ({item['confidence']:.2f}): “{item['current']}” → "
            f"“{item['replacement']}” — {item['reason']} [{item.get('reason_status', '')}]"
            for item in items
        ]
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def range_diff(chapters: list[int]) -> str:
    """Before/after of every chapter that has an address result."""
    parts = ["# Address Pass — Before/After", ""]
    for number in chapters:
        paths = chapter_paths(number)
        if not paths["result"].exists() or not paths["baseline"].exists():
            continue
        result = json.loads(read_text(paths["result"]))
        parts.append(diff_markdown(number, read_text(paths["baseline"]), read_text(paths["translation"]),
                                   result.get("findings", [])))
    return "\n".join(parts).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    run = sub.add_parser("run", help="check one finalized chapter and stop before commit")
    run.add_argument("chapter", type=int)
    run.add_argument("--model", help="override docs/address.json model")
    run.add_argument("--retries", type=int, help="override docs/address.json model_retries")
    for name in ("status", "reset"):
        sub.add_parser(name).add_argument("chapter", type=int)
    revert = sub.add_parser("revert", help="undo applied findings after human review; stops at READY_TO_COMMIT")
    revert.add_argument("chapter", type=int)
    revert.add_argument("ids", nargs="+", help="finding IDs, e.g. A01 A02")
    revert.add_argument("--reason", required=True)
    for name in ("report", "diff"):
        command = sub.add_parser(name, help="human-review findings" if name == "report" else "before/after diff")
        command.add_argument("start", type=int)
        command.add_argument("end", type=int)
        command.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.command == "status":
        state = load_state(args.chapter)
        print(f"Chapter: {args.chapter}\nStage: {state.get('stage')}\nCounts: {state.get('counts', {})}")
        return 0
    if args.command in {"report", "diff"}:
        text = (range_report(args.start, args.end) if args.command == "report"
                else range_diff(list(range(args.start, args.end + 1))))
        if args.output:
            atomic_text(args.output, text)
            print(args.output)
        else:
            print(text, end="")
        return 0
    try:
        from tools.run_lock import ADDRESS_LOCK_NAME, hold_address_lock, parent_delegated
    except ModuleNotFoundError:
        from run_lock import ADDRESS_LOCK_NAME, hold_address_lock, parent_delegated
    if args.command == "run":
        cfg = load_config()
        if args.model:
            cfg["model"] = args.model
        if args.retries is not None:
            cfg["model_retries"] = max(0, args.retries)
        action = lambda number: command_run(number, cfg)  # noqa: E731
    elif args.command == "revert":
        action = lambda number: command_revert(number, args.ids, args.reason)  # noqa: E731
    else:
        action = command_reset
    if parent_delegated(ADDRESS_LOCK_NAME):
        action(args.chapter)
        return 0
    try:
        from tools.run_address_pass import refuse_live_locks
    except ModuleNotFoundError:
        from run_address_pass import refuse_live_locks
    refuse_live_locks()
    with hold_address_lock(ROOT, holder="address_pass", chapter=args.chapter, stage=args.command):
        action(args.chapter)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
