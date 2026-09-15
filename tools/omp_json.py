#!/usr/bin/env python3
"""Strict parsing and aggregation for OMP JSON event streams."""

from __future__ import annotations

import json
import numbers
import os
import selectors
import signal
import subprocess
import threading
import time
from pathlib import Path
from typing import Callable, Iterable


class OmpJsonError(ValueError):
    """Raised when OMP's event stream cannot provide exact usage."""


SUBSCRIPTION_PROVIDERS = frozenset({"openai-codex", "cursor"})
FALLBACK_EVENTS = frozenset({"retry_fallback_applied", "retry_fallback_succeeded"})
TOKEN_FIELDS = {
    "input": "input_tokens",
    "output": "output_tokens",
    "cacheRead": "cache_read_tokens",
    "cacheWrite": "cache_write_tokens",
    "totalTokens": "total_tokens",
}


def selector_provider(selector: str) -> str:
    return selector.split("/", 1)[0] if selector else ""


def billing_type_for(provider: str) -> str:
    return "subscription" if provider in SUBSCRIPTION_PROVIDERS else "api"


def _number(value: object, label: str) -> int | float:
    if not isinstance(value, numbers.Real) or isinstance(value, bool) or value < 0:
        raise OmpJsonError(f"OMP usage field {label} is missing or invalid")
    return value


def _message_text(message: dict) -> str:
    content = message.get("content")
    if not isinstance(content, list):
        return ""
    return "".join(
        block.get("text", "")
        for block in content
        if isinstance(block, dict) and block.get("type") == "text" and isinstance(block.get("text"), str)
    )


def _usage_record(message: dict) -> dict:
    provider = message.get("provider")
    model = message.get("model")
    usage = message.get("usage")
    if not isinstance(provider, str) or not provider or not isinstance(model, str) or not model:
        raise OmpJsonError("OMP assistant message is missing its actual provider or model")
    if not isinstance(usage, dict):
        raise OmpJsonError(f"OMP did not report usage for {provider}/{model}")
    record = {
        "provider": provider,
        "model": model,
        **{target: _number(usage.get(source), source) for source, target in TOKEN_FIELDS.items()},
    }
    reasoning = usage.get("reasoning", usage.get("reasoningTokens"))
    if reasoning is not None:
        record["reasoning_tokens"] = _number(reasoning, "reasoning")
    cost = usage.get("cost")
    if isinstance(cost, dict) and cost.get("total") is not None:
        record["cost_usd"] = _number(cost["total"], "cost.total")
    return record


