#!/usr/bin/env python3
"""Run final touches on the oldest mastered chapter and commit that copy."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from cost_report import build_report, format_report, format_resource_report
from run_lock import hold_commit_lock, hold_final_lock
from run_next import changed_paths, commit_paths, git
from run_next_mastering import foreign_overlap_paths

try:
    from tools.final_touches import (
        final_owns_path,
        foreign_final_paths,
        load_state,
        save_state,
    )
    from tools.mastering import state_for
    from tools.workflow import is_harness_artifact
except ModuleNotFoundError:
    from final_touches import (
        final_owns_path,
        foreign_final_paths,
        load_state,
        save_state,
    )
    from mastering import state_for
    from workflow import is_harness_artifact


def translation_numbers() -> list[int]:
    folder = ROOT / "translations"
    if not folder.is_dir():
        return []
    return [int(path.stem) for path in sorted(folder.glob("[0-9][0-9][0-9][0-9].md"))]


def mastering_done(number: int) -> bool:
    state = state_for(number)
    return state.get("stage") == "PROMOTED" and bool(state.get("qa_passed"))


def final_record(number: int) -> dict:
    return load_state(number)


def final_done(number: int, dirty: set[str]) -> bool:
    state = final_record(number)
    if state.get("stage") != "PROMOTED" or not state.get("qa_passed"):
        return False
    return not any(final_owns_path(path, number) for path in dirty)


def translation_blocked(number: int) -> str | None:
    try:
        from tools.workflow import active_mastering_chapters, incomplete_chapter, translation_write_paths
    except ModuleNotFoundError:
        from workflow import active_mastering_chapters, incomplete_chapter, translation_write_paths
    path = f"translations/{number:04d}.md"
    in_flight = incomplete_chapter()
    if in_flight is not None and path in translation_write_paths(in_flight):
        return (
            f"chapter {number} is in the in-flight translation write window; "
            "wait until that translation run commits, then rerun "
            "python tools/run_next_final.py"
        )
    if any(path == f"translations/{active:04d}.md" for active in active_mastering_chapters()):
        return (
            f"chapter {number} is still being mastered; "
            "wait until that mastering run commits, then rerun "
            "python tools/run_next_final.py"
        )
    return None


def next_final_chapter(dirty: list[str] | None = None) -> int | None:
    dirty_set = set(changed_paths() if dirty is None else dirty)
    pending: list[int] = []
    for number in translation_numbers():
        if final_done(number, dirty_set):
            continue
        if not mastering_done(number):
            break
        pending.append(number)
    if not pending:
        return None
    number = pending[0]
    blocked = translation_blocked(number)
    if blocked:
        raise SystemExit(blocked)
    return number


def allowed_paths(number: int, dirty: list[str]) -> set[str]:
    prefix = f"reviews/final/{number:04d}/"
    return {f"translations/{number:04d}.md", *(path for path in dirty if path.startswith(prefix))}


def require_repository(number: int, *, resume: bool) -> None:
    try:
        git("rev-parse", "--verify", "HEAD")
        dirty = changed_paths()
    except subprocess.CalledProcessError as error:
        raise SystemExit(error.stderr.strip() or "project must be an initialized Git repository") from None
    foreign = set(foreign_overlap_paths(dirty, number)) | foreign_final_paths(dirty)
    foreign.difference_update(path for path in dirty if final_owns_path(path, number))
    harness = [path for path in dirty if path not in foreign and is_harness_artifact(path)]
    ours = {path for path in harness if final_owns_path(path, number)}
    unexpected = [path for path in harness if path not in ours]
    if unexpected:
        raise SystemExit("working tree has unexpected changes: " + ", ".join(unexpected))
    if not resume and ours:
        raise SystemExit(
            "working tree must be clean of final-touches files before run_next_final; "
            "commit or stash existing changes"
        )


def run_final(number: int) -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "final_touches.py"), "run", str(number)],
        cwd=ROOT,
    )
    if result.returncode:
        raise SystemExit(f"final touches failed with exit code {result.returncode}")


def print_cost_report(number: int) -> None:
    report = build_report(live_usage=True)
    print(flush=True)
    print(format_report(report, number), flush=True)
    print(flush=True)
    print(format_resource_report(report), flush=True)


def commit_final(number: int) -> None:
    state = final_record(number)
    if state.get("stage") not in {"READY_TO_COMMIT", "PROMOTED"} or not state.get("qa_passed"):
        raise SystemExit(f"final touches stopped at {state.get('stage')}; expected READY_TO_COMMIT")
    dirty = changed_paths()
    allowed = allowed_paths(number, dirty)
    foreign = set(foreign_overlap_paths(dirty, number)) | foreign_final_paths(dirty)
    foreign.difference_update(allowed)
    unexpected = [
        path for path in dirty
        if path not in allowed and path not in foreign and is_harness_artifact(path)
    ]
    if unexpected:
        raise SystemExit("refusing to commit unexpected paths: " + ", ".join(unexpected))
    ours = [path for path in dirty if path in allowed]
    if not ours:
        existing = git("log", "--all", "-1", "--format=%H", "--grep", f"^Final Chapter {number}$")
        already_in_head = bool(git(
            "ls-tree", "-r", "--name-only", "HEAD", "--",
            f"translations/{number:04d}.md",
            f"reviews/final/{number:04d}/final.md",
        ))
        if not existing and not already_in_head:
            raise SystemExit("final touches produced no checkpointable changes")
        if state.get("stage") != "PROMOTED":
            save_state(number, stage="PROMOTED", qa_passed=True)
            dirty = changed_paths()
            ours = [path for path in dirty if path in allowed_paths(number, dirty)]
        if not ours:
            print("  ✓ commit     already recorded", flush=True)
            print(f"Chapter {number}  final", flush=True)
            return
    if state.get("stage") != "PROMOTED":
        save_state(number, stage="PROMOTED", qa_passed=True)
        dirty = changed_paths()
        ours = [path for path in dirty if path in allowed_paths(number, dirty)]
    print(f"  ✓ commit     {len(ours)} files", flush=True)
    print("             Checkpoint final-touches chapter artifacts in Git", flush=True)
    with hold_commit_lock(ROOT, holder="run_next_final", chapter=number, stage="committing"):
        commit_paths(ours, f"Final Chapter {number}")
    print(f"Chapter {number}  final", flush=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    chapter = next_final_chapter()
    if chapter is None:
        print("Nothing to finish: mastered chapters are already through final touches, or mastering has not caught up.", flush=True)
        return 0
    state = final_record(chapter)
    resume = state.get("stage") in {"RUNNING", "QA_FAILED", "READY_TO_COMMIT", "PROMOTED"}
    with hold_final_lock(ROOT, holder="run_next_final", chapter=chapter, stage=state.get("stage") or "starting") as lock:
        require_repository(chapter, resume=resume)
        from progress import chapter_banner
        chapter_banner(
            chapter,
            "final" if not resume else "resume",
            pipeline="Final touches → deterministic QA → commit",
        )
        if state.get("stage") != "READY_TO_COMMIT":
            lock.update(stage="final")
            run_final(chapter)
        print_cost_report(chapter)
        lock.update(stage="committing")
        commit_final(chapter)
        lock.update(stage="PROMOTED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
