#!/usr/bin/env python3
"""Rich progress output for chapter and mastering runs."""

from __future__ import annotations

import re
import sys
import time
from typing import Iterable

try:
    from rich.console import Console, Group
    from rich.live import Live
    from rich.spinner import Spinner
    from rich.text import Text
except ImportError:  # pragma: no cover - rich is expected, but keep a soft path
    Console = None  # type: ignore[misc, assignment]
    Group = None  # type: ignore[misc, assignment]
    Live = None  # type: ignore[misc, assignment]
    Spinner = None  # type: ignore[misc, assignment]
    Text = None  # type: ignore[misc, assignment]


STAGE_NOTES = {
    "prepare": "Assemble the bounded draft packet from source, rules, glossary, and profiles",
    "draft": "Translate the Korean chapter into English Markdown",
    "review": "Structured fidelity review with exact replacement spans",
    "revise": "Apply review replacements and re-run deterministic QA",
    "update": "Generate names, profiles, CONTEXT, STATE, and chapter beats",
    "summarize": "Write the block summary for the completed interval",
    "checkpoint": "Block-wide checkpoint review across recent chapters",
    "accept": "Promote the revised reading copy into translations/",
    "master": "Full-copy Sol master edit against the Korean source",
    "adjudicate": "Choose SOL / BASE / REPAIR for each changed paragraph",
    "assemble": "Rebuild the chapter from adjudication decisions",
    "fidelity": "Semantic fidelity gate against source and baseline",
    "verify": "Final deterministic QA after mastery",
    "retry": "Bounded mastering retry after QA failure",
    "promote": "Overwrite translations/ with the verified mastered copy",
    "commit": "Checkpoint chapter artifacts in Git",
}

WORD_RE = re.compile(r"[A-Za-z0-9]+(?:'[A-Za-z]+)?")


def format_elapsed(seconds: float) -> str:
    total = max(0, int(round(seconds)))
    hours, rem = divmod(total, 3600)
    minutes, secs = divmod(rem, 60)
    if hours:
        return f"{hours}h{minutes:02d}m{secs:02d}s"
    if minutes:
        return f"{minutes}m{secs:02d}s"
    return f"{secs}s"


def compact_n(value: int | float) -> str:
    number = float(value)
    abs_value = abs(number)
    if abs_value >= 10000:
        return f"{number / 1000:.1f}k"
    if abs_value >= 1000:
        return f"{int(round(number)):,}"
    if isinstance(value, float) and not value.is_integer():
        return f"{number:.1f}"
    return str(int(round(number)))


def short_model(selector: str) -> str:
    name = selector.split("/")[-1].split(":")[0].lower()
    for key in ("luna", "sol", "grok", "deepseek"):
        if key in name:
            return key
    return name or selector


def qa_brief(qa: dict) -> str:
    warnings = len(qa.get("warnings") or [])
    errors = len(qa.get("errors") or [])
    if qa.get("passed"):
        return "QA PASS" + (f" · {warnings}w" if warnings else "")
    return f"QA FAIL · {errors}e · {warnings}w"


def word_count(text: str) -> int:
    return len(WORD_RE.findall(text))


def length_ratio(source: str, english: str) -> float:
    return len(english) / max(1, len(source))


def copy_facts(source: str, english: str, *, glossary: int | None = None) -> list[str]:
    facts = [f"{compact_n(word_count(english))} words", f"×{length_ratio(source, english):.2f}"]
    if glossary is not None:
        facts.append(f"{glossary} glossary")
    return facts


def findings_facts(review: dict) -> list[str]:
    findings = review.get("findings") or []
    if not findings:
        return ["0 findings"]
    counts = {"critical": 0, "major": 0, "minor": 0}
    for item in findings:
        severity = str(item.get("severity") or "minor")
        counts[severity] = counts.get(severity, 0) + 1
    bits = [f"{len(findings)} findings"]
    for key in ("critical", "major", "minor"):
        if counts.get(key):
            bits.append(f"{counts[key]} {key}")
    return bits


def changed_file_facts(paths: Iterable[object], root=None) -> list[str]:
    names: list[str] = []
    kinds = {"names": 0, "address": 0, "context": 0, "state": 0, "beats": 0, "profiles": 0, "other": 0}
    for path in paths:
        text = str(path)
        if root is not None:
            try:
                text = str(path.relative_to(root))  # type: ignore[union-attr]
            except Exception:
                text = str(path)
        lower = text.lower()
        if lower.endswith("names.md"):
            kinds["names"] += 1
        elif lower.endswith("address.md"):
            kinds["address"] += 1
        elif lower.endswith("context.json"):
            kinds["context"] += 1
        elif lower.endswith("state.md"):
            kinds["state"] += 1
        elif "/beats/" in lower or lower.startswith("summaries/beats/"):
            kinds["beats"] += 1
        elif lower.startswith("characters/") or "/characters/" in lower:
            kinds["profiles"] += 1
            names.append(text.rsplit("/", 1)[-1].removesuffix(".md"))
        else:
            kinds["other"] += 1
    bits = [f"{sum(kinds.values())} files"]
    for key, label in (
        ("names", "names"),
        ("address", "address"),
        ("context", "context"),
        ("state", "state"),
        ("beats", "beat"),
        ("profiles", "profiles"),
    ):
        if kinds[key]:
            bits.append(f"{kinds[key]} {label}")
    if names:
        shown = ", ".join(names[:3])
        if len(names) > 3:
            shown += f" +{len(names) - 3}"
        bits.append(shown)
    return bits


