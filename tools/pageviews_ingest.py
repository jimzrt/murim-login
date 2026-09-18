#!/usr/bin/env python3
"""Tail Caddy JSON access logs and store Murim chapter pageviews in SQLite."""

from __future__ import annotations

import hashlib
import json
import os
import re
import sqlite3
import threading
import time
from pathlib import Path
from urllib.parse import urlparse

CHAPTER_RE = re.compile(r"^(?:/murim-login)?/chapter/(\d+)/?$")
HOME_RE = re.compile(r"^(?:/murim-login)?/?$")
BOT_RE = re.compile(
    r"(bot|crawler|spider|slurp|fetch|preview|scanner|scrapy|"
    r"bytespider|gptbot|claudebot|amazonbot|applebot|semrush|"
    r"ahrefs|mj12|petal|pingdom|uptimerobot|headless)",
    re.I,
)

SCHEMA = """
CREATE TABLE IF NOT EXISTS pageviews (
  id INTEGER PRIMARY KEY,
  ts TEXT NOT NULL,
  chapter INTEGER,
  path TEXT NOT NULL,
  status INTEGER NOT NULL,
  ip_hash TEXT,
  ua TEXT,
  referer TEXT,
  bytes INTEGER,
  duration_ms INTEGER
);
CREATE INDEX IF NOT EXISTS idx_pageviews_ts ON pageviews(ts);
CREATE INDEX IF NOT EXISTS idx_pageviews_chapter ON pageviews(chapter);
"""


def _env_path(name: str, default: str) -> Path:
    return Path(os.environ.get(name, default))


def log_path() -> Path:
    return _env_path("CADDY_LOG", "/var/log/caddy/murim.json")


def db_path() -> Path:
    return _env_path("PAGEVIEWS_DB", "/data/pageviews.db")


def state_path() -> Path:
    return _env_path("PAGEVIEWS_STATE", "/data/ingest-state.json")


def salt_path() -> Path:
    return _env_path("PAGEVIEWS_SALT_FILE", "/data/ip-salt")


def poll_seconds() -> float:
    return float(os.environ.get("PAGEVIEWS_POLL", "0.5"))


def ip_salt() -> str:
    env = os.environ.get("PAGEVIEWS_IP_SALT", "").strip()
    if env:
        return env
    path = salt_path()
    if path.is_file():
        return path.read_text(encoding="utf-8").strip()
    path.parent.mkdir(parents=True, exist_ok=True)
    salt = os.urandom(16).hex()
    path.write_text(salt, encoding="utf-8")
    return salt


def hash_ip(ip: str, salt: str) -> str | None:
    ip = (ip or "").strip()
    if not ip:
        return None
    return hashlib.sha256(f"{salt}:{ip}".encode()).hexdigest()[:32]


def header_first(headers: dict | None, *names: str) -> str:
    if not headers:
        return ""
    lowered = {str(key).lower(): value for key, value in headers.items()}
    for name in names:
        value = lowered.get(name.lower())
        if isinstance(value, list) and value:
            return str(value[0])
        if isinstance(value, str):
            return value
    return ""


def normalize_path(uri: str) -> str:
    path = urlparse(uri or "/").path or "/"
    if path != "/" and path.endswith("/"):
        path = path.rstrip("/") + "/"
    return path


def classify(path: str) -> int | None | False:
    match = CHAPTER_RE.match(path)
    if match:
        return int(match.group(1))
    if HOME_RE.match(path):
        return None
    return False


