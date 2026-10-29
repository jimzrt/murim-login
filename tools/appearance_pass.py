#!/usr/bin/env python3
"""Spoiler-safe, range-aware `Appearance` field for the most recurring character profiles.

Repeatable and resumable. Stages per character, saved in
`reviews/appearance/NNN-slug.json` (rank-ordered, with exact Korean quotes):

1. rank       chapters (whole book, no Safe-through cap) naming the character (profile names/aliases + docs/NAMES.md)
2. candidates cue paragraphs from ALL chapters, spread evenly over the
              chapter range; the narrator also gets mirror/self-description paragraphs
3. extract    Sonnet calls over passage batches: facts with chapter, kind and verbatim Korean quote
4. verify     drop facts whose quote is not in that chapter's source
5. triage     one Sonnet call groups facts that conflict on an attribute
6. judge      Sonnet checks conflicting facts and change candidates with +-3 paragraphs of context
              (this character? literal and present, not flashback/metaphor/disguise? lasting change?);
              a change candidate also needs a Korean change marker (CHANGE_RE), checked deterministically
7. write      one Sonnet call merges the kept facts into look ranges. A range after the first may open only
              at an approved lasting change and must differ visibly from the previous one; no range may use
              a later fact; conflicts are not mixed (best-supported value kept, `conflicts` recorded in the
              JSON and summarised in reviews/appearance/conflicts.md); no verified fact is dropped silently
8. apply      one profile line per range:
                 - **Appearance (ch A–B):** Name ... Tags: ...
                 - **Appearance (from ch C):** Name ... Tags: ...
              or `- **Appearance:** not described`

Reruns keep every earlier verified fact (current evidence, `--seed-rev`) unless the judge rejects it;
`--reuse-facts` skips extraction. Judge verdicts are cached in the evidence JSON.

A reader at chapter < C only needs the ranges that start before C. The lines are excluded from
translation packets (`compact_profile`) and preserved by update/compress.

    python tools/appearance_pass.py rank --top 50 --source /path/to/source
    python tools/appearance_pass.py run --only "Jin Taekyung" Mungyeong --source /path/to/source
    python tools/appearance_pass.py run --workers 6 --force --source /path/to/source
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

try:
    from tools.names import (
        ALIAS_LINE, ALIAS_PAIR, HEADING, is_korean_key, profile_gender,
        profile_koreans, set_profile_appearance, strip_english,
    )
except ModuleNotFoundError:  # run as a script
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from names import (  # type: ignore
        ALIAS_LINE, ALIAS_PAIR, HEADING, is_korean_key, profile_gender,
        profile_koreans, set_profile_appearance, strip_english,
    )

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reviews" / "appearance"
VERSION = 3
CONTEXT_PARAS = 3            # paragraphs of context each side for the judge
CONTEXT_CHARS = 320
JUDGE_BATCH = 6
JUDGE_MODEL = "sonnet"
BINS = 8                     # chapter-range bins; each keeps its strongest passages
PER_BIN = 7
PASSAGE_CHARS = 520
BUDGET_CHARS = 30000
MIN_QUOTE = 4
BATCH = 8                    # passages per extraction call
EXTRACT_MODEL = "sonnet"
WRITE_MODEL = "sonnet"
WRITE_TRIES = 3
FIRST_PERSON = {"Jin Taekyung"}   # narrator: also scan mirror / self-description scenes

STRONG_CUES = (
    "외모", "얼굴", "머리카락", "머리를", "머리는", "머리가", "머릿결", "머리칼", "머리색", "눈동자", "눈매", "눈썹", "체격",
    "덩치", "체구", "키가", "키는", "장신", "피부", "수염", "흉터", "복장", "무복", "도포", "차림", "의복", "백발", "흑발",
    "은발", "흰머리", "반백", "미남", "미녀", "인상", "콧날", "입술", "풍채", "생김", "미모", "몸집", "안색", "용모", "턱",
    "이마", "미소년", "노인", "청년", "소년", "소녀", "잘생", "못생", "예쁘", "아름다", "준수", "수려", "훤칠", "건장", "왜소",
    "마른", "뚱뚱", "비쩍", "근골", "외팔", "애꾸", "안대", "문신", "회춘", "반로환동", "환골탈태", "젊어", "늙어", "팔을 잃",
    "눈을 잃", "다리를 잃", "한쪽 눈", "한쪽 팔",
)
WEAK_CUES = ("옷", "나이", "중년", "어깨", "허리", "눈빛", "상처", "두건", "관을", "근육", "장포", "검을", "도를", "칼을",
             "창을", "활을", "변했", "달라졌", "거울", "비친", "반사", "수면에")
STRONG_RE = re.compile("|".join(map(re.escape, STRONG_CUES)))
WEAK_RE = re.compile("|".join(map(re.escape, WEAK_CUES)))
COLOUR_RE = re.compile(r"(붉|푸르|푸른|검|까맣|새까|하얀|하얗|흰|은빛|금빛|백색|흑색|회색|자색|보랏빛|녹색|초록|파란|파랗|빨간|빨갛|노란|금발)\S{0,4}\s?(눈|머리|수염|옷|의|복|피부|동공)")
# narrator self-description: mirror / reflection scenes and "my face / body" paragraphs
# Korean change markers: a new range needs one next to the quote (checked deterministically).
CHANGE_RE = re.compile(
    "잃어 ?버|흉터가 ?(가득|생|남)|흉터투성|청년으로 돌아|돌아간 |젊은 모습|젊어 ?보|젊어졌|변했|변해|변하|변모|탈바꿈|바뀌었|바뀐|되어 ?버린|되어 ?버렸|잃었|잃은|잃고|잘려 ?나간|잘려 ?나갔|잘렸|베어 ?나갔|"
    "회춘|반로환동|환골탈태|젊어진|젊어졌|늙어 ?버린|늙어 ?버렸|부쩍 늙|늙어 있|하얗게 ?세|백발이 되|새하얀 백발|"
    "흉터가 생|외팔|애꾸|돌아갔|되돌아|사라졌|없어졌|재가 되|해골|강시|언데드|변이"
)
SELF_RE = re.compile(r"(거울|비친|반사|수면에 )|((내|나의|제)\s?(얼굴|머리|눈|몸|피부|키|체격|인상|몸매|손|팔|옷))")

# --------------------------------------------------------------------- names

def plain(english: str) -> str:
    return strip_english(english).casefold()


def load_profiles() -> list[dict]:
    """One entry per profile: english, korean names, safe_through, role, gender."""
    ledger: dict[str, list[str]] = {}
    names_path = ROOT / "docs" / "NAMES.md"
    if names_path.is_file():
        for line in names_path.read_text(encoding="utf-8").splitlines():
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 2 and is_korean_key(cells[0]):
                ledger.setdefault(plain(cells[1]), []).append(cells[0])
    profiles = []
    for path in sorted((ROOT / "characters").glob("*.md")):
        body = path.read_text(encoding="utf-8")
        heading = next((HEADING.match(x) for x in body.splitlines() if HEADING.match(x)), None)
        if heading is None:
            continue
        english = heading.group(1).strip()
        labels = {plain(english)}
        alias = next((ALIAS_LINE.match(x) for x in body.splitlines() if ALIAS_LINE.match(x)), None)
        if alias:
            labels |= {plain(m.group(1)) for m in ALIAS_PAIR.finditer(alias.group(1))}
        names = list(profile_koreans(body))
        for label in labels:
            names.extend(ledger.get(label, []))
        safe = re.search(r"Safe through:\*\*\s*Chapter\s*(\d+)", body)
        role = re.search(r"^- \*\*Role:\*\*\s*(.+)$", body, re.MULTILINE)
        profiles.append({
            "english": english,
            "path": str(path.relative_to(ROOT)),
            "names": sorted(set(names), key=lambda n: (-len(n), n)),
            "safe_through": int(safe.group(1)) if safe else 0,
            "role": role.group(1).strip() if role else "",
            "gender": profile_gender(body),
        })
    return profiles


def load_source(source_dir: Path) -> dict[int, str]:
    chapters = {}
    for path in sorted(source_dir.glob("[0-9][0-9][0-9][0-9].txt")):
        chapters[int(path.stem)] = path.read_text(encoding="utf-8")
    if not chapters:
        raise SystemExit(f"no chapters in {source_dir}")
    return chapters


# Profiles that would duplicate another entry or whose Korean key is a common word.
SKIP = {
    "Divine Physician": "title profile (신의 is also a common word); Mungyeong is ranked on his own",
    "Michael": "same person as Michael Silbert",
}


# Korean names of skipped duplicate profiles, credited to the profile that is ranked.
EXTRA_NAMES = {"Michael Silbert": ["미카엘"]}


def rank(profiles: list[dict], chapters: dict[int, str], top: int) -> list[dict]:
    """Chapter counts per profile. Longest-match-first across all profiles, so 진태 does not
    claim the 진태경 occurrences of another character."""
    profiles = [p for p in profiles if p["names"] and p["english"] not in SKIP]
    for profile in profiles:
        profile["names"] = sorted({*profile["names"], *EXTRA_NAMES.get(profile["english"], [])},
                                  key=lambda n: (-len(n), n))
    owners: dict[str, set[int]] = {}
    for index, profile in enumerate(profiles):
        for name in profile["names"]:
            owners.setdefault(name, set()).add(index)
    pattern = re.compile("|".join(map(re.escape, sorted(owners, key=lambda n: (-len(n), n)))))
    hits: list[list[int]] = [[] for _ in profiles]
    for number, text in chapters.items():
        seen: set[int] = set()
        for match in pattern.finditer(text):
            seen |= owners[match.group(0)]
        for index in seen:
            hits[index].append(number)
    rows = []
    for profile, found in zip(profiles, hits):
        rows.append({**profile, "chapter_count": len(found), "first_chapter": min(found) if found else None,
                     "chapters": found})
    rows.sort(key=lambda r: (-r["chapter_count"], r["english"]))
    return rows[:top]




# ---------------------------------------------------------------- candidates

def paragraphs(text: str) -> list[str]:
    return [p.strip() for p in text.split("\n") if p.strip()]


def candidates(row: dict, chapters: dict[int, str]) -> list[dict]:
    """Cue paragraphs about the character from every chapter of the book (no Safe-through cap).

    A paragraph qualifies when it names the character (or one of the two paragraphs before it
    does) and carries appearance cues; the narrator also qualifies on self/mirror cues. The
    chapter range is cut into BINS equal-count bins and each bin keeps its strongest paragraphs,
    so late looks (and look changes) are sampled as well as early ones.
    """
    pattern = re.compile("|".join(map(re.escape, row["names"])))
    narrator = row["english"] in FIRST_PERSON
    scan = sorted(chapters if narrator else row["chapters"])
    found: list[dict] = []
    for chapter in scan:
        paras = paragraphs(chapters[chapter])
        named = [bool(pattern.search(p)) for p in paras]
        for i, para in enumerate(paras):
            if para.startswith("＃"):
                continue
            strong = set(STRONG_RE.findall(para)) | {m.group(0) for m in COLOUR_RE.finditer(para)}
            weak = set(WEAK_RE.findall(para))
            if not (strong or len(weak) >= 2):
                continue
            by_name = named[i] or any(named[max(0, i - 2):i])
            by_self = narrator and bool(SELF_RE.search(para))
            if not (by_name or by_self):
                continue
            text = para[:PASSAGE_CHARS]
            if not named[i] and i > 0 and named[i - 1]:
                text = paras[i - 1][:160] + "\n" + text      # keep the sentence that names them
            found.append({"chapter": chapter, "text": text, "score": 3 * len(strong) + len(weak)})
    if not found:
        return []
    edges = [scan[min(len(scan) - 1, k * len(scan) // BINS)] for k in range(BINS)] + [scan[-1] + 1]
    picked: list[dict] = []
    for b in range(BINS):
        pool = [c for c in found if edges[b] <= c["chapter"] < edges[b + 1]]
        pool.sort(key=lambda c: (-min(c["score"], 9), c["chapter"]))
        picked.extend(pool[:PER_BIN])
    picked.sort(key=lambda c: c["chapter"])
    used, result = 0, []
    for item in picked:
        if used + len(item["text"]) <= BUDGET_CHARS:
            result.append(item)
            used += len(item["text"])
    return result


# ------------------------------------------------------------------ models

_LOCAL = threading.local()


def claude(model: str, prompt: str) -> str:
    """One `claude -p` call from a scratch directory, no tools; cost is recorded."""
    with tempfile.TemporaryDirectory() as scratch:
        proc = subprocess.run(
            ["claude", "-p", "--model", model, "--output-format", "json", "--tools", "",
             "--no-session-persistence"],
            input=prompt, capture_output=True, text=True, cwd=scratch, timeout=900,
        )
    if proc.returncode != 0:
        raise RuntimeError(f"claude {model} failed: {proc.stderr[:300] or proc.stdout[:300]}")
    data = json.loads(proc.stdout)
    if not hasattr(_LOCAL, "calls"):
        _LOCAL.calls = []
    _LOCAL.calls.append({"model": model, "cost_usd": data.get("total_cost_usd", 0.0)})
    if data.get("is_error"):
        raise RuntimeError(f"claude {model} error: {str(data.get('result'))[:300]}")
    return data["result"]


def parse_json(raw: str) -> dict:
    """First JSON object in the output, ignoring any fence or trailing commentary."""
    start = raw.find("{")
    if start < 0:
        raise ValueError("no JSON object in model output")
    value, _ = json.JSONDecoder().raw_decode(raw[start:])
    if not isinstance(value, dict):
        raise ValueError("model output is not a JSON object")
    return value


EXTRACT_PROMPT = """You extract PHYSICAL APPEARANCE facts about one character from Korean web-novel passages.
Character: {english} (Korean names: {names}). Gender: {gender}.{narrator}

