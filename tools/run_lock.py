#!/usr/bin/env python3
"""Exclusive locks for translation, mastering, and Git commits.

Kernel flocks on `.work/run.lock`, `.work/master.lock`, and `.work/commit.lock`
are the mutexes. Each file's JSON is only a status record (pid, holder, chapter,
stage). Nested `run_until` → `run_next` → `workflow.py` processes join the
matching holder instead of taking a second lock. A dead process releases the
flock even if the JSON file remains.

Translation and mastering may overlap. Git commits take `commit.lock` and wait.
"""

from __future__ import annotations

import fcntl
import json
import os
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterator

LOCK_ENV = "MURIM_RUN_LOCK"
MASTER_LOCK_ENV = "MURIM_MASTER_LOCK"
COMMIT_LOCK_ENV = "MURIM_COMMIT_LOCK"
LOCK_NAME = "run.lock"
MASTER_LOCK_NAME = "master.lock"
COMMIT_LOCK_NAME = "commit.lock"
IDENTITY_KEYS = ("pid", "holder", "started")
LOCK_LABELS = {
    LOCK_NAME: "translation",
    MASTER_LOCK_NAME: "mastering",
    COMMIT_LOCK_NAME: "git commit",
}


def lock_env_name(name: str) -> str:
    if name == LOCK_NAME:
        return LOCK_ENV
    if name == MASTER_LOCK_NAME:
        return MASTER_LOCK_ENV
    if name == COMMIT_LOCK_NAME:
        return COMMIT_LOCK_ENV
    return f"MURIM_LOCK_{name.replace('.', '_').upper()}"


def lock_path(root: Path, name: str = LOCK_NAME) -> Path:
    return root / ".work" / name


def utcnow() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def pid_is_alive(pid: int) -> bool:
    if pid <= 0:
        return False
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def _ppid(pid: int) -> int | None:
    try:
        text = Path(f"/proc/{pid}/stat").read_text(encoding="utf-8")
    except OSError:
        return None
    close = text.rfind(")")
    if close < 0:
        return None
    parts = text[close + 1 :].split()
    if len(parts) < 2:
        return None
    try:
        return int(parts[1])
    except ValueError:
        return None


def ancestor_pids() -> set[int]:
    pids: set[int] = set()
    pid = os.getppid()
    while pid > 1 and pid not in pids:
        pids.add(pid)
        parent = _ppid(pid)
        if parent is None or parent == pid:
            break
        pid = parent
    return pids


def in_lock_family(holder_pid: int, env_key: str = LOCK_ENV) -> bool:
    if holder_pid == os.getpid():
        return True
    if holder_pid in ancestor_pids():
        return True
    token = os.environ.get(env_key)
    return token == str(holder_pid) and pid_is_alive(holder_pid)


def read_payload(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, dict) else {}


