#!/usr/bin/env python3
"""HTTP service: in-reader line reports and GitHub App webhooks."""

from __future__ import annotations

import hashlib
import hmac
import json
import os
import subprocess
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

from tools.github_app import GitHubApp, GitHubError
from tools.line_report import (
    LABEL,
    NOTE_MAX,
    QUOTE_MAX,
    ROOT,
    apply_patches,
    cheap_gates,
    format_evaluation_comment,
    format_issue_body,
    normalize_note,
    normalize_quote,
    parse_apply_command,
    parse_evaluation_comment,
    parse_issue_body,
    parse_reopen_command,
    parse_revise_command,
    run_evaluation,
)

ISSUE_MARKER = "<!-- line-report-issue {n} -->"
BRANCH_RE_PREFIX = "report-line-"


class RateLimiter:
    def __init__(self, limit: int, window: float):
        self.limit = limit
        self.window = window
        self._hits: dict[str, list[float]] = {}
        self._lock = threading.Lock()

    def allow(self, key: str) -> bool:
        now = time.time()
        with self._lock:
            stamps = [stamp for stamp in self._hits.get(key, []) if now - stamp < self.window]
            if len(stamps) >= self.limit:
                self._hits[key] = stamps
                return False
            stamps.append(now)
            self._hits[key] = stamps
            return True


class Settings:
    def __init__(self, env: dict[str, str] | None = None):
        env = env or os.environ
        self.root = Path(env.get("MURIM_ROOT") or ROOT)
        self.host = env.get("REPORT_HOST", "0.0.0.0")
        self.port = int(env.get("REPORT_PORT") or "8080")
        self.repo = env.get("GITHUB_REPO", "jimzrt/murim-login")
        self.app_id = env.get("GITHUB_APP_ID", "")
        self.installation_id = env.get("GITHUB_APP_INSTALLATION_ID", "")
        self.webhook_secret = env.get("GITHUB_WEBHOOK_SECRET", "")
        self.apply_users = {
            name.strip()
            for name in env.get("GITHUB_APPLY_USERS", "jimzrt").split(",")
            if name.strip()
        }
        self.rate_limit = int(env.get("REPORT_LINE_RATE") or "10")
        self.rate_window = float(env.get("REPORT_LINE_WINDOW") or "3600")
        pem = env.get("GITHUB_APP_PEM", "")
        pem_file = env.get("GITHUB_APP_PEM_FILE", "")
        if pem_file:
            path = Path(pem_file)
            if path.is_file():
                pem = path.read_text(encoding="utf-8")
        self.pem = pem.replace("\\n", "\n")
        self.allowed_origins = {
            origin.strip()
            for origin in env.get(
                "REPORT_CORS_ORIGINS",
                "https://murim-login.com,https://www.murim-login.com,http://localhost:4321,http://127.0.0.1:4321",
            ).split(",")
            if origin.strip()
        }