Rules:
- Only visible traits of THIS character: apparent age, build/height, hair colour and style, eyes, face, skin,
  distinguishing marks, scars, missing limbs/eyes, typical clothing, carried weapon, signature or aura colours.
- No personality, no plot, no actions, no feelings. If a passage is about someone else, ignore it.
- Include lasting changes of look (returned to youth, visible aging, lost limb or eye, permanent scar, lasting
  hair/eye colour change, transformation) and mark them kind "change". Ordinary traits are kind "base".
- Skip temporary disguises, costumes worn for one scene, make-up, one-scene states (glowing eyes in a fight,
  bloodied, tired, blushing) and metaphors.
- Every fact needs the chapter number of its passage and a QUOTE copied character-for-character from that
  passage (one phrase or sentence, at least 4 characters, no ellipses). Never paraphrase the quote.
- Return an empty list if nothing qualifies.

Return only JSON: {{"facts": [{{"attribute": "hair", "kind": "base", "fact": "short English statement", "chapter": 12, "quote": "Korean quote"}}]}}

Passages:
{passages}
"""

NARRATOR_NOTE = """
This character narrates in the first person (나). Self-description, mirror/reflection scenes and other
characters describing him by name all count, but only when the passage is clearly about him."""

WRITE_PROMPT = """Write the Appearance ranges for a character page that also drives small illustration prompts.
Character: {english}. Gender: {gender}. First chapter they appear: {first}.