def _encoded(payload: dict) -> bytes:
    return (json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def _write_fd(fd: int, payload: dict) -> None:
    data = _encoded(payload)
    os.lseek(fd, 0, os.SEEK_SET)
    os.write(fd, data)
    os.ftruncate(fd, len(data))
    os.fsync(fd)


def _write_path(path: Path, payload: dict) -> None:
    data = _encoded(payload)
    fd = os.open(str(path), os.O_RDWR | os.O_CLOEXEC)
    try:
        os.write(fd, data)
        os.ftruncate(fd, len(data))
        os.fsync(fd)
    finally:
        os.close(fd)


def format_payload(payload: dict) -> str:
    lines = []
    for key in ("holder", "pid", "chapter", "stage", "until", "started", "updated"):
        if key in payload and payload[key] is not None:
            lines.append(f"  {key}: {payload[key]}")
    return "\n".join(lines)


def conflict_message(path: Path, payload: dict, name: str = LOCK_NAME) -> str:
    pid = payload.get("pid")
    live = isinstance(pid, int) and pid_is_alive(pid)
    details = format_payload(payload) or f"  path: {path}"
    liveness = "active" if live else "lock held, recorded pid is not running"
    kind = LOCK_LABELS.get(name, name)
    return (
        f"Another {kind} run is already in progress ({liveness}):\n"
        f"{details}\n"
        f"Stop that process before starting another run. Lock: {path}"
    )


class RunLock:
    def __init__(
        self,
        root: Path,
        *,
        owned: bool,
        fd: int | None,
        payload: dict,
        name: str = LOCK_NAME,
    ) -> None:
        self.root = root
        self.name = name
        self.env_key = lock_env_name(name)
        self.path = lock_path(root, name)
        self.owned = owned
        self._fd = fd
        self.payload = payload

    def _persist(self, payload: dict) -> None:
        self.payload = payload
        if self._fd is not None:
            _write_fd(self._fd, payload)
        else:
            _write_path(self.path, payload)

    def update(self, **fields: object) -> dict:
        current = read_payload(self.path) or dict(self.payload)
        incoming = {key: value for key, value in fields.items() if value is not None}
        merged = dict(current)
        merged.update(incoming)
        if not self.owned:
            for key in IDENTITY_KEYS:
                if key in current:
                    merged[key] = current[key]
            if current.get("until") is not None:
                merged["until"] = current["until"]
        merged["updated"] = utcnow()
        self._persist(merged)
        return merged

    def release(self) -> None:
        if not self.owned:
            return
        self.owned = False
        fd = self._fd
        self._fd = None
        if fd is None:
            return
        try:
            released = dict(self.payload)
            released["stage"] = "released"
            released["released"] = utcnow()
            released["updated"] = released["released"]
            _write_fd(fd, released)
            self.payload = released
            fcntl.flock(fd, fcntl.LOCK_UN)
        finally:
            os.close(fd)
        if os.environ.get(self.env_key) == str(os.getpid()):
            del os.environ[self.env_key]


def acquire_or_join(
    root: Path,
    *,
    holder: str,
    chapter: int | None = None,
    stage: str | None = None,
    until: int | None = None,
    name: str = LOCK_NAME,
    blocking: bool = False,
) -> RunLock:
    env_key = lock_env_name(name)
    path = lock_path(root, name)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd = os.open(str(path), os.O_RDWR | os.O_CREAT | os.O_CLOEXEC, 0o644)
    try:
        fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        os.close(fd)
        existing = read_payload(path)
        holder_pid = existing.get("pid")
        if isinstance(holder_pid, int) and in_lock_family(holder_pid, env_key):
            os.environ[env_key] = str(holder_pid)
            lock = RunLock(root, owned=False, fd=None, payload=existing, name=name)
            lock.update(chapter=chapter, stage=stage, until=until)
            return lock
        if not blocking:
            raise SystemExit(conflict_message(path, existing, name)) from None
        fd = os.open(str(path), os.O_RDWR | os.O_CREAT | os.O_CLOEXEC, 0o644)
        fcntl.flock(fd, fcntl.LOCK_EX)

    started = utcnow()
    payload = {
        "pid": os.getpid(),
        "holder": holder,
        "chapter": chapter,
        "stage": stage or "starting",
        "until": until,
        "started": started,
        "updated": started,
    }
    _write_fd(fd, payload)
    os.environ[env_key] = str(os.getpid())
    return RunLock(root, owned=True, fd=fd, payload=payload, name=name)


@contextmanager
def hold_named_lock(
    root: Path,
    *,
    holder: str,
    name: str,
    chapter: int | None = None,
    stage: str | None = None,
    until: int | None = None,
    blocking: bool = False,
) -> Iterator[RunLock]:
    lock = acquire_or_join(
        root,
        holder=holder,
        chapter=chapter,
        stage=stage,
        until=until,
        name=name,
        blocking=blocking,
    )
    try:
        yield lock
    finally:
        lock.release()


@contextmanager
def hold_run_lock(
    root: Path,
    *,
    holder: str,
    chapter: int | None = None,
    stage: str | None = None,
    until: int | None = None,
) -> Iterator[RunLock]:
    with hold_named_lock(
        root, holder=holder, name=LOCK_NAME, chapter=chapter, stage=stage, until=until
    ) as lock:
        yield lock


@contextmanager
def hold_master_lock(
    root: Path,
    *,
    holder: str,
    chapter: int | None = None,
    stage: str | None = None,
    until: int | None = None,
) -> Iterator[RunLock]:
    with hold_named_lock(
        root, holder=holder, name=MASTER_LOCK_NAME, chapter=chapter, stage=stage, until=until
    ) as lock:
        yield lock


@contextmanager
def hold_commit_lock(
    root: Path,
    *,
    holder: str,
    chapter: int | None = None,
    stage: str | None = None,
) -> Iterator[RunLock]:
    with hold_named_lock(
        root,
        holder=holder,
        name=COMMIT_LOCK_NAME,
        chapter=chapter,
        stage=stage,
        blocking=True,
    ) as lock:
        yield lock


@contextmanager
def hold_audit_locks(
    root: Path,
    *,
    holder: str,
    chapter: int | None = None,
    stage: str | None = None,
) -> Iterator[tuple[RunLock, RunLock]]:
    with hold_run_lock(root, holder=holder, chapter=chapter, stage=stage) as run:
        with hold_master_lock(root, holder=holder, chapter=chapter, stage=stage) as master:
            yield run, master


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    any_lock = False
    for name, label in (
        (LOCK_NAME, "Run lock"),
        (MASTER_LOCK_NAME, "Master lock"),
        (COMMIT_LOCK_NAME, "Commit lock"),
    ):
        path = lock_path(root, name)
        payload = read_payload(path)
        if not payload and not path.exists():
            continue
        any_lock = True
        pid = payload.get("pid")
        live = isinstance(pid, int) and pid_is_alive(pid)
        print(f"{label} ({'live pid' if live else 'stale pid'}): {path}")
        print(format_payload(payload) or "  (empty)")
    if not any_lock:
        print("No run lock.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
