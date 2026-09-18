#!/usr/bin/env python3
"""Compress oversized durable context with one specialized OMP call."""
from __future__ import annotations
import argparse
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path

try:
    from tools.context import ROOT, load_active_context, workflow_config
    from tools.model_io import parse_json_object
    from tools.run_lock import hold_run_lock
    from tools.workflow import atomic_json, atomic_text, project_config, run_omp
except ModuleNotFoundError:
    from context import ROOT, load_active_context, workflow_config
    from model_io import parse_json_object
    from run_lock import hold_run_lock
    from workflow import atomic_json, atomic_text, project_config, run_omp

FIELDS = ("Safe through", "Aliases", "Role", "Personality", "Voice", "Relationships")


def oversized_profiles(limit: int | None = None) -> list[tuple[Path, str]]:
    threshold = int(workflow_config().get("profile_compress_trigger_bytes", 4096))
    profiles = [(path, path.read_text(encoding="utf-8").strip())
                for path in sorted((ROOT / "characters").glob("*.md"))
                if path.stat().st_size > threshold]
    return profiles if limit is None else profiles[:limit]

def context_compression_due() -> bool:
    path = ROOT / "docs" / "CONTEXT.json"
    if not path.is_file():
        return False
    cfg = workflow_config()
    raw = (ROOT / "docs" / "CONTEXT.json").read_text(encoding="utf-8")
    value = json.loads(raw)
    limits = cfg.get("context_thresholds", {})
    return (len(raw.encode("utf-8")) > int(limits.get("bytes", 12000))
            or any(len(value.get(key, [])) > int(limits.get(key, 999999))
                   for key in ("active_continuity", "open_questions", "temporary_decisions")))


def compression_due() -> bool:
    return context_compression_due() or bool(oversized_profiles())


def build_packet(number: int, profiles: list[tuple[Path, str]]) -> str:
    cfg = workflow_config()
    context = load_active_context(number, enforce_max_bytes=False)
    body = "\n\n".join(f"### {path.relative_to(ROOT)}\n\n{text}" for path, text in profiles) or "(None.)"
    return f"""# Context Compression Task

Return exactly one JSON object and no Markdown fence. Remove stale recaps,
resolved events, speculative story points, and duplicated details. Preserve only
facts needed for upcoming chapters: stable identity, voice, relationships,
unresolved hooks, active medical/status facts, and terminology. Never invent a
future spoiler. Keep the profile under {cfg.get('profile_compress_trigger_bytes', 4096)} bytes,
using only these fields: Safe through, Aliases, Role, Personality, Voice,
Relationships, Sources. Context list limits: {json.dumps(cfg.get('context_thresholds', {}))}.

Return {{"context": {{"version": 1, "safe_through": {context['safe_through']},
"continuity_sources": {json.dumps(context['continuity_sources'])}, "active_continuity": [],
"open_questions": [], "temporary_decisions": []}}, "profiles":
[{{"path": "characters/Name.md", "replacement": "complete Markdown profile"}}]}}.

## Current durable context
```json
{json.dumps(context, ensure_ascii=False, indent=2)}
```

## Oversized profiles
{body}
"""


def validate(value: dict, safe_through: int, paths: set[str]) -> tuple[dict, dict[str, str]]:
    context = value.get("context")
    if not isinstance(context, dict) or context.get("version") != 1 or context.get("safe_through") != safe_through:
        raise ValueError("compression returned invalid context identity")
    limits = workflow_config().get("context_thresholds", {})
    for key in ("active_continuity", "open_questions", "temporary_decisions"):
        items = context.get(key)
        if not isinstance(items, list) or any(not isinstance(item, str) or not item.strip() for item in items):
            raise ValueError(f"compression returned invalid {key}")
        if len(items) > int(limits.get(key, 999999)):
            raise ValueError(f"compression left too many {key}")
    if len(json.dumps(context, ensure_ascii=False).encode("utf-8")) > int(limits.get("bytes", 12000)):
        raise ValueError("compression context remains oversized")
    replacements = {}
    for item in value.get("profiles", []):
        path, replacement = item.get("path"), item.get("replacement")
        if path not in paths or not isinstance(replacement, str):
            raise ValueError("compression returned an unknown profile")
        if not replacement.startswith("# ") or any(f"- **{field}:**" not in replacement for field in FIELDS):
            raise ValueError(f"compressed profile has invalid fields: {path}")
        if len(replacement.encode("utf-8")) > int(workflow_config().get("profile_compress_trigger_bytes", 4096)):
            raise ValueError(f"compressed profile remains oversized: {path}")
        replacements[path] = replacement.rstrip() + "\n"
    if set(replacements) != paths:
        raise ValueError("compression must replace every oversized profile")
    return context, replacements


def compress_one(number: int, profile: tuple[Path, str]) -> tuple[dict, dict[str, str]]:
    packet = ROOT / ".work" / f"context-compress-{profile[0].stem}.md"
    atomic_text(packet, build_packet(number, [profile]))
    raw, _metrics, _call = run_omp(
        packet, project_config()["compress_model"], 960, label="compress", hold=True,
    )
    return validate(parse_json_object(raw), number - 1, {str(profile[0].relative_to(ROOT))})


def run_compression(number: int, *, workers: int = 1) -> list[str]:
    if not compression_due():
        return []
    written: list[str] = []
    profiles = oversized_profiles()
    replacements: dict[str, str] = {}
    if profiles:
        with ThreadPoolExecutor(max_workers=max(1, min(workers, len(profiles)))) as pool:
            for _context, result in pool.map(lambda item: compress_one(number, item), profiles):
                replacements.update(result)
        for relative, text in replacements.items():
            atomic_text(ROOT / relative, text)
            written.append(relative)
    if context_compression_due():
        packet = ROOT / ".work" / "context-compress-context.md"
        atomic_text(packet, build_packet(number, []))
        raw, _metrics, _call = run_omp(
            packet, project_config()["compress_model"], 960, label="compress-context", hold=True,
        )
        context, _ = validate(parse_json_object(raw), number - 1, set())
        atomic_json(ROOT / "docs" / "CONTEXT.json", context)
        written.append("docs/CONTEXT.json")
    return written


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("chapter", type=int, help="next chapter number")
    parser.add_argument("--workers", type=int, default=1, help="parallel profile model calls")
    args = parser.parse_args()
    if args.workers < 1:
        parser.error("--workers must be positive")
    if not compression_due():
        print("context compression not due")
        return 0
    with hold_run_lock(ROOT, holder="context-compress", chapter=args.chapter, stage="compress"):
        written = run_compression(args.chapter, workers=args.workers)
    print(f"compressed {len(written)} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