Verified, context-checked facts (index, chapter, flags, attribute, fact, Korean quote):
{facts}

Flags: APPROVED-CHANGE = confirmed lasting change shown in that chapter (only these may open a new range);
CONFLICT#n = the fact disagrees with others of the same group n.

Rules:
- Return one or more ranges. Range 1 is the base look. A later range may start ONLY at the chapter of an
  APPROVED-CHANGE fact that the range uses. Several APPROVED-CHANGE facts may describe the SAME change
  (repeated reactions, later mentions): open ONE range at the earliest chapter among them, never one per mention. Everything else (a trait first mentioned late, a different age
  guess, a new hair colour with no change marker) is NOT a change: fold it into the existing range.
- A later range must differ VISIBLY from the previous one; give that in "difference" (e.g. "old man -> youth of
  about twenty"). If the earlier facts already show the same look (a boy before and after), the "change" is
  mere exposition: do not open a range. If the base look has no visual trait at all (only titles/reputation),
  return that range with description "not described" and start the next range at the change.
- Each description is a complete, illustration-ready look for that range: 1-3 concrete visual sentences, then
  "Tags: " plus short comma-separated tags. It STARTS WITH the name "{english}".
- Include every non-conflicting fact's trait (age, build/height, hair, eyes, face/marks, clothing, weapon,
  colour motifs). Never invent or add outside knowledge.
