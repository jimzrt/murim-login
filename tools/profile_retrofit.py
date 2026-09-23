#!/usr/bin/env python3
"""Build reviewable character-profile proposals from accepted chapter evidence."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIELDS = ("Role", "Personality", "Voice", "Relationships")
FIELD_LINE = re.compile(r"^- \*\*(Role|Personality|Voice|Relationships):\*\* (.+)$", re.MULTILINE)

try:
    from tools.chapter import chapter_path, extract_chapter, source_chapters
    from tools.names import profile_koreans
    from tools.model_io import parse_json_object
    from tools.workflow import atomic_json, atomic_text, estimated_tokens, project_config, run_omp
except ModuleNotFoundError:
    from chapter import chapter_path, extract_chapter, source_chapters
    from names import profile_koreans
    from model_io import parse_json_object
    from workflow import atomic_json, atomic_text, estimated_tokens, project_config, run_omp


def translation_path(number: int) -> Path:
    return ROOT / "translations" / f"{number:04d}.md"


def digest_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def profile_path(name: str) -> Path:
    path = Path(name)
    if path.name != name or path.suffix not in {"", ".md"}:
        raise SystemExit("profile must be a character filename or stem")
    result = ROOT / "characters" / (name if name.endswith(".md") else f"{name}.md")
    if not result.is_file():
        raise SystemExit(f"character profile not found: {result.relative_to(ROOT)}")
    return result


def chapters_for(
    profile: Path,
    sources: dict[int, str] | None = None,
    *,
    from_chapter: int | None = None,
) -> list[int]:
    names = profile_koreans(profile.read_text(encoding="utf-8"))
    if not names:
        return []
    source_texts = sources or {number: extract_chapter(number) for number in source_chapters()}
    return [
        number
        for number, source in source_texts.items()
        if (from_chapter is None or number >= from_chapter)
        and translation_path(number).is_file() and any(name in source for name in names)
    ]


def weak_voice(body: str) -> bool:
    match = next((value.strip().casefold() for key, value in FIELD_LINE.findall(body) if key == "Voice"), "")
    return not match or any(term in match for term in ("not established", "unknown", "no distinctive", "not yet established"))


def inventory(limit: int) -> None:
    sources = {number: extract_chapter(number) for number in source_chapters()}
    profiles = sorted((ROOT / "characters").glob("*.md"))
    rows = [(path, chapters_for(path, sources), weak_voice(path.read_text(encoding="utf-8"))) for path in profiles]
    rows.sort(key=lambda row: (not row[2], -len(row[1]), row[0].name.casefold()))
    print("Profile\tChapters\tVoice needs evidence")
    for path, chapters, needs_voice in rows[:max(0, limit)]:
        print(f"{path.name}\t{len(chapters)}\t{'yes' if needs_voice else 'no'}")


def sampled_chapters(chapters: list[int], count: int) -> list[int]:
    if count < 1:
        raise SystemExit("--samples must be positive")
    if len(chapters) <= count:
        return chapters
    # Spread evidence across the character's history rather than sampling one arc.
    indexes = [round(index * (len(chapters) - 1) / (count - 1)) for index in range(count)] if count > 1 else [len(chapters) - 1]
    return [chapters[index] for index in dict.fromkeys(indexes)]


def build_packet(profile: Path, chapters: list[int]) -> tuple[str, dict[str, dict[str, str]]]:
    body = profile.read_text(encoding="utf-8")
    refs: dict[str, dict[str, str]] = {}
    sections = []
    for number in chapters:
        source_path = chapter_path(number)
        english_path = translation_path(number)
        source = extract_chapter(number)
        translation = english_path.read_text(encoding="utf-8")
        refs[str(number)] = {
            "source_sha256": digest_bytes(source_path.read_bytes()),
            "translation_sha256": digest_bytes(english_path.read_bytes()),
        }
        sections.append(f"""## Chapter {number}

### Korean source

```text
{source.rstrip()}
```

