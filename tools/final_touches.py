#!/usr/bin/env python3
"""Final-touches pass: footnotes, format, duplicates, and omissions.

One mastered chapter at a time. The model returns a full reading copy. Deterministic
QA must pass before that copy replaces translations/NNNN.md. Commit is separate.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "docs" / "final.json"
BRIEF_PATH = ROOT / "FINAL.md"
IN_FLIGHT = {"RUNNING", "QA_FAILED", "READY_TO_COMMIT"}
PROFILE_DIR = ROOT / "characters"
ROLE_LIMIT = 300
ALIASES_LIMIT = 200

try:
    from tools.final_qa import assess, normalize_reading_copy
    from tools.name_check import name_at_boundary, name_corrections
    from tools.names import ALIAS_LINE, HEADING, profile_gender, profile_koreans
    from tools.mastering import (
        atomic_json,
        atomic_text,
        current_source,
        exact_glossary,
        glossary_text,
        normalize_chapter,
        read_text,
        run_omp,
        sha256_text,
        validate_chapter,
    )
except ModuleNotFoundError:
    sys.path.insert(0, str(ROOT / "tools"))
    from final_qa import assess, normalize_reading_copy
    from name_check import name_at_boundary, name_corrections
    from names import ALIAS_LINE, HEADING, profile_gender, profile_koreans
    from mastering import (
        atomic_json,
        atomic_text,
        current_source,
        exact_glossary,
        glossary_text,
        normalize_chapter,
        read_text,
        run_omp,
        sha256_text,
        validate_chapter,
    )


def load_config() -> dict:
    value = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    model = (value.get("models") or {}).get("final")
    if not isinstance(model, str) or not model.strip():
        raise SystemExit("docs/final.json models.final must name a model")
    currency = value.get("currency") or {}
    for key in ("krw_per_usd", "krw_per_eur"):
        amount = currency.get(key)
        if not isinstance(amount, (int, float)) or isinstance(amount, bool) or amount <= 0:
            raise SystemExit(f"docs/final.json currency.{key} must be a positive number")
    value["min_baseline_preserved"] = float(value.get("min_baseline_preserved", 0.8))
    value["model_retries"] = max(0, int(value.get("model_retries", 1)))
    value["packet_token_limit"] = int(value.get("packet_token_limit", 90000))
    return value


def chapter_paths(number: int) -> dict[str, Path]:
    folder = ROOT / "reviews" / "final" / f"{number:04d}"
    return {
        "root": folder,
        "state": folder / "state.json",
        "baseline": folder / "baseline.md",
        "source": folder / "source.txt",
        "packet": folder / "packet.md",
        "final": folder / "final.md",
        "qa": folder / "qa.json",
        "metrics": folder / "metrics.json",
        "log": folder / "omp" / "final.jsonl",
        "translation": ROOT / "translations" / f"{number:04d}.md",
    }


def load_state(number: int) -> dict:
    path = chapter_paths(number)["state"]
    if not path.exists():
        return {"version": 1, "chapter": number, "stage": "NOT_STARTED"}
    state = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(state, dict):
        return {"version": 1, "chapter": number, "stage": "NOT_STARTED"}
    return state


def save_state(number: int, **fields: object) -> dict:
    path = chapter_paths(number)["state"]
    state = load_state(number)
    state["version"] = 1
    state["chapter"] = number
    state.update(fields)
    atomic_json(path, state)
    return state


def final_owns_path(path: str, number: int) -> bool:
    return path == f"translations/{number:04d}.md" or path.startswith(f"reviews/final/{number:04d}/")


def active_final_chapters() -> list[int]:
    folder = ROOT / "reviews" / "final"
    if not folder.is_dir():
        return []
    found: list[int] = []
    for path in sorted(folder.glob("[0-9][0-9][0-9][0-9]/state.json")):
        try:
            state = json.loads(path.read_text(encoding="utf-8"))
            number = int(path.parent.name)
        except (OSError, json.JSONDecodeError, ValueError):
            continue
        if state.get("stage") in IN_FLIGHT:
            found.append(number)
    return found


def foreign_final_paths(dirty: list[str]) -> set[str]:
    """Paths owned by this queue, so translation and mastering can ignore them."""
    active = set(active_final_chapters())
    foreign: set[str] = set()
    for path in dirty:
        if path.startswith("reviews/final/"):
            foreign.add(path)
            continue
        if any(final_owns_path(path, number) for number in active):
            foreign.add(path)
    return foreign


def _rates(cfg: dict) -> str:
    usd = cfg["currency"]["krw_per_usd"]
    eur = cfg["currency"]["krw_per_eur"]
    usd_text = f"{usd:g}"
    eur_text = f"{eur:g}"
    return f"""## Project conversion rates