- A fact that describes an event or transformation (losing, regaining or regrowing a body part, an injury,
  a change of form) and is NOT marked APPROVED-CHANGE must be omitted from every description; list it in
  "omitted" with a reason. Never hint at it in a range that starts before it.
- CONFLICT groups: do not mix the values. Keep the best-supported value (clearer, repeated, or earlier quote),
  say nothing about the others, and report the group in "conflicts".
- A range may use only facts whose chapter is before the next range's start; the description must not mention
  that a later change happens. Later ranges restate the traits that persist.
- Visual only; no personality, plot or relationships; nothing about hidden true age or backstory.
- Gender "unknown": avoid gendered pronouns.

Return only JSON: {{"ranges": [{{"start": 1, "description": "{english} ... Tags: a, b", "used": [fact indices], "difference": "what visibly changed (later ranges only)"}}],
"conflicts": [{{"attribute": "hair colour", "indices": [3, 7], "kept": [7], "resolved": true, "reason": "why"}}],
"omitted": [{{"index": 4, "reason": "why this fact is left out"}}]}}
Set "resolved": false when the evidence is about equally strong on both sides.
{feedback}"""

TRIAGE_PROMPT = """Below are appearance facts about one character ({english}) taken from different chapters.
List groups of facts that CONFLICT: they state incompatible values for the same attribute (hair colour, apparent
age band, build, eye colour, ...). Only list real disagreements, not complementary traits. Do not decide which
is right.

{facts}

Return only JSON: {{"groups": [{{"attribute": "hair colour", "indices": [2, 5]}}]}}
"""

JUDGE_PROMPT = """You verify appearance facts about a character in a Korean web novel, using the surrounding text.
Character: {english} (Korean names: {names}).{narrator}

For each numbered item decide, from the context (the quoted line is marked >>> <<<):
- this_character: the described look really belongs to {english}, not another person.
- literal_present: it is a literal, present-time description (not a flashback, backstory about someone's past
  form, hypothetical, metaphor/simile, disguise, costume, illusion or one-scene state).
- lasting_change: the text shows a DRASTIC, lasting change of {english}'s look happening in this scene or
  having just happened (returned to youth, a big jump in apparent age, lost limb/eye that stays lost, permanent
  scar, lasting hair/eye colour change, transformation). False for ordinary descriptions, for looking more
  tired/worn/aged by a little, for anything temporary or that heals/regrows at once, and for a summary of
  someone's past or whole life (that is backstory: literal_present false as well).

{items}

Return only JSON: {{"verdicts": [{{"index": 0, "this_character": true, "literal_present": true, "lasting_change": false, "reason": "short"}}]}}
"""


def norm(text: str) -> str:
    return re.sub(r"\s+", "", text)


def extract(row: dict, passages: list[dict]) -> list[dict]:
    """Sonnet over small passage batches (better recall than one long prompt); facts are merged."""
    facts: list[dict] = []
    seen: set[tuple] = set()
    note = NARRATOR_NOTE if row["english"] in FIRST_PERSON else ""
    for start in range(0, len(passages), BATCH):
        text = "\n\n".join(f"[Chapter {p['chapter']}]\n{p['text']}" for p in passages[start:start + BATCH])
        prompt = EXTRACT_PROMPT.format(
            english=row["english"], names=", ".join(row["names"][:6]), gender=row["gender"],
            narrator=note, passages=text,
        )
        for fact in parse_json(claude(EXTRACT_MODEL, prompt)).get("facts", []):
            if not isinstance(fact, dict):
                continue
            key = (fact.get("chapter"), norm(str(fact.get("quote"))))
            if key not in seen:
                seen.add(key)
                facts.append(fact)
    facts.sort(key=lambda f: f["chapter"] if isinstance(f.get("chapter"), int) else 0)
    return facts


def verify(facts: list[dict], chapters: dict[int, str]) -> tuple[list[dict], list[dict]]:
    good, dropped = [], []
    for fact in facts:
        chapter, quote = fact.get("chapter"), fact.get("quote")
        ok = (isinstance(chapter, int) and chapter in chapters
              and isinstance(quote, str) and len(norm(quote)) >= MIN_QUOTE
              and isinstance(fact.get("fact"), str) and norm(quote) in norm(chapters[chapter]))
        (good if ok else dropped).append(fact)
    return good, dropped


def locate(fact: dict, chapters: dict[int, str]) -> tuple[list[str], int | None]:
    paras = paragraphs(chapters[fact["chapter"]])
    quote = norm(fact["quote"])
    for i, para in enumerate(paras):
        if quote in norm(para):
            return paras, i
    for i in range(len(paras) - 1):
        if quote in norm(paras[i] + paras[i + 1]):
            return paras, i
    return paras, None


def context_for(fact: dict, chapters: dict[int, str]) -> str:
    paras, i = locate(fact, chapters)
    if i is None:
        return f">>> {fact['quote']} <<<"
    lines = []
    for j in range(max(0, i - CONTEXT_PARAS), min(len(paras), i + CONTEXT_PARAS + 1)):
        text = paras[j][:CONTEXT_CHARS]
        lines.append(f">>> {text} <<<" if j == i else text)
    return "\n".join(lines)


def has_marker(fact: dict, chapters: dict[int, str]) -> bool:
    """Deterministic: a Korean change marker in the quote's paragraph or its neighbours."""
    paras, i = locate(fact, chapters)
    window = fact["quote"] if i is None else " ".join(paras[max(0, i - 1):i + 2])
    return bool(CHANGE_RE.search(window))


