#!/usr/bin/env python3
"""Spoiler-safe, range-aware `Appearance` field for the most recurring character profiles.

Repeatable and resumable. Stages per character, saved in
`reviews/appearance/NNN-slug.json` (rank-ordered, with exact Korean quotes):

1. rank       chapters naming the character (profile names/aliases + docs/NAMES.md)
2. candidates cue paragraphs from ALL chapters up to `Safe through`, spread evenly over the
              chapter range; the narrator also gets mirror/self-description paragraphs
3. extract    Sonnet calls over passage batches: facts with chapter, kind and verbatim Korean quote
4. verify     drop facts whose quote is not in that chapter's source
5. write      one Sonnet call merges the facts into look ranges (a new range only for a lasting,
              drastic change); ranges are validated so no range leaks a later fact
6. apply      one profile line per range:
                 - **Appearance (ch A–B):** Name ... Tags: ...
                 - **Appearance (from ch C):** Name ... Tags: ...
              or `- **Appearance:** not described`

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
VERSION = 2
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
    """Cue paragraphs about the character from every chapter up to Safe through.

    A paragraph qualifies when it names the character (or one of the two paragraphs before it
    does) and carries appearance cues; the narrator also qualifies on self/mirror cues. The
    chapter range is cut into BINS equal-count bins and each bin keeps its strongest paragraphs,
    so late looks (and look changes) are sampled as well as early ones.
    """
    pattern = re.compile("|".join(map(re.escape, row["names"])))
    narrator = row["english"] in FIRST_PERSON
    safe = row["safe_through"]
    scan = sorted(n for n in (chapters if narrator else row["chapters"]) if n <= safe)
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

Verified facts (index, chapter, kind, attribute, fact, Korean quote):
{facts}

Rules:
- Return one or more ranges. Range 1 is the base look. Start another range ONLY for a lasting, drastic change
  (returned to youth, aging, lost limb/eye, permanent scar, lasting hair/eye colour change, transformation).
  Ignore temporary disguises and one-scene states. Its "start" is the chapter where the change is first shown
  and must equal the chapter of a fact you use in that range. Do not start a range for minor changes.
- A new range needs a visible before/after: an earlier fact the new look contradicts. A trait merely mentioned
  for the first time (e.g. "elderly") with no contradicting earlier fact belongs in the base range. Narration
  about hidden true age, past rejuvenation, backstory or identity is NOT a visual change: never mention it;
  describe only the apparent look.
- Each description is a complete, illustration-ready look for that range: 1-3 concrete visual sentences, then
  "Tags: " plus short comma-separated tags. It STARTS WITH the name "{english}".
- Merge thin facts from ALL chapters so the range covers apparent age, build/height, hair, eyes, face/marks,
  clothing and weapon, colour motifs wherever the facts support it. Never invent or add outside knowledge.
- A range may use only facts whose chapter is before the next range's start (nothing later may leak in), and
  the description must not mention that a later change happens. Later ranges restate the traits that persist.
- Visual only; no personality, plot or relationships. Keep established names; plain English for clothes/weapons.
- Gender "unknown": avoid gendered pronouns. Resolve conflicting facts toward the clearer, repeated one.
- Only if the facts hold nothing visual at all, return {{"ranges": []}}.

Return only JSON: {{"ranges": [{{"start": 1, "description": "{english} ... Tags: a, b", "used": [fact indices]}}]}}
{feedback}"""


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


def verify(facts: list[dict], chapters: dict[int, str], safe_through: int) -> tuple[list[dict], list[dict]]:
    good, dropped = [], []
    for fact in facts:
        chapter, quote = fact.get("chapter"), fact.get("quote")
        ok = (isinstance(chapter, int) and chapter in chapters and chapter <= safe_through
              and isinstance(quote, str) and len(norm(quote)) >= MIN_QUOTE
              and isinstance(fact.get("fact"), str) and norm(quote) in norm(chapters[chapter]))
        (good if ok else dropped).append(fact)
    return good, dropped


