"""GitHub App REST helper for line reports."""

from __future__ import annotations

import base64
import json
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Any

try:
    import jwt
except ImportError:  # pragma: no cover - installed in the report image
    jwt = None


class GitHubError(RuntimeError):
    def __init__(self, status: int, body: str):
        super().__init__(f"GitHub HTTP {status}: {body[:400]}")
        self.status = status
        self.body = body


class GitHubApp:
    def __init__(
        self,
        app_id: str,
        installation_id: str,
        pem: str,
        repo: str,
        user_agent: str = "murim-login-line-report",
    ):
        self.app_id = str(app_id)
        self.installation_id = str(installation_id)
        self.pem = pem
        self.repo = repo
        self.user_agent = user_agent
        self._token: str | None = None
        self._token_expires = 0.0

    def _app_jwt(self) -> str:
        if jwt is None:
            raise RuntimeError("PyJWT is required for GitHub App authentication")
        now = int(time.time())
        payload = {"iat": now - 60, "exp": now + 540, "iss": self.app_id}
        return jwt.encode(payload, self.pem, algorithm="RS256")

    def _installation_token(self) -> str:
        if self._token and time.time() < self._token_expires - 60:
            return self._token
        data = self._request(
            "POST",
            f"/app/installations/{self.installation_id}/access_tokens",
            token=self._app_jwt(),
        )
        self._token = data["token"]
        self._token_expires = time.time() + 3500
        return self._token

    def _request(
        self,
        method: str,
        path: str,
        payload: dict | None = None,
        token: str | None = None,
    ) -> Any:
        url = path if path.startswith("https://") else f"https://api.github.com{path}"
        body = None if payload is None else json.dumps(payload).encode("utf-8")
        headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token or self._installation_token()}",
            "User-Agent": self.user_agent,
            "X-GitHub-Api-Version": "2022-11-28",
        }
        if body is not None:
            headers["Content-Type"] = "application/json"
        request = urllib.request.Request(url, data=body, method=method, headers=headers)
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                raw_body = response.read()
                if not raw_body:
                    return {}
                return json.loads(raw_body.decode("utf-8"))
        except urllib.error.HTTPError as error:
            detail = error.read().decode("utf-8", "replace")
            raise GitHubError(error.code, detail) from None

    def graphql(self, query: str, variables: dict | None = None) -> dict:
        data = self._request(
            "POST",
            "https://api.github.com/graphql",
            {"query": query, "variables": variables or {}},
        )
        if data.get("errors"):
            raise GitHubError(200, json.dumps(data["errors"]))
        return data["data"]

    def create_issue(self, title: str, body: str, labels: list[str]) -> dict:
        try:
            return self._request(
                "POST",
                f"/repos/{self.repo}/issues",
                {"title": title, "body": body, "labels": labels},
            )
        except GitHubError as error:
            if error.status != 422:
                raise
            self.ensure_label(labels[0])
            return self._request(
                "POST",
                f"/repos/{self.repo}/issues",
                {"title": title, "body": body, "labels": labels},
            )

    def ensure_label(self, name: str) -> None:
        try:
            self._request("GET", f"/repos/{self.repo}/labels/{urllib.parse.quote(name)}")
        except GitHubError as error:
            if error.status != 404:
                raise
            self._request(
                "POST",
                f"/repos/{self.repo}/labels",
                {
                    "name": name,
                    "color": "6b4f2a",
                    "description": "Reader-reported translation line",
                },
            )

    def comment(self, issue: int, body: str) -> dict:
        return self._request(
            "POST",
            f"/repos/{self.repo}/issues/{issue}/comments",
            {"body": body},
        )

    def update_comment(self, comment_id: int, body: str) -> dict:
        return self._request(
            "PATCH",
            f"/repos/{self.repo}/issues/comments/{comment_id}",
            {"body": body},
        )

    def list_comments(self, issue: int) -> list[dict]:
        return self._request(
            "GET",
            f"/repos/{self.repo}/issues/{issue}/comments?per_page=100",
        )

    def list_issues(self, label: str, state: str = "open") -> list[dict]:
        quoted = urllib.parse.quote(label)
        issues: list[dict] = []
        for page in range(1, 11):
            batch = self._request(
                "GET",
                f"/repos/{self.repo}/issues?labels={quoted}&state={state}&per_page=100&page={page}",
            )
            if not isinstance(batch, list):
                break
            issues.extend(batch)
            if len(batch) < 100:
                break
        return issues

    def add_labels(self, issue: int, labels: list[str]) -> None:
        self._request("POST", f"/repos/{self.repo}/issues/{issue}/labels", {"labels": labels})

    def remove_label(self, issue: int, name: str) -> None:
        try:
            self._request(
                "DELETE",
                f"/repos/{self.repo}/issues/{issue}/labels/{urllib.parse.quote(name)}",
            )
        except GitHubError as error:
            if error.status != 404:
                raise

    def close_issue(self, issue: int) -> None:
        self._request("PATCH", f"/repos/{self.repo}/issues/{issue}", {"state": "closed"})

    def reopen_issue(self, issue: int) -> None:
        self._request("PATCH", f"/repos/{self.repo}/issues/{issue}", {"state": "open"})

    def get_issue(self, issue: int) -> dict:
        return self._request("GET", f"/repos/{self.repo}/issues/{issue}")

    def repository(self) -> dict:
        return self._request("GET", f"/repos/{self.repo}")

    def default_branch(self) -> str:
        return self.repository()["default_branch"]

    def get_ref_sha(self, branch: str) -> str:
        data = self._request("GET", f"/repos/{self.repo}/git/ref/heads/{urllib.parse.quote(branch)}")
        return data["object"]["sha"]

    def create_branch(self, name: str, sha: str) -> None:
        self._request(
            "POST",
            f"/repos/{self.repo}/git/refs",
            {"ref": f"refs/heads/{name}", "sha": sha},
        )

    def get_file(self, path: str, ref: str) -> tuple[str, str]:
        data = self._request(
            "GET",
            f"/repos/{self.repo}/contents/{urllib.parse.quote(path)}?ref={urllib.parse.quote(ref)}",
        )
        content = base64.b64decode(data["content"].replace("\n", "")).decode("utf-8")
        return content, data["sha"]

    def put_file(self, path: str, content: str, message: str, branch: str, sha: str) -> None:
        encoded = base64.b64encode(content.encode("utf-8")).decode("ascii")
        self._request(
            "PUT",
            f"/repos/{self.repo}/contents/{urllib.parse.quote(path)}",
            {
                "message": message,
                "content": encoded,
                "branch": branch,
                "sha": sha,
            },
        )

    def create_pull(
        self,
        title: str,
        head: str,
        base: str,
        body: str,
        issue_number: int,
        _issue_node_id: str = "",
    ) -> dict:
        repo = self.repository()
        try:
            data = self.graphql(
                """
                mutation($repositoryId: ID!, $base: String!, $head: String!, $title: String!, $body: String!, $issue: Int!) {
                  createPullRequest(input: {
                    repositoryId: $repositoryId
                    baseRefName: $base
                    headRefName: $head
                    title: $title
                    body: $body
                    closingIssueReferences: [{ issueNumber: $issue }]
                  }) {
                    pullRequest { number url node_id }
                  }
                }
                """,
                {
                    "repositoryId": repo["node_id"],
                    "base": base,
                    "head": head,
                    "title": title,
                    "body": body,
                    "issue": issue_number,
                },
            )
            pull = data["createPullRequest"]["pullRequest"]
            return {
                "number": pull["number"],
                "html_url": pull["url"],
                "node_id": pull["node_id"],
            }
        except (GitHubError, KeyError, TypeError):
            return self._request(
                "POST",
                f"/repos/{self.repo}/pulls",
                {"title": title, "head": head, "base": base, "body": body},
            )
