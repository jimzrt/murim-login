#!/usr/bin/env python3
"""Durable Korean→English names ledger and Revised Romanization helpers."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KOREAN = re.compile(r"[가-힣]{2,}")
TABLE_ROW = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|.*$")
# Ledger keys may contain spaces: 파이 첸, 김 집사, 지크프리트 바스만.
KOREAN_KEY = re.compile(r"[가-힣]+(?: [가-힣]+)*")
HEADING = re.compile(r"^#\s+(.+?)\s*\(([가-힣]+(?: [가-힣]+)*)\)\s*$")
ALIAS_LINE = re.compile(r"^- \*\*Aliases:\*\*\s*(.+)$")
ALIAS_PAIR = re.compile(r"([^;,(]+?)\s*\(([가-힣]+(?: [가-힣]+)*)\)")
GENDER_LINE = re.compile(r"^- \*\*Gender:\*\*\s*(.*)$", re.MULTILINE)
GENDERS = ("female", "male", "unknown")
# One line per range: `- **Appearance (ch A–B):** text`, `- **Appearance (from ch C):** text`,
# or `- **Appearance:** not described`. The legacy `(as of ch N)` bound is still recognised.
APPEARANCE_LINE = re.compile(
    r"^- \*\*Appearance(?: \((?:as of ch \d+|ch \d+–\d+|from ch \d+)\))?:\*\*.*$", re.MULTILINE
)
APPEARANCE_RANGE = re.compile(
    r"^- \*\*Appearance \((?:ch (?P<start>\d+)–(?P<end>\d+)|from ch (?P<from>\d+))\):\*\* (?P<text>.+)$"
)

CHOSEONG = ["g", "kk", "n", "d", "tt", "r", "m", "b", "pp", "s", "ss", "", "j", "jj", "ch", "k", "t", "p", "h"]
JUNGSEONG = [
    "a", "ae", "ya", "yae", "eo", "e", "yeo", "ye", "o", "wa", "wae", "oe", "yo",
    "u", "wo", "we", "wi", "yu", "eu", "ui", "i",
]
JONGSEONG = [
    "", "k", "k", "k", "n", "n", "n", "t", "l", "l", "l", "l", "l", "l", "l", "l",
    "m", "p", "p", "t", "t", "ng", "t", "t", "k", "t", "p", "t",
]


def is_korean_key(value: str) -> bool:
    """Hangul words separated by single spaces, at least two syllables."""
    value = value.strip()
    return KOREAN_KEY.fullmatch(value) is not None and len(value.replace(" ", "")) >= 2


def strip_english(value: str) -> str:
    return re.sub(r"[*_`]", "", value).strip()


def preferred_english_terms(english: str) -> list[str]:
    """Preferred glossary renderings; slash-separated cells are alternatives."""
    parts = [part.strip() for part in strip_english(english).split(" / ") if part.strip()]
    if len(parts) <= 1:
        return parts
    substantial = [part for part in parts if len(part) >= 3]
    return substantial or parts


def preferred_english_present(text: str, english: str) -> bool:
    folded = text.casefold()
    return any(term.casefold() in folded for term in preferred_english_terms(english))


def romanize_syllable(char: str) -> str:
    code = ord(char) - 0xAC00
    if not 0 <= code <= 11171:
        return char
    initial, rest = divmod(code, 21 * 28)
    medial, final = divmod(rest, 28)
    return CHOSEONG[initial] + JUNGSEONG[medial] + JONGSEONG[final]


def romanize(text: str) -> str:
    return "".join(romanize_syllable(char) if "가" <= char <= "힣" else char for char in text)


def profile_koreans(body: str) -> list[str]:
    names: list[str] = []
    for line in body.splitlines():
        heading = HEADING.match(line)
        if heading:
            if is_korean_key(heading.group(2)):
                names.append(heading.group(2))
            continue
        aliases = ALIAS_LINE.match(line)
        if aliases:
            names.extend(
                match.group(2)
                for match in ALIAS_PAIR.finditer(aliases.group(1))
                if is_korean_key(match.group(2))
            )
    return names


def normalize_gender(value: object) -> str:
    """Profile gender is female, male, or unknown; anything else is unknown."""
    if not isinstance(value, str):
        return "unknown"
    words = re.findall(r"[a-z]+", value.casefold())
    return words[0] if words and words[0] in GENDERS else "unknown"


def profile_gender(body: str) -> str:
    match = GENDER_LINE.search(body)
    return normalize_gender(match.group(1)) if match else "unknown"


def set_profile_gender(body: str, gender: str) -> str:
    """Write one Gender line, placed after Aliases (or Safe through)."""
    line = f"- **Gender:** {normalize_gender(gender)}"
    if GENDER_LINE.search(body):
        return GENDER_LINE.sub(line, body, count=1)
    lines = body.splitlines()
    anchor = None
    for index, text in enumerate(lines):
        if text.startswith("- **Aliases:**"):
            anchor = index
            break
        if text.startswith("- **Safe through:**"):
            anchor = index
    if anchor is None:
        raise ValueError("character profile has no Aliases or Safe through line")
    lines.insert(anchor + 1, line)
    text = "\n".join(lines)
    return text + "\n" if body.endswith("\n") else text


def profile_appearance(body: str) -> str | None:
    """All Appearance lines (one per range) joined by newlines, or None when the profile has none."""
    lines = [m.group(0) for m in APPEARANCE_LINE.finditer(body)]
    return "\n".join(lines) if lines else None


def appearance_ranges(body: str) -> list[dict]:
    """Parsed ranges: start, end (None = open-ended), text. Empty for 'not described'."""
    ranges = []
    for line in body.split("\n"):
        match = APPEARANCE_RANGE.match(line)
        if match:
            start = int(match["start"] or match["from"])
            ranges.append({"start": start, "end": int(match["end"]) if match["end"] else None,
                           "text": match["text"]})
    return ranges


def strip_appearance(body: str) -> str:
    """Body without its Appearance lines (generated tools never see or edit them)."""
    kept = [line for line in body.split("\n") if not APPEARANCE_LINE.match(line)]
    return "\n".join(kept)


def set_profile_appearance(body: str, lines: str | list[str] | None) -> str:
    """Write the Appearance lines after Relationships (else before Sources, else at the end)."""
    body = strip_appearance(body)
    if not lines:
        return body
    new = lines.split("\n") if isinstance(lines, str) else list(lines)
    existing = body.rstrip("\n").splitlines()
    anchor = None
    for index, text in enumerate(existing):
        if text.startswith("- **Relationships:**"):
            anchor = index + 1
            break
    if anchor is None:
        anchor = next((i for i, t in enumerate(existing) if t.startswith("- **Sources:**")), len(existing))
    existing[anchor:anchor] = new
    return "\n".join(existing) + "\n"


def _row(korean: str, english: str, note: str = "") -> dict:
    plain = strip_english(english)
    display = english.strip() if english.strip().startswith("**") else f"**{plain}**"
    suffix = f" | {note}" if note else ""
    return {"korean": korean, "english": display, "row": f"| {korean} | {display}{suffix} |"}


def _add(index: dict[str, dict], korean: str, english: str, *, overwrite: bool = False) -> None:
    korean = korean.strip()
    if not is_korean_key(korean):
        return
    if korean in index and not overwrite:
        return
    index[korean] = _row(korean, english)


def _load_table(path: Path, index: dict[str, dict], *, overwrite: bool) -> None:
    if not path.is_file():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        match = TABLE_ROW.match(line)
        if not match:
            continue
        korean = match.group(1).strip()
        english = match.group(2).strip()
        if not is_korean_key(korean):
            continue
        if korean in index and not overwrite:
            continue
        index[korean] = {"korean": korean, "english": english, "row": line}


def _load_profiles(index: dict[str, dict]) -> None:
    directory = ROOT / "characters"
    if not directory.is_dir():
        return
    for path in sorted(directory.glob("*.md")):
        body = path.read_text(encoding="utf-8")
        heading_english = path.stem
        for line in body.splitlines():
            heading = HEADING.match(line)
            if heading:
                heading_english = heading.group(1).strip()
                _add(index, heading.group(2), heading_english)
                continue
            aliases = ALIAS_LINE.match(line)
            if not aliases:
                continue
            text = aliases.group(1).strip()
            if text.casefold() in {"none revealed", "name not yet revealed"}:
                continue
            for match in ALIAS_PAIR.finditer(text):
                _add(index, match.group(2), match.group(1).strip())


def unique_korean_for_english(english: str, extra: list[tuple[str, str]] | None = None) -> str | None:
    """Return a unique Hangul name for an English person label, or None."""
    needle = strip_english(english).casefold()
    if not needle:
        return None
    found: list[str] = []
    for korean, label in extra or []:
        if strip_english(label).casefold() == needle and is_korean_key(korean):
            found.append(korean.strip())
    directory = ROOT / "characters"
    if directory.is_dir():
        for path in directory.glob("*.md"):
            body = path.read_text(encoding="utf-8")
            heading = next((HEADING.match(line) for line in body.splitlines() if HEADING.match(line)), None)
            if heading is None:
                continue
            labels = {heading.group(1).strip().casefold(), path.stem.casefold()}
            if needle in labels:
                found.append(heading.group(2))
    unique = list(dict.fromkeys(found))
    if len(unique) == 1:
        return unique[0]
    return None


def load_names_ledger() -> list[dict]:
    index: dict[str, dict] = {}
    _load_table(ROOT / "compendium.md", index, overwrite=False)
    _load_profiles(index)
    _load_table(ROOT / "docs" / "NAMES.md", index, overwrite=True)
    return list(index.values())


def ledger_for_source(source: str) -> list[dict]:
    entries: list[dict] = []
    seen: set[str] = set()
    for item in load_names_ledger():
        korean = item["korean"]
        if korean in source and korean not in seen:
            entries.append(item)
            seen.add(korean)
    return entries


JOSA = (
    "에게서", "으로부터", "에서", "으로", "에게", "부터", "까지", "처럼", "보다",
    "이나", "이랑", "이란", "이", "가", "을", "를", "은", "는", "의", "도", "만", "과", "와", "로",
)
IGNORED_KOREAN = {"하하하"}


def _cores(token: str) -> list[str]:
    cores = [token]
    for josa in JOSA:
        if token.endswith(josa) and len(token) - len(josa) >= 2:
            cores.append(token[: -len(josa)])
            break
    return cores


def romanization_variants(korean: str) -> set[str]:
    syllables = [romanize_syllable(char) for char in korean if "가" <= char <= "힣"]
    joined = "".join(syllables).casefold()
    variants = {joined}
    if len(syllables) >= 2:
        variants.add("-".join(syllables).casefold())
        variants.add(" ".join(syllables).casefold())
    return {item for item in variants if item}


TOKEN = re.compile(r"[A-Za-z]+(?:-[A-Za-z]+)*")


def _english_tokens(translation: str) -> set[str]:
    tokens: set[str] = set()
    for raw in TOKEN.findall(translation):
        if not raw[0].isupper():
            continue
        folded = raw.casefold()
        tokens.add(folded)
        tokens.add(folded.replace("-", ""))
    return tokens


def _romanization_sequences(translation: str) -> set[str]:
    words = [word.casefold() for word in re.findall(r"[A-Za-z]+(?:-[A-Za-z]+)*", translation)]
    return {" ".join(words[index:index + size]) for size in (2, 3) for index in range(len(words) - size + 1)}


def _romanization_hit(korean: str, tokens: set[str]) -> bool:
    for item in romanization_variants(korean):
        letters = re.sub(r"[^a-z]", "", item)
        if len(letters) < 6:
            continue
        if item in tokens or item.replace("-", "").replace(" ", "") in tokens:
            return True
    return False


def novel_romanizations(source: str, translation: str, ledger: list[dict] | None = None) -> list[dict]:
    known = {item["korean"] for item in (ledger if ledger is not None else load_names_ledger())}
    tokens = _english_tokens(translation)
    sequences = _romanization_sequences(translation)
    found: list[dict] = []
    seen: set[str] = set()
    for korean in KOREAN.findall(source):
        if korean in IGNORED_KOREAN:
            continue
        if any(korean == term or korean.startswith(term) for term in known):
            continue
        for core in _cores(korean):
            if core in seen or core in known:
                continue
            variants = romanization_variants(core)
            if _romanization_hit(core, tokens) or any(
                item in sequences and len(re.sub(r"[^a-z]", "", item)) >= 6
                for item in variants
                if " " in item
            ):
                found.append({"korean": core, "romanization": romanize(core)})
                seen.add(core)
                break
    return found
