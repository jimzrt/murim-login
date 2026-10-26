#!/usr/bin/env python3
"""Entity consistency pass over finished chapters.

Fixes only entity errors: wrong gender or pronouns for named characters, wrong
referent, wrong name, title, or affiliation, and kinship errors. No style or
fluency edits.

Per chapter:

1. Deterministic prefilter (free): pronoun conflicts near profiled names,
   known wrong name variants, and proper names whose preferred English is
   absent. It only prioritizes and annotates the packet.
2. Detector model (docs/entity.json models.detector) returns structured
   findings with exact `current` → `replacement` spans and an `uncertain` flag.
3. Escalation model re-checks low-confidence findings and uncertain chapters.
4. Confirmed high-confidence findings are applied atomically; missing,
   repeated, or overlapping spans are never applied. Final QA must not gain an
   error. Everything else goes to the human-review report.

State lives under reviews/entity/NNNN/. Commit is separate (run_entity_pass.py
or run_next_entity.py).
"""

from __future__ import annotations

import argparse
import difflib
import json
import re
import shutil
import sys
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "docs" / "entity.json"
RUBRIC_PATH = ROOT / "docs" / "ENTITY.md"
PROFILE_DIR = ROOT / "characters"
ENTITY_ROOT = ROOT / "reviews" / "entity"
DRY_ROOT = ROOT / ".work" / "entity-dry"

try:
    from tools.final_qa import FOOTNOTE_DEF, assess
    from tools.final_touches import matching_profiles, profiles_text
    from tools.mastering import (
        atomic_json,
        atomic_text,
        current_source,
        exact_glossary,
        glossary_text,
        read_text,
        sha256_text,
    )
    from tools.name_check import (
        _any_name_word,
        check_names,
        english_present,
        matched_names,
        proper_name_entries,
    )
    from tools.names import ALIAS_LINE, ALIAS_PAIR, HEADING, profile_gender
except ModuleNotFoundError:
    sys.path.insert(0, str(ROOT / "tools"))
    from final_qa import FOOTNOTE_DEF, assess
    from final_touches import matching_profiles, profiles_text
    from mastering import (
        atomic_json,
        atomic_text,
        current_source,
        exact_glossary,
        glossary_text,
        read_text,
        sha256_text,
    )
    from name_check import (
        _any_name_word,
        check_names,
        english_present,
        matched_names,
        proper_name_entries,
    )
    from names import ALIAS_LINE, ALIAS_PAIR, HEADING, profile_gender

CATEGORIES = ("gender", "referent", "name", "title", "affiliation", "kinship")
FOOTNOTE_CATEGORIES = {"gender", "name"}
HANGUL = re.compile(r"[가-힣]")
FOOTNOTE_REF = re.compile(r"\[\^[^\]]+\]")
IN_FLIGHT = {"PREPARED", "DETECTED", "ESCALATED", "READY_TO_COMMIT", "QA_FAILED", "FAILED"}
PRONOUNS = {
    "male": re.compile(r"\b(?:he|him|his|himself)\b", re.IGNORECASE),
    "female": re.compile(r"\b(?:she|her|hers|herself)\b", re.IGNORECASE),
}
OPPOSITE = {"male": "female", "female": "male"}
QUOTED = re.compile(r"“[^”]*(?:”|$)|\"[^\"]*\"")
SENTENCE_SPLIT = re.compile(r"(?:(?<=[.!?…—][”’*])|(?<=[.!?…—]))\s+")
# Korean words that mark a person's gender. A gender fix resting on the card
# alone is never auto-applied, since a wrong card would spread a wrong pronoun.
GENDER_MARKER = re.compile(
    r"그녀|그(?:는|가|의|를|에게|와|도)(?![가-힣])|여자|남자|여인|사내|소저|낭자|공자|아가씨|"
    r"할머니|할아버지|노파|노인|부인|언니|누나|오빠|형님|여성|남성|비구니|여승|아저씨|"
    r"아줌마|아들|딸|어머니|아버지|엄마|아빠|사모|여왕|왕비|황후|공주|왕자|성녀|마녀"
)
FLAG_TYPES = (
    "pronoun_conflict",
    "name_variant",
    "name_variant_suspect",
    "name_absent",
    "term_absent",
)


# ---------------------------------------------------------------- config


def load_config(path: Path = CONFIG_PATH) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if value.get("version") != 1:
        raise SystemExit("docs/entity.json version must be 1")
    models = value.get("models") or {}
    for role in ("detector", "escalation"):
        if not isinstance(models.get(role), str) or not models[role].strip():
            raise SystemExit(f"docs/entity.json models.{role} must name a model")
    for key, default in (
        ("escalate_below_confidence", 0.9),
        ("auto_apply_min_confidence", 0.9),
        ("min_baseline_preserved", 0.97),
    ):
        number = float(value.get(key, default))
        if not 0 <= number <= 1:
            raise SystemExit(f"docs/entity.json {key} must be between 0 and 1")
        value[key] = number
    value["packet_token_limit"] = int(value.get("packet_token_limit", 60000))
    value["model_retries"] = max(0, int(value.get("model_retries", 1)))
    value["max_changed_chars"] = int(value.get("max_changed_chars", 120))
    value["pronoun_window_sentences"] = max(0, int(value.get("pronoun_window_sentences", 1)))
    value["batch_workers"] = max(1, int(value.get("batch_workers", 3)))
    value["escalate_all_findings"] = bool(value.get("escalate_all_findings", True))
    value.setdefault("timeouts", {})
    value.setdefault("estimate", {})
    return value


