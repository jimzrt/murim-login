import json
import unittest
from pathlib import Path

from tools.omp_json import OmpJsonError, parse_json_lines


def event(model="gpt-test", input_tokens=100, output_tokens=20, text="done", stop="stop", provider="openai-codex"):
    return json.dumps({
        "type": "message_end",
        "message": {
            "role": "assistant",
            "provider": provider,
            "model": model,
            "content": [{"type": "text", "text": text}],
            "usage": {
                "input": input_tokens,
                "output": output_tokens,
                "Vrij": "ignored",
                "cacheRead": 30,
                "cacheWrite": 0,
                "totalTokens": input_tokens + output_tokens + 30,
                "reasoning": 7,
                "cost": {"total": 0.0123},
            },
            "stopReason": stop,
        },
    })


class OmpJsonTest(unittest.TestCase):
    def test_extracts_output_and_exact_usage(self):
        output, usage = parse_json_lines([event()], "requested/high")
        self.assertEqual(output, "done\n")
        self.assertTrue(usage["exact"])
        self.assertEqual(usage["input_tokens"], 100)
        self.assertEqual(usage["output_tokens"], 20)
        self.assertEqual(usage["cache_read_tokens"], 30)
        self.assertEqual(usage["reasoning_tokens"], 7)
        self.assertEqual(usage["models"]["openai-codex/gpt-test"]["requests"], 1)
        self.assertFalse(usage["fallback_used"])
        self.assertEqual(usage["billing_type"], "subscription")

    def test_aggregates_every_assistant_request_by_actual_model(self):
        _, usage = parse_json_lines([
            event("gpt-a", 100, 20, "intermediate"),
            event("gpt-b", 40, 5, "final"),
        ], "requested/high")
        self.assertEqual(usage["requests"], 2)
        self.assertEqual(usage["input_tokens"], 140)
        self.assertEqual(set(usage["models"]), {"openai-codex/gpt-a", "openai-codex/gpt-b"})

    def test_error_stop_text_is_recovered(self):
        output, usage = parse_json_lines(
            [event(text="<<<TRANSLATION>>>\n# Chapter 1\n", stop="error")],
            "requested/high",
        )
        self.assertIn("Chapter 1", output)
        self.assertTrue(usage["recovered_from_error_stop"])
        self.assertEqual(usage["stop_reasons"], ["error"])

    def test_non_error_text_wins_over_later_error_stop(self):
        output, usage = parse_json_lines([
            event("gpt-a", 100, 20, "keep this", "stop"),
            event("gpt-b", 40, 5, "", "error"),
        ], "requested/high")
        self.assertEqual(output, "keep this\n")
        self.assertNotIn("recovered_from_error_stop", usage)

    def test_error_stop_without_text_names_the_stop_reason(self):
        with self.assertRaises(OmpJsonError) as error:
            parse_json_lines([event(text="", stop="error")], "requested/high")
        self.assertIn("stopReason=error", str(error.exception))

    def test_missing_usage_is_a_hard_failure(self):

        bad = json.dumps({"type": "message_end", "message": {
            "role": "assistant", "provider": "openai-codex", "model": "gpt-test",
            "content": [{"type": "text", "text": "done"}], "stopReason": "stop",
        }})
        with self.assertRaises(OmpJsonError):
            parse_json_lines([bad], "requested/high")

    def test_fallback_events_set_actual_provider_and_api_billing(self):
        _, usage = parse_json_lines([
            json.dumps({
                "type": "retry_fallback_applied",
                "from": "cursor/gpt-5.6-luna:high",
                "to": "openrouter/openai/gpt-5.6-luna:high",
                "role": "draft",
            }),
            json.dumps({
                "type": "retry_fallback_succeeded",
                "model": "openrouter/openai/gpt-5.6-luna:high",
                "role": "draft",
            }),
            event(model="openai/gpt-5.6-luna", provider="openrouter"),
        ], "cursor/gpt-5.6-luna:high")
        self.assertTrue(usage["fallback_used"])
        self.assertEqual(usage["provider"], "openrouter")
        self.assertEqual(usage["model"], "openai/gpt-5.6-luna")
        self.assertEqual(usage["billing_type"], "api")
        self.assertEqual(usage["cost_reported"], 0.0123)
        self.assertEqual(usage["models"]["openrouter/openai/gpt-5.6-luna"]["billing_type"], "api")
        self.assertEqual(usage["fallbacks"][0]["from"], "cursor/gpt-5.6-luna:high")

    def test_provider_mismatch_without_events_is_still_fallback(self):
        _, usage = parse_json_lines(
            [event(model="gpt-5.6-sol", provider="cursor")],
            "openai-codex/gpt-5.6-sol:low",
        )
        self.assertTrue(usage["fallback_used"])
        self.assertEqual(usage["provider"], "cursor")
        self.assertEqual(usage["billing_type"], "subscription")

    def test_matching_requested_provider_is_not_fallback(self):
        _, usage = parse_json_lines(
            [event(model="gpt-5.6-luna")],
            "openai-codex/gpt-5.6-luna:high",
        )
        self.assertFalse(usage["fallback_used"])
        self.assertEqual(usage["provider"], "openai-codex")
        self.assertNotIn("fallbacks", usage)

    def test_project_omp_config_defines_subscription_overflow_chains(self):
        root = Path(__file__).resolve().parents[1]
        text = (root / ".omp" / "config.yml").read_text(encoding="utf-8")
        self.assertIn("usageAwareFallback: true", text)
        self.assertIn("usageReservePct: 5", text)
        self.assertIn("fallbackRevertPolicy: cooldown-expiry", text)
        self.assertIn("openai-codex/gpt-5.6-sol:", text)
        self.assertIn("openai-codex/gpt-5.6-luna:", text)
        self.assertIn("cursor/gpt-5.6-luna:", text)
        self.assertIn("cursor/cursor-grok-4.6:", text)
        self.assertNotIn("deepseek-v4.1-flash", text)
        overlay = (root / ".omp" / "adjudicator-overlay.yml").read_text(encoding="utf-8")
        self.assertIn("openrouter/deepseek/deepseek-v4.1-flash:low", overlay)


    def test_run_json_command_streams_without_dumping_events(self):
        import sys
        import tempfile
        from pathlib import Path
        from tools.omp_json import run_json_command
        from tools.progress import ModelCall

        script = r"""
import json, sys
print(json.dumps({"type": "agent_start"}), flush=True)
print(json.dumps({"type": "message_update", "assistantMessageEvent": {"type": "thinking_start"}}), flush=True)
print(json.dumps({
    "type": "message_end",
    "message": {
        "role": "assistant",
        "provider": "openai-codex",
        "model": "gpt-test",
        "content": [{"type": "text", "text": "done"}],
        "usage": {"input": 10, "output": 4, "cacheRead": 0, "cacheWrite": 0, "totalTokens": 14},
        "stopReason": "stop",
    },
}), flush=True)
"""
        painted: list[tuple[str, bool]] = []
        listener = ModelCall(
            "draft", "openai-codex/gpt-5.6-luna:high", 30,
            writer=lambda line, live: painted.append((line, live)),
            tty=True,
        )
        with tempfile.TemporaryDirectory() as directory:
            output, metrics = run_json_command(
                [sys.executable, "-c", script],
                cwd=Path(directory),
                requested_model="openai-codex/gpt-5.6-luna:high",
                timeout=10,
                listener=listener,
            )
        listener.done(metrics)
        self.assertEqual(output.strip(), "done")
        self.assertEqual(metrics["output_tokens"], 4)
        self.assertTrue(any(live for _line, live in painted))
        self.assertIn("luna", painted[-1][0])
        self.assertFalse(painted[-1][1])

    def test_run_json_command_does_not_inherit_stdin(self):
        import sys
        import tempfile
        from tools.omp_json import run_json_command

        script = r"""
import json, sys
assert sys.stdin.read() == ""
print(json.dumps({
    "type": "message_end",
    "message": {
        "role": "assistant",
        "provider": "openai-codex",
        "model": "gpt-test",
        "content": [{"type": "text", "text": "ok"}],
        "usage": {"input": 1, "output": 1, "cacheRead": 0, "cacheWrite": 0, "totalTokens": 2},
        "stopReason": "stop",
    },
}), flush=True)
"""
        with tempfile.TemporaryDirectory() as directory:
            output, metrics = run_json_command(
                [sys.executable, "-c", script],
                cwd=Path(directory),
                requested_model="openai-codex/gpt-test",
                timeout=10,
            )
        self.assertEqual(output.strip(), "ok")
        self.assertEqual(metrics["output_tokens"], 1)


if __name__ == "__main__":
    unittest.main()
