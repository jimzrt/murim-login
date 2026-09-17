#!/usr/bin/env python3
"""Re-adjudicate a frozen mastered chapter under the current briefs.

Does not promote. Does not remaster. Rebuilds the adjudicator packet from the
live baseline/sol/source and runs one or more models in parallel.

  python tools/mastering_ab.py 161
  python tools/mastering_ab.py 161 --models openai-codex/gpt-5.6-luna:medium,openrouter/openai/gpt-4.1-mini
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import traceback
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.mastering import (  # noqa: E402
    adjudicator_packet,
    assemble_from_decisions,
    current_source,
    exact_glossary,
    load_config,
    normalize_chapter,
    parse_json_object,
    validate_adjudication,
    validate_chapter,
)
from tools.omp_json import run_json_command  # noqa: E402

GOLD_PATH = ROOT / "benchmark" / "mastering-gold.json"
DEFAULT_MODELS = [
    "openai-codex/gpt-5.6-luna:medium",
    "openai-codex/gpt-5.6-luna:high",
    "openrouter/openai/gpt-4.1-mini",
    "openrouter/meta/muse-spark-1.3-contributor",
]
TIMEOUT = 900


def slug(model: str) -> str:
    return model.replace(":", "-").replace("/", "-")


def salvage(obj: dict) -> dict:
    decisions = obj.get("decisions")
    if not isinstance(decisions, list):
        raise ValueError(f"no decisions array; keys={list(obj)[:12]}")
    for item in decisions:
        if isinstance(item, dict) and not item.get("hunk_id"):
            for key in list(item):
                if key.endswith("unk_id") or key in {"id", "hunk"}:
                    item["hunk_id"] = item[key]
                    break
    decisions.sort(key=lambda d: int(str(d.get("hunk_id", "H999"))[1:] or 999))
    obj["decisions"] = decisions
    return obj


def parse_output(output: str) -> dict:
    cleaned = re.sub(r"\\u(?![0-9a-fA-F]{4})", r"\\\\u", output)
    try:
        obj = parse_json_object(cleaned)
        if isinstance(obj, dict) and obj.get("decisions"):
            return salvage(obj)
    except Exception:
        pass
    obj = json.loads(cleaned)
    if not isinstance(obj, dict):
        raise ValueError(f"parsed non-object: {type(obj)}")
    return salvage(obj)


def load_gold(number: int) -> dict:
    data = json.loads(GOLD_PATH.read_text(encoding="utf-8"))
    return data.get(str(number), {})


def score_run(number: int, decisions: dict[str, str], final: str, gold: dict) -> dict:
    hunks = gold.get("hunks") or {}
    acceptable = 0
    best = 0
    detail = []
    for hid, spec in hunks.items():
        got = decisions.get(hid, "?")
        ok = got in spec.get("accept", [])
        hit = got == spec.get("best")
        acceptable += int(ok)
        best += int(hit)
        detail.append({"hunk_id": hid, "got": got, "best": spec.get("best"), "ok": ok, "why": spec.get("why")})
    forbid = {phrase: (phrase in final) for phrase in gold.get("forbid") or []}
    prefer = {phrase: (phrase in final) for phrase in gold.get("prefer") or []}
    return {
        "gold_acceptable": acceptable,
        "gold_total": len(hunks),
        "gold_best": best,
        "forbid_hits": forbid,
        "prefer_hits": prefer,
        "detail": detail,
    }


def prepare(number: int, dest: Path, brief_path: Path | None = None) -> dict:
    src = ROOT / "reviews" / "mastering" / f"{number:04d}"
    baseline = normalize_chapter((src / "baseline.md").read_text(encoding="utf-8"))
    sol = normalize_chapter((src / "sol.md").read_text(encoding="utf-8"))
    source = current_source(number)
    glossary = exact_glossary(source)
    diff = json.loads((src / "diff.json").read_text(encoding="utf-8"))
    packet = adjudicator_packet(
        number, source, baseline, sol, glossary, diff, brief_path=brief_path,
    )
    src = ROOT / "reviews" / "mastering" / f"{number:04d}"
    baseline = normalize_chapter((src / "baseline.md").read_text(encoding="utf-8"))
    sol = normalize_chapter((src / "sol.md").read_text(encoding="utf-8"))
    source = current_source(number)
    glossary = exact_glossary(source)
    diff = json.loads((src / "diff.json").read_text(encoding="utf-8"))
    packet = adjudicator_packet(number, source, baseline, sol, glossary, diff)
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "packet.md").write_text(packet, encoding="utf-8")
    (dest / "baseline.md").write_text(baseline, encoding="utf-8")
    (dest / "sol.md").write_text(sol, encoding="utf-8")
    (dest / "diff.json").write_text(json.dumps(diff) + "\n", encoding="utf-8")
    return {"baseline": baseline, "sol": sol, "diff": diff, "packet": dest / "packet.md"}


def run_one(number: int, model: str, dest: Path, prepared: dict, overlay: str | None) -> dict:
    run_dir = dest / "runs" / slug(model)
    run_dir.mkdir(parents=True, exist_ok=True)
    command = [
        "omp", "--mode", "json", "--no-session", "--no-tools", "--no-rules",
        "--no-extensions", "--config", str(ROOT / ".omp/review-overlay.yml"),
    ]
    if overlay:
        command += ["--config", overlay]
    command += ["--model", model, "--max-time", str(TIMEOUT - 60), f"@{prepared['packet']}"]
    result = {"model": model, "chapter": number, "ok": False}
    try:
        output, metrics = run_json_command(
            command, cwd=ROOT, requested_model=model, timeout=TIMEOUT,
            log_path=run_dir / "omp.jsonl",
        )
        (run_dir / "raw.txt").write_text(output, encoding="utf-8")
        (run_dir / "metrics.json").write_text(json.dumps(metrics, indent=2) + "\n")
        value = validate_adjudication(parse_output(output), number, prepared["diff"])
        (run_dir / "adjudication.json").write_text(
            json.dumps(value, indent=2, ensure_ascii=False) + "\n"
        )
        final = assemble_from_decisions(prepared["baseline"], prepared["sol"], value)
        validate_chapter(final, number, "final")
        (run_dir / "final.md").write_text(final, encoding="utf-8")
        counts = {
            k: sum(1 for d in value["decisions"] if d["decision"] == k)
            for k in ("SOL", "BASE", "REPAIR")
        }
        decisions = {d["hunk_id"]: d["decision"] for d in value["decisions"]}
        gold = load_gold(number)
        result.update(
            ok=True,
            counts=counts,
            cost_usd=metrics.get("cost_usd"),
            elapsed=metrics.get("elapsed_seconds"),
            score=score_run(number, decisions, final, gold) if gold else None,
        )
    except Exception as exc:
        (run_dir / "error.txt").write_text(f"{type(exc).__name__}: {exc}\n\n{traceback.format_exc()}")
        result["error"] = f"{type(exc).__name__}: {exc}"
    (run_dir / "result.json").write_text(json.dumps(result, indent=2) + "\n")
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("chapter", type=int)
    parser.add_argument("--models", default=",".join(DEFAULT_MODELS))
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument(
        "--brief",
        default="",
        help="optional adjudicator brief path (default: MASTERING_ADJUDICATOR.md)",
    )
    parser.add_argument(
        "--out",
        default="",
        help="experiment directory under .work/experiments (default: ab-NNNN)",
    )
    args = parser.parse_args()
    number = args.chapter
    models = [item.strip() for item in args.models.split(",") if item.strip()]
    dest = ROOT / ".work" / "experiments" / (args.out or f"ab-{number:04d}")
    brief_path = ROOT / args.brief if args.brief else None
    prepared = prepare(number, dest, brief_path=brief_path)
    cfg = load_config()
    overlay = str(ROOT / cfg["adjudicator_omp_config"]) if cfg.get("adjudicator_omp_config") else None
    print(
        f"chapter {number} hunks={prepared['diff']['hunk_count']} "
        f"packet={prepared['packet'].stat().st_size} models={len(models)}",
        flush=True,
    )
    results = []
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        futs = {pool.submit(run_one, number, model, dest, prepared, overlay): model for model in models}
        for fut in as_completed(futs):
            row = fut.result()
            results.append(row)
            score = row.get("score") or {}
            gold = (
                f"gold {score.get('gold_acceptable')}/{score.get('gold_total')}"
                if score else ""
            )
            print(
                ("OK" if row.get("ok") else "FAIL"),
                row["model"],
                f"{row.get('elapsed') or 0:.0f}s",
                row.get("counts") or row.get("error"),
                gold,
                flush=True,
            )
    (dest / "summary.json").write_text(json.dumps(results, indent=2) + "\n")
    print(f"done ab {sum(1 for r in results if r.get('ok'))}/{len(results)} -> {dest}", flush=True)
    return 0 if any(r.get("ok") for r in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
