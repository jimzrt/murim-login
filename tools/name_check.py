#!/usr/bin/env python3
"""Precise proper-name checks: Korean name boundaries, wrong variants, drift.

The generic terminology warning in qa.py matches any glossary key as a
substring (진태 inside 진태경, 상태 inside 상태창) and compares common words, so
it is noise. This module limits itself to proper names (people, sects, places,
skills), requires the Korean to stand at a word boundary, and reports:

- known wrong English variants from docs/NAME_VARIANTS.md (blocking in final QA);
- capitalized renderings that look like a drifted spelling of a ledger name;
- a profiled person's name whose English is absent.
"""

from __future__ import annotations

import difflib
import re
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VARIANTS_PATH = ROOT / "docs" / "NAME_VARIANTS.md"

try:
    from tools.names import (
        ALIAS_LINE, ALIAS_PAIR, HEADING, KOREAN, TABLE_ROW, preferred_english_terms,
        romanize_syllable, strip_english,
    )
except ModuleNotFoundError:
    from names import (
        ALIAS_LINE, ALIAS_PAIR, HEADING, KOREAN, TABLE_ROW, preferred_english_terms,
        romanize_syllable, strip_english,
    )

HANGUL = re.compile(r"[가-힣]")
# Particles, endings, and honorifics that may follow a name inside one Hangul run.
SUFFIXES = sorted(
    {
        "에게서", "으로부터", "한테서", "이라는", "이라고", "이라면", "이었다", "이었던",
        "이에요", "이여", "이시여", "께서는", "께서", "에게", "한테", "에서", "으로", "부터",
        "까지", "처럼", "보다", "조차", "마저", "이나", "이랑", "이란", "이라", "이다",
        "이고", "이며", "이든", "이야", "이지", "이가", "이는", "이를", "이의", "이도",
        "이만", "이와", "이요", "였다", "였던", "라는", "라고", "라면", "하고", "랑",
        "였", "이", "가", "을", "를", "은", "는", "의", "도", "만", "과", "와", "로",
        "에", "께", "야", "아", "여", "요", "나", "든", "다", "고", "며", "지", "들",
        "님", "씨", "형", "누나", "언니", "오빠", "선배",
        "소저", "대협", "공자", "낭자", "부인", "사부", "사형", "사제", "사매", "사저",
        "님이", "님은", "님의", "님을", "님께", "님께서",
    },
    key=len,
    reverse=True,
)
LOWER_CONNECTORS = {"of", "the", "and", "de", "du", "von", "van", "al", "bin", "la", "le", "in", "on", "to", "a"}
NAME_WORD = re.compile(r"^[A-Z][A-Za-z'’.-]*$")
CAPITALIZED_RUN = re.compile(r"\b[A-Z][a-z'’-]+(?:[ -][A-Z][a-z'’-]+){0,3}\b")
# Ordinary English words that open a sentence and are never a name rendering.
COMMON_CAPS = {
    "The", "A", "An", "And", "But", "Or", "So", "If", "He", "She", "It", "They", "We",
    "I", "You", "His", "Her", "Their", "Our", "My", "Your", "This", "That", "These",
    "Those", "What", "Why", "How", "When", "Where", "Who", "Then", "There", "Here",
    "Yes", "No", "Not", "Now", "Just", "Still", "Even", "Only", "Well", "Oh", "Ah",
    "Hey", "Huh", "Hmm", "System", "Chapter", "Level", "Lv", "Skill", "Status",
}


def name_at_boundary(source: str, korean: str) -> bool:
    """True when the Korean name occurs as a whole word plus particles/honorifics."""
    start = 0
    while True:
        index = source.find(korean, start)
        if index < 0:
            return False
        start = index + 1
        if index > 0 and HANGUL.match(source[index - 1]):
            continue
        end = index + len(korean)
        run_end = end
        while run_end < len(source) and HANGUL.match(source[run_end]):
            run_end += 1
        if _only_suffixes(source[end:run_end]):
            return True


def _only_suffixes(rest: str) -> bool:
    while rest:
        for suffix in SUFFIXES:
            if rest.startswith(suffix):
                rest = rest[len(suffix):]
                break
        else:
            return False
    return True


def is_proper_name(english: str) -> bool:
    """Capitalized name-like English: every non-connector word starts uppercase."""
    terms = preferred_english_terms(english)
    if len(terms) != 1:
        return False
    words = terms[0].split()
    if not words or not NAME_WORD.match(words[0]):
        return False
    if any(any(char.isdigit() for char in word) for word in words):
        return False
    return all(NAME_WORD.match(word) or word in LOWER_CONNECTORS for word in words)


def fold_quotes(text: str) -> str:
    return text.replace("’", "'").replace("‘", "'")


