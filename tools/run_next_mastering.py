#!/usr/bin/env python3
"""Run the next unmastered accepted chapter and checkpoint the overlay."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from cost_report import build_report, format_report, format_resource_report
from run_lock import hold_commit_lock, hold_master_lock
from run_next import changed_paths, commit_paths, git

try:
    from tools.workflow import (
        accept_allowed_paths,
        command_committed,
        incomplete_chapter,
        incomplete_mastering_chapter,
        is_harness_artifact,
        master_allowed_paths,
        master_owns_path,
        paths,
        translation_write_paths,
    )
    from tools.mastering import state_for
except ModuleNotFoundError:
    from workflow import (
        accept_allowed_paths,
        command_committed,
        incomplete_chapter,
        incomplete_mastering_chapter,
        is_harness_artifact,
        master_allowed_paths,
        master_owns_path,
        paths,
        translation_write_paths,
    )
    from mastering import state_for


def primary_stage(number: int) -> str | None:
    state_path = paths(number)["state"]
    if not state_path.exists():
        return None
    try:
        return json.loads(state_path.read_text(encoding="utf-8")).get("stage")
    except (OSError, json.JSONDecodeError):
        return None


def overlay_promoted(number: int) -> bool:
    state = state_for(number)
    return state.get("stage") == "PROMOTED" and bool(state.get("qa_passed"))


def accepted_translation_numbers() -> list[int]:
    folder = ROOT / "translations"
    if not folder.is_dir():
        return []
    numbers = []
    for path in sorted(folder.glob("[0-9][0-9][0-9][0-9].md")):
        numbers.append(int(path.stem))
    return numbers


def needs_mastering(number: int) -> bool:
    stage = primary_stage(number)
    if stage == "MASTERED":
        return True
    if stage == "MASTERED_COMMITTED":
        return False
    if stage not in {None, "COMMITTED"}:
        return False
    return not overlay_promoted(number)


def translation_window_paths() -> set[str]:
    in_flight = incomplete_chapter()
    if in_flight is None:
        return set()
    return translation_write_paths(in_flight) | accept_allowed_paths(in_flight)


def overlay_resumable(number: int) -> bool:
    state = state_for(number)
    stage = state.get("stage")
    if stage in {None, "NOT_STARTED"}:
        return False
    if stage == "PROMOTED" and state.get("qa_passed"):
        return False
    return True


def next_mastering_chapter() -> int | None:
    in_progress = incomplete_mastering_chapter()
    if in_progress is not None:
        return in_progress
    blocked = translation_window_paths()
    for number in accepted_translation_numbers():
        if not needs_mastering(number):
            continue
        translation = f"translations/{number:04d}.md"
        if translation in blocked:
            raise SystemExit(
                f"chapter {number} is in the in-flight translation write window; "
                "wait until that translation run commits, then rerun "
                "python tools/run_next_mastering.py"
            )
        return number
    return None


def foreign_translate_paths(dirty: list[str], chapter: int) -> set[str]:
    in_flight = incomplete_chapter()
    if in_flight is None:
        return set()
    allowed = accept_allowed_paths(in_flight)
    return {path for path in dirty if path in allowed and not master_owns_path(path, chapter)}


def require_repository(chapter: int, *, resume: bool) -> None:
    try:
        git("rev-parse", "--verify", "HEAD")
        dirty = changed_paths()
    except subprocess.CalledProcessError as error:
        raise SystemExit(error.stderr.strip() or "project must be an initialized Git repository") from None
    foreign = foreign_translate_paths(dirty, chapter)
    allowed_accept = accept_allowed_paths(chapter) if resume else set()
    harness = [path for path in dirty if path not in foreign and is_harness_artifact(path)]
    unexpected = [
        path for path in harness
        if not master_owns_path(path, chapter) and path not in allowed_accept
    ]
    if unexpected:
        raise SystemExit("working tree has unexpected changes: " + ", ".join(unexpected))
    ours = [path for path in harness if master_owns_path(path, chapter) or path in allowed_accept]
    if not resume and ours:
        raise SystemExit(
            "working tree must be clean of mastering files before run_next_mastering; "
            "commit or stash existing changes"
        )


def run_master(chapter: int) -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "workflow.py"), "master", str(chapter)],
        cwd=ROOT,
    )
    if result.returncode:
        raise SystemExit(f"workflow master failed with exit code {result.returncode}")


def print_cost_report(chapter: int) -> None:
    report = build_report(live_usage=True)
    print(flush=True)
    print(format_report(report, chapter), flush=True)
    print(flush=True)
    print(format_resource_report(report), flush=True)


def commit_mastered(chapter: int) -> None:
    transaction = json.loads(paths(chapter)["state"].read_text(encoding="utf-8"))
    if transaction.get("stage") != "MASTERED":
        raise SystemExit(f"workflow stopped at {transaction.get('stage')}; expected MASTERED")
    dirty = changed_paths()
    allowed = master_allowed_paths(chapter, dirty) | accept_allowed_paths(chapter)
    foreign = foreign_translate_paths(dirty, chapter)
    unexpected = [
        path for path in dirty
        if path not in allowed and path not in foreign and is_harness_artifact(path)
    ]
    if unexpected:
        raise SystemExit("refusing to commit unexpected paths: " + ", ".join(unexpected))
    ours = [path for path in dirty if path in allowed]
    if not ours:
        raise SystemExit("workflow reached MASTERED without checkpointable changes")
    print(f"  ✓ commit     {len(ours)} files", flush=True)
    print("             Checkpoint mastered chapter artifacts in Git", flush=True)
    with hold_commit_lock(ROOT, holder="run_next_mastering", chapter=chapter, stage="committing"):
        commit_paths(ours, f"Master Chapter {chapter}")
        command_committed(chapter, "HEAD")
    print(f"Chapter {chapter}  mastered", flush=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    chapter = next_mastering_chapter()
    if chapter is None:
        print("Nothing to master: accepted translations are already promoted.", flush=True)
        return 0
    state_path = paths(chapter)["state"]
    stage = json.loads(state_path.read_text(encoding="utf-8")).get("stage") if state_path.exists() else None
    resume = (
        stage == "MASTERED"
        or incomplete_mastering_chapter() == chapter
        or overlay_resumable(chapter)
    )
    with hold_master_lock(ROOT, holder="run_next_mastering", chapter=chapter, stage=stage or "starting") as lock:
        require_repository(chapter, resume=resume)
        from progress import chapter_banner
        chapter_banner(
            chapter,
            "master" if not resume else "resume",
            pipeline="Deterministic master → adjudicate → promote → commit",
        )
        if stage != "MASTERED":
            lock.update(stage="master")
            run_master(chapter)
        print_cost_report(chapter)
        lock.update(stage="committing")
        commit_mastered(chapter)
        lock.update(stage="MASTERED_COMMITTED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