def fact_key(fact: dict) -> str:
    return f"{fact['chapter']}|{norm(fact['quote'])}"


def facts_listing(facts: list[dict], flags: dict[int, str] | None = None) -> str:
    return "\n".join(
        f"{i}. ch{f['chapter']} |{(' ' + flags[i]) if flags and flags.get(i) else ''} | {f.get('attribute', '')} | "
        f"{f['fact']} | {f['quote']}" for i, f in enumerate(facts)
    )


def triage(row: dict, facts: list[dict]) -> list[dict]:
    if len(facts) < 2:
        return []
    result = parse_json(claude(JUDGE_MODEL, TRIAGE_PROMPT.format(english=row["english"], facts=facts_listing(facts))))
    groups = []
    for group in result.get("groups", []):
        idx = sorted({i for i in group.get("indices", []) if isinstance(i, int) and 0 <= i < len(facts)})
        if len(idx) >= 2:
            groups.append({"attribute": str(group.get("attribute", "")), "indices": idx})
    return groups


def share_paragraph_verdicts(facts: list[dict], verdicts: dict[int, dict], chapters: dict[int, str]) -> None:
    """Facts quoting the same paragraph share one verdict (the strictest value wins)."""
    groups: dict[tuple, list[int]] = {}
    for i in verdicts:
        paras, para = locate(facts[i], chapters)
        groups.setdefault((facts[i]["chapter"], para if para is not None else i), []).append(i)
    for members in groups.values():
        if len(members) < 2:
            continue
        for key in ("this_character", "literal_present", "lasting_change"):
            value = all(bool(verdicts[i].get(key)) for i in members)
            for i in members:
                verdicts[i] = {**verdicts[i], key: value}


def judge(row: dict, facts: list[dict], indices: list[int], chapters: dict[int, str],
          cache: dict[str, dict]) -> dict[int, dict]:
    """Context check for the given fact indices; verdicts are cached by chapter+quote."""
    verdicts: dict[int, dict] = {}
    todo = []
    for i in indices:
        cached = cache.get(fact_key(facts[i]))
        if cached:
            verdicts[i] = cached
        else:
            todo.append(i)
    note = NARRATOR_NOTE if row["english"] in FIRST_PERSON else ""
    for start in range(0, len(todo), JUDGE_BATCH):
        batch = todo[start:start + JUDGE_BATCH]
        items = "\n\n".join(
            f"[{n}] Chapter {facts[i]['chapter']}; fact: {facts[i]['fact']}\n{context_for(facts[i], chapters)}"
            for n, i in enumerate(batch)
        )
        prompt = JUDGE_PROMPT.format(english=row["english"], names=", ".join(row["names"][:6]),
                                     narrator=note, items=items)
        for item in parse_json(claude(JUDGE_MODEL, prompt)).get("verdicts", []):
            n = item.get("index")
            if isinstance(n, int) and 0 <= n < len(batch):
                verdicts[batch[n]] = {k: item.get(k) for k in
                                      ("this_character", "literal_present", "lasting_change", "reason")}
    return verdicts


