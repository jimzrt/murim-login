#!/usr/bin/env python3
"""Spoiler-safe `Appearance` field for the most recurring character profiles.

Repeatable and resumable. Stages per character, each saved in
`reviews/appearance/NNN-slug.json` (rank-ordered, with exact Korean quotes):

1. rank      chapters naming the character (profile names/aliases + docs/NAMES.md)
2. candidates deterministic appearance-cue paragraphs from the earliest chapters
3. extract   Sonnet calls over passage batches: facts, each with chapter + verbatim Korean quote
4. verify    drop facts whose quote is not in that chapter's source
5. write     one Sonnet call consolidates verified facts into the English field
6. apply     `- **Appearance (as of ch N):** ...` or `- **Appearance:** not described`

Evidence never goes past the profile's `Safe through`; N is the latest chapter
of a fact actually used. The line is excluded from translation packets
(`compact_profile`) and preserved by update/compress.

    python tools/appearance_pass.py rank --top 50
    python tools/appearance_pass.py run --limit 5 --source /path/to/source
    python tools/appearance_pass.py run --workers 4
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
        ALIAS_LINE, ALIAS_PAIR, HEADING, is_korean_key, profile_appearance, profile_gender,
        profile_koreans, set_profile_appearance, strip_english,
    )
except ModuleNotFoundError:  # run as a script
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from names import (  # type: ignore
        ALIAS_LINE, ALIAS_PAIR, HEADING, is_korean_key, profile_appearance, profile_gender,
        profile_koreans, set_profile_appearance, strip_english,
    )

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reviews" / "appearance"
EARLY_SPAN = 60              # chapters after first appearance scanned for cues
WIDE_SPAN = 300              # fallback span when the early scan is thin
MIN_PASSAGES = 5
MAX_PASSAGES = 18
PASSAGE_CHARS = 500
BUDGET_CHARS = 8000
MIN_QUOTE = 4
BATCH = 5                    # passages per extraction call
EXTRACT_MODEL = "sonnet"

STRONG_CUES = (
    "외모", "얼굴", "머리카락", "머리를", "머리는", "머리가", "머릿결", "눈동자", "눈매", "눈썹", "체격", "덩치", "체구", "키가",
    "키는", "장신", "피부", "수염", "흉터", "복장", "무복", "도포", "차림", "의복", "백발", "흑발", "은발", "미남", "미녀",
    "인상", "콧날", "입술", "풍채", "생김", "미모", "몸집", "안색", "용모", "턱", "이마", "미소년", "노인", "청년", "소년", "소녀",
)
WEAK_CUES = ("옷", "나이", "중년", "어깨", "허리", "눈빛", "상처", "두건", "관을", "근육", "장포", "검을", "도를", "칼을")
STRONG_RE = re.compile("|".join(map(re.escape, STRONG_CUES)))
WEAK_RE = re.compile("|".join(map(re.escape, WEAK_CUES)))


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


def rank(profiles: list[dict], chapters: dict[int, str], top: int) -> list[dict]:
    """Chapter counts per profile. Longest-match-first across all profiles, so 진태 does not
    claim the 진태경 occurrences of another character."""
    profiles = [p for p in profiles if p["names"] and p["english"] not in SKIP]
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
    """Cue paragraphs naming the character (or right after a paragraph that does), earliest first."""
    pattern = re.compile("|".join(map(re.escape, row["names"])))
    usable = [n for n in row["chapters"] if n <= row["safe_through"]]
    found: list[dict] = []
    for span in (EARLY_SPAN, WIDE_SPAN):
        found = []
        for chapter in (n for n in usable if n <= usable[0] + span):
            paras = paragraphs(chapters[chapter])
            for i, para in enumerate(paras):
                strong, weak = set(STRONG_RE.findall(para)), set(WEAK_RE.findall(para))
                if para.startswith("＃") or not (strong or len(weak) >= 2):
                    continue
                named = pattern.search(para) or (i > 0 and pattern.search(paras[i - 1]) and len(paras[i - 1]) < 120)
                if not named:
                    continue
                score = 3 * len(strong) + len(weak)
                found.append({"chapter": chapter, "text": para[:PASSAGE_CHARS], "score": score})
        if sum(1 for f in found if f["score"] >= 3) >= MIN_PASSAGES:
            break
    # strongest cues win, but keep the earliest chapters when scores tie
    found.sort(key=lambda c: (-min(c["score"], 9), c["chapter"]))
    picked, used = [], 0
    for item in found:
        if len(picked) >= MAX_PASSAGES or used + len(item["text"]) > BUDGET_CHARS:
            continue
        picked.append(item)
        used += len(item["text"])
    return sorted(picked, key=lambda c: c["chapter"])


# ------------------------------------------------------------------ models

_LOCAL = threading.local()


def claude(model: str, prompt: str) -> str:
    """One `claude -p` call from a scratch directory, no tools; cost is recorded."""
    with tempfile.TemporaryDirectory() as scratch:
        proc = subprocess.run(
            ["claude", "-p", "--model", model, "--output-format", "json", "--tools", "",
             "--no-session-persistence"],
            input=prompt, capture_output=True, text=True, cwd=scratch, timeout=600,
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
Character: {english} (Korean names: {names}). Gender: {gender}.

Rules:
- Only visible traits of THIS character: apparent age, build/height, hair colour and style, eyes, face, skin,
  distinguishing marks, scars, typical clothing, carried weapon, signature colours or aura colour.
- No personality, no plot, no actions, no feelings.
- Skip anything about disguises, borrowed faces, transformations, forms gained later, or later injuries/losses.
- Every fact needs the chapter number of its passage and a QUOTE copied character-for-character from that
  passage (one phrase or sentence, at least 4 characters, no ellipses). Never paraphrase the quote.
- If a passage is about someone else, ignore it. Return an empty list if nothing qualifies.

Return only JSON: {{"facts": [{{"attribute": "hair", "fact": "short English statement", "chapter": 12, "quote": "Korean quote"}}]}}

Passages:
{passages}
"""

