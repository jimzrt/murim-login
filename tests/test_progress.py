import unittest

from tools.progress import ModelCall, compact_n, qa_brief, short_model


class ProgressTest(unittest.TestCase):
    def test_short_model_and_counts(self):
        self.assertEqual(short_model("openai-codex/gpt-5.6-luna:high"), "luna")
        self.assertEqual(short_model("cursor/cursor-grok-4.6:low"), "grok")
        self.assertEqual(compact_n(14765), "14.8k")
        self.assertEqual(compact_n(4984), "4,984")
        self.assertEqual(qa_brief({"passed": True, "errors": [], "warnings": [{}]}), "QA PASS  1w")
        self.assertEqual(qa_brief({"passed": True, "errors": [], "warnings": []}), "QA PASS")

    def test_live_row_stays_on_one_line_then_freezes_with_stats(self):
        painted: list[tuple[str, bool]] = []
        call = ModelCall(
            "draft",
            "openai-codex/gpt-5.6-luna:high",
            960,
            packet_tokens=13101,
            started=0,
            writer=lambda line, live: painted.append((line, live)),
            tty=True,
        )
        call.start()
        call.on_event({"type": "message_update", "assistantMessageEvent": {"type": "thinking_start"}})
        call.done({"elapsed_seconds": 270, "output_tokens": 14765}, "QA PASS")
        self.assertTrue(painted[0][1])
        self.assertIn("draft", painted[0][0])
        self.assertIn("luna", painted[0][0])
        self.assertFalse(painted[-1][1])
        self.assertIn("4m30s", painted[-1][0])
        self.assertIn("14.8k out", painted[-1][0])
        self.assertIn("QA PASS", painted[-1][0])
        self.assertEqual(sum(1 for _line, live in painted if not live), 1)


if __name__ == "__main__":
    unittest.main()
