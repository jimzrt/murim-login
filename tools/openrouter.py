"""OpenRouter chat completions for the line-report worker."""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request

API_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_MODEL = "openai/gpt-5.6-sol"


def normalize_model(model: str) -> str:
    name = model.strip()
    if name.startswith("openrouter/"):
        name = name[len("openrouter/") :]
    if ":" in name:
        name = name.rsplit(":", 1)[0]
    return name


def complete(prompt: str, *, api_key: str | None = None, model: str | None = None, timeout: int = 180) -> str:
    key = (api_key or os.environ.get("OPENROUTER_API_KEY") or "").strip()
    if not key:
        raise RuntimeError("OPENROUTER_API_KEY is not set")
    selected = normalize_model(model or os.environ.get("MURIM_REPORT_MODEL") or DEFAULT_MODEL)
    payload = {
        "model": selected,
        "messages": [
            {
                "role": "system",
                "content": "Return exactly one JSON object. No Markdown fence, no extra prose.",
            },
            {"role": "user", "content": prompt},
        ],
        "response_format": {"type": "json_object"},
        "temperature": 0.2,
    }
    request = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        method="POST",
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://murim-login.com",
            "X-Title": "Murim Login line report",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        detail = error.read().decode("utf-8", "replace")
        raise RuntimeError(f"OpenRouter HTTP {error.code}: {detail[:400]}") from None
    try:
        content = data["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as error:
        raise RuntimeError(f"OpenRouter response missing message content: {data!r}"[:400]) from error
    if not isinstance(content, str) or not content.strip():
        raise RuntimeError("OpenRouter returned an empty message")
    return content