class LineReportService:
    def __init__(self, settings: Settings, github: GitHubApp | None = None, evaluate=run_evaluation):
        self.settings = settings
        self.github = github
        self.evaluate = evaluate
        self.limiter = RateLimiter(settings.rate_limit, settings.rate_window)
        self._jobs = threading.Semaphore(2)

    def create_report(self, payload: dict, ip: str) -> tuple[int, dict]:
        if not self.limiter.allow(ip or "unknown"):
            return 429, {"error": "Too many reports from this address. Try later."}
        try:
            chapter = int(payload.get("chapter"))
        except (TypeError, ValueError):
            return 400, {"error": "Chapter must be a number."}
        quote = normalize_quote(str(payload.get("quote") or ""))
        note = normalize_note(str(payload.get("note") or ""))
        url = str(payload.get("url") or "").strip()
        if not quote:
            return 400, {"error": "Select a passage in the chapter first."}
        if len(str(payload.get("quote") or "")) > QUOTE_MAX + 200:
            return 400, {"error": "Selection is too long."}
        if len(str(payload.get("note") or "")) > NOTE_MAX + 200:
            return 400, {"error": "Note is too long."}
        if not self.github:
            return 503, {"error": "Line reports are not configured yet."}
        gate = cheap_gates(chapter, quote, self.settings.root)
        if gate and (
            "not found exactly" in gate.lower()
            or "not been mastered" in gate.lower()
        ):
            self._sync_repo()
            gate = cheap_gates(chapter, quote, self.settings.root)
        if gate:
            return 400, {"error": gate}
        body = format_issue_body(chapter, quote, note, url)
        issue = self.github.create_issue(
            f"Chapter {chapter}: report line",
            body,
            [LABEL],
        )
        return 201, {
            "number": issue["number"],
            "url": issue.get("html_url") or issue.get("url"),
        }

    def handle_webhook(self, event: str, payload: dict) -> None:
        if event == "issues" and payload.get("action") == "opened":
            self._on_issue_opened(payload)
        elif event == "issue_comment" and payload.get("action") == "created":
            self._on_comment(payload)
        elif event == "pull_request" and payload.get("action") == "closed":
            self._on_pull_closed(payload)

    def _on_issue_opened(self, payload: dict) -> None:
        issue = payload.get("issue") or {}
        if not _has_label(issue, LABEL):
            return
        number = int(issue["number"])
        if self.github and any(
            "line-report-eval" in (comment.get("body") or "")
            for comment in self.github.list_comments(number)
        ):
            return
        threading.Thread(target=self._evaluate_issue, args=(issue,), daemon=True).start()

    def _evaluate_issue(self, issue: dict) -> None:
        with self._jobs:
            number = int(issue["number"])
            try:
                parsed = parse_issue_body(issue.get("body") or "")
                self._sync_repo()
                evaluation = self.evaluate(
                    parsed["chapter"],
                    parsed["quote"],
                    parsed["note"],
                    self.settings.root,
                )
                comment = format_evaluation_comment(evaluation)
                if self.github:
                    self.github.comment(number, comment)
                    self._after_evaluation(number, evaluation)
            except Exception as error:
                if self.github:
                    self.github.comment(
                        number,
                        f"Line report evaluation failed:\n\n```\n{error}\n```",
                    )

    def _on_comment(self, payload: dict) -> None:
        comment = payload.get("comment") or {}
        issue = payload.get("issue") or {}
        sender = ((payload.get("sender") or {}).get("login") or "")
        if comment.get("user", {}).get("type") == "Bot":
            return
        if sender not in self.settings.apply_users:
            return
        if not _has_label(issue, LABEL):
            return
        body = comment.get("body") or ""
        strategy = parse_apply_command(body)
        if strategy:
            threading.Thread(
                target=self._apply_strategy,
                args=(int(issue["number"]), strategy, issue),
                daemon=True,
            ).start()
            return
        if parse_reopen_command(body) is not None:
            threading.Thread(
                target=self._reopen_issue,
                args=(issue, body),
                daemon=True,
            ).start()
            return
        if parse_revise_command(body) is None:
            return
        threading.Thread(
            target=self._revise_issue,
            args=(issue, body),
            daemon=True,
        ).start()

    def _latest_evaluation(self, issue_number: int) -> dict | None:
        if not self.github:
            return None
        for comment in reversed(self.github.list_comments(issue_number)):
            try:
                return parse_evaluation_comment(comment.get("body") or "")
            except ValueError:
                continue
        return None

    def _after_evaluation(self, number: int, evaluation: dict) -> None:
        if not self.github:
            return
        if evaluation["plausible"]:
            self.github.remove_label(number, "implausible")
            return
        self.github.add_labels(number, ["implausible"])
        self.github.close_issue(number)

    def _run_evaluate(self, chapter: int, quote: str, note: str, **kwargs):
        try:
            return self.evaluate(chapter, quote, note, self.settings.root, **kwargs)
        except TypeError:
            extra = kwargs.get("revise_note") or ""
            combined = note
            if extra:
                combined = f"{note}\nMaintainer revision: {extra}".strip() if note else extra
            return self.evaluate(chapter, quote, combined, self.settings.root)

    def _reopen_issue(self, issue: dict, body: str) -> None:
        with self._jobs:
            number = int(issue["number"])
            if not self.github:
                return
            feedback = parse_reopen_command(body) or ""
            try:
                self.github.reopen_issue(number)
                self.github.remove_label(number, "implausible")
                parsed = parse_issue_body(issue.get("body") or "")
                previous = self._latest_evaluation(number)
                self._sync_repo()
                evaluation = self._run_evaluate(
                    parsed["chapter"],
                    parsed["quote"],
                    parsed["note"],
                    previous=previous,
                    revise_note=feedback,
                    force=True,
                )
                self.github.comment(number, format_evaluation_comment(evaluation))
                if not evaluation["plausible"]:
                    self.github.comment(
                        number,
                        "Forced evaluation still returned no strategies. Try `/reopen` with a more specific note.",
                    )
            except Exception as error:
                self.github.comment(
                    number,
                    f"Could not reopen:\n\n```\n{error}\n```",
                )

    def _revise_issue(self, issue: dict, body: str) -> None:
        with self._jobs:
            number = int(issue["number"])
            if not self.github:
                return
            feedback = parse_revise_command(body) or ""
            if not feedback:
                self.github.comment(
                    number,
                    "Add what you want changed after `/revise`, for example:\n\n"
                    "`/revise keep the meaning but drop \"hot breath\"; more idiomatic English`",
                )
                return
            try:
                parsed = parse_issue_body(issue.get("body") or "")
                previous = self._latest_evaluation(number)
                self._sync_repo()
                try:
                    evaluation = self.evaluate(
                        parsed["chapter"],
                        parsed["quote"],
                        parsed["note"],
                        self.settings.root,
                        previous=previous,
                        revise_note=feedback,
                    )
                except TypeError:
                    combined = parsed["note"]
                    extra = f"Maintainer revision: {feedback}"
                    combined = f"{combined}\n{extra}".strip() if combined else extra
                    evaluation = self.evaluate(
                        parsed["chapter"],
                        parsed["quote"],
                        combined,
                        self.settings.root,
                    )
                self.github.comment(number, format_evaluation_comment(evaluation))
                self._after_evaluation(number, evaluation)
            except Exception as error:
                self.github.comment(
                    number,
                    f"Could not revise strategies:\n\n```\n{error}\n```",
                )

    def _apply_strategy(self, issue_number: int, strategy_id: str, issue: dict) -> None:
        with self._jobs:
            if not self.github:
                return
            try:
                evaluation = None
                for comment in reversed(self.github.list_comments(issue_number)):
                    try:
                        evaluation = parse_evaluation_comment(comment.get("body") or "")
                        break
                    except ValueError:
                        continue
                if evaluation is None:
                    self.github.comment(issue_number, "No stored evaluation to apply.")
                    return
                if not evaluation["plausible"]:
                    self.github.comment(issue_number, "This report was not plausible.")
                    return
                strategy = next((item for item in evaluation["strategies"] if item["id"] == strategy_id), None)
                if strategy is None:
                    self.github.comment(issue_number, f"Unknown strategy `{strategy_id}`.")
                    return
                base = self.github.default_branch()
                sha = self.github.get_ref_sha(base)
                branch = f"{BRANCH_RE_PREFIX}{issue_number}-{strategy_id}"
                try:
                    self.github.create_branch(branch, sha)
                except GitHubError as error:
                    if error.status != 422:
                        raise
                files: dict[str, str] = {}
                shas: dict[str, str] = {}
                for patch in strategy["patches"]:
                    path = patch["path"]
                    if path not in files:
                        content, blob = self.github.get_file(path, branch)
                        files[path] = content
                        shas[path] = blob
                updated = apply_patches(files, strategy["patches"])
                for path, content in updated.items():
                    if content == files[path]:
                        continue
                    self.github.put_file(
                        path,
                        content,
                        f"Apply line report #{issue_number} strategy {strategy_id}",
                        branch,
                        shas[path],
                    )
                    files[path] = content
                    _, shas[path] = self.github.get_file(path, branch)
                body = (
                    f"{ISSUE_MARKER.format(n=issue_number)}\n\n"
                    f"Applies strategy **{strategy_id}** ({strategy['label']}) "
                    f"from line report #{issue_number}."
                )
                chapter = parse_issue_body(issue.get("body") or "")["chapter"]
                node_id = issue.get("node_id") or self.github.get_issue(issue_number)["node_id"]
                pull = self.github.create_pull(
                    f"Report line: chapter {chapter} ({strategy_id})",
                    branch,
                    base,
                    body,
                    issue_number,
                    node_id,
                )
                url = pull.get("html_url") or pull.get("url")
                self.github.comment(issue_number, f"Opened pull request: {url}")
            except Exception as error:
                self.github.comment(issue_number, f"Could not apply `{strategy_id}`:\n\n```\n{error}\n```")

    def _on_pull_closed(self, payload: dict) -> None:
        pull = payload.get("pull_request") or {}
        if not pull.get("merged"):
            return
        issue_number = _issue_from_pull(pull)
        if issue_number is None or not self.github:
            return
        issue = self.github.get_issue(issue_number)
        if issue.get("state") != "closed":
            self.github.close_issue(issue_number)

    def _sync_repo(self) -> None:
        git_dir = self.settings.root / ".git"
        if not git_dir.exists():
            return
        subprocess.run(
            ["git", "fetch", "origin"],
            cwd=self.settings.root,
            check=False,
            capture_output=True,
        )
        subprocess.run(
            ["git", "reset", "--hard", "origin/master"],
            cwd=self.settings.root,
            check=False,
            capture_output=True,
        )