def check_ranges(result: dict, kept: list[dict], english: str, first: int,
                 approved: set[int] | frozenset[int] = frozenset()) -> list[dict]:
    """Validate the writer's ranges; raises ValueError describing the first problem.

    `approved` holds the kept-fact indices that are confirmed lasting changes; a range after the
    first may only start at the chapter of one of them that the range uses.
    """
    raw = result.get("ranges")
    if not isinstance(raw, list):
        raise ValueError("ranges must be a list")
    ranges, placeholders = [], []
    for item in raw:
        text = item.get("description")
        if isinstance(text, str) and text.casefold().strip().rstrip(".") == "not described":
            if isinstance(item.get("start"), int):
                placeholders.append(item["start"])
            continue
        used = [i for i in item.get("used", []) if isinstance(i, int) and 0 <= i < len(kept)]
        if not isinstance(text, str) or not used or not isinstance(item.get("start"), int):
            raise ValueError("every range needs start, description and used fact indices")
        text = " ".join(CJK_PAREN.sub("", text).split())
        if not text.startswith(english):
            raise ValueError(f"description must start with the name '{english}'")
        if "Tags:" not in text:
            raise ValueError("description must end with a 'Tags: ...' list")
        ranges.append({"start": item["start"], "description": text, "used": sorted(set(used)),
                       "difference": str(item.get("difference", "")).strip()})
    ranges.sort(key=lambda r: r["start"])
    base_missing = bool(placeholders) and (not ranges or min(placeholders) <= ranges[0]["start"])
    if ranges and not base_missing:
        ranges[0]["start"] = first
    for k, rng in enumerate(ranges):
        if k or base_missing:
            openers = {kept[i]["chapter"] for i in rng["used"] if i in approved}
            if rng["start"] not in openers:
                raise ValueError(
                    f"range start {rng['start']} must be the chapter of an APPROVED-CHANGE fact the range uses")
            if k and rng["start"] <= ranges[k - 1]["start"]:
                raise ValueError("range starts must increase")
            if len(rng["difference"]) < 8:
                raise ValueError("every range after the base needs a concrete visible \"difference\"")
        if k + 1 < len(ranges):
            late = [i for i in rng["used"] if kept[i]["chapter"] >= ranges[k + 1]["start"]]
            if late:
                raise ValueError(f"range {k + 1} uses facts {late} from chapters at or after the next range start")
    return ranges


def clean_conflicts(result: dict, count: int) -> list[dict]:
    conflicts = []
    for item in result.get("conflicts", []):
        idx = sorted({i for i in item.get("indices", []) if isinstance(i, int) and 0 <= i < count})
        if len(idx) < 2:
            continue
        kept = sorted({i for i in item.get("kept", []) if i in idx})
        conflicts.append({"attribute": str(item.get("attribute", "")), "indices": idx, "kept": kept,
                          "resolved": bool(item.get("resolved", False)) and bool(kept),
                          "reason": str(item.get("reason", ""))})
    return conflicts


def write(row: dict, kept: list[dict], approved: set[int], groups: list[dict]) -> tuple[list[dict], list[dict], list[int], list[dict]]:
    """Writer with validation; every kept fact must be used or be a reported conflict loser."""
    flags: dict[int, str] = {}
    for n, group in enumerate(groups, 1):
        for i in group["indices"]:
            flags[i] = f"CONFLICT#{n}"
    for i in approved:
        flags[i] = (flags[i] + " " if i in flags else "") + "APPROVED-CHANGE"
    listing = facts_listing(kept, flags)
    feedback = ""
    result: dict = {}
    ranges: list[dict] = []
    unused: list[int] = []
    for attempt in range(WRITE_TRIES):
        prompt = WRITE_PROMPT.format(english=row["english"], gender=row["gender"], first=row["first_chapter"],
                                     facts=listing, feedback=feedback)
        try:
            result = parse_json(claude(WRITE_MODEL, prompt))
            ranges = check_ranges(result, kept, row["english"], row["first_chapter"], approved)
        except ValueError as error:
            feedback = f"\nYour previous answer was rejected: {error}. Fix it and answer again.\n"
            if attempt == WRITE_TRIES - 1:
                raise ValueError(f"writer failed validation: {error}") from None
            continue
        conflicts = clean_conflicts(result, len(kept))
        losers = {i for c in conflicts for i in c["indices"] if i not in c["kept"]}
        omitted = {o["index"] for o in result.get("omitted", [])
                   if isinstance(o, dict) and isinstance(o.get("index"), int) and str(o.get("reason", "")).strip()}
        used = {i for r in ranges for i in r["used"]}
        used |= {i for r in result.get("ranges", []) if isinstance(r, dict) and isinstance(r.get("used"), list)
                 and str(r.get("description", "")).casefold().strip().rstrip(".") == "not described"
                 for i in r["used"] if isinstance(i, int)}
        unused = [i for i in range(len(kept)) if i not in used and i not in losers and i not in omitted]
        if unused and attempt < WRITE_TRIES - 1:
            feedback = (f"\nYour previous answer left facts {unused} unused. Include their traits (or report them as "
                        "losers of a conflict group). Answer again.\n")
            continue
        return ranges, conflicts, unused, [o for o in result.get("omitted", []) if isinstance(o, dict)]
    raise ValueError("writer failed")


CJK_PAREN = re.compile(r"\s*\([^)]*[一-鿿가-힣][^)]*\)")
NOT_DESCRIBED = "- **Appearance:** not described"


def render_lines(ranges: list[dict]) -> list[str]:
    """Profile lines: (from ch C) for a single range, else (ch A–B) ... (from ch C)."""
    if not ranges:
        return [NOT_DESCRIBED]
    if len(ranges) == 1:
        return [f"- **Appearance (from ch {ranges[0]['start']}):** {ranges[0]['description']}"]
    lines = []
    for k, rng in enumerate(ranges):
        if k + 1 < len(ranges):
            lines.append(f"- **Appearance (ch {rng['start']}–{ranges[k + 1]['start'] - 1}):** {rng['description']}")
        else:
            lines.append(f"- **Appearance (from ch {rng['start']}):** {rng['description']}")
    return lines