@lru_cache(maxsize=8192)
def _english_pattern(term: str) -> re.Pattern:
    # Plural and possessive forms count: Orcs, Liches, Faye Chen's.
    return re.compile(
        r"(?<![A-Za-z])" + re.escape(fold_quotes(term)) + r"(?:s|es|'s)?(?![A-Za-z])"
    )


def english_present(text: str, term: str) -> bool:
    return _english_pattern(term).search(fold_quotes(text)) is not None


@lru_cache(maxsize=4)
def _entries_cached(root: str) -> tuple[dict, ...]:
    base = Path(root)
    index: dict[str, dict] = {}

    def add(korean: str, english: str, kind: str, *, overwrite: bool) -> None:
        korean = korean.strip()
        plain = strip_english(english)
        if not KOREAN.search(korean) or not plain:
            return
        if korean in index and not overwrite:
            return
        index[korean] = {"korean": korean, "english": plain, "kind": kind}

    def table(path: Path, *, overwrite: bool) -> None:
        if not path.is_file():
            return
        for line in path.read_text(encoding="utf-8").splitlines():
            match = TABLE_ROW.match(line)
            if not match:
                continue
            korean, english = match.group(1).strip(), match.group(2).strip()
            if not re.fullmatch(r"[가-힣]+(?: [가-힣]+)*", korean):
                continue
            if is_proper_name(english):
                add(korean, english, "ledger", overwrite=overwrite)
            elif overwrite:
                index.pop(korean, None)

    table(base / "compendium.md", overwrite=False)
    directory = base / "characters"
    if directory.is_dir():
        for path in sorted(directory.glob("*.md")):
            body = path.read_text(encoding="utf-8")
            for line in body.splitlines():
                heading = HEADING.match(line)
                if heading:
                    add(heading.group(2), heading.group(1), "person", overwrite=True)
                    continue
                aliases = ALIAS_LINE.match(line)
                if aliases:
                    for match in ALIAS_PAIR.finditer(aliases.group(1)):
                        english = match.group(1).strip()
                        if is_proper_name(english):
                            add(match.group(2), english, "person", overwrite=True)
    table(base / "docs" / "NAMES.md", overwrite=True)
    # NAMES.md overrides the English; a profiled person stays a person.
    people = {
        heading.group(2)
        for path in (directory.glob("*.md") if directory.is_dir() else [])
        for heading in [HEADING.match(path.read_text(encoding="utf-8").splitlines()[0])]
        if heading
    }
    for korean in people:
        if korean in index:
            index[korean]["kind"] = "person"
    variants = load_variants(base / "docs" / "NAME_VARIANTS.md")
    for korean, item in index.items():
        item["variants"] = variants.get(korean, [])
    return tuple(index.values())


def proper_name_entries(root: Path = ROOT) -> list[dict]:
    return [dict(item) for item in _entries_cached(str(root))]


def load_variants(path: Path = VARIANTS_PATH) -> dict[str, list[str]]:
    """`| Korean | Preferred | Wrong variants (semicolon-separated) |` rows."""
    found: dict[str, list[str]] = {}
    if not path.is_file():
        return found
    for line in path.read_text(encoding="utf-8").splitlines():
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 3 or not KOREAN.search(cells[0]) or not re.fullmatch(r"[가-힣 ]+", cells[0]):
            continue
        wrong = [strip_english(part) for part in cells[2].split(";") if strip_english(part)]
        if wrong:
            found.setdefault(cells[0], []).extend(wrong)
    return found


def matched_names(source: str, entries: list[dict] | None = None) -> list[dict]:
    """Proper-name entries whose Korean stands at a word boundary in the source.

    A shorter key covered by a longer matched key at every occurrence is
    already excluded by the boundary rule (진태 never stands alone in 진태경).
    """
    entries = proper_name_entries() if entries is None else entries
    return [item for item in entries if item["korean"] in source and name_at_boundary(source, item["korean"])]


def romanization(korean: str) -> str:
    return "".join(romanize_syllable(char) for char in korean if "가" <= char <= "힣")


def _similar(left: str, right: str) -> float:
    return difflib.SequenceMatcher(None, left.casefold(), right.casefold()).ratio()


def _known_english(entries: list[dict]) -> set[str]:
    return {fold_quotes(item["english"]).casefold() for item in entries}


def _windows(translation: str, width: int) -> list[str]:
    """Every run of `width` consecutive capitalized words."""
    spans: list[str] = []
    for match in CAPITALIZED_RUN.finditer(fold_quotes(translation)):
        words = match.group(0).split(" ")
        for index in range(len(words) - width + 1):
            spans.append(" ".join(words[index:index + width]))
    return spans


