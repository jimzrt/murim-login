#!/usr/bin/env python3
"""HTTP service: in-reader line reports and GitHub App webhooks."""

from __future__ import annotations

import hashlib
import hmac
import json
import os
import re
import subprocess
import threading
import time
import traceback
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

from tools.github_app import GitHubApp, GitHubError
from tools.pageviews_ingest import query_all_counts, query_counts, start_background as start_pageviews
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
CORS_POST_PATHS = {"/report-line", "/view-counts"}
MAX_VIEW_COUNT_CHAPTERS = 5000
STATUS_PENDING = "<!-- line-report-status pending -->"
STATUS_FAILED = "<!-- line-report-status failed -->"
RETRY_RE = re.compile(r"<!-- line-report-status retry (\d+) (\d+) -->")
RETRY_STATE_NAME = "line-report-retry.json"


def format_pending_comment(lead: str) -> str:
    return f"{lead}. This comment will be updated when the result is ready.\n\n{STATUS_PENDING}\n"


def format_retry_comment(error: str, retry_at: int, attempt: int) -> str:
    return (
        "The model is not available yet, so this report stays queued. "
        "This comment will be updated automatically when evaluation finishes.\n\n"
        f"```\n{error[:1500]}\n```\n\n"
        f"<!-- line-report-status retry {int(retry_at)} {int(attempt)} -->\n"
    )


def format_failed_comment(error: str) -> str:
    return (
        "Line report evaluation failed and will not be retried automatically.\n\n"
        f"```\n{error[:1500]}\n```\n\n"
        f"{STATUS_FAILED}\n"
    )


def retry_delay(attempt: int) -> float:
    return min(900.0, 60.0 * (2 ** max(0, attempt - 1)))


def comments_have_evaluation(comments: list[dict]) -> bool:
    return any("line-report-eval" in (comment.get("body") or "") for comment in comments)


def comments_have_failure(comments: list[dict]) -> bool:
    return any(STATUS_FAILED in (comment.get("body") or "") for comment in comments)


def status_comment(comments: list[dict]) -> dict | None:
    found = None
    for comment in comments:
        body = comment.get("body") or ""
        if "line-report-status" in body and "line-report-eval" not in body:
            found = comment
    return found


def retry_not_before(comments: list[dict]) -> int | None:
    latest = None
    for comment in comments:
        match = RETRY_RE.search(comment.get("body") or "")
        if match:
            latest = int(match.group(1))
    return latest


def git_ssh_env(ssh_key: Path | None) -> dict[str, str]:
    env = os.environ.copy()
    if ssh_key is None or not ssh_key.is_file():
        return env
    env["GIT_SSH_COMMAND"] = (
        f"ssh -i {ssh_key} -o IdentitiesOnly=yes -o StrictHostKeyChecking=accept-new"
    )
    return env


def sync_git(cwd: Path, ssh_key: Path | None = None) -> None:
    if not (cwd / ".git").exists():
        return
    env = git_ssh_env(ssh_key)
    subprocess.run(
        ["git", "fetch", "origin"],
        cwd=cwd,
        env=env,
        check=False,
        capture_output=True,
    )
    subprocess.run(
        ["git", "reset", "--hard", "origin/master"],
        cwd=cwd,
        env=env,
        check=False,
        capture_output=True,
    )


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
        self.retry_interval = float(env.get("REPORT_RETRY_INTERVAL") or "60")
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
        ssh_key = env.get("MURIM_SOURCE_SSH_KEY", "/run/secrets/source_deploy_key")
        self.source_ssh_key = Path(ssh_key) if ssh_key else None