# ----------------------------------------------------------------- pipeline

def slug(index: int, english: str) -> Path:
    return OUT / f"{index:03d}-{re.sub(r'[^A-Za-z0-9]+', '-', english).strip('-')}.json"


def prior_facts(path: Path, rev: str | None) -> list[dict]:
    """Facts from this character's earlier evidence (current file and, optionally, a git revision)."""
    texts = []
    if path.is_file():
        texts.append(path.read_text(encoding="utf-8"))
    if rev:
        shown = subprocess.run(["git", "show", f"{rev}:{path.relative_to(ROOT)}"], cwd=ROOT,
                               capture_output=True, text=True)
        if shown.returncode == 0:
            texts.append(shown.stdout)
    facts = []
    for text in texts:
        try:
            facts.extend(json.loads(text).get("facts", []))
        except ValueError:
            pass
    return facts


def merge_facts(*groups: list[dict]) -> list[dict]:
    """Union by (chapter, quote); a re-run never loses a verified detail."""
    merged: dict[tuple, dict] = {}
    for group in groups:
        for fact in group:
            merged.setdefault((fact.get("chapter"), norm(str(fact.get("quote")))), fact)
    return sorted(merged.values(), key=lambda f: f["chapter"] if isinstance(f.get("chapter"), int) else 0)


def prior_judgments(path: Path) -> dict[str, dict]:
    if path.is_file():
        try:
            return json.loads(path.read_text(encoding="utf-8")).get("judgments", {})
        except ValueError:
            pass
    return {}


def process(index: int, row: dict, chapters: dict[int, str], force: bool, seed_revs: list[str] | None = None,
            reuse_facts: bool = False) -> dict:
    path = slug(index, row["english"])
    if path.is_file() and not force:
        cached = json.loads(path.read_text(encoding="utf-8"))
        if cached.get("version") == VERSION:
            return cached
    _LOCAL.calls = []
    earlier = merge_facts(prior_facts(path, None), *(prior_facts(path, rev) for rev in seed_revs or []))
    cache = prior_judgments(path)
    passages = [] if (reuse_facts and earlier) else candidates(row, chapters)
    evidence: dict = {
        "version": VERSION, "rank": index, "english": row["english"], "profile": row["path"],
        "names": row["names"], "chapter_count": row["chapter_count"], "first_chapter": row["first_chapter"],
        "profile_safe_through": row["safe_through"], "passages": [(p["chapter"], len(p["text"])) for p in passages],
        "facts": [], "dropped_facts": [], "rejected": [], "judgments": {}, "conflicts": [], "unused": [],
        "ranges": [], "lines": [NOT_DESCRIBED],
    }
    extracted = extract(row, passages) if passages else []
    verified, dropped = verify(merge_facts(extracted, earlier), chapters)
    evidence["dropped_facts"] = dropped
    if verified:
        groups = triage(row, verified)
        in_conflict = {i for g in groups for i in g["indices"]}
        marked = {i for i, f in enumerate(verified) if has_marker(f, chapters)}
        to_judge = sorted(in_conflict | marked | {i for i, f in enumerate(verified) if f.get("kind") == "change"})
        verdicts = judge(row, verified, to_judge, chapters, cache)
        share_paragraph_verdicts(verified, verdicts, chapters)
        evidence["judgments"] = {fact_key(verified[i]): v for i, v in verdicts.items()}
        rejected = {i for i in to_judge
                    if not (verdicts.get(i, {}).get("this_character") and verdicts.get(i, {}).get("literal_present"))}
        approved_orig = {i for i in marked if i not in rejected and verdicts[i].get("lasting_change")}
        for i, fact in enumerate(verified):
            fact["marker"] = i in marked
            fact["verdict"] = verdicts.get(i)
            fact["status"] = "rejected" if i in rejected else ("approved-change" if i in approved_orig else "kept")
        evidence["facts"] = verified
        evidence["rejected"] = [i for i in sorted(rejected)]
        order = [i for i in range(len(verified)) if i not in rejected]
        remap = {old: new for new, old in enumerate(order)}
        kept = [verified[i] for i in order]
        kept_groups = [{"attribute": g["attribute"], "indices": [remap[i] for i in g["indices"] if i in remap]}
                       for g in groups]
        kept_groups = [g for g in kept_groups if len(g["indices"]) >= 2]
        if kept:
            ranges, conflicts, unused, omitted = write(row, kept, {remap[i] for i in approved_orig}, kept_groups)
            for rng in ranges:  # evidence indices refer to the full `facts` list
                rng["used"] = [order[i] for i in rng["used"]]
            for c in conflicts:
                for key in ("indices", "kept"):
                    c[key] = [order[i] for i in c[key]]
            evidence["ranges"], evidence["conflicts"] = ranges, conflicts
            evidence["unused"] = [order[i] for i in unused]
            evidence["omitted"] = [{"index": order[o["index"]], "reason": o.get("reason", "")}
                                   for o in omitted if isinstance(o.get("index"), int) and 0 <= o["index"] < len(order)]
            evidence["lines"] = render_lines(ranges)
    evidence["calls"] = list(_LOCAL.calls)
    OUT.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return evidence