class EventCapture:
    """Collect final text and exact provider usage from JSONL events."""

    def __init__(self, requested_model: str):
        self.requested_model = requested_model
        self.records: list[dict] = []
        self.final_text = ""
        self.stop_reasons: list[str] = []
        self.used_error_text = False
        self.fallbacks: list[dict] = []

    def consume(self, event: dict) -> None:
        event_type = event.get("type")
        if event_type in FALLBACK_EVENTS:
            payload = {"event": event_type}
            for key in ("from", "to", "role", "model"):
                value = event.get(key)
                if isinstance(value, str) and value:
                    payload[key] = value
            self.fallbacks.append(payload)
            return
        if event_type != "message_end":
            return
        message = event.get("message")
        if not isinstance(message, dict) or message.get("role") != "assistant":
            return
        record = _usage_record(message)
        self.records.append(record)
        text = _message_text(message)
        stop = message.get("stopReason")
        if isinstance(stop, str) and stop:
            self.stop_reasons.append(stop)
            record["stop_reason"] = stop
        if not text.strip():
            return
        if stop != "error":
            self.final_text = text
            self.used_error_text = False
        elif not self.final_text.strip():
            self.final_text = text
            self.used_error_text = True

    def finish(self, *, require_output: bool = True) -> tuple[str, dict]:
        if not self.records:
            raise OmpJsonError("OMP JSON stream contained no assistant usage records")
        if require_output and not self.final_text.strip():
            reasons = ", ".join(self.stop_reasons) or "unknown"
            raise OmpJsonError(
                f"OMP JSON stream contained no final assistant text (stopReason={reasons})"
            )
        models: dict[str, dict] = {}
        for record in self.records:
            key = f"{record['provider']}/{record['model']}"
            aggregate = models.setdefault(key, {
                "provider": record["provider"],
                "model": record["model"],
                "requests": 0,
                "input_tokens": 0,
                "output_tokens": 0,
                "cache_read_tokens": 0,
                "cache_write_tokens": 0,
                "total_tokens": 0,
                "reasoning_tokens": 0,
                "cost_usd": 0,
                "_cost_reported": True,
                "_reasoning_reported": True,
            })
            aggregate["requests"] += 1
            for field in (
                "input_tokens", "output_tokens", "cache_read_tokens",
                "cache_write_tokens", "total_tokens",
            ):
                aggregate[field] += record[field]
            if "reasoning_tokens" in record:
                aggregate["reasoning_tokens"] += record["reasoning_tokens"]
            else:
                aggregate["_reasoning_reported"] = False
            if "cost_usd" in record:
                aggregate["cost_usd"] += record["cost_usd"]
            else:
                aggregate["_cost_reported"] = False
        totals = {
            "requests": len(self.records),
            "input_tokens": sum(item["input_tokens"] for item in self.records),
            "output_tokens": sum(item["output_tokens"] for item in self.records),
            "cache_read_tokens": sum(item["cache_read_tokens"] for item in self.records),
            "cache_write_tokens": sum(item["cache_write_tokens"] for item in self.records),
            "total_tokens": sum(item["total_tokens"] for item in self.records),
        }
        if all("reasoning_tokens" in item for item in self.records):
            totals["reasoning_tokens"] = sum(item["reasoning_tokens"] for item in self.records)
        if all("cost_usd" in item for item in self.records):
            totals["cost_usd"] = sum(item["cost_usd"] for item in self.records)
        for aggregate in models.values():
            if not aggregate.pop("_cost_reported"):
                aggregate.pop("cost_usd")
            if not aggregate.pop("_reasoning_reported"):
                aggregate.pop("reasoning_tokens")
            aggregate["billing_type"] = billing_type_for(aggregate["provider"])
        requested_provider = selector_provider(self.requested_model)
        successful = [item for item in self.records if item.get("stop_reason") != "error"]
        if not successful:
            successful = list(self.records)
        last = successful[-1] if successful else None
        fallback_used = bool(self.fallbacks)
        if requested_provider in SUBSCRIPTION_PROVIDERS or requested_provider == "openrouter":
            fallback_used = fallback_used or any(
                item["provider"] != requested_provider for item in successful
            )
        metrics = {
            "exact": True,
            "usage_source": "omp_provider_reported",
            "requested_model": self.requested_model,
            "fallback_used": fallback_used,
            **totals,
            "models": models,
        }
        if last is not None:
            metrics["provider"] = last["provider"]
            metrics["model"] = last["model"]
            metrics["billing_type"] = billing_type_for(last["provider"])
        if "cost_usd" in totals:
            metrics["cost_reported"] = totals["cost_usd"]
        if self.fallbacks:
            metrics["fallbacks"] = list(self.fallbacks)
        if self.stop_reasons:
            metrics["stop_reasons"] = list(self.stop_reasons)
        if self.used_error_text:
            metrics["recovered_from_error_stop"] = True
        return self.final_text.strip() + ("\n" if self.final_text.strip() else ""), metrics


def parse_json_lines(lines: Iterable[str], requested_model: str, on_event: Callable[[dict], None] | None = None) -> tuple[str, dict]:
    capture = EventCapture(requested_model)
    for line_number, line in enumerate(lines, 1):
        if not line.strip():
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError as error:
            raise OmpJsonError(f"invalid OMP JSON event on line {line_number}: {error}") from None
        if not isinstance(event, dict):
            raise OmpJsonError(f"OMP JSON event on line {line_number} is not an object")
        capture.consume(event)
        if on_event:
            on_event(event)
    return capture.finish()


def _decode_captured(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, bytes):
        return value.decode("utf-8", errors="replace")
    return str(value)


def write_model_logs(log_path: Path | None, stdout: str, stderr: str = "", parsed: str | None = None) -> None:
    if log_path is None:
        return
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.write_text(stdout, encoding="utf-8")
    if stderr.strip():
        log_path.with_name(log_path.stem + ".stderr.txt").write_text(stderr, encoding="utf-8")
    if parsed is not None:
        log_path.with_name(log_path.stem + ".txt").write_text(parsed, encoding="utf-8")


def _stream_stdout_lines(proc: subprocess.Popen, timeout_end: float, on_idle: Callable[[], None]) -> Iterable[str]:
    assert proc.stdout is not None
    selector = selectors.DefaultSelector()
    selector.register(proc.stdout, selectors.EVENT_READ)
    buf = ""
    try:
        while True:
            remaining = timeout_end - time.monotonic()
            if remaining <= 0:
                raise subprocess.TimeoutExpired(proc.args, timeout=None)
            events = selector.select(timeout=min(1.0, remaining))
            if not events:
                on_idle()
                if proc.poll() is not None:
                    rest = proc.stdout.read()
                    if rest:
                        buf += rest
                    break
                continue
            chunk = proc.stdout.read(65536)
            if chunk == "":
                break
            buf += chunk
            while "\n" in buf:
                line, buf = buf.split("\n", 1)
                yield line
        if buf:
            yield buf
    finally:
        selector.close()


