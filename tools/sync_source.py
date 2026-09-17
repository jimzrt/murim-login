#!/usr/bin/env python3
"""Clone or update the private Korean source tree into source/."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "source"
DEFAULT_REPO = "jimzrt/murim-login-source"
DEFAULT_BRANCH = "master"


def run(command: list[str], *, cwd: Path | None = None, env: dict[str, str] | None = None) -> None:
    subprocess.run(command, cwd=cwd, env=env, check=True)


def gh_token() -> str | None:
    try:
        result = subprocess.run(
            ["gh", "auth", "token"],
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    token = result.stdout.strip()
    return token or None


def git_env(token: str | None) -> dict[str, str]:
    env = os.environ.copy()
    if token:
        env["GIT_CONFIG_COUNT"] = "1"
        env["GIT_CONFIG_KEY_0"] = "http.extraHeader"
        env["GIT_CONFIG_VALUE_0"] = f"Authorization: Bearer {token}"
    return env


def git(source: Path, *args: str, token: str | None) -> None:
    run(["git", *args], cwd=source, env=git_env(token))


def clone_into(source: Path, repo: str, branch: str, token: str | None) -> None:
    url = f"https://github.com/{repo}.git"
    if token:
        run(["gh", "repo", "clone", repo, str(source), "--", "--branch", branch])
        return
    run(["git", "clone", "--branch", branch, url, str(source)])


def only_placeholder(source: Path) -> bool:
    if not source.is_dir():
        return True
    names = {path.name for path in source.iterdir() if path.name != ".DS_Store"}
    return names <= {"README.md"}


def attach_existing(source: Path, repo: str, branch: str, token: str | None) -> None:
    url = f"https://github.com/{repo}.git"
    if not (source / ".git").exists():
        run(["git", "init", "-b", branch], cwd=source)
        git(source, "remote", "add", "origin", url, token=token)
    git(source, "fetch", "origin", token=token)
    git(source, "checkout", "-f", "-B", branch, f"origin/{branch}", token=token)
    git(source, "branch", f"--set-upstream-to=origin/{branch}", branch, token=token)


def pull(source: Path, branch: str, token: str | None) -> None:
    git(source, "fetch", "origin", token=token)
    git(source, "checkout", branch, token=token)
    git(source, "pull", "--ff-only", "origin", branch, token=token)


def chapter_count(source: Path) -> tuple[int, int | None]:
    numbers = sorted(
        int(path.stem)
        for path in source.glob("[0-9][0-9][0-9][0-9].txt")
        if path.stem.isdigit()
    )
    if not numbers:
        return 0, None
    return len(numbers), numbers[-1]


def refresh_reader_count() -> None:
    script = ROOT / "reader" / "scripts" / "sync-source-count.mjs"
    if not script.is_file():
        return
    subprocess.run(["node", str(script)], cwd=ROOT / "reader", check=False)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=os.environ.get("MURIM_SOURCE_REPO", DEFAULT_REPO))
    parser.add_argument("--branch", default=os.environ.get("MURIM_SOURCE_BRANCH", DEFAULT_BRANCH))
    args = parser.parse_args()
    token = gh_token()
    source = SOURCE_DIR

    if (source / ".git").is_dir():
        print(f"Updating {source} from {args.repo}…")
        pull(source, args.branch, token)
    elif only_placeholder(source):
        if source.exists():
            shutil.rmtree(source)
        print(f"Cloning {args.repo} into {source}…")
        clone_into(source, args.repo, args.branch, token)
    else:
        print(f"Attaching existing files in {source} to {args.repo}…")
        attach_existing(source, args.repo, args.branch, token)

    total, last = chapter_count(source)
    if total:
        print(f"{total} source chapters (max {last})")
    else:
        print("no numbered chapter files in source/", file=sys.stderr)
        return 1
    refresh_reader_count()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