def suspect_variants(item: dict, translation: str, entries: list[dict]) -> list[str]:
    """Capitalized renderings that look like a drifted spelling of this name.

    Same word count as the preferred English and not itself a ledger
    rendering. A one-word name must be a transliteration, be spelled almost
    alike, and never occur in lowercase. A longer name must share a word with the preferred English,
    and each other word must be spelled alike or sound like the Korean.
    """
    preferred = fold_quotes(item["english"])
    target_words = preferred.split()
    known = _known_english(entries)
    roman = [romanization(part) for part in item["korean"].split()]
    folded_text = fold_quotes(translation)
    # A one-word English common noun (Status, Fame) is not a spelling target.
    transliterated = _similar(preferred.replace("-", ""), "".join(roman)) >= 0.5
    found: list[str] = []
    for candidate in _windows(translation, len(target_words)):
        words = candidate.split()
        if "'" in candidate or candidate in found or candidate.casefold() in known:
            continue
        if words[0] in COMMON_CAPS or _inflection(words, target_words):
            continue
        if len(words) == 1:
            if (
                transliterated
                and len(candidate) >= 4
                and _similar(candidate, preferred) >= 0.8
                and not re.search(r"(?<![A-Za-z])" + re.escape(candidate.casefold()) + r"(?![A-Za-z])", folded_text)
            ):
                found.append(candidate)
            continue
        same = [a.casefold() == b.casefold() for a, b in zip(words, target_words)]
        if not any(same):
            continue
        drifted = True
        for position, (word, target) in enumerate(zip(words, target_words)):
            if same[position]:
                continue
            sound = roman[position] if len(roman) == len(words) else ""
            if _similar(word, target) >= 0.7 or (sound and _similar(word, sound) >= 0.6):
                continue
            drifted = False
            break
        if drifted:
            found.append(candidate)
    return found


def _squeeze(word: str) -> str:
    """Fold drawn-out spellings: Caaaptain, Taekyuuung."""
    return re.sub(r"(.)\1{2,}|([aeiou])\2", r"\1\2", word.casefold())


def _inflection(words: list[str], target: list[str]) -> bool:
    """Same name with a derived last word: Japan/Japanese, Magic/Magical."""
    if [word.casefold() for word in words[:-1]] != [word.casefold() for word in target[:-1]]:
        return False
    last, goal = _squeeze(words[-1]), _squeeze(target[-1])
    if last == goal or last.replace("men", "man") == goal:
        return True
    stem = min(len(last), len(goal))
    return stem >= 3 and (last.startswith(goal) or goal.startswith(last) or last[: stem - 1] == goal[: stem - 1] and abs(len(last) - len(goal)) <= 2)


def check_names(source: str, translation: str, entries: list[dict] | None = None) -> dict[str, list[dict]]:
    """Name findings for one chapter: blocking errors and high-signal warnings."""
    entries = proper_name_entries() if entries is None else entries
    errors: list[dict] = []
    warnings: list[dict] = []
    matched = matched_names(source, entries)
    for item in matched:
        korean, preferred = item["korean"], item["english"]
        # A variant that is another matched name's preferred English (대마도사 →
        # Grand Mage next to 대술사 → Grand Sorceress) is legitimate here.
        others = {fold_quotes(other["english"]).casefold() for other in matched if other["korean"] != korean}
        wrong = [
            variant for variant in item.get("variants", [])
            if english_present(translation, variant) and fold_quotes(variant).casefold() not in others
        ]
        if wrong:
            errors.append({
                "code": "name_variant",
                "message": "a known wrong English rendering of a ledger name is used; use the preferred English",
                "details": {"korean": korean, "preferred": preferred, "found": wrong},
            })
            continue
        suspects = suspect_variants(item, translation, entries)
        if suspects and not english_present(translation, preferred):
            warnings.append({
                "code": "name_variant_suspect",
                "message": "the preferred English for a ledger name is absent and a similar spelling is used",
                "details": {"korean": korean, "preferred": preferred, "found": suspects},
            })
            continue
        # Two-syllable names are often ordinary words too (신의, 태산, 황소).
        distinctive = " " in korean or len(korean) >= 3
        if item["kind"] == "person" and distinctive and not _any_name_word(translation, preferred):
            warnings.append({
                "code": "name_absent",
                "message": "a profiled character named in the source is absent from the English",
                "details": {"korean": korean, "preferred": preferred},
            })
    return {"errors": errors, "warnings": warnings}


def _any_name_word(translation: str, preferred: str) -> bool:
    if english_present(translation, preferred):
        return True
    words = [word for word in preferred.split() if word not in LOWER_CONNECTORS and len(word) >= 3]
    return any(english_present(translation, word) for word in words)


def name_corrections(source: str, baseline: str, entries: list[dict] | None = None) -> list[dict]:
    """Known wrong variants already present in the baseline, for the packet."""
    return [
        {**finding["details"]}
        for finding in check_names(source, baseline, entries)["errors"]
    ]
