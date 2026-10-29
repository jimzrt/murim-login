#!/usr/bin/env python3
"""Character portraits from the range-aware `Appearance` profile lines, generated through Codex.

Stages:

1. prompts   deterministic: one prompt per character range from `characters/*.md` (top 50 in
             reviews/appearance/) plus hand-curated reviews/illustrations/overrides.json, written to
             reviews/illustrations/prompts.json with the source facts and the filled-in choices kept apart.
             A range prompt uses only its own profile line and the overrides for that range; `not
             described` characters are skipped. Characters without overrides are `curated: false`.
2. generate  sequential and resumable: one `codex exec` turn per prompt; the newest PNG in
             ~/.codex/generated_images/<thread_id>/ is the result. Originals stay in
             .work/illustrations/originals/ (outside git); a 512 px WebP goes to
             reader/public/characters/<slug>-<start>.webp and reader/src/data/character-illustrations.json
             maps character -> ranges. Done ids are skipped. Any failure stops the run; a quota or
             rate-limit failure is recorded as `blocked` and never retried in the same run.
3. status    done / stale / pending / failed per id.

    python tools/illustrate.py prompts
    python tools/illustrate.py generate jin-taekyung-1 --max 1
    python tools/illustrate.py generate --max 20
    python tools/illustrate.py status
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APPEARANCE_DIR = ROOT / "reviews" / "appearance"
ILLUSTRATIONS = ROOT / "reviews" / "illustrations"
OVERRIDES = ILLUSTRATIONS / "overrides.json"
PROMPTS = ILLUSTRATIONS / "prompts.json"
MANIFEST = ILLUSTRATIONS / "manifest.json"
WORK = ROOT / ".work" / "illustrations"
ORIGINALS = WORK / "originals"
PUBLIC = ROOT / "reader" / "public" / "characters"
READER_DATA = ROOT / "reader" / "src" / "data" / "character-illustrations.json"
CODEX_IMAGES = Path.home() / ".codex" / "generated_images"

MURIM_SETTING = "wuxia murim setting inspired by Ming-dynasty China"
STYLE = (
    "Semi-realistic Korean webtoon (manhwa) illustration, {setting}. Bust portrait, three-quarter view, "
    "eye-level, character centered, plain softly blurred ink-wash background in muted warm tones, soft "
    "cinematic lighting, clean linework, painterly shading. No text, no watermark, no border."
)
HALF_BODY = "Framing: half-body (waist-up) instead of a bust, so the build reads clearly."
WRAPPER = (
    "Use your image generation tool to create exactly one image from the prompt below. "
    "Generate exactly one image and do not retry. Do not read files, run shell commands, or copy, "
    "move or save any files. After the single generation, reply only with: done\n\nPROMPT:\n"
)
REFERENCE_WRAPPER = (
    "New image, new pose and composition. Use the attached image only as an art-style reference "
    "(linework, shading, palette, lighting); do not copy its character, face, hair, clothing or composition.\n\n"
)
WEBP_WIDTH = 512
WEBP_QUALITY = 80
CODEX_TIMEOUT = 900

LINE_RE = re.compile(r"^- \*\*Appearance \((?:ch (\d+)[–-](\d+)|from ch (\d+))\):\*\* (.+)$", re.M)
GENDER_RE = re.compile(r"^- \*\*Gender:\*\* (.+)$", re.M)
BLOCKED_RE = re.compile(r"usage limit|rate.?limit|quota|too many requests|\b429\b|insufficient|limit reached|try again (later|in)", re.I)


class Blocked(Exception):
    """Quota or rate limit: stop the run, never retry automatically."""


class Failed(Exception):
    pass


# --------------------------------------------------------------------- prompts

def slugify(english: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", english.casefold()).strip("-")


def parse_profile(text: str) -> tuple[str | None, list[dict]]:
    """Gender and appearance ranges (`to` is None for an open `from ch C` line)."""
    gender = GENDER_RE.search(text)
    ranges = []
    for match in LINE_RE.finditer(text):
        start = int(match.group(1) or match.group(3))
        end = int(match.group(2)) if match.group(2) else None
        body = match.group(4).strip()
        description, _, tags = body.partition(" Tags: ")
        ranges.append({
            "from": start,
            "to": end,
            "line": match.group(0),
            "description": description.strip(),
            "tags": [tag.strip() for tag in tags.split(",") if tag.strip()],
        })
    return (gender.group(1).strip() if gender else None), ranges


def characters() -> list[dict]:
    """Rank-ordered characters from the appearance evidence, read from their profiles."""
    rows = []
    for path in sorted(APPEARANCE_DIR.glob("[0-9][0-9][0-9]-*.json")):
        evidence = json.loads(path.read_text(encoding="utf-8"))
        profile = ROOT / evidence["profile"]
        rows.append({"rank": evidence["rank"], "english": evidence["english"], "profile": evidence["profile"],
                     "text": profile.read_text(encoding="utf-8")})
    return rows


def resolve(character: dict, start: int) -> dict:
    """Character-level overrides with the range-level ones layered on top."""
    merged = {key: value for key, value in character.items() if key != "ranges"}
    merged["fill_ins"] = dict(character.get("fill_ins", {}))
    extra = character.get("ranges", {}).get(str(start), {})
    for key, value in extra.items():
        if key == "fill_ins":
            merged["fill_ins"].update(value)
        else:
            merged[key] = value
    return merged


def auto_eyes(tags: list[str]) -> dict:
    """Lessons 1 and 2: name the iris colour; 맑은 눈 means clear and sharp, not pale."""
    colours = [tag for tag in tags if re.search(r"\b(black|brown|gr[ae]y|blue|green|red|golden|amber|violet|white) eyes\b", tag)]
    clear = any(re.search(r"\b(clear|transparent|bright)\b", tag) for tag in tags if "eye" in tag)
    if colours:
        colour = re.sub(r"\s*eyes\b.*", "", colours[0]).split()[-1]
        text = f"{colour} irises"
        basis = f"profile tag: {colours[0]}"
    else:
        text = "dark brown irises"
        basis = None
    if clear:
        text += "; the eyes are strikingly clear, bright and sharp"
    return {"text": text, "basis": basis}


def build_entry(row: dict, item: dict, gender: str | None, overrides: dict) -> dict:
    curated = row["english"] in overrides
    spec = resolve(overrides.get(row["english"], {}), item["from"])
    setting = spec.get("setting") or MURIM_SETTING
    framing = spec.get("framing", "bust")
    appearance = spec.get("appearance") or re.sub(rf"^{re.escape(row['english'])}(,\s*)?\s*(is|has|wears)?\s*", "", item["description"]).rstrip(".")
    eyes = spec.get("eyes") or auto_eyes(item["tags"])
    expression = spec.get("expression") or {"text": "a calm, composed expression", "basis": None}
    fill_ins = {key: value for key, value in spec.get("fill_ins", {}).items() if value and value != "none"}
    identity = spec.get("identity")

    parts = [STYLE.format(setting=setting)]
    if framing == "half-body":
        parts.append(HALF_BODY)
    label = f"{row['english']}, {gender}" if gender in ("male", "female") else row["english"]
    subject = f"Subject: {label}: {appearance}."
    if identity:
        subject += f" Constant identity features: {identity}."
    for key in ("hair", "clothing"):
        if key in fill_ins:
            subject += f" {key.capitalize()}: {fill_ins[key]}."
    parts.append(subject)
    parts.append(f"Eyes: {eyes['text']}.")
    parts.append(f"Expression: {expression['text']}.")
    if "motif" in fill_ins:
        parts.append(f"Motif: {fill_ins['motif']}.")
    prompt = "\n".join(parts)

    source = {"line": item["line"], "tags": item["tags"], "gender": gender, "appearance": appearance}
    filled = dict(fill_ins)
    if identity:
        filled["identity"] = identity
    for name, value in (("eyes", eyes), ("expression", expression)):
        if value.get("basis"):
            source[name] = value
        else:
            filled[name] = value["text"]
    slug = slugify(row["english"])
    return {
        "id": f"{slug}-{item['from']}",
        "character": row["english"],
        "slug": slug,
        "rank": row["rank"],
        "profile": row["profile"],
        "from": item["from"],
        "to": item["to"],
        "curated": curated,
        "setting": setting,
        "framing": framing,
        "framing_reason": spec.get("framing_reason"),
        "prompt": prompt,
        "prompt_hash": hashlib.sha256(prompt.encode("utf-8")).hexdigest()[:16],
        "source_facts": source,
        "fill_ins": filled,
        "alt": item["description"],
    }


def build_prompts(rows: list[dict] | None = None, overrides: dict | None = None) -> list[dict]:
    rows = characters() if rows is None else rows
    if overrides is None:
        overrides = json.loads(OVERRIDES.read_text(encoding="utf-8")) if OVERRIDES.exists() else {}
    overrides = {key: value for key, value in overrides.items() if not key.startswith("_")}
    entries = []
    for row in rows:
        gender, ranges = parse_profile(row["text"])
        for item in ranges:
            entries.append(build_entry(row, item, gender, overrides))
    return entries


def command_prompts(args: argparse.Namespace) -> int:
    entries = build_prompts()
    write_json(PROMPTS, {"version": 1, "style": STYLE, "wrapper": WRAPPER, "prompts": entries})
    if MANIFEST.exists():
        write_json(READER_DATA, reader_data(load_manifest(), entries))
    curated = sum(entry["curated"] for entry in entries)
    print(f"{len(entries)} prompts ({curated} curated) -> {PROMPTS.relative_to(ROOT)}")
    return 0


# --------------------------------------------------------------------- manifest

def write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(tmp, path)


def load_manifest() -> dict:
    if MANIFEST.exists():
        return json.loads(MANIFEST.read_text(encoding="utf-8"))
    return {"version": 1, "items": {}}


def load_prompts() -> list[dict]:
    if not PROMPTS.exists():
        raise SystemExit("run `python tools/illustrate.py prompts` first")
    return json.loads(PROMPTS.read_text(encoding="utf-8"))["prompts"]


def state(entry: dict, record: dict | None) -> str:
    if not record:
        return "pending"
    if record.get("status") != "done":
        return record.get("status", "pending")
    if record.get("prompt_hash") != entry["prompt_hash"]:
        return "stale"
    return "done"


def key_for(entry: dict, variant: str | None) -> str:
    return f"{entry['id']}~{variant}" if variant else entry["id"]


def select(entries: list[dict], manifest: dict, ids: list[str], force: bool, allow_uncurated: bool,
           variant: str | None = None) -> list[dict]:
    by_id = {entry["id"]: entry for entry in entries}
    unknown = [name for name in ids if name not in by_id]
    if unknown:
        raise SystemExit(f"unknown ids: {', '.join(unknown)}")
    chosen = [by_id[name] for name in ids] if ids else entries
    if not allow_uncurated:
        blocked = [entry["id"] for entry in chosen if not entry["curated"]]
        if ids and blocked:
            raise SystemExit(f"uncurated (add overrides or pass --allow-uncurated): {', '.join(blocked)}")
        chosen = [entry for entry in chosen if entry["curated"]]
    if not force:
        chosen = [entry for entry in chosen
                  if state(entry, manifest["items"].get(key_for(entry, variant))) not in ("done", "stale")]
    return chosen


def reader_data(manifest: dict, entries: list[dict]) -> dict:
    by_id = {entry["id"]: entry for entry in entries}
    data: dict[str, list[dict]] = {}
    for item_id, record in manifest["items"].items():
        if record.get("status") != "done" or item_id not in by_id:
            continue
        entry = by_id[item_id]
        data.setdefault(entry["character"], []).append({
            "from": entry["from"], "to": entry["to"], "image": record["image"], "alt": entry["alt"],
        })
    ordered = sorted(data.items(), key=lambda pair: next(e["rank"] for e in entries if e["character"] == pair[0]))
    return {name: sorted(ranges, key=lambda item: item["from"]) for name, ranges in ordered}


# --------------------------------------------------------------------- codex

def codex_command(prompt: str, workdir: Path, reference: Path | None) -> list[str]:
    command = ["codex", "exec", "--skip-git-repo-check", "--sandbox", "workspace-write", "--json",
               "-C", str(workdir), "-c", 'model_reasoning_effort="low"']
    text = WRAPPER + prompt
    if reference:
        command.append(f"--image={reference}")  # -i is variadic and would swallow the prompt
        text = REFERENCE_WRAPPER + text
    return command + [text]


def parse_events(lines: list[str]) -> dict:
    result = {"thread_id": None, "usage": None, "errors": [], "messages": []}
    for line in lines:
        line = line.strip()
        if not line.startswith("{"):
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        kind = event.get("type")
        if kind == "thread.started":
            result["thread_id"] = event.get("thread_id")
        elif kind == "turn.completed":
            result["usage"] = event.get("usage")
        elif kind in ("error", "turn.failed"):
            error = event.get("error") or event
            result["errors"].append(error.get("message") if isinstance(error, dict) else str(error))
        elif kind == "item.completed" and event.get("item", {}).get("type") == "agent_message":
            result["messages"].append(event["item"].get("text", ""))
    return result


def thread_images(thread_id: str | None) -> list[Path]:
    if not thread_id:
        return []
    folder = CODEX_IMAGES / thread_id
    return sorted(folder.glob("*.png"), key=lambda path: path.stat().st_mtime) if folder.is_dir() else []


def run_codex(entry: dict, reference: Path | None = None, runner=subprocess.run) -> dict:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    workdir = WORK / "codex" / f"{entry['id']}-{stamp}"
    workdir.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()
    try:
        proc = runner(codex_command(entry["prompt"], workdir, reference), stdin=subprocess.DEVNULL,
                      capture_output=True, text=True, timeout=CODEX_TIMEOUT)
    except subprocess.TimeoutExpired as error:
        raise Failed(f"codex timed out after {CODEX_TIMEOUT}s") from error
    seconds = round(time.monotonic() - started, 1)
    (workdir / "events.jsonl").write_text(proc.stdout or "", encoding="utf-8")
    (workdir / "stderr.txt").write_text(proc.stderr or "", encoding="utf-8")
    events = parse_events((proc.stdout or "").splitlines())
    images = thread_images(events["thread_id"])
    info = {"thread_id": events["thread_id"], "seconds": seconds, "usage": events["usage"],
            "generations": len(images), "log": str(workdir.relative_to(ROOT))}
    if not images:
        detail = " | ".join(events["errors"] + [line for line in (proc.stderr or "").splitlines()[-5:] if line.strip()])
        info["error"] = detail[-1000:] or f"no image (exit {proc.returncode})"
        if BLOCKED_RE.search(detail):
            raise Blocked(json.dumps(info, ensure_ascii=False))
        raise Failed(json.dumps(info, ensure_ascii=False))
    info["png"] = images[-1]
    return info


def derive_webp(original: Path, target: Path) -> int:
    from PIL import Image

    target.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(original) as image:
        image = image.convert("RGB")
        height = round(image.height * WEBP_WIDTH / image.width)
        image.resize((WEBP_WIDTH, height), Image.LANCZOS).save(target, "WEBP", quality=WEBP_QUALITY, method=6)
    return target.stat().st_size


def generate_one(entry: dict, manifest: dict, entries: list[dict], reference: Path | None = None,
                 runner=subprocess.run, variant: str | None = None) -> dict:
    """A variant (e.g. a style-reference comparison) keeps its original only: no WebP, no reader data."""
    info = run_codex(entry, reference, runner)
    key = key_for(entry, variant)
    ORIGINALS.mkdir(parents=True, exist_ok=True)
    original = ORIGINALS / f"{key}.png"
    shutil.copy2(info.pop("png"), original)
    record = {
        "status": "done",
        "prompt_hash": entry["prompt_hash"],
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "original": str(original.relative_to(ROOT)),
        "reference": str(reference) if reference else None,
        **info,
    }
    if not variant:
        webp = PUBLIC / f"{entry['id']}.webp"
        record["image"] = f"characters/{webp.name}"
        record["webp_bytes"] = derive_webp(original, webp)
    manifest["items"][key] = record
    write_json(MANIFEST, manifest)
    if not variant:
        write_json(READER_DATA, reader_data(manifest, entries))
    return record


def command_generate(args: argparse.Namespace) -> int:
    entries = load_prompts()
    manifest = load_manifest()
    queue = select(entries, manifest, args.ids, args.force, args.allow_uncurated, args.variant)[: args.max]
    if not queue:
        print("nothing to generate")
        return 0
    reference = Path(args.reference).resolve() if args.reference else None
    for index, entry in enumerate(queue, 1):
        print(f"[{index}/{len(queue)}] {entry['id']} ...", flush=True)
        try:
            record = generate_one(entry, manifest, entries, reference, variant=args.variant)
        except (Blocked, Failed) as error:
            status = "blocked" if isinstance(error, Blocked) else "failed"
            detail = json.loads(str(error)) if str(error).startswith("{") else {"error": str(error)}
            manifest["items"][key_for(entry, args.variant)] = {"status": status, "prompt_hash": entry["prompt_hash"],
                                              "failed_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                                              **detail}
            write_json(MANIFEST, manifest)
            print(f"{status}: {entry['id']}: {detail.get('error')}", file=sys.stderr)
            print("stopped; rerun the same command to resume", file=sys.stderr)
            return 3 if status == "blocked" else 1
        usage = record.get("usage") or {}
        print(f"  done in {record['seconds']}s, {usage.get('input_tokens', '?')} in / {usage.get('output_tokens', '?')} out tokens, "
              f"{record['generations']} generation(s), {record.get('webp_bytes', 0) // 1024} KB webp", flush=True)
    return 0


def command_status(args: argparse.Namespace) -> int:
    entries = load_prompts()
    manifest = load_manifest()
    counts: dict[str, int] = {}
    for entry in entries:
        label = state(entry, manifest["items"].get(entry["id"]))
        if not entry["curated"] and label == "pending":
            label = "uncurated"
        counts[label] = counts.get(label, 0) + 1
        if args.verbose or label in ("failed", "blocked", "stale"):
            print(f"{label:10} {entry['id']}")
    print(", ".join(f"{label}: {count}" for label, count in sorted(counts.items())))
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("prompts", help="rebuild reviews/illustrations/prompts.json")
    gen = sub.add_parser("generate", help="generate pending images through codex, sequentially")
    gen.add_argument("ids", nargs="*")
    gen.add_argument("--max", type=int, default=1, help="images to generate in this run (default 1)")
    gen.add_argument("--force", action="store_true", help="regenerate done or stale ids")
    gen.add_argument("--allow-uncurated", action="store_true", help="include characters without overrides")
    gen.add_argument("--reference", help="attach an image as an art-style reference (experimental)")
    gen.add_argument("--variant", help="store as <id>~<variant> (original only, not in reader data)")
    status = sub.add_parser("status", help="done / stale / pending per id")
    status.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args(argv)
    return {"prompts": command_prompts, "generate": command_generate, "status": command_status}[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