def _has_label(issue: dict, name: str) -> bool:
    labels = issue.get("labels") or []
    for label in labels:
        if isinstance(label, str) and label == name:
            return True
        if isinstance(label, dict) and label.get("name") == name:
            return True
    return False


def _issue_from_pull(pull: dict) -> int | None:
    head = ((pull.get("head") or {}).get("ref") or "")
    prefix = BRANCH_RE_PREFIX
    if head.startswith(prefix):
        rest = head[len(prefix):]
        number = rest.split("-", 1)[0]
        if number.isdigit():
            return int(number)
    body = pull.get("body") or ""
    marker = "line-report-issue "
    start = body.find(marker)
    if start >= 0:
        digits = []
        for char in body[start + len(marker):]:
            if char.isdigit():
                digits.append(char)
            else:
                break
        if digits:
            return int("".join(digits))
    return None


def verify_signature(secret: str, payload: bytes, header: str) -> bool:
    if not secret or not header.startswith("sha256="):
        return False
    expected = "sha256=" + hmac.new(secret.encode("utf-8"), payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, header)


def _client_ip(handler: BaseHTTPRequestHandler) -> str:
    forwarded = handler.headers.get("X-Forwarded-For", "")
    if forwarded:
        return forwarded.split(",")[0].strip()
    return handler.client_address[0]