def metrics_facts(metrics: dict | None) -> list[str]:
    if not metrics:
        return []
    bits: list[str] = []
    for key, label in (
        ("output_tokens", "out"),
        ("reasoning_tokens", "think"),
        ("cache_read_tokens", "cache"),
    ):
        value = metrics.get(key)
        if isinstance(value, (int, float)) and value:
            bits.append(f"{compact_n(int(value))} {label}")
    cost = metrics.get("cost_usd", metrics.get("cost_reported"))
    if isinstance(cost, (int, float)) and cost:
        bits.append(f"${cost:.3f}")
    return bits


def join_bits(*parts: object) -> str:
    bits: list[str] = []
    for part in parts:
        if part is None:
            continue
        if isinstance(part, (list, tuple)):
            bits.extend(str(item) for item in part if item not in ("", None))
        else:
            text = str(part).strip()
            if text:
                bits.append(text)
    return " · ".join(bits)


def _tty() -> bool:
    return hasattr(sys.stdout, "isatty") and sys.stdout.isatty()


def _console() -> Console | None:
    if Console is None:
        return None
    return Console(highlight=False, soft_wrap=True, emoji=False)


def banner(text: str) -> None:
    console = _console()
    if console is not None and Text is not None:
        console.print(Text(text, style="bold"))
        return
    print(text, flush=True)


def chapter_banner(chapter: int, label: str, *, pipeline: str | None = None) -> None:
    banner(f"Chapter {chapter}  {label}")
    note = pipeline or "Deterministic draft → review → revise → update → accept → commit"
    console = _console()
    if console is not None and Text is not None:
        console.print(Text(f"  {note}", style="dim"))
        console.print()
        return
    print(f"  {note}", flush=True)
    print(flush=True)


def step(stage: str, detail: str = "", *, note: str = "", facts: Iterable[str] | None = None) -> None:
    body = join_bits(detail, list(facts or []))
    note_text = note or STAGE_NOTES.get(stage, "")
    _emit_final(stage, body, note_text, ok=True)


def _emit_final(stage: str, detail: str, note: str = "", *, ok: bool = True) -> None:
    console = _console()
    mark = "✓" if ok else "✗"
    style = "green" if ok else "red"
    if console is not None and Text is not None:
        line = Text()
        line.append(f"  {mark} ", style=style)
        line.append(f"{stage:<11}", style="bold")
        if detail:
            line.append(detail)
        console.print(line)
        if note:
            console.print(Text(f"             {note}", style="dim"))
        return
    prefix = f"  {mark} {stage:<11}"
    print(f"{prefix}{detail}".rstrip(), flush=True)
    if note:
        print(f"             {note}", flush=True)


class NullCall:
    """Stand-in when a test or skip path has no live model row."""

    completed = True

    def done(self, metrics: dict | None = None, extra: str = "", *, facts: Iterable[str] | None = None, note: str = "") -> None:
        return None

    def fail(self, message: str) -> None:
        return None