### Accepted English translation

```markdown
{translation.rstrip()}
```""")
    packet = f"""# Character Profile Retrofit — {profile.stem}

Use only the supplied accepted source/translation pairs and current profile.
Propose concise stable guidance that will improve future translation decisions,
not a biography or chapter recap. Update only fields supported by repeated or
otherwise clear evidence. For Voice, describe observable register, cadence,
word choice, and/or address habits when these distinguish the character. Do not
invent a signature voice from one utterance or confuse temporary emotion with a
stable trait. Keep a genuinely unsupported field unchanged; do not replace it
with generic filler. Cite every proposed change with one or more supplied
chapter numbers. The only allowed `evidence_chapters` are {chapters}; the old
profile's Sources line is not evidence for a new change. Return exactly one
JSON object, no Markdown fence:

{{
  "fields": {{"Role": "...", "Personality": "...", "Voice": "...", "Relationships": "..."}},
  "evidence_chapters": {chapters}
}}

Return the complete four-field set. Keep each value to one concise sentence.

## Current profile

```markdown
{body.rstrip()}
```

{chr(10).join(sections)}
"""
    return packet, refs


def validated_model_result(result: dict) -> tuple[dict[str, str], list[int]]:
    fields = result.get("fields")
    evidence = result.get("evidence_chapters")
    if not isinstance(fields, dict):
        raise SystemExit("proposal must return a fields object")
    if "evidence_chapters" in fields:
        if fields["evidence_chapters"] != evidence:
            raise SystemExit("nested evidence_chapters must match the top-level list")
        fields = {key: value for key, value in fields.items() if key != "evidence_chapters"}
    if set(fields) != set(FIELDS):
        raise SystemExit("proposal must return exactly Role, Personality, Voice, and Relationships")
    if any(not isinstance(fields[field], str) or not fields[field].strip() or "\n" in fields[field] for field in FIELDS):
        raise SystemExit("every proposed profile field must be a nonempty single line")
    if not isinstance(evidence, list) or not evidence:
        raise SystemExit("proposal evidence_chapters must cite supplied chapter numbers")
    return fields, evidence


def propose(name: str, samples: int, from_chapter: int | None = None) -> Path:
    profile = profile_path(name)
    profile_hash = digest_bytes(profile.read_bytes())
    chapters = chapters_for(profile, from_chapter=from_chapter)
    if not chapters:
        raise SystemExit(f"no accepted source/translation chapters matched {profile.name}")
    selected = sampled_chapters(chapters, samples)
    packet, refs = build_packet(profile, selected)
    token_limit = int(project_config().get("retrofit_review_token_limit", 70000))
    tokens = estimated_tokens(packet)
    if tokens > token_limit:
        raise SystemExit(f"profile packet estimate {tokens} exceeds configured limit {token_limit}; reduce --samples")
    work = ROOT / ".work" / "profile-retrofit"
    work.mkdir(parents=True, exist_ok=True)
    stem = profile.stem
    packet_path = work / f"{stem}.md"
    atomic_text(packet_path, packet)
    raw, _metrics, _call = run_omp(
        packet_path, project_config()["summary_model"], 960,
        log_path=work / f"{stem}.jsonl", label="profile-retrofit",
    )
    result = parse_json_object(raw)
    fields, evidence = validated_model_result(result)
    if any(type(number) is not int or str(number) not in refs for number in evidence):
        raise SystemExit("proposal evidence_chapters must cite supplied chapter numbers")
    if digest_bytes(profile.read_bytes()) != profile_hash:
        raise SystemExit("profile changed while its proposal was being generated")
    current = {field: value for field, value in FIELD_LINE.findall(profile.read_text(encoding="utf-8"))}
    if set(current) != set(FIELDS):
        raise SystemExit("profile must contain exactly one current line for each editable field")
    proposal = {
        "version": 1,
        "profile": profile.name,
        "profile_sha256": profile_hash,
        "chapters": {number: refs[str(number)] for number in sorted(set(evidence))},
        "fields": {field: fields[field].strip() for field in FIELDS},
    }
    path = work / f"{stem}.proposal.json"
    atomic_json(path, proposal)
    print(f"Evidence chapters: {', '.join(map(str, selected))}")
    print(f"Review and edit proposal before applying: {path.relative_to(ROOT)}")
    return path


def apply(proposal_path: Path) -> None:
    proposal = json.loads(proposal_path.read_text(encoding="utf-8"))
    if proposal.get("version") != 1:
        raise SystemExit("unsupported profile proposal version")
    profile = profile_path(proposal.get("profile", ""))
    if digest_bytes(profile.read_bytes()) != proposal.get("profile_sha256"):
        raise SystemExit("profile changed since proposal; regenerate it before applying")
    chapters = proposal.get("chapters")
    if not isinstance(chapters, dict) or not chapters:
        raise SystemExit("proposal requires cited source chapters")
    for number, hashes in chapters.items():
        if not number.isdigit() or not isinstance(hashes, dict):
            raise SystemExit("invalid chapter evidence record")
        source, translation = chapter_path(int(number)), translation_path(int(number))
        if not source.is_file() or not translation.is_file():
            raise SystemExit(f"evidence chapter {number} is no longer available")
        if digest_bytes(source.read_bytes()) != hashes.get("source_sha256") or digest_bytes(translation.read_bytes()) != hashes.get("translation_sha256"):
            raise SystemExit(f"evidence chapter {number} changed since proposal")
    fields = proposal.get("fields")
    if not isinstance(fields, dict) or set(fields) != set(FIELDS) or any(
        not isinstance(fields[field], str) or not fields[field].strip() or "\n" in fields[field]
        for field in FIELDS
    ):
        raise SystemExit("proposal fields are invalid")
    body = profile.read_text(encoding="utf-8")
    matches = {field: value for field, value in FIELD_LINE.findall(body)}
    if set(matches) != set(FIELDS):
        raise SystemExit("profile must contain exactly one editable line per field")
    for field in FIELDS:
        body, count = re.subn(
            rf"^- \*\*{field}:\*\* .+$",
            f"- **{field}:** {fields[field].strip()}", body, count=1, flags=re.MULTILINE,
        )
        if count != 1:
            raise SystemExit(f"could not update unique {field} field")
    evidence_text = ", ".join(sorted(chapters, key=int))
    source_line = re.search(r"^- \*\*Sources:\*\* (.+)$", body, re.MULTILINE)
    if source_line:
        existing = source_line.group(1)
        citation = f"Profile retrofit evidence: Chapters {evidence_text}"
        if citation not in existing:
            body = body.replace(source_line.group(0), source_line.group(0) + "; " + citation, 1)
    else:
        body = body.rstrip() + f"\n- **Sources:** Profile retrofit evidence: Chapters {evidence_text}\n"
    atomic_text(profile, body)
    print(f"Updated {profile.relative_to(ROOT)} from reviewed proposal; cited chapters {evidence_text}.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    listing = commands.add_parser("inventory", help="rank profiles by recurrence and weak voice fields")
    listing.add_argument("--limit", type=int, default=40)
    proposal = commands.add_parser("propose", help="build evidence packet and save a reviewable proposal")
    proposal.add_argument("profile", help="profile filename or English stem")
    proposal.add_argument("--samples", type=int, default=6)
    proposal.add_argument("--from-chapter", type=int, help="exclude earlier same-name identities")
    applying = commands.add_parser("apply", help="apply a reviewed proposal after hash checks")
    applying.add_argument("proposal", type=Path)
    args = parser.parse_args()
    if args.command == "inventory":
        inventory(args.limit)
    elif args.command == "propose":
        propose(args.profile, args.samples, args.from_chapter)
    else:
        apply(args.proposal if args.proposal.is_absolute() else ROOT / args.proposal)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