def make_handler(service: LineReportService):
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, format: str, *args) -> None:
            return

        def _cors(self) -> str | None:
            origin = self.headers.get("Origin", "")
            if origin in service.settings.allowed_origins:
                return origin
            parsed = urlparse(origin)
            if parsed.hostname in {"localhost", "127.0.0.1"}:
                return origin
            return None

        def _write(self, status: int, payload: dict | str, origin: str | None = None, content_type: str = "application/json") -> None:
            body = payload if isinstance(payload, bytes) else (
                payload.encode("utf-8") if isinstance(payload, str) else json.dumps(payload).encode("utf-8")
            )
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(body)))
            if origin:
                self.send_header("Access-Control-Allow-Origin", origin)
                self.send_header("Access-Control-Allow-Headers", "Content-Type")
                self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
                self.send_header("Vary", "Origin")
            self.end_headers()
            self.wfile.write(body)

        def do_OPTIONS(self) -> None:
            origin = self._cors()
            if self.path.rstrip("/") != "/report-line":
                self._write(404, {"error": "not found"})
                return
            self._write(204, b"", origin=origin, content_type="text/plain")

        def do_GET(self) -> None:
            if self.path.rstrip("/") in {"/health", "/report-line"}:
                self._write(200, {"ok": True})
                return
            self._write(404, {"error": "not found"})

        def do_POST(self) -> None:
            length = int(self.headers.get("Content-Length") or "0")
            if length > 200_000:
                self._write(413, {"error": "payload too large"})
                return
            raw = self.rfile.read(length) if length else b""
            path = self.path.rstrip("/")
            if path == "/report-line":
                origin = self._cors()
                try:
                    payload = json.loads(raw.decode("utf-8") or "{}")
                except json.JSONDecodeError:
                    self._write(400, {"error": "invalid JSON"}, origin=origin)
                    return
                if not isinstance(payload, dict):
                    self._write(400, {"error": "invalid JSON"}, origin=origin)
                    return
                status, body = service.create_report(payload, _client_ip(self))
                self._write(status, body, origin=origin)
                return
            if path == "/github-hooks/murim-login":
                signature = self.headers.get("X-Hub-Signature-256", "")
                if not verify_signature(service.settings.webhook_secret, raw, signature):
                    self._write(401, {"error": "invalid signature"})
                    return
                event = self.headers.get("X-GitHub-Event", "")
                if event == "ping":
                    self._write(204, b"", content_type="text/plain")
                    return
                try:
                    payload = json.loads(raw.decode("utf-8") or "{}")
                except json.JSONDecodeError:
                    self._write(400, {"error": "invalid JSON"})
                    return
                threading.Thread(target=service.handle_webhook, args=(event, payload), daemon=True).start()
                self._write(204, b"", content_type="text/plain")
                return
            self._write(404, {"error": "not found"})

    return Handler


def main() -> int:
    settings = Settings()
    github = None
    if settings.app_id and settings.installation_id and settings.pem:
        github = GitHubApp(settings.app_id, settings.installation_id, settings.pem, settings.repo)
    service = LineReportService(settings, github)
    server = ThreadingHTTPServer((settings.host, settings.port), make_handler(service))
    print(f"line-report listening on {settings.host}:{settings.port}", flush=True)
    server.serve_forever()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