def chapter_paths(number: int, root: Path = ENTITY_ROOT) -> dict[str, Path]:
    folder = root / f"{number:04d}"
    return {
        "root": folder,
        "state": folder / "state.json",
        "baseline": folder / "baseline.md",
        "prefilter": folder / "prefilter.json",
        "detect_packet": folder / "detect-packet.md",
        "detect": folder / "detect.json",
        "escalate_packet": folder / "escalate-packet.md",
        "escalate": folder / "escalate.json",
        "result": folder / "result.json",
        "report": folder / "report.md",
        "qa": folder / "qa.json",
        "metrics": folder / "metrics.json",
        "detect_log": folder / "omp" / "detect.jsonl",
        "escalate_log": folder / "omp" / "escalate.jsonl",
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


def entity_owns_path(path: str, number: int) -> bool:
    return path == f"translations/{number:04d}.md" or path.startswith(f"reviews/entity/{number:04d}/")


def active_entity_chapters() -> list[int]:
    if not ENTITY_ROOT.is_dir():
        return []
    found: list[int] = []
    for path in sorted(ENTITY_ROOT.glob("[0-9][0-9][0-9][0-9]/state.json")):
        try:
            state = json.loads(path.read_text(encoding="utf-8"))
            number = int(path.parent.name)
        except (OSError, json.JSONDecodeError, ValueError):
            continue
        if state.get("stage") in IN_FLIGHT:
            found.append(number)
    return found


def foreign_entity_paths(dirty: list[str]) -> set[str]:
    """Paths owned by the entity queue, so the other runners can ignore them."""
    active = set(active_entity_chapters())
    foreign: set[str] = set()
    for path in dirty:
        if path.startswith("reviews/entity/"):
            foreign.add(path)
        elif any(entity_owns_path(path, number) for number in active):
            foreign.add(path)
    return foreign


# ------------------------------------------------------------- prefilter


@lru_cache(maxsize=2)
def _cards_cached(directory: str) -> tuple[dict, ...]:
    cards: list[dict] = []
    folder = Path(directory)
    if not folder.is_dir():
        return ()
    for path in sorted(folder.glob("*.md")):
        body = path.read_text(encoding="utf-8")
        lines = body.splitlines()
        heading = next((HEADING.match(line) for line in lines if HEADING.match(line)), None)
        if heading is None:
            continue
        english = [heading.group(1).strip()]
        korean = [heading.group(2)]
        for line in lines:
            aliases = ALIAS_LINE.match(line)
            if aliases:
                for pair in ALIAS_PAIR.finditer(aliases.group(1)):
                    name = pair.group(1).strip()
                    if name and name[0].isupper():
                        english.append(name)
                    korean.append(pair.group(2))
        cards.append({
            "english": english[0],
            "english_names": sorted(set(english), key=len, reverse=True),
            "korean_names": sorted(set(korean), key=len, reverse=True),
            "gender": profile_gender(body),
        })
    return tuple(cards)


def gendered_cards(source: str, directory: Path = PROFILE_DIR) -> list[dict]:
    try:
        from tools.name_check import name_at_boundary
    except ModuleNotFoundError:
        from name_check import name_at_boundary
    return [
        dict(card)
        for card in _cards_cached(str(directory))
        if any(name in source and name_at_boundary(source, name) for name in card["korean_names"])
    ]


def _name_pattern(names: list[str]) -> re.Pattern:
    escaped = "|".join(re.escape(name) for name in names)
    return re.compile(r"(?<![A-Za-z])(?:" + escaped + r")(?:['’]s)?(?![A-Za-z])")


def _sentences(paragraph: str) -> list[str]:
    return [part for part in SENTENCE_SPLIT.split(paragraph) if part.strip()]


# Subject, possessive, and reflexive pronouns only. Object him/her usually
# points at someone else (“Jin Taekyung gave her a smile”).
CONFLICT_PRONOUNS = {
    "male": re.compile(r"\b(?:he|his|himself)\b", re.IGNORECASE),
    "female": re.compile(r"\b(?:she|hers|herself|her(?=\s+(?!(?:a|an|the|this|that|to|in|on|at|for|with|from|by|of|and|or|as|up|down|away|off|out|back|again|now|then|alone|too)\b)[a-z]))\b", re.IGNORECASE),
}
SUBJECT_START = re.compile(r"^(?:he|she)\b", re.IGNORECASE)
# Person nouns of each gender: a window that has one may be about that person.
PERSON_NOUNS = {
    "male": re.compile(
        r"\b(?:man|men|boy|boys|guy|guys|father|brother|son|husband|king|emperor|monk|"
        r"gentleman|lord|uncle|grandfather|old man|coachman|sir|prince|master)\b", re.IGNORECASE,
    ),
    "female": re.compile(
        r"\b(?:woman|women|girl|girls|lady|ladies|mother|sister|daughter|wife|queen|empress|"
        r"nun|aunt|grandmother|old woman|madam|princess|maiden|mistress)\b", re.IGNORECASE,
    ),
}
CAPITALIZED = re.compile(r"\b[A-Z][a-z’'-]+\b")
LEAD_WORDS = re.compile(r"^(?:the|[A-Z][A-Za-z’'-]*)$")
# Capitalized openers that put the name in a subordinate phrase, not the subject.
OPENERS = {
    "Unlike", "If", "With", "Without", "To", "Did", "Does", "Do", "Even", "Leaving", "As", "At",
    "After", "Before", "When", "While", "For", "From", "In", "On", "By", "Like", "Since",
    "Because", "Although", "Though", "Once", "Until", "Despite", "Only", "And", "But", "So",
    "Then", "Was", "Is", "Had", "Has", "Not", "Neither", "Nor", "Than", "Beside", "Behind",
}
# A pronoun after a preposition or a clause word usually belongs to someone else
# (“nodded at her whisper”, “understood how he felt”).
NOT_SUBJECT_BEFORE = re.compile(
    r"\b(?:at|to|toward|towards|with|from|for|of|over|into|onto|on|by|about|behind|beside|"
    r"before|after|like|than|how|what|whom|who|why|where|when|that|as|if|whether|because|"
    r"until|while|though|although)\s+$",
    re.IGNORECASE,
)


def _subject_match(sentence: str, pattern: re.Pattern) -> re.Match | None:
    """The name as the sentence subject: only title words before it, not possessive."""
    match = pattern.search(sentence)
    if not match or re.search(r"['’]s$", match.group(0)):
        return None
    lead = re.sub(r"^[\s“\"*_>—-]+", "", sentence[:match.start()]).split()
    if len(lead) > 3 or not all(LEAD_WORDS.match(word) and word not in OPENERS for word in lead):
        return None
    return match


def _other_people(text: str, card: dict, cards: list[dict], patterns: dict) -> bool:
    if any(other["english"] != card["english"] and patterns[other["english"]].search(text) for other in cards):
        return True
    own = {word for name in card["english_names"] for word in name.split()}
    try:
        from tools.name_check import COMMON_CAPS
    except ModuleNotFoundError:
        from name_check import COMMON_CAPS
    words = [word for word in CAPITALIZED.findall(text) if word not in own and word not in COMMON_CAPS]
    # The first word of each sentence is capitalized anyway.
    starts = {sentence.split()[0].strip("“\"*") for sentence in _sentences(text) if sentence.split()}
    return any(word not in starts for word in words)


def pronoun_conflicts(translation: str, cards: list[dict], window: int = 1) -> list[dict]:
    """Narration where a gendered character is the subject but the other gender's pronoun follows.

    The window is the naming sentence after the name plus up to `window`
    following sentences that open with he/she. Only subject, possessive, and
    reflexive pronouns count. Quoted speech is ignored. A window that names
    any other person or uses an opposite-gender person noun is skipped, since
    the pronoun may be theirs.
    """
    flags: list[dict] = []
    known = [card for card in cards if card.get("gender") in OPPOSITE]
    if not known:
        return flags
    patterns = {card["english"]: _name_pattern(card["english_names"]) for card in cards}
    for paragraph in re.split(r"\n\s*\n", translation):
        if FOOTNOTE_DEF.match(paragraph.strip()):
            continue
        sentences = [QUOTED.sub(" ", sentence) for sentence in _sentences(paragraph)]
        for index, sentence in enumerate(sentences):
            for card in known:
                match = _subject_match(sentence, patterns[card["english"]])
                if not match:
                    continue
                following = []
                for nxt in sentences[index + 1:index + 1 + window]:
                    if not SUBJECT_START.match(nxt.strip()):
                        break
                    following.append(nxt)
                text = " ".join([sentence[match.end():], *following])
                full = " ".join([sentence, *following])
                opposite = OPPOSITE[card["gender"]]
                if _other_people(text, card, cards, patterns) or PERSON_NOUNS[opposite].search(full):
                    continue
                wrong = [
                    found.group(0) for found in CONFLICT_PRONOUNS[opposite].finditer(text)
                    if not NOT_SUBJECT_BEFORE.search(text[:found.start()])
                ]
                right = PRONOUNS[card["gender"]].findall(text)
                if wrong and not right:
                    flags.append({
                        "type": "pronoun_conflict",
                        "character": card["english"],
                        "gender": card["gender"],
                        "pronouns": sorted({word.lower() for word in wrong}),
                        "excerpt": full.strip()[:400],
                    })
    return flags


def name_flags(source: str, translation: str, entries: list[dict] | None = None) -> list[dict]:
    entries = proper_name_entries() if entries is None else entries
    flags: list[dict] = []
    result = check_names(source, translation, entries)
    for item in result["errors"] + result["warnings"]:
        flags.append({"type": item["code"], **item["details"]})
    reported = {flag["korean"] for flag in flags}
    for item in matched_names(source, entries):
        korean = item["korean"]
        if item["kind"] == "person" or korean in reported:
            continue
        distinctive = " " in korean or len(korean) >= 3
        if distinctive and not _any_name_word(translation, item["english"]):
            flags.append({"type": "term_absent", "korean": korean, "preferred": item["english"]})
    return flags


def prefilter(source: str, translation: str, *, window: int = 1, cards: list[dict] | None = None,
              entries: list[dict] | None = None) -> dict:
    cards = gendered_cards(source) if cards is None else cards
    flags = pronoun_conflicts(translation, cards, window) + name_flags(source, translation, entries)
    counts = {kind: 0 for kind in FLAG_TYPES}
    for flag in flags:
        counts[flag["type"]] = counts.get(flag["type"], 0) + 1
    return {"version": 1, "flags": flags, "counts": counts, "flagged": bool(flags)}


def flags_text(report: dict) -> str:
    if not report["flags"]:
        return "(No deterministic flags. Still check the whole chapter.)"
    lines: list[str] = []
    for flag in report["flags"]:
        kind = flag["type"]
        if kind == "pronoun_conflict":
            lines.append(
                f"- pronoun_conflict: {flag['character']} is {flag['gender']}, but nearby narration "
                f"uses {', '.join(flag['pronouns'])}: “{flag['excerpt']}”"
            )
        elif kind == "name_variant":
            lines.append(
                f"- name_variant: {flag['korean']} must be “{flag['preferred']}”, found "
                + ", ".join(f"“{item}”" for item in flag.get("found", []))
            )
        elif kind == "name_variant_suspect":
            lines.append(
                f"- name_variant_suspect: {flag['korean']} should be “{flag['preferred']}”; similar "
                + ", ".join(f"“{item}”" for item in flag.get("found", []))
            )
        else:
            lines.append(f"- {kind}: {flag['korean']} (“{flag['preferred']}”) is in the source but not the English")
    return "\n".join(lines)


# ---------------------------------------------------------------- packets


SCHEMA = """{
  "uncertain": false,
  "uncertain_reason": "",
  "summary": "one sentence",
  "findings": [
    {
      "category": "gender|referent|name|title|affiliation|kinship",
      "current": "exact unique English span",
      "replacement": "same span with only the entity words fixed",
      "korean": "exact Korean evidence",
      "explanation": "who or what it must be, and why",
      "confidence": 0.0
    }
  ]
}"""


def _context_sections(number: int, source: str, translation: str, glossary: list[dict],
                      profiles: list[dict], omitted: int, flags: dict) -> str:
    return f"""## Character cards

Identity only. Gender `unknown` means the source has not settled it.

{profiles_text(profiles, omitted)}

## Exact glossary matches

{glossary_text(glossary)}

## Deterministic flags

Leads only; many are false alarms. Verify each against the source.

{flags_text(flags)}

## Korean source

```text
{source.rstrip()}
```

## Current English — Chapter {number}

```markdown
{translation.rstrip()}
```"""


def build_detect_packet(number: int, source: str, translation: str, glossary: list[dict],
                        profiles: list[dict], flags: dict, omitted: int = 0) -> str:
    rubric = read_text(RUBRIC_PATH).strip()
    return f"""# Entity Check — Chapter {number}

Check only this chapter. Do not use tools. Return exactly one JSON object with
no Markdown fence, in this shape:

{SCHEMA}

Use an empty findings array when nothing is wrong.

{rubric}

{_context_sections(number, source, translation, glossary, profiles, omitted, flags)}
"""


def build_escalate_packet(number: int, source: str, translation: str, glossary: list[dict],
                          profiles: list[dict], flags: dict, detection: dict, ids: list[str],
                          omitted: int = 0) -> str:
    rubric = read_text(RUBRIC_PATH).strip()
    findings = [item for item in detection["findings"] if item["id"] in set(ids)]
    reason = detection.get("uncertain_reason") or ""
    uncertain = (
        f"The first checker marked this chapter uncertain: {reason or 'no reason given'}. "
        "Re-check the whole chapter's speakers and pronouns and add any finding it missed."
        if detection.get("uncertain") else
        "Add a finding only if you see a clear entity error the first checker missed."
    )
    return f"""# Entity Check Escalation — Chapter {number}

A first checker reported the findings below. Decide each one against the
Korean source: `confirm` it, `reject` it, or `amend` it with a corrected
`current` and `replacement`. {uncertain}

Return exactly one JSON object with no Markdown fence:

{{
  "summary": "one sentence",
  "decisions": [
    {{"id": "E01", "verdict": "confirm|reject|amend", "current": "only for amend",
      "replacement": "only for amend", "confidence": 0.0, "reason": "specific reason"}}
  ],
  "added": [
    {{"category": "…", "current": "…", "replacement": "…", "korean": "…",
      "explanation": "…", "confidence": 0.0}}
  ]
}}

Give exactly one decision per finding ID below. `confidence` is your own.

## Findings to decide

```json
{json.dumps(findings, ensure_ascii=False, indent=2)}
```

{rubric}

{_context_sections(number, source, translation, glossary, profiles, omitted, flags)}
"""


def packet_tokens(text: str) -> int:
    return (len(text.encode("utf-8")) + 3) // 4


def fitted(builder, profiles: list[dict], limit: int, **kwargs) -> str:
    """Drop the least-present character cards until the packet fits."""
    kept = list(profiles)
    while True:
        packet = builder(profiles=kept, omitted=len(profiles) - len(kept), **kwargs)
        if packet_tokens(packet) <= limit:
            return packet
        if not kept:
            raise SystemExit(f"entity packet estimate {packet_tokens(packet)} exceeds limit {limit}")
        kept.pop()


# ------------------------------------------------------------- validation


def _squash(text: str) -> str:
    return re.sub(r"\s+", "", text)


def _confidence(value: object, label: str) -> float:
    if not isinstance(value, (int, float)) or isinstance(value, bool) or not 0 <= value <= 1:
        raise ValueError(f"{label} confidence must be a number between 0 and 1")
    return float(value)


def _finding(raw: object, label: str) -> dict:
    if not isinstance(raw, dict):
        raise ValueError(f"{label} must be an object")
    for key in ("category", "current", "replacement", "korean", "explanation"):
        if not isinstance(raw.get(key), str) or not raw[key].strip():
            raise ValueError(f"{label} requires nonempty {key}")
    category = raw["category"].strip().lower()
    if category not in CATEGORIES:
        raise ValueError(f"{label} has invalid category {category!r}")
    if raw["current"] == raw["replacement"]:
        raise ValueError(f"{label} replacement must differ from current")
    if HANGUL.search(raw["replacement"]):
        raise ValueError(f"{label} replacement contains Hangul")
    return {
        "category": category,
        "current": raw["current"],
        "replacement": raw["replacement"],
        "korean": raw["korean"].strip(),
        "explanation": raw["explanation"].strip(),
        "confidence": _confidence(raw.get("confidence"), label),
    }


def annotate(finding: dict, source: str, translation: str) -> dict:
    finding["span_count"] = translation.count(finding["current"])
    finding["evidence_found"] = _squash(finding["korean"]) in _squash(source)
    return finding


def validate_detection(value: dict, source: str, translation: str) -> dict:
    findings = value.get("findings")
    if not isinstance(findings, list):
        raise ValueError("entity response requires a findings array")
    uncertain = value.get("uncertain", False)
    if not isinstance(uncertain, bool):
        raise ValueError("uncertain must be true or false")
    normalized = []
    for position, raw in enumerate(findings, 1):
        item = _finding(raw, f"finding {position}")
        item["id"] = f"E{position:02d}"
        item["origin"] = "detector"
        normalized.append(annotate(item, source, translation))
    summary = value.get("summary", "")
    reason = value.get("uncertain_reason", "")
    return {
        "version": 1,
        "uncertain": uncertain,
        "uncertain_reason": reason.strip() if isinstance(reason, str) else "",
        "summary": summary.strip() if isinstance(summary, str) else "",
        "findings": normalized,
    }


def select_escalation(detection: dict, cfg: dict) -> list[str]:
    """Finding IDs Sol must decide.

    With `escalate_all_findings` (the default) every detector finding needs a
    second model's confirmation before it is applied: the smoke test showed a
    0.99-confidence detector finding that was wrong. Otherwise an uncertain
    chapter escalates every finding, and a low-confidence finding, one whose
    Korean evidence is not in the source, or one whose span is not exactly once
    in the chapter is escalated.
    An uncertain chapter with no findings returns an empty list; callers check
    `needs_escalation`.
    """
    if detection.get("uncertain") or cfg.get("escalate_all_findings"):
        return [item["id"] for item in detection["findings"]]
    threshold = cfg["escalate_below_confidence"]
    return [
        item["id"]
        for item in detection["findings"]
        if item["confidence"] < threshold or not item["evidence_found"] or item["span_count"] != 1
    ]


def needs_escalation(detection: dict, cfg: dict) -> bool:
    return bool(detection.get("uncertain")) or bool(select_escalation(detection, cfg))


def validate_escalation(value: dict, ids: list[str], source: str, translation: str) -> dict:
    decisions = value.get("decisions", [])
    added = value.get("added", [])
    if not isinstance(decisions, list) or not isinstance(added, list):
        raise ValueError("escalation response requires decisions and added arrays")
    expected = set(ids)
    seen: dict[str, dict] = {}
    for position, raw in enumerate(decisions, 1):
        if not isinstance(raw, dict):
            raise ValueError(f"decision {position} must be an object")
        identifier = str(raw.get("id", "")).strip()
        if identifier not in expected:
            raise ValueError(f"decision {position} names unknown finding {identifier!r}")
        if identifier in seen:
            raise ValueError(f"duplicate decision for {identifier}")
        verdict = str(raw.get("verdict", "")).strip().lower()
        if verdict not in {"confirm", "reject", "amend"}:
            raise ValueError(f"decision {identifier} has invalid verdict {verdict!r}")
        decision = {
            "id": identifier,
            "verdict": verdict,
            "confidence": _confidence(raw.get("confidence"), f"decision {identifier}"),
            "reason": str(raw.get("reason", "")).strip(),
        }
        if verdict == "amend":
            for key in ("current", "replacement"):
                if not isinstance(raw.get(key), str) or not raw[key].strip():
                    raise ValueError(f"amended decision {identifier} requires {key}")
            if raw["current"] == raw["replacement"]:
                raise ValueError(f"amended decision {identifier} replacement must differ")
            if HANGUL.search(raw["replacement"]):
                raise ValueError(f"amended decision {identifier} replacement contains Hangul")
            decision["current"] = raw["current"]
            decision["replacement"] = raw["replacement"]
        seen[identifier] = decision
    missing = sorted(expected - set(seen))
    if missing:
        raise ValueError("escalation did not decide: " + ", ".join(missing))
    extra = []
    for position, raw in enumerate(added, 1):
        item = _finding(raw, f"added finding {position}")
        item["id"] = f"S{position:02d}"
        item["origin"] = "escalation"
        extra.append(annotate(item, source, translation))
    summary = value.get("summary", "")
    return {
        "version": 1,
        "summary": summary.strip() if isinstance(summary, str) else "",
        "decisions": [seen[identifier] for identifier in ids],
        "added": extra,
    }


# ------------------------------------------------------------------ apply


def changed_chars(current: str, replacement: str) -> int:
    matcher = difflib.SequenceMatcher(None, current, replacement, autojunk=False)
    return sum(
        max(i2 - i1, j2 - j1)
        for tag, i1, i2, j1, j2 in matcher.get_opcodes()
        if tag != "equal"
    )


def _span_lines(text: str, start: int, end: int) -> list[str]:
    line_start = text.rfind("\n", 0, start) + 1
    line_end = text.find("\n", end)
    return text[line_start: len(text) if line_end < 0 else line_end].splitlines()


def resolve(detection: dict, escalation: dict | None, escalated: list[str], cfg: dict,
            source: str, translation: str) -> list[dict]:
    """Every finding with a status: auto, human, or rejected, plus a reason."""
    minimum = cfg["auto_apply_min_confidence"]
    decisions = {item["id"]: item for item in (escalation or {}).get("decisions", [])}
    resolved: list[dict] = []
    for item in detection["findings"]:
        finding = dict(item)
        if item["id"] in escalated:
            decision = decisions.get(item["id"])
            if decision is None:
                finding.update(status="human", reason="escalation did not run")
                resolved.append(finding)
                continue
            finding["escalation"] = decision
            if decision["verdict"] == "reject":
                finding.update(status="rejected", reason=decision["reason"] or "rejected on escalation")
                resolved.append(finding)
                continue
            if decision["verdict"] == "amend":
                finding["current"] = decision["current"]
                finding["replacement"] = decision["replacement"]
                annotate(finding, source, translation)
            finding["confidence"] = decision["confidence"]
        if finding["confidence"] >= minimum:
            finding.update(status="auto", reason="")
        else:
            finding.update(status="human", reason=f"confidence {finding['confidence']:.2f} below {minimum:.2f}")
        resolved.append(finding)
    for item in (escalation or {}).get("added", []):
        finding = dict(item)
        if finding["confidence"] >= minimum:
            finding.update(status="auto", reason="")
        else:
            finding.update(status="human", reason=f"confidence {finding['confidence']:.2f} below {minimum:.2f}")
        resolved.append(finding)
    return screen(resolved, cfg, translation)


def screen(findings: list[dict], cfg: dict, translation: str) -> list[dict]:
    """Demote auto findings that cannot be applied safely to human review."""
    limit = cfg["max_changed_chars"]
    for finding in findings:
        if finding["status"] != "auto":
            continue
        current, replacement = finding["current"], finding["replacement"]
        count = translation.count(current)
        problem = ""
        if count == 0:
            problem = "current span is missing from the chapter"
        elif count > 1:
            problem = f"current span occurs {count} times"
        elif not finding.get("evidence_found"):
            problem = "Korean evidence is not in the source"
        elif finding["category"] == "gender" and not GENDER_MARKER.search(finding["korean"]):
            problem = "gender fix has no gendered Korean evidence; check the character card"
        elif sorted(FOOTNOTE_REF.findall(current)) != sorted(FOOTNOTE_REF.findall(replacement)):
            problem = "replacement changes footnote references"
        elif changed_chars(current, replacement) > limit:
            problem = f"edit changes more than {limit} characters"
        else:
            start = translation.index(current)
            lines = _span_lines(translation, start, start + len(current))
            if any(FOOTNOTE_DEF.match(line.strip()) for line in lines) and finding["category"] not in FOOTNOTE_CATEGORIES:
                problem = "only gender or name fixes may touch a footnote definition"
        if problem:
            finding.update(status="human", reason=problem)
    spans = []
    for finding in findings:
        if finding["status"] == "auto":
            start = translation.index(finding["current"])
            spans.append((start, start + len(finding["current"]), finding))
    for index, (start, end, finding) in enumerate(spans):
        for other_start, other_end, other in spans[index + 1:]:
            if start < other_end and other_start < end:
                for item in (finding, other):
                    item.update(status="human", reason="overlaps another finding")
    return findings


def apply_findings(text: str, findings: list[dict]) -> str:
    """Apply exact unique spans atomically: any missing, repeated, or overlapping span blocks all."""
    spans: list[tuple[int, int, str, str]] = []
    for finding in findings:
        current = finding["current"]
        count = text.count(current)
        if count != 1:
            raise ValueError(f"finding {finding['id']} current text occurs {count} times")
        start = text.index(current)
        spans.append((start, start + len(current), finding["replacement"], finding["id"]))
    spans.sort()
    for (start, end, _, left), (next_start, _, _, right) in zip(spans, spans[1:]):
        if next_start < end:
            raise ValueError(f"findings {left} and {right} overlap")
    result = text
    for start, end, replacement, _identifier in reversed(spans):
        result = result[:start] + replacement + result[end:]
    return result


def _error_keys(qa: dict) -> set[str]:
    return {
        json.dumps({"code": item.get("code"), "details": item.get("details")}, sort_keys=True, ensure_ascii=False)
        for item in qa.get("errors") or []
    }


def entity_qa(number: int, source: str, baseline: str, candidate: str, glossary: list[dict], cfg: dict) -> dict:
    """Final QA; only errors the baseline does not already have block the edit."""
    pairs = [(item.get("korean", ""), item.get("english", "")) for item in glossary]
    before = assess(number, source, baseline, baseline, pairs, min_baseline_preserved=0.0)
    after = assess(number, source, baseline, candidate, pairs,
                   min_baseline_preserved=cfg["min_baseline_preserved"])
    known = _error_keys(before)
    new = [item for item in after.get("errors") or [] if json.dumps(
        {"code": item.get("code"), "details": item.get("details")}, sort_keys=True, ensure_ascii=False
    ) not in known]
    after["preexisting_errors"] = len(after.get("errors") or []) - len(new)
    after["new_errors"] = new
    after["passed"] = not new
    return after


# ------------------------------------------------------------------ report


def report_markdown(number: int, findings: list[dict], detection: dict, escalation: dict | None,
                    flags: dict, applied: bool) -> str:
    lines = [f"# Entity Pass — Chapter {number}", ""]
    lines.append(f"- Detector: {detection.get('summary') or '—'}")
    if detection.get("uncertain"):
        lines.append(f"- Uncertain: {detection.get('uncertain_reason') or 'yes'}")
    if escalation is not None:
        lines.append(f"- Escalation: {escalation.get('summary') or '—'}")
    lines.append(f"- Prefilter flags: {len(flags['flags'])}")
    lines.append(f"- Applied: {'yes' if applied else 'no'}")
    lines.append("")
    for status, title in (("auto", "Applied"), ("human", "Needs human review"), ("rejected", "Rejected")):
        items = [item for item in findings if item["status"] == status]
        lines += [f"## {title} ({len(items)})", ""]
        if not items:
            lines += ["None.", ""]
            continue
        for item in items:
            lines.append(f"### {item['id']} · {item['category']} · {item['confidence']:.2f}")
            lines.append("")
            lines.append(f"- Current: “{item['current']}”")
            lines.append(f"- Replacement: “{item['replacement']}”")
            lines.append(f"- Korean: {item['korean']}")
            lines.append(f"- Why: {item['explanation']}")
            if item.get("escalation"):
                decision = item["escalation"]
                lines.append(f"- Escalation: {decision['verdict']} — {decision['reason']}")
            if item.get("reason"):
                lines.append(f"- Status reason: {item['reason']}")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


# ------------------------------------------------------------- model calls


def _save_metrics(path: Path, number: int, stage: str, metrics: dict) -> None:
    data = {"version": 1, "chapter": number, "stages": {}}
    if path.exists():
        data = json.loads(path.read_text(encoding="utf-8"))
        data.setdefault("stages", {})
    data["stages"][stage] = metrics
    atomic_json(path, data)


def call_model(packet_path: Path, model: str, timeout: int, log_path: Path, label: str, hint: str = ""):
    try:
        from tools.mastering import run_omp
    except ModuleNotFoundError:
        from mastering import run_omp
    try:
        return run_omp(packet_path, model, timeout, log_path, label=label, hint=hint, hold=True)
    except RuntimeError as exc:
        raise SystemExit(str(exc)) from None


def _structured_call(number: int, paths: dict, kind: str, cfg: dict, validate) -> tuple[dict, str]:
    try:
        from tools.model_io import parse_json_object
    except ModuleNotFoundError:
        from model_io import parse_json_object
    role = "detector" if kind == "detect" else "escalation"
    model = cfg["models"][role]
    timeout = int(cfg["timeouts"].get(role, 1800))
    attempts = 1 + cfg["model_retries"]
    error = ""
    for attempt in range(1, attempts + 1):
        stage = kind if attempt == 1 else f"{kind}_retry_{attempt - 1}"
        output, metrics, call = call_model(
            paths[f"{kind}_packet"], model, timeout, paths[f"{kind}_log"], label=f"entity-{kind}",
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
        return value, model
    raise SystemExit(f"entity {kind} for chapter {number} returned invalid JSON: {error}")


# --------------------------------------------------------------- pipeline


def final_promoted(number: int) -> bool:
    path = ROOT / "reviews" / "final" / f"{number:04d}" / "state.json"
    try:
        state = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False
    return state.get("stage") == "PROMOTED" and bool(state.get("qa_passed"))


def chapter_inputs(number: int, cfg: dict, translation: str | None = None) -> dict:
    source = current_source(number)
    text = read_text(chapter_paths(number)["translation"]) if translation is None else translation
    glossary = exact_glossary(source)
    profiles = matching_profiles(source)
    flags = prefilter(source, text, window=cfg["pronoun_window_sentences"])
    return {"source": source, "translation": text, "glossary": glossary, "profiles": profiles, "flags": flags}


def detect_packet_for(number: int, inputs: dict, cfg: dict) -> str:
    return fitted(
        build_detect_packet,
        inputs["profiles"],
        cfg["packet_token_limit"],
        number=number,
        source=inputs["source"],
        translation=inputs["translation"],
        glossary=inputs["glossary"],
        flags=inputs["flags"],
    )


def dry_run_chapter(number: int, cfg: dict, out_root: Path = DRY_ROOT) -> dict:
    inputs = chapter_inputs(number, cfg)
    packet = detect_packet_for(number, inputs, cfg)
    folder = out_root / f"{number:04d}"
    atomic_text(folder / "detect-packet.md", packet)
    atomic_json(folder / "prefilter.json", inputs["flags"])
    return {
        "chapter": number,
        "packet_tokens": packet_tokens(packet),
        "counts": inputs["flags"]["counts"],
        "flagged": inputs["flags"]["flagged"],
        "final_promoted": final_promoted(number),
        "pronoun_characters": sorted({
            flag["character"] for flag in inputs["flags"]["flags"] if flag["type"] == "pronoun_conflict"
        }),
    }


def command_run(number: int, *, require_final: bool = True) -> dict:
    cfg = load_config()
    paths = chapter_paths(number)
    if not paths["translation"].exists():
        raise SystemExit(f"missing translation: translations/{number:04d}.md")
    if require_final and not final_promoted(number):
        raise SystemExit(f"chapter {number} has not been promoted by final touches")
    state = load_state(number)
    stage = state.get("stage", "NOT_STARTED")
    if stage == "COMMITTED":
        return state
    live = read_text(paths["translation"])
    if stage == "READY_TO_COMMIT":
        if sha256_text(live) != state.get("translation_sha256"):
            raise SystemExit(f"chapter {number} translation changed after the entity edit; run reset {number}")
        return state
    if stage in {"QA_FAILED", "FAILED"}:
        raise SystemExit(f"chapter {number} entity pass is {stage}; inspect reviews/entity/{number:04d}/ and run reset {number}")

    try:
        from tools.progress import step
    except ModuleNotFoundError:
        from progress import step

    if stage == "NOT_STARTED":
        paths["root"].mkdir(parents=True, exist_ok=True)
        atomic_text(paths["baseline"], live)
        inputs = chapter_inputs(number, cfg, live)
        atomic_json(paths["prefilter"], inputs["flags"])
        atomic_text(paths["detect_packet"], detect_packet_for(number, inputs, cfg))
        state = save_state(
            number,
            stage="PREPARED",
            baseline_sha256=sha256_text(live),
            source_sha256=sha256_text(inputs["source"]),
            flags=inputs["flags"]["counts"],
        )
    baseline = read_text(paths["baseline"])
    if sha256_text(live) != state.get("baseline_sha256"):
        raise SystemExit(f"chapter {number} translation changed since the entity pass began; run reset {number}")
    inputs = chapter_inputs(number, cfg, baseline)
    if sha256_text(inputs["source"]) != state.get("source_sha256"):
        raise SystemExit(f"chapter {number} source changed since the entity pass began; run reset {number}")
    source = inputs["source"]

    if state["stage"] == "PREPARED":
        detection, model = _structured_call(
            number, paths, "detect", cfg, lambda value: validate_detection(value, source, baseline),
        )
        detection["model"] = model
        atomic_json(paths["detect"], detection)
        state = save_state(number, stage="DETECTED")
    detection = json.loads(read_text(paths["detect"]))
    escalated = select_escalation(detection, cfg)

    if state["stage"] == "DETECTED":
        if needs_escalation(detection, cfg):
            packet = fitted(
                build_escalate_packet,
                inputs["profiles"],
                cfg["packet_token_limit"],
                number=number,
                source=source,
                translation=baseline,
                glossary=inputs["glossary"],
                flags=inputs["flags"],
                detection=detection,
                ids=escalated,
            )
            atomic_text(paths["escalate_packet"], packet)
            escalation, model = _structured_call(
                number, paths, "escalate", cfg,
                lambda value: validate_escalation(value, escalated, source, baseline),
            )
            escalation["model"] = model
            escalation["escalated"] = escalated
            atomic_json(paths["escalate"], escalation)
        state = save_state(number, stage="ESCALATED", escalated=escalated)
    escalation = json.loads(read_text(paths["escalate"])) if paths["escalate"].exists() else None

    findings = resolve(detection, escalation, escalated, cfg, source, baseline)
    auto = [item for item in findings if item["status"] == "auto"]
    candidate = baseline
    qa: dict | None = None
    applied = False
    if auto:
        try:
            candidate = apply_findings(baseline, auto)
        except ValueError as exc:
            for item in auto:
                item.update(status="human", reason=f"atomic apply blocked: {exc}")
            candidate = baseline
        else:
            qa = entity_qa(number, source, baseline, candidate, inputs["glossary"], cfg)
            atomic_json(paths["qa"], qa)
            if not qa["passed"]:
                messages = "; ".join(item.get("message", "") for item in qa["new_errors"])
                for item in auto:
                    item.update(status="human", reason=f"final QA failed: {messages}")
                atomic_json(paths["result"], {"version": 1, "chapter": number, "findings": findings})
                atomic_text(paths["report"], report_markdown(number, findings, detection, escalation, inputs["flags"], False))
                save_state(number, stage="QA_FAILED")
                raise SystemExit(f"entity edit for chapter {number} failed final QA: {messages}")
            applied = True
    counts = {status: sum(1 for item in findings if item["status"] == status) for status in ("auto", "human", "rejected")}
    atomic_json(paths["result"], {"version": 1, "chapter": number, "applied": applied, "counts": counts, "findings": findings})
    atomic_text(paths["report"], report_markdown(number, findings, detection, escalation, inputs["flags"], applied))
    if applied:
        atomic_text(paths["translation"], candidate)
    state = save_state(
        number,
        stage="READY_TO_COMMIT",
        applied=applied,
        counts=counts,
        translation_sha256=sha256_text(candidate),
    )
    step("entity", "ready to commit", facts=[f"{counts['auto']} applied", f"{counts['human']} for review"])
    return state


def command_reset(number: int) -> None:
    paths = chapter_paths(number)
    state = load_state(number)
    if state.get("stage") == "COMMITTED":
        raise SystemExit(f"chapter {number} entity pass is committed; nothing to reset")
    if paths["baseline"].exists() and state.get("stage") in {"READY_TO_COMMIT", "QA_FAILED"}:
        live = read_text(paths["translation"])
        if sha256_text(live) == state.get("translation_sha256"):
            atomic_text(paths["translation"], read_text(paths["baseline"]))
    if paths["root"].exists():
        shutil.rmtree(paths["root"])
    print(f"Chapter {number}: entity state removed")


# ---------------------------------------------------------------- estimate


def estimate(records: list[dict], cfg: dict, workers: int) -> dict:
    est = cfg.get("estimate") or {}
    det = est.get("detector_usd_per_chapter", [0.003, 0.006])
    esc = est.get("escalation_usd_per_chapter", [0.06, 0.08])
    det_s = float(est.get("detector_seconds_per_chapter", 60))
    esc_s = float(est.get("escalation_seconds_per_chapter", 50))
    count = len(records)
    flagged = sum(1 for item in records if item.get("flagged"))
    tokens = sum(item["packet_tokens"] for item in records)
    rates = sorted({round(flagged / count, 3) if count else 0.0, *est.get("escalation_rate_scenarios", [0.1, 0.3, 0.6])})
    scenarios = []
    for rate in rates:
        sol = count * rate
        scenarios.append({
            "escalation_rate": rate,
            "escalated_chapters": round(sol),
            "usd_low": round(count * det[0] + sol * esc[0], 2),
            "usd_high": round(count * det[1] + sol * esc[1], 2),
            "hours": round((count * det_s + sol * esc_s) / max(1, workers) / 3600, 1),
        })
    return {
        "chapters": count,
        "flagged_chapters": flagged,
        "packet_tokens_total": tokens,
        "packet_tokens_mean": round(tokens / count) if count else 0,
        "packet_tokens_max": max((item["packet_tokens"] for item in records), default=0),
        "detector_usd": [round(count * det[0], 2), round(count * det[1], 2)],
        "workers": workers,
        "flagged_rate": round(flagged / count, 3) if count else 0.0,
        "scenarios": scenarios,
    }


def summary_markdown(records: list[dict], est: dict) -> str:
    totals = {kind: sum(item["counts"].get(kind, 0) for item in records) for kind in FLAG_TYPES}
    chapters = {kind: sum(1 for item in records if item["counts"].get(kind)) for kind in FLAG_TYPES}
    lines = [
        "# Entity Pass — Dry-Run Prefilter Summary",
        "",
        f"Chapters: {est['chapters']} · flagged: {est['flagged_chapters']} · "
        f"not final-promoted yet: {sum(1 for item in records if not item['final_promoted'])}",
        "",
        "| Flag | Hits | Chapters |",
        "| ---- | ---: | -------: |",
        *[f"| {kind} | {totals[kind]} | {chapters[kind]} |" for kind in FLAG_TYPES],
        "",
        "## Top chapters",
        "",
        "| Chapter | Flags | Breakdown |",
        "| ------: | ----: | --------- |",
    ]
    ranked = sorted(records, key=lambda item: (-sum(item["counts"].values()), item["chapter"]))
    for item in ranked[:30]:
        total = sum(item["counts"].values())
        if not total:
            break
        parts = ", ".join(f"{kind} {value}" for kind, value in item["counts"].items() if value)
        lines.append(f"| {item['chapter']} | {total} | {parts} |")
    by_character: dict[str, list[int]] = {}
    for item in records:
        for name in item.get("pronoun_characters", []):
            by_character.setdefault(name, []).append(item["chapter"])
    ranked_characters = sorted(by_character.items(), key=lambda pair: (-len(pair[1]), pair[0]))[:25]
    lines += [
        "",
        "## Characters with pronoun conflicts",
        "",
        "Many chapters for one character usually means the profile gender is wrong, not the text.",
        "Fix the profile before the real run.",
        "",
        "| Character | Chapters | First chapters |",
        "| --------- | -------: | -------------- |",
        *[
            f"| {name} | {len(numbers)} | {', '.join(map(str, numbers[:8]))} |"
            for name, numbers in ranked_characters
        ],
        "",
    ]
    lines += [
        "## Cost and time estimate",
        "",
        f"Packet tokens: total {est['packet_tokens_total']:,}, mean {est['packet_tokens_mean']:,}, "
        f"max {est['packet_tokens_max']:,}. Detector on every chapter: "
        f"${est['detector_usd'][0]}–${est['detector_usd'][1]}.",
        "",
        f"| Escalation rate | Sol chapters | USD | Hours ({est['workers']} workers) |",
        "| --------------: | -----------: | --: | ----: |",
        *[
            f"| {row['escalation_rate']:.0%} | {row['escalated_chapters']} | "
            f"${row['usd_low']}–${row['usd_high']} | {row['hours']} |"
            for row in est["scenarios"]
        ],
        "",
        f"The {est['flagged_rate']:.0%} row is the prefilter-flagged share, a rough escalation rate.",
    ]
    return "\n".join(lines) + "\n"


def range_report(start: int, end: int) -> str:
    lines = [f"# Entity Pass — Human Review {start}–{end}", ""]
    for number in range(start, end + 1):
        path = chapter_paths(number)["result"]
        if not path.exists():
            continue
        result = json.loads(read_text(path))
        items = [item for item in result.get("findings", []) if item.get("status") == "human"]
        if not items:
            continue
        lines += [f"## Chapter {number}", ""]
        for item in items:
            lines.append(
                f"- **{item['id']}** {item['category']} ({item['confidence']:.2f}): "
                f"“{item['current']}” → “{item['replacement']}” — {item['explanation']} "
                f"[{item.get('reason', '')}]"
            )
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    run = sub.add_parser("run", help="check one finalized chapter and stop before commit")
    run.add_argument("chapter", type=int)
    for name in ("status", "reset"):
        sub.add_parser(name).add_argument("chapter", type=int)
    report = sub.add_parser("report", help="human-review findings for a range")
    report.add_argument("start", type=int)
    report.add_argument("end", type=int)
    report.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.command == "status":
        state = load_state(args.chapter)
        print(f"Chapter: {args.chapter}\nStage: {state.get('stage')}\nCounts: {state.get('counts', {})}")
        return 0
    if args.command == "report":
        text = range_report(args.start, args.end)
        if args.output:
            atomic_text(args.output, text)
            print(args.output)
        else:
            print(text, end="")
        return 0
    try:
        from tools.run_lock import ENTITY_LOCK_NAME, hold_entity_lock, parent_delegated
    except ModuleNotFoundError:
        from run_lock import ENTITY_LOCK_NAME, hold_entity_lock, parent_delegated
    action = command_run if args.command == "run" else command_reset
    if parent_delegated(ENTITY_LOCK_NAME):
        action(args.chapter)
        return 0
    with hold_entity_lock(ROOT, holder="entity_pass", chapter=args.chapter, stage=args.command):
        action(args.chapter)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