class LineReportService:
    def __init__(self, settings: Settings, github: GitHubApp | None = None, evaluate=run_evaluation):
        self.settings = settings
        self.github = github
        self.evaluate = evaluate
        self.limiter = RateLimiter(settings.rate_limit, settings.rate_window)
        self._jobs = threading.Semaphore(2)
        self._inflight: set[int] = set()
        self._inflight_lock = threading.Lock()
        self._retry_lock = threading.Lock()
        self._retry_state = self._read_retry_state()

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
        if self.github and comments_have_evaluation(self.github.list_comments(number)):
            return
        self._schedule_evaluation(issue, respect_backoff=False)

    def _schedule_evaluation(self, issue: dict, *, respect_backoff: bool, comments: list[dict] | None = None) -> None:
        number = int(issue["number"])
        if not self._try_reserve(number):
            return
        try:
            if comments is None and self.github:
                comments = self.github.list_comments(number)
            if respect_backoff and not self._retry_due(number, comments or []):
                self._release(number)
                return
            comment_id = self._begin_status(number, "Evaluating this report") if self.github else None
        except (Exception, SystemExit) as error:
            self._release(number)
            print(f"line-report #{number} could not start: {error}", flush=True)
            return
        self._spawn(self._evaluate_issue, (issue, comment_id, True))

    def _evaluate_issue(self, issue: dict, comment_id: int | None = None, reserved: bool = False) -> None:
        number = int(issue["number"])
        if not reserved and not self._try_reserve(number):
            return
        try:
            if self.github and comment_id is None:
                comment_id = self._begin_status(number, "Evaluating this report")
            with self._jobs:
                try:
                    parsed = parse_issue_body(issue.get("body") or "")
                except ValueError as error:
                    self._publish(number, comment_id, format_failed_comment(str(error)))
                    self._clear_retry(number)
                    return
                try:
                    self._sync_repo()
                    evaluation = self.evaluate(
                        parsed["chapter"],
                        parsed["quote"],
                        parsed["note"],
                        self.settings.root,
                    )
                    self._publish(number, comment_id, format_evaluation_comment(evaluation))
                    self._clear_retry(number)
                    self._after_evaluation(number, evaluation)
                except (Exception, SystemExit) as error:
                    self._fail_retryable(number, comment_id, "evaluate", error)
        finally:
            self._release(number)

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
            self._spawn(self._reopen_issue, (issue, body))
            return
        if parse_revise_command(body) is None:
            return
        self._spawn(self._revise_issue, (issue, body))

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
        if not self.github:
            return
        self._reopen_reserved(issue, body)

    def _reopen_reserved(self, issue: dict, body: str) -> None:
        number = int(issue["number"])
        comment_id = self._begin_status(number, "Reopening this report and preparing strategies")
        with self._jobs:
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
                self._publish(number, comment_id, format_evaluation_comment(evaluation))
                self._clear_retry(number)
                if not evaluation["plausible"]:
                    self.github.comment(
                        number,
                        "Forced evaluation still returned no strategies. Try `/reopen` with a more specific note.",
                    )
            except ValueError as error:
                self._publish(number, comment_id, format_failed_comment(str(error)))
                self._clear_retry(number)
            except (Exception, SystemExit) as error:
                self._fail_retryable(number, comment_id, "reopen", error, command=body)

    def _revise_issue(self, issue: dict, body: str) -> None:
        if not self.github:
            return
        self._revise_reserved(issue, body)

    def _revise_reserved(self, issue: dict, body: str) -> None:
        number = int(issue["number"])
        feedback = parse_revise_command(body) or ""
        if not feedback:
            self.github.comment(
                number,
                "Add what you want changed after `/revise`, for example:\n\n"
                "`/revise keep the meaning but drop \"hot breath\"; more idiomatic English`",
            )
            return
        comment_id = self._begin_status(number, "Revising strategies for this report")
        with self._jobs:
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
                self._publish(number, comment_id, format_evaluation_comment(evaluation))
                self._clear_retry(number)
                self._after_evaluation(number, evaluation)
            except ValueError as error:
                self._publish(number, comment_id, format_failed_comment(str(error)))
                self._clear_retry(number)
            except (Exception, SystemExit) as error:
                self._fail_retryable(number, comment_id, "revise", error, command=body)

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
        sync_git(self.settings.root)
        sync_git(self.settings.root / "source", ssh_key=self.settings.source_ssh_key)

    def _spawn(self, target, args: tuple) -> None:
        threading.Thread(target=target, args=args, daemon=True).start()

    def _try_reserve(self, number: int) -> bool:
        with self._inflight_lock:
            if number in self._inflight:
                return False
            self._inflight.add(number)
            return True

    def _release(self, number: int) -> None:
        with self._inflight_lock:
            self._inflight.discard(number)

    def _retry_path(self) -> Path:
        return self.settings.root / ".work" / RETRY_STATE_NAME

    def _read_retry_state(self) -> dict:
        path = self._retry_path()
        if not path.is_file():
            return {}
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return {}
        return data if isinstance(data, dict) else {}

    def _write_retry_state(self) -> None:
        path = self._retry_path()
        path.parent.mkdir(parents=True, exist_ok=True)
        temporary = path.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(self._retry_state, indent=2), encoding="utf-8")
        temporary.replace(path)

    def _clear_retry(self, number: int) -> None:
        with self._retry_lock:
            if self._retry_state.pop(str(number), None) is not None:
                self._write_retry_state()

    def _retry_due(self, number: int, comments: list[dict]) -> bool:
        now = time.time()
        with self._retry_lock:
            entry = self._retry_state.get(str(number))
        if entry and now < float(entry.get("retry_at") or 0):
            if self.github:
                current = status_comment(comments)
                if current and STATUS_PENDING in (current.get("body") or ""):
                    self._publish(
                        number,
                        int(current["id"]),
                        format_retry_comment(
                            str(entry.get("error") or "model unavailable"),
                            int(entry["retry_at"]),
                            int(entry.get("attempt") or 1),
                        ),
                    )
            return False
        if entry:
            return True
        marker = retry_not_before(comments)
        return marker is None or now >= marker

    def _begin_status(self, number: int, lead: str) -> int:
        comments = self.github.list_comments(number)
        body = format_pending_comment(lead)
        existing = status_comment(comments)
        if existing:
            self.github.update_comment(int(existing["id"]), body)
            return int(existing["id"])
        created = self.github.comment(number, body)
        return int(created["id"])

    def _publish(self, number: int, comment_id: int | None, body: str) -> None:
        if not self.github:
            return
        if comment_id is None:
            self.github.comment(number, body)
            return
        try:
            self.github.update_comment(comment_id, body)
        except Exception:
            self.github.comment(number, body)

    def _fail_retryable(
        self,
        number: int,
        comment_id: int | None,
        kind: str,
        error: BaseException,
        command: str = "",
    ) -> None:
        text = str(error).strip() or error.__class__.__name__
        with self._retry_lock:
            previous = dict(self._retry_state.get(str(number)) or {})
            attempt = int(previous.get("attempt") or 0) + 1
            retry_at = time.time() + retry_delay(attempt)
            self._retry_state[str(number)] = {
                "kind": kind,
                "attempt": attempt,
                "retry_at": retry_at,
                "command": command,
                "error": text[:500],
            }
            self._write_retry_state()
        print(
            f"line-report #{number} {kind} failed (attempt {attempt}); "
            f"retry in {retry_delay(attempt):.0f}s: {text}",
            flush=True,
        )
        self._publish(number, comment_id, format_retry_comment(text, int(retry_at), attempt))

    def _retry_followup(self, number: int, kind: str, issue: dict, command: str) -> None:
        if not self._try_reserve(number):
            return
        try:
            if kind == "reopen":
                self._reopen_reserved(issue, command)
            else:
                self._revise_reserved(issue, command)
        finally:
            self._release(number)

    def sweep_open_reports(self) -> None:
        if not self.github:
            return
        for issue in self.github.list_issues(LABEL):
            if not isinstance(issue, dict) or issue.get("pull_request"):
                continue
            if not _has_label(issue, LABEL):
                continue
            number = int(issue["number"])
            try:
                comments = self.github.list_comments(number)
            except Exception as error:
                print(f"line-report #{number} sweep skipped: {error}", flush=True)
                continue
            if not isinstance(comments, list):
                continue
            with self._retry_lock:
                entry = dict(self._retry_state.get(str(number)) or {})
            kind = entry.get("kind")
            if kind in {"revise", "reopen"}:
                if not self._retry_due(number, comments):
                    continue
                command = str(entry.get("command") or "")
                self._spawn(self._retry_followup, (number, kind, issue, command))
                continue
            if comments_have_evaluation(comments) or comments_have_failure(comments):
                continue
            self._schedule_evaluation(issue, respect_backoff=True, comments=comments)

    def serve_retry_loop(self) -> None:
        while True:
            try:
                self.sweep_open_reports()
            except Exception:
                traceback.print_exc()
            time.sleep(self.settings.retry_interval)


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