def write_conflicts_md() -> int:
    """reviews/appearance/conflicts.md: every conflict group, unresolved first. Returns unresolved count."""
    rows, unresolved = [], 0
    for path in sorted(OUT.glob("[0-9]*.json")):
        ev = json.loads(path.read_text(encoding="utf-8"))
        for c in ev.get("conflicts", []):
            unresolved += not c["resolved"]
            rows.append((c["resolved"], ev["english"], ev, c))
    rows.sort(key=lambda r: (r[0], r[1]))
    out = ["# Appearance conflicts", "",
           f"{len(rows)} conflict group(s); {unresolved} unresolved (evidence about equally strong; the writer "
           "kept one value). Resolved groups kept the best-supported value.", ""]
    for resolved, english, ev, c in rows:
        out.append(f"## {english} — {c['attribute']} ({'resolved' if resolved else 'UNRESOLVED'})")
        out.append(f"Reason: {c['reason']}")
        for i in c["indices"]:
            fact = ev["facts"][i]
            mark = "KEPT" if i in c["kept"] else "dropped"
            out.append(f"- [{mark}] ch{fact['chapter']}: {fact['fact']} — `{fact['quote']}`")
        out.append("")
    (OUT / "conflicts.md").write_text("\n".join(out), encoding="utf-8")
    return unresolved


def apply(evidences: list[dict]) -> list[str]:
    changed = []
    for ev in evidences:
        path = ROOT / ev["profile"]
        body = path.read_text(encoding="utf-8")
        new = set_profile_appearance(body, ev["lines"])
        if new != body:
            path.write_text(new, encoding="utf-8")
            changed.append(ev["profile"])
    return changed


def command_rank(args: argparse.Namespace) -> list[dict]:
    chapters = load_source(Path(args.source))
    rows = rank(load_profiles(), chapters, args.top)
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "ranking.json").write_text(json.dumps(
        [{k: v for k, v in r.items() if k not in ("chapters", "role")} for r in rows],
        ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for i, r in enumerate(rows, 1):
        print(f"{i:>3}. {r['english']} ({r['chapter_count']} ch, first {r['first_chapter']}, safe {r['safe_through']})")
    return rows


def command_run(args: argparse.Namespace) -> int:
    chapters = load_source(Path(args.source))
    rows = rank(load_profiles(), chapters, args.top)
    selected = list(enumerate(rows, 1))
    if args.only:
        wanted = {w.casefold() for w in args.only}
        selected = [(i, r) for i, r in selected if r["english"].casefold() in wanted]
    elif args.limit:
        selected = selected[:args.limit]
    if args.beyond_safe:  # name/alias occurs after the profile's Safe through: needs a re-run
        selected = [(i, r) for i, r in selected if any(n > r["safe_through"] for n in r["chapters"])]
        print("beyond Safe through:", ", ".join(r["english"] for _, r in selected))
    OUT.mkdir(parents=True, exist_ok=True)

    def job(item):
        index, row = item
        try:
            return process(index, row, chapters, args.force, args.seed_rev, args.reuse_facts)
        except Exception as error:  # keep other characters going
            print(f"FAILED {row['english']}: {error}", file=sys.stderr)
            return None

    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        results = [r for r in pool.map(job, selected) if r]
    changed = apply(results) if not args.no_apply else []
    unresolved = write_conflicts_md()
    calls = [c for r in results for c in r.get("calls", [])]
    cost = sum(c.get("cost_usd", 0) for c in calls)
    real = sum(1 for r in results if r["lines"] != [NOT_DESCRIBED])
    multi = [(r["english"], [g["start"] for g in r["ranges"]]) for r in results if len(r["ranges"]) > 1]
    print(f"{len(results)}/{len(selected)} done; {real} described, {len(results) - real} not described; "
          f"{len(calls)} calls, ${cost:.3f}; ${cost / max(1, len(results)):.3f}/character; "
          f"{len(changed)} profiles changed; {unresolved} unresolved conflicts; multi-range: {multi}")
    return 0 if len(results) == len(selected) else 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("rank", "run"):
        p = sub.add_parser(name)
        p.add_argument("--top", type=int, default=50)
        p.add_argument("--source", default=os.environ.get("MURIM_SOURCE_DIR", str(ROOT / "source")))
    run = sub.choices["run"]
    run.add_argument("--limit", type=int, default=0, help="only the first N ranked characters")
    run.add_argument("--only", nargs="*", help="English profile names")
    run.add_argument("--workers", type=int, default=3)
    run.add_argument("--beyond-safe", action="store_true",
                     help="only profiles whose name or alias appears after their Safe through")
    run.add_argument("--seed-rev", nargs="*", help="git revisions whose evidence facts are merged in (re-verified)")
    run.add_argument("--reuse-facts", action="store_true",
                     help="skip extraction when earlier facts exist; redo judging and consolidation only")
    run.add_argument("--force", action="store_true", help="redo characters that already have current evidence")
    run.add_argument("--no-apply", action="store_true", help="write evidence only, leave profiles untouched")
    args = parser.parse_args()
    if args.command == "rank":
        command_rank(args)
        return 0
    return command_run(args)


if __name__ == "__main__":
    raise SystemExit(main())
