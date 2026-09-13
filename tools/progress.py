#!/usr/bin/env python3
"""Compact, single-line progress for chapter and mastering runs."""

from __future__ import annotations

import sys
import time


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
        return "QA PASS" + (f"  {warnings}w" if warnings else "")
    return f"QA FAIL  {errors}e  {warnings}w"


def _tty() -> bool:
    return hasattr(sys.stdout, "isatty") and sys.stdout.isatty()


def banner(text: str) -> None:
    print(text, flush=True)


def step(stage: str, detail: str = "") -> None:
    print(_format_row(stage, detail), flush=True)


class NullCall:
    """Stand-in when a test or skip path has no live model row."""

    def done(self, metrics: dict | None = None, extra: str = "") -> None:
        return None


def _format_row(stage: str, detail: str) -> str:
    body = detail.strip()
    if not body:
        return f"  {stage}"
    return f"  {stage:<12}{body}"


class ModelCall:
    """One table row: live-updated during the call, then frozen with stats."""

    def __init__(
        self,
        stage: str,
        model: str,
        timeout: int,
        packet_tokens: int | None = None,
        *,
        hint: str = "",
        started: float | None = None,
        writer=None,
        tty: bool | None = None,
    ) -> None:
        self.stage = stage
        self.model_id = model
        self.model = short_model(model)
        self.timeout = timeout
        self.packet_tokens = packet_tokens
        self.hint = hint
        self.started = time.monotonic() if started is None else started
        self.phase = "waiting"
        self.output_chars = 0
        self.fallback = ""
        self.metrics: dict | None = None
        self.extra = ""
        self.completed = False
        self._last_paint = 0.0
        self._writer = writer
        self._tty = _tty() if tty is None else tty

    def elapsed(self) -> float:
        return time.monotonic() - self.started

    def start(self) -> None:
        self._paint(live=True)

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
                elif kind in {"text_start", "text_delta", "text_end"}:
                    self.phase = "writing"
                    if kind == "text_delta" and isinstance(inner.get("delta"), str):
                        self.output_chars += len(inner["delta"])
                    elif kind == "text_end" and isinstance(inner.get("content"), str):
                        self.output_chars = max(self.output_chars, len(inner["content"]))
            self._paint(live=True)
            return
        self._paint(live=True)

    def idle(self) -> None:
        self._paint(live=True)

    def done(self, metrics: dict | None = None, extra: str = "") -> None:
        if self.completed:
            return
        if metrics is not None:
            self.metrics = metrics
        if extra:
            self.extra = extra
        self.completed = True
        self._paint(live=False)

    def fail(self, message: str) -> None:
        self.extra = message
        self.completed = True
        self._paint(live=False)

    def live_detail(self) -> str:
        bits = [self._model_bit(), self.phase, format_elapsed(self.elapsed())]
        if self.hint:
            bits.insert(1, self.hint)
        if self.phase == "writing" and self.output_chars:
            bits.append(compact_n(self.output_chars))
        return "  ".join(bit for bit in bits if bit)

    def final_detail(self) -> str:
        metrics = self.metrics or {}
        elapsed = metrics.get("elapsed_seconds", self.elapsed())
        bits = [format_elapsed(float(elapsed)), self._model_bit()]
        output = metrics.get("output_tokens")
        if isinstance(output, (int, float)) and output:
            bits.append(f"{compact_n(int(output))} out")
        if self.hint:
            bits.append(self.hint)
        if self.extra:
            bits.append(self.extra)
        return "  ".join(bits)

    def _model_bit(self) -> str:
        if self.fallback:
            return f"{self.model}→{self.fallback}"
        return self.model

    def _paint(self, *, live: bool, force: bool = False) -> None:
        now = time.monotonic()
        if live and not force and self._tty and (now - self._last_paint) < 1.0:
            return
        if live and not self._tty:
            return
        self._last_paint = now
        detail = self.live_detail() if live else self.final_detail()
        line = _format_row(self.stage, detail)
        if self._writer is not None:
            self._writer(line, live=live)
            return
        if live and self._tty:
            sys.stdout.write("\r" + line + "\033[K")
            sys.stdout.flush()
            return
        if self._tty:
            sys.stdout.write("\r" + line + "\033[K\n")
            sys.stdout.flush()
            return
        print(line, flush=True)