def iso_ts(value) -> str:
    try:
        return time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime(float(value))) + "Z"
    except (TypeError, ValueError, OverflowError):
        return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def parse_event(raw: dict, salt: str) -> tuple | None:
    request = raw.get("request") or {}
    method = str(request.get("method") or "").upper()
    status = int(raw.get("status") or 0)
    if method != "GET" or status not in {200, 304}:
        return None
    path = normalize_path(str(request.get("uri") or "/"))
    chapter = classify(path)
    if chapter is False:
        return None
    ua = header_first(request.get("headers"), "User-Agent")[:512]
    if not ua or BOT_RE.search(ua):
        return None
    duration = raw.get("duration")
    try:
        duration_ms = int(float(duration) * 1000) if duration is not None else None
    except (TypeError, ValueError):
        duration_ms = None
    ip = str(request.get("client_ip") or request.get("remote_ip") or "")
    size = raw.get("size")
    try:
        size = int(size) if size is not None else None
    except (TypeError, ValueError):
        size = None
    return (
        iso_ts(raw.get("ts")),
        chapter,
        path,
        status,
        hash_ip(ip, salt),
        ua or None,
        header_first(request.get("headers"), "Referer", "Referrer")[:512] or None,
        size,
        duration_ms,
    )


def connect() -> sqlite3.Connection:
    path = db_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.executescript(SCHEMA)
    return conn


def query_counts(chapters: list[int]) -> list[dict[str, int]]:
    unique = sorted({int(ch) for ch in chapters if int(ch) >= 0})
    if not unique:
        return []
    path = db_path()
    if not path.is_file():
        return [{"chapter": chapter, "count": 0} for chapter in unique]
    conn = sqlite3.connect(path)
    try:
        placeholders = ",".join("?" * len(unique))
        rows = conn.execute(
            f"""SELECT chapter, COUNT(DISTINCT ip_hash)
                FROM pageviews
                WHERE chapter IN ({placeholders}) AND ip_hash IS NOT NULL
                GROUP BY chapter""",
            unique,
        ).fetchall()
        counts = {int(row[0]): int(row[1]) for row in rows}
        return [{"chapter": chapter, "count": counts.get(chapter, 0)} for chapter in unique]
    finally:
        conn.close()


def load_state() -> dict:
    path = state_path()
    if not path.is_file():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def save_state(state: dict) -> None:
    path = state_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(state), encoding="utf-8")
    tmp.replace(path)


def open_log(state: dict):
    path = log_path()
    while not path.is_file():
        time.sleep(1)
    handle = path.open("rb")
    inode = path.stat().st_ino
    offset = int(state.get("offset") or 0)
    if state.get("inode") == inode:
        handle.seek(0, os.SEEK_END)
        size = handle.tell()
        handle.seek(min(offset, size))
    else:
        handle.seek(0)
    return handle, inode


def run() -> None:
    salt = ip_salt()
    conn = connect()
    state = load_state()
    handle, inode = open_log(state)
    print(f"pageviews: watching {log_path()} -> {db_path()}", flush=True)
    while True:
        path = log_path()
        try:
            current = path.stat()
        except FileNotFoundError:
            handle.close()
            time.sleep(1)
            handle, inode = open_log({})
            continue
        if current.st_ino != inode or current.st_size < handle.tell():
            handle.close()
            handle, inode = open_log({})
            continue
        chunk = handle.readline()
        if not chunk:
            time.sleep(poll_seconds())
            continue
        if not chunk.endswith(b"\n"):
            handle.seek(-len(chunk), os.SEEK_CUR)
            time.sleep(poll_seconds())
            continue
        line = chunk.decode("utf-8", "replace").strip()
        if not line:
            continue
        try:
            raw = json.loads(line)
        except json.JSONDecodeError:
            continue
        event = parse_event(raw, salt)
        if event:
            conn.execute(
                """INSERT INTO pageviews
                   (ts, chapter, path, status, ip_hash, ua, referer, bytes, duration_ms)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                event,
            )
            conn.commit()
        save_state({"inode": inode, "offset": handle.tell()})


def start_background() -> None:
    if os.environ.get("PAGEVIEWS_DISABLED", "").strip() in {"1", "true", "yes"}:
        return

    def loop() -> None:
        while True:
            try:
                run()
            except Exception as exc:
                print(f"pageviews: {exc!r}; retrying", flush=True)
                time.sleep(2)

    threading.Thread(target=loop, name="pageviews-ingest", daemon=True).start()


if __name__ == "__main__":
    run()