WRITE_PROMPT = """Write the Appearance field for a character page that will also drive small illustration prompts.
Character: {english}. Gender: {gender}.

Verified facts (index, chapter, attribute, fact, Korean quote):
{facts}

Rules:
- 1-3 concrete visual sentences, then an optional "Tags:" list of short comma-separated illustration tags.
- Visual only: apparent age, build/height, hair colour/style, eyes, face and marks, scars, typical clothing and
  weapon, colour motifs. No personality, no plot, no relationships, no speculation.
- Describe the character as first established. Use only the facts above; never add details. Resolve conflicts by
  keeping the earliest-established look. Skip disguises, transformations, later injuries, true identity, aging.
- English terms: keep established names/titles; weapons and clothes in plain English.
- Gender "unknown": avoid gendered pronouns; start sentences with the name or a trait.
- Clothing or a weapon alone is not enough; apparent age, build, hair, face or colour traits must carry the text.
- Drop any fact that hints at a disguise, rejuvenation, transformation or later change of form.
- If the facts give too little to picture the character (fewer than two distinct visual traits), set
  "description" to "not described".

Return only JSON: {{"description": "text, or not described", "used": [indices of facts actually used],
"excluded": [{{"index": 0, "reason": "why dropped"}}]}}
"""


def extract(row: dict, passages: list[dict]) -> list[dict]:
    """Sonnet over small passage batches (better recall than one long prompt); facts are merged."""
    facts: list[dict] = []
    seen: set[tuple] = set()
    for start in range(0, len(passages), BATCH):
        text = "\n\n".join(f"[Chapter {p['chapter']}]\n{p['text']}" for p in passages[start:start + BATCH])
        prompt = EXTRACT_PROMPT.format(
            english=row["english"], names=", ".join(row["names"][:6]), gender=row["gender"], passages=text,
        )
        for fact in parse_json(claude(EXTRACT_MODEL, prompt)).get("facts", []):
            key = (fact.get("chapter"), norm(str(fact.get("quote"))))
            if isinstance(fact, dict) and key not in seen:
                seen.add(key)
                facts.append(fact)
    facts.sort(key=lambda f: f["chapter"] if isinstance(f.get("chapter"), int) else 0)
    return facts


def norm(text: str) -> str:
    return re.sub(r"\s+", "", text)