def check_ranges(result: dict, verified: list[dict], english: str, first: int, safe: int) -> list[dict]:
    """Validate the writer's ranges; raises ValueError describing the first problem."""
    raw = result.get("ranges")
    if not isinstance(raw, list):
        raise ValueError("ranges must be a list")
    ranges = []
    for item in raw:
        used = [i for i in item.get("used", []) if isinstance(i, int) and 0 <= i < len(verified)]
        text = item.get("description")
        if not isinstance(text, str) or not used or not isinstance(item.get("start"), int):
            raise ValueError("every range needs start, description and used fact indices")
        text = " ".join(CJK_PAREN.sub("", text).split())
        if not text.startswith(english):
            raise ValueError(f"description must start with the name '{english}'")
        if text.casefold().rstrip(".") == "not described":
            continue
        ranges.append({"start": item["start"], "description": text, "used": sorted(set(used))})
    ranges.sort(key=lambda r: r["start"])
    if ranges:
        ranges[0]["start"] = first
    for k, rng in enumerate(ranges):
        chapters_used = {verified[i]["chapter"] for i in rng["used"]}
        if k and rng["start"] not in chapters_used:
            raise ValueError(f"range start {rng['start']} must equal the chapter of a fact it uses")
        if k and rng["start"] <= ranges[k - 1]["start"]:
            raise ValueError("range starts must increase")
        if rng["start"] > safe:
            raise ValueError("range starts after Safe through")
        if k + 1 < len(ranges):
            late = [i for i in rng["used"] if verified[i]["chapter"] >= ranges[k + 1]["start"]]
            if late:
                raise ValueError(f"range {k + 1} uses facts {late} from chapters at or after the next range start")
    return ranges


def write(row: dict, verified: list[dict]) -> list[dict]:
    facts = "\n".join(
        f"{i}. ch{f['chapter']} | {f.get('kind', 'base')} | {f.get('attribute', '')} | {f['fact']} | {f['quote']}"
        for i, f in enumerate(verified)
    )
    feedback = ""
    for _ in range(WRITE_TRIES):
        prompt = WRITE_PROMPT.format(
            english=row["english"], gender=row["gender"], first=row["first_chapter"], facts=facts, feedback=feedback,
        )
        try:
            return check_ranges(parse_json(claude(WRITE_MODEL, prompt)), verified, row["english"],
                                row["first_chapter"], row["safe_through"])
        except ValueError as error:
            feedback = f"\nYour previous answer was rejected: {error}. Fix it and answer again.\n"
    raise ValueError(f"writer failed validation: {feedback.strip()}")


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


def process(index: int, row: dict, chapters: dict[int, str], force: bool) -> dict:
    path = slug(index, row["english"])
    if path.is_file() and not force:
        cached = json.loads(path.read_text(encoding="utf-8"))
        if cached.get("version") == VERSION:
            return cached
    _LOCAL.calls = []
    passages = candidates(row, chapters)
    evidence: dict = {
        "version": VERSION, "rank": index, "english": row["english"], "profile": row["path"],
        "names": row["names"], "chapter_count": row["chapter_count"], "first_chapter": row["first_chapter"],
        "safe_through": row["safe_through"], "passages": [(p["chapter"], len(p["text"])) for p in passages],
        "facts": [], "dropped_facts": [], "ranges": [], "lines": [NOT_DESCRIBED],
    }
    if passages:
        verified, dropped = verify(extract(row, passages), chapters, row["safe_through"])
        evidence["facts"], evidence["dropped_facts"] = verified, dropped
        if verified:
            evidence["ranges"] = write(row, verified)
            evidence["lines"] = render_lines(evidence["ranges"])
    evidence["calls"] = list(_LOCAL.calls)
    OUT.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return evidence


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
    OUT.mkdir(parents=True, exist_ok=True)

    def job(item):
        index, row = item
        try:
            return process(index, row, chapters, args.force)
        except Exception as error:  # keep other characters going
            print(f"FAILED {row['english']}: {error}", file=sys.stderr)
            return None

    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        results = [r for r in pool.map(job, selected) if r]
    changed = apply(results) if not args.no_apply else []
    calls = [c for r in results for c in r.get("calls", [])]
    cost = sum(c.get("cost_usd", 0) for c in calls)
    real = sum(1 for r in results if r["lines"] != [NOT_DESCRIBED])
    multi = [(r["english"], [g["start"] for g in r["ranges"]]) for r in results if len(r["ranges"]) > 1]
    print(f"{len(results)}/{len(selected)} done; {real} described, {len(results) - real} not described; "
          f"{len(calls)} calls, ${cost:.3f}; ${cost / max(1, len(results)):.3f}/character; "
          f"{len(changed)} profiles changed; multi-range: {multi}")
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
    run.add_argument("--force", action="store_true", help="redo characters that already have current evidence")
    run.add_argument("--no-apply", action="store_true", help="write evidence only, leave profiles untouched")
    args = parser.parse_args()
    if args.command == "rank":
        command_rank(args)
        return 0
    return command_run(args)


if __name__ == "__main__":
    raise SystemExit(main())