These rates are binding. Do not look up or substitute a market rate.

- 1 US dollar = {usd_text} Korean won
- 1 euro = {eur_text} Korean won

Convert every won amount with these rates. In each footnote, give dollars first and euros second.
"""


def _shorten(text: str, limit: int) -> str:
    text = " ".join(text.split())
    if len(text) <= limit:
        return text
    sentence = re.match(r"^(.{40,}?[.;])\s", text[: limit + 1])
    if sentence:
        return sentence.group(1)
    return text[: limit - 1].rstrip(" ,;") + "…"


def _field(body: str, name: str) -> str:
    match = re.search(rf"^- \*\*{re.escape(name)}:\*\*\s*(.*)$", body, re.MULTILINE)
    return match.group(1).strip() if match else ""


def matching_profiles(source: str, directory: Path = PROFILE_DIR) -> list[dict]:
    """Compact identity cards for profiled characters named in this source.

    Ordered by how often the Korean names occur, so trimming for the packet
    budget drops the least-present characters first.
    """
    cards: list[dict] = []
    if not directory.is_dir():
        return cards
    for path in sorted(directory.glob("*.md")):
        body = path.read_text(encoding="utf-8")
        names = [name for name in profile_koreans(body) if name in source and name_at_boundary(source, name)]
        if not names:
            continue
        heading = next((HEADING.match(line) for line in body.splitlines() if HEADING.match(line)), None)
        if heading is None:
            continue
        aliases = next((ALIAS_LINE.match(line) for line in body.splitlines() if ALIAS_LINE.match(line)), None)
        cards.append({
            "english": heading.group(1).strip(),
            "korean": heading.group(2),
            "aliases": _shorten(aliases.group(1), ALIASES_LIMIT) if aliases else "None",
            "gender": profile_gender(body),
            "role": _shorten(_field(body, "Role") or "Not established.", ROLE_LIMIT),
            "hits": sum(source.count(name) for name in names),
        })
    cards.sort(key=lambda card: (-card["hits"], card["english"]))
    return cards


def profiles_text(cards: list[dict], omitted: int = 0) -> str:
    if not cards:
        return "(No profiled characters are named in this chapter.)"
    lines = [
        f"- **{card['english']}** ({card['korean']}) — gender: {card['gender']}; "
        f"aliases: {card['aliases']}; role: {card['role']}"
        for card in cards
    ]
    if omitted:
        lines.append(f"- ({omitted} less-present profiles omitted for the packet budget.)")
    return "\n".join(lines)


def corrections_text(corrections: list[dict]) -> str:
    if not corrections:
        return "(None.)"
    return "\n".join(
        f"- {item['korean']}: replace {', '.join(f'“{variant}”' for variant in item['found'])} "
        f"with “{item['preferred']}” everywhere in the chapter."
        for item in corrections
    )


def build_packet(
    number: int,
    source: str,
    baseline: str,
    glossary: list[dict],
    cfg: dict,
    profiles: list[dict] | None = None,
    corrections: list[dict] | None = None,
    omitted_profiles: int = 0,
) -> str:
    brief = read_text(BRIEF_PATH).strip()
    return f"""# Final Touches — Chapter {number}