def _stop_process(proc: subprocess.Popen) -> None:
    if proc.poll() is not None:
        return
    try:
        os.killpg(proc.pid, signal.SIGTERM)
    except (ProcessLookupError, PermissionError, OSError):
        proc.kill()
        proc.wait()
        return
    try:
        proc.wait(timeout=3)
    except subprocess.TimeoutExpired:
        try:
            os.killpg(proc.pid, signal.SIGKILL)
        except (ProcessLookupError, PermissionError, OSError):
            proc.kill()
        proc.wait()


def run_json_command(
    command: list[str],
    *,
    cwd: Path,
    requested_model: str,
    timeout: int,
    log_path: Path | None = None,
    listener: object | None = None,
) -> tuple[str, dict]:
    started = time.monotonic()
    stdout_lines: list[str] = []
    stderr_chunks: list[str] = []
    capture = EventCapture(requested_model)

    def on_idle() -> None:
        idle = getattr(listener, "idle", None)
        if callable(idle):
            idle()

    proc = subprocess.Popen(
        command,
        cwd=cwd,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=0,
        start_new_session=True,
    )
    assert proc.stdout is not None
    assert proc.stderr is not None
    if hasattr(proc.stdout, "reconfigure"):
        proc.stdout.reconfigure(line_buffering=True)
    stderr_thread = threading.Thread(
        target=lambda: stderr_chunks.append(proc.stderr.read() if proc.stderr else ""),
        daemon=True,
    )
    stderr_thread.start()
    log_handle = None
    parse_error: OmpJsonError | None = None
    returncode = 1
    try:
        if log_path is not None:
            log_path.parent.mkdir(parents=True, exist_ok=True)
            log_handle = log_path.open("w", encoding="utf-8")
        start = getattr(listener, "start", None)
        if callable(start):
            start()
        on_event = getattr(listener, "on_event", None)
        for line in _stream_stdout_lines(proc, started + timeout, on_idle):
            stdout_lines.append(line)
            if log_handle is not None:
                log_handle.write(line)
                log_handle.write("\n")
                log_handle.flush()
            if not line.strip():
                continue
            try:
                event = json.loads(line)
            except json.JSONDecodeError as error:
                parse_error = OmpJsonError(f"invalid OMP JSON event on line {len(stdout_lines)}: {error}")
                _stop_process(proc)
                break
            if not isinstance(event, dict):
                parse_error = OmpJsonError(f"OMP JSON event on line {len(stdout_lines)} is not an object")
                _stop_process(proc)
                break
            capture.consume(event)
            if callable(on_event):
                on_event(event)
        returncode = proc.wait(timeout=max(1, timeout - (time.monotonic() - started)))
    except subprocess.TimeoutExpired as error:
        _stop_process(proc)
        proc.wait()
        stdout = "\n".join(stdout_lines)
        stderr_thread.join(timeout=2)
        stderr = "".join(stderr_chunks) or _decode_captured(proc.stderr.read() if proc.stderr else "")
        write_model_logs(log_path, stdout, stderr)
        fail = getattr(listener, "fail", None)
        if callable(fail):
            fail("timed out")
        extra = f"\nevents saved: {log_path}" if log_path else ""
        raise OmpJsonError(f"model call timed out: {error}{extra}") from None
    finally:
        if log_handle is not None:
            log_handle.close()
        stderr_thread.join(timeout=2)
        if proc.stdout is not None:
            proc.stdout.close()
        if proc.stderr is not None:
            proc.stderr.close()

    stdout = "\n".join(stdout_lines)
    if stdout_lines:
        stdout += "\n"
    stderr = "".join(stderr_chunks)
    if parse_error is not None:
        write_model_logs(log_path, stdout, stderr)
        fail = getattr(listener, "fail", None)
        if callable(fail):
            fail("invalid model stream")
        extra = f"\nevents saved: {log_path}" if log_path else ""
        raise OmpJsonError(str(parse_error) + extra) from None
    if returncode:
        fail = getattr(listener, "fail", None)
        if callable(fail):
            fail("model call failed")
        extra = f"\nevents saved: {log_path}" if log_path else ""
        raise OmpJsonError((stderr.strip() or stdout.strip() or "model call failed") + extra)
    try:
        output, metrics = capture.finish()
    except OmpJsonError as error:
        fail = getattr(listener, "fail", None)
        if callable(fail):
            fail("no model output")
        extra = f"\nevents saved: {log_path}" if log_path else ""
        raise OmpJsonError(str(error) + extra) from None
    write_model_logs(log_path, stdout, stderr, parsed=output)
    metrics.update({
        "elapsed_seconds": round(time.monotonic() - started, 3),
        "output_bytes": len(output.encode("utf-8")),
    })
    if log_path is not None:
        metrics["event_log"] = str(log_path)
    return output, metrics