def parse_chapter_list(raw: bytes) -> list[int] | None:
    try:
        payload = json.loads(raw.decode("utf-8") or "[]")
    except json.JSONDecodeError:
        return None
    if not isinstance(payload, list):
        return None
    chapters: list[int] = []
    for item in payload:
        try:
            chapter = int(item)
        except (TypeError, ValueError):
            return None
        if chapter < 0:
            return None
        chapters.append(chapter)
    if len(chapters) > MAX_VIEW_COUNT_CHAPTERS:
        return None
    return chapters


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
                self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
                self.send_header("Vary", "Origin")
            self.end_headers()
            self.wfile.write(body)

        def do_OPTIONS(self) -> None:
            origin = self._cors()
            if self.path.rstrip("/") not in CORS_POST_PATHS:
                self._write(404, {"error": "not found"})
                return
            self._write(204, b"", origin=origin, content_type="text/plain")

        def do_GET(self) -> None:
            path = self.path.rstrip("/")
            if path in {"/health", "/report-line"}:
                self._write(200, {"ok": True})
                return
            if path == "/view-counts":
                origin = self._cors()
                self._write(200, query_all_counts(), origin=origin)
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
            if path == "/view-counts":
                origin = self._cors()
                chapters = parse_chapter_list(raw)
                if chapters is None:
                    self._write(400, {"error": "expected JSON array of chapter numbers"}, origin=origin)
                    return
                self._write(200, query_counts(chapters), origin=origin)
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
    if settings.retry_interval > 0:
        threading.Thread(target=service.serve_retry_loop, daemon=True).start()
    start_pageviews()
    server = ThreadingHTTPServer((settings.host, settings.port), make_handler(service))
    print(f"line-report listening on {settings.host}:{settings.port}", flush=True)
    server.serve_forever()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