{brief}

{_rates(cfg)}
## Exact glossary matches for this Korean chapter

{glossary_text(glossary)}

## Characters named in this chapter

Identity only, safe for this chapter. Use these for pronouns and names. Gender
`unknown` means the source has not settled it: do not change the mastered
pronouns for that character. Never turn these cards into footnotes.

{profiles_text(profiles or [], omitted_profiles)}

## Required name corrections

The mastered English uses a known wrong spelling of these names. Fix every
occurrence; final QA rejects the chapter otherwise.

{corrections_text(corrections or [])}

## Korean source

```text
{source.rstrip()}
```

## Mastered English

```markdown
{baseline.rstrip()}
```

## Final instruction

Apply the final-touches brief to this chapter only. Return only the complete English Markdown chapter beginning exactly with `# Chapter {number}`.
"""


def packet_tokens(text: str) -> int:
    return (len(text.encode("utf-8")) + 3) // 4


def enforce_budget(text: str, cfg: dict) -> None:
    estimate = packet_tokens(text)
    limit = int(cfg["packet_token_limit"])
    if estimate > limit:
        raise SystemExit(f"final packet estimate {estimate} exceeds limit {limit}")


def fitted_packet(
    number: int,
    source: str,
    baseline: str,
    glossary: list[dict],
    cfg: dict,
    profiles: list[dict],
    corrections: list[dict],
) -> str:
    """Drop the least-present profiles until the packet fits its token limit."""
    limit = int(cfg["packet_token_limit"])
    kept = list(profiles)
    while True:
        packet = build_packet(
            number, source, baseline, glossary, cfg, kept, corrections, len(profiles) - len(kept)
        )
        if packet_tokens(packet) <= limit or not kept:
            return packet
        kept.pop()


def slice_chapter(text: str, number: int) -> str:
    marker = f"# Chapter {number}"
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.strip() == marker:
            return "\n".join(lines[index:])
    return text


def _save_metrics(path: Path, number: int, stage: str, metrics: dict) -> None:
    data = {"version": 1, "chapter": number, "stages": {}}
    if path.exists():
        data = json.loads(path.read_text(encoding="utf-8"))
        data.setdefault("stages", {})
    data["stages"][stage] = metrics
    atomic_json(path, data)


def _ready(number: int, paths: dict[str, Path], state: dict) -> bool:
    if state.get("stage") != "READY_TO_COMMIT" or not state.get("qa_passed"):
        return False
    if not paths["translation"].exists() or not paths["qa"].exists():
        return False
    qa = json.loads(paths["qa"].read_text(encoding="utf-8"))
    if not qa.get("passed"):
        return False
    digest = sha256_text(read_text(paths["translation"]))
    return digest == state.get("translation_sha256")


def command_run(number: int) -> None:
    if number < 0:
        raise SystemExit("chapter must be a non-negative integer")
    paths = chapter_paths(number)
    translation = paths["translation"]
    if not translation.exists():
        raise SystemExit(f"missing mastered translation: {translation.relative_to(ROOT)}")
    state = load_state(number)
    if state.get("stage") == "PROMOTED" and state.get("qa_passed"):
        return
    if _ready(number, paths, state):
        return

    try:
        from tools.progress import qa_brief, step
    except ModuleNotFoundError:
        from progress import qa_brief, step

    cfg = load_config()
    paths["root"].mkdir(parents=True, exist_ok=True)
    if not paths["baseline"].exists():
        atomic_text(paths["baseline"], read_text(translation))
    baseline = read_text(paths["baseline"])
    source = current_source(number)
    atomic_text(paths["source"], source)
    glossary = exact_glossary(source)
    packet = fitted_packet(
        number,
        source,
        baseline,
        glossary,
        cfg,
        matching_profiles(source),
        name_corrections(source, baseline),
    )
    enforce_budget(packet, cfg)
    atomic_text(paths["packet"], packet)
    save_state(
        number,
        stage="RUNNING",
        qa_passed=False,
        baseline_sha256=sha256_text(baseline),
        source_sha256=sha256_text(source),
    )

    pairs = [(item.get("korean", ""), item.get("english", "")) for item in glossary]
    attempts = 1 + int(cfg["model_retries"])
    model = cfg["models"]["final"]
    timeout = int((cfg.get("timeouts") or {}).get("final", 1800))
    last_qa: dict | None = None
    for attempt in range(1, attempts + 1):
        stage_name = "final" if attempt == 1 else f"final_retry_{attempt - 1}"
        try:
            output, metrics, call = run_omp(
                paths["packet"],
                model,
                timeout,
                paths["log"],
                label="final",
                hint=f"attempt {attempt}/{attempts}",
                hold=True,
            )
        except RuntimeError as exc:
            raise SystemExit(str(exc)) from None
        try:
            candidate = normalize_reading_copy(
                baseline, normalize_chapter(slice_chapter(output, number))
            )
            validate_chapter(candidate, number, "final")
        except ValueError as exc:
            last_qa = {
                "version": 1,
                "chapter": number,
                "passed": False,
                "errors": [{"code": "output", "message": str(exc), "details": {}}],
                "warnings": [],
                "metrics": {},
            }
            atomic_text(paths["final"], output if isinstance(output, str) else "")
            atomic_json(paths["qa"], last_qa)
            _save_metrics(paths["metrics"], number, stage_name, metrics)
            call.done(metrics, qa_brief(last_qa))
            continue
        last_qa = assess(
            number,
            source,
            baseline,
            candidate,
            pairs,
            min_baseline_preserved=float(cfg["min_baseline_preserved"]),
        )
        atomic_text(paths["final"], candidate)
        atomic_json(paths["qa"], last_qa)
        _save_metrics(paths["metrics"], number, stage_name, metrics)
        call.done(metrics, qa_brief(last_qa))
        if last_qa.get("passed"):
            atomic_text(translation, candidate)
            save_state(
                number,
                stage="READY_TO_COMMIT",
                qa_passed=True,
                final_sha256=sha256_text(candidate),
                translation_sha256=sha256_text(candidate),
            )
            step("final", "ready to commit", facts=[f"attempt {attempt}/{attempts}"])
            return
    save_state(number, stage="QA_FAILED", qa_passed=False)
    summary = ""
    if last_qa:
        messages = [item.get("message", "") for item in last_qa.get("errors") or []]
        summary = "; ".join(message for message in messages if message)
    raise SystemExit(
        f"final touches QA failed for chapter {number}"
        + (f": {summary}" if summary else "")
    )


def command_status(number: int | None) -> None:
    if number is None:
        print("usage: python tools/final_touches.py status N")
        return
    state = load_state(number)
    print(f"Chapter: {number}")
    print(f"Stage: {state.get('stage', 'NOT_STARTED')}")
    print(f"QA: {state.get('qa_passed', '')}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    run = sub.add_parser("run", help="edit one mastered chapter and stop before commit")
    run.add_argument("chapter", type=int)
    status = sub.add_parser("status", help="show final-touches state for one chapter")
    status.add_argument("chapter", type=int)
    args = parser.parse_args()
    if args.command == "status":
        command_status(args.chapter)
        return 0
    try:
        from tools.run_lock import FINAL_LOCK_NAME, hold_final_lock, parent_delegated
    except ModuleNotFoundError:
        from run_lock import FINAL_LOCK_NAME, hold_final_lock, parent_delegated
    if parent_delegated(FINAL_LOCK_NAME):
        command_run(args.chapter)
        return 0
    with hold_final_lock(ROOT, holder="final_touches", chapter=args.chapter, stage="run"):
        command_run(args.chapter)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