def verify(facts: list[dict], chapters: dict[int, str], safe_through: int) -> tuple[list[dict], list[dict]]:
    good, dropped = [], []
    for fact in facts:
        chapter, quote = fact.get("chapter"), fact.get("quote")
        ok = (isinstance(chapter, int) and chapter in chapters and chapter <= safe_through
              and isinstance(quote, str) and len(norm(quote)) >= MIN_QUOTE
              and isinstance(fact.get("fact"), str) and norm(quote) in norm(chapters[chapter]))
        (good if ok else dropped).append(fact)
    return good, dropped


def write(row: dict, verified: list[dict]) -> dict:
    facts = "\n".join(
        f"{i}. ch{f['chapter']} | {f.get('attribute', '')} | {f['fact']} | {f['quote']}"
        for i, f in enumerate(verified)
    )
    prompt = WRITE_PROMPT.format(english=row["english"], gender=row["gender"], facts=facts)
    result = parse_json(claude("sonnet", prompt))
    description = result.get("description")
    if not isinstance(description, str) or not description.strip():
        raise ValueError("writer returned no description")
    return result


CJK_PAREN = re.compile(r"\s*\([^)]*[\u4e00-\u9fff\uac00-\ud7a3][^)]*\)")


def render_line(description: str, used: list[dict]) -> str:
    description = " ".join(CJK_PAREN.sub("", description).split())
    if description.casefold().rstrip(".") == "not described" or not used:
        return "- **Appearance:** not described"
    bound = max(f["chapter"] for f in used)
    return f"- **Appearance (as of ch {bound}):** {description}"


# ----------------------------------------------------------------- pipeline

def slug(index: int, english: str) -> Path:
    return OUT / f"{index:03d}-{re.sub(r'[^A-Za-z0-9]+', '-', english).strip('-')}.json"


def process(index: int, row: dict, chapters: dict[int, str], force: bool) -> dict:
    path = slug(index, row["english"])
    if path.is_file() and not force:
        return json.loads(path.read_text(encoding="utf-8"))
    _LOCAL.calls = []
    passages = candidates(row, chapters)
    evidence: dict = {
        "rank": index, "english": row["english"], "profile": row["path"], "names": row["names"],
        "chapter_count": row["chapter_count"], "first_chapter": row["first_chapter"],
        "safe_through": row["safe_through"], "passages": [(p["chapter"], len(p["text"])) for p in passages],
        "facts": [], "dropped_facts": [], "used": [], "excluded": [], "line": None,
    }
    if passages:
        raw_facts = extract(row, passages)
        verified, dropped = verify(raw_facts, chapters, row["safe_through"])
        evidence["facts"], evidence["dropped_facts"] = verified, dropped
        if verified:
            result = write(row, verified)
            used_idx = [i for i in result.get("used", []) if isinstance(i, int) and 0 <= i < len(verified)]
            used = [verified[i] for i in used_idx]
            evidence["used"] = used_idx
            evidence["excluded"] = result.get("excluded", [])
            evidence["line"] = render_line(result["description"], used)
    if evidence["line"] is None:
        evidence["line"] = "- **Appearance:** not described"
    evidence["calls"] = list(_LOCAL.calls)
    OUT.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return evidence


def apply(evidences: list[dict]) -> list[str]:
    changed = []
    for ev in evidences:
        path = ROOT / ev["profile"]
        body = path.read_text(encoding="utf-8")
        new = set_profile_appearance(body, ev["line"])
        if new != body:
            path.write_text(new, encoding="utf-8")
            changed.append(ev["profile"])
    return changed


def command_rank(args: argparse.Namespace) -> list[dict]:
    chapters = load_source(Path(args.source))
    rows = rank(load_profiles(), chapters, args.top)
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "ranking.json").write_text(json.dumps(
        [{k: v for k, v in r.items() if k not in ("chapters", "names", "role")} | {"names": r["names"]}
         for r in rows], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
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
    changed = apply(results)
    cost = sum(c.get("cost_usd", 0) for r in results for c in r.get("calls", []))
    real = sum(1 for r in results if "not described" not in r["line"])
    print(f"{len(results)}/{len(selected)} done; {real} described, {len(results) - real} not described; "
          f"{sum(len(r.get('calls', [])) for r in results)} calls, ${cost:.3f} (this run); "
          f"{len(changed)} profiles changed")
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
    run.add_argument("--force", action="store_true", help="redo characters that already have evidence")
    args = parser.parse_args()
    if args.command == "rank":
        command_rank(args)
        return 0
    return command_run(args)


if __name__ == "__main__":
    raise SystemExit(main())