class ModelCall:
    """Live-updating stage row that freezes into a rich final summary."""

    def __init__(
        self,
        stage: str,
        model: str,
        timeout: int,
        packet_tokens: int | None = None,
        *,
        hint: str = "",
        note: str = "",
        facts: Iterable[str] | None = None,
        started: float | None = None,
        writer=None,
        tty: bool | None = None,
        refresh_seconds: float = 0.2,
    ) -> None:
        self.stage = stage
        self.model_id = model
        self.model = short_model(model)
        self.timeout = timeout
        self.packet_tokens = packet_tokens
        self.hint = hint
        self.note = note or STAGE_NOTES.get(stage, "")
        self.facts = [item for item in (facts or []) if item]
        self.started = time.monotonic() if started is None else started
        self.phase = "waiting"
        self.thinking_chars = 0
        self.output_chars = 0
        self.fallback = ""
        self.metrics: dict | None = None
        self.extra = ""
        self.completed = False
        self._last_paint = 0.0
        self._writer = writer
        self._tty = _tty() if tty is None else tty
        self._refresh_seconds = refresh_seconds
        self._live = None
        self._console = _console()

    def elapsed(self) -> float:
        return time.monotonic() - self.started

    def start(self) -> None:
        if self._writer is not None:
            self._paint(live=True, force=True)
            return
        if self._tty and self._console is not None and Live is not None:
            self._live = Live(
                self._render_live(),
                console=self._console,
                refresh_per_second=max(1, int(round(1 / self._refresh_seconds))),
                transient=True,
            )
            self._live.start()
            return
        self._paint(live=True, force=True)

    def on_event(self, event: dict) -> None:
        event_type = event.get("type")
        if event_type == "retry_fallback_applied":
            dest = event.get("to") or event.get("model") or ""
            self.fallback = short_model(str(dest)) if dest else "fallback"
            self.phase = "fallback"
            self._paint(live=True, force=True)
            return
        if event_type == "message_update":
            inner = event.get("assistantMessageEvent")
            if isinstance(inner, dict):
                kind = inner.get("type")
                if kind in {"thinking_start", "thinking_delta"}:
                    self.phase = "thinking"
                    if kind == "thinking_delta" and isinstance(inner.get("delta"), str):
                        self.thinking_chars += len(inner["delta"])
                elif kind in {"text_start", "text_delta", "text_end"}:
                    self.phase = "writing"
                    if kind == "text_delta" and isinstance(inner.get("delta"), str):
                        self.output_chars += len(inner["delta"])
                    elif kind == "text_end" and isinstance(inner.get("content"), str):
                        self.output_chars = max(self.output_chars, len(inner["content"]))
            self._paint(live=True)
            return
        if event_type == "message_end":
            message = event.get("message") if isinstance(event.get("message"), dict) else {}
            if message.get("role") == "assistant":
                self.phase = "finishing"
            self._paint(live=True, force=True)
            return
        self._paint(live=True)

    def idle(self) -> None:
        self._paint(live=True)

    def done(
        self,
        metrics: dict | None = None,
        extra: str = "",
        *,
        facts: Iterable[str] | None = None,
        note: str = "",
    ) -> None:
        if self.completed:
            return
        if metrics is not None:
            self.metrics = metrics
        if extra:
            self.extra = extra
        if facts is not None:
            self.facts = [item for item in facts if item]
        if note:
            self.note = note
        self.completed = True
        self._stop_live()
        self._paint(live=False, force=True)

    def fail(self, message: str) -> None:
        self.extra = message
        self.completed = True
        self._stop_live()
        self._paint(live=False, force=True, ok=False)

    def live_detail(self) -> str:
        bits = [self._model_bit(), self.phase, format_elapsed(self.elapsed())]
        if self.packet_tokens is not None:
            bits.append(f"packet {compact_n(self.packet_tokens)}")
        if self.hint:
            bits.append(self.hint)
        if self.phase == "thinking" and self.thinking_chars:
            bits.append(f"{compact_n(self.thinking_chars)} chars")
        if self.phase == "writing" and self.output_chars:
            bits.append(f"{compact_n(self.output_chars)} chars")
        bits.extend(self.facts)
        return join_bits(bits)

    def final_detail(self) -> str:
        metrics = self.metrics or {}
        elapsed = metrics.get("elapsed_seconds", self.elapsed())
        bits = [format_elapsed(float(elapsed)), self._model_bit()]
        bits.extend(metrics_facts(metrics))
        if self.hint:
            bits.append(self.hint)
        if self.extra:
            bits.append(self.extra)
        bits.extend(self.facts)
        return join_bits(bits)

    def _model_bit(self) -> str:
        if self.fallback:
            return f"{self.model}→{self.fallback}"
        return self.model

    def _stop_live(self) -> None:
        if self._live is not None:
            self._live.stop()
            self._live = None

    def _render_live(self):
        detail = self.live_detail()
        label = f"{self.stage:<11}{detail}"
        if Spinner is None or Group is None or Text is None:
            return f"  {label}"
        spinner = Spinner("dots", text=label, style="cyan")
        if self.note:
            return Group(spinner, Text(f"             {self.note}", style="dim"))
        return spinner

    def _render_final(self, *, ok: bool = True):
        detail = self.final_detail()
        if Text is None:
            mark = "✓" if ok else "✗"
            return f"  {mark} {self.stage:<11}{detail}"
        line = Text()
        line.append(f"  {'✓' if ok else '✗'} ", style="green" if ok else "red")
        line.append(f"{self.stage:<11}", style="bold")
        line.append(detail)
        if self.note and not ok:
            return Group(line, Text(f"             {self.note}", style="dim"))
        if self.note:
            return Group(line, Text(f"             {self.note}", style="dim"))
        return line

    def _paint(self, *, live: bool, force: bool = False, ok: bool = True) -> None:
        now = time.monotonic()
        if live and not force and (now - self._last_paint) < self._refresh_seconds:
            return
        if live and not self._tty and self._writer is None and self._live is None:
            return
        self._last_paint = now
        if self._writer is not None:
            detail = self.live_detail() if live else self.final_detail()
            self._writer(f"  {self.stage:<11}{detail}", live=live)
            return
        if live and self._live is not None:
            self._live.update(self._render_live())
            return
        if live and self._tty:
            line = f"  {self.stage:<11}{self.live_detail()}"
            sys.stdout.write("\r" + line + "\033[K")
            sys.stdout.flush()
            return
        if self._console is not None:
            self._console.print(self._render_final(ok=ok))
            return
        mark = "✓" if ok else "✗"
        print(f"  {mark} {self.stage:<11}{self.final_detail()}", flush=True)
        if self.note:
            print(f"             {self.note}", flush=True)
