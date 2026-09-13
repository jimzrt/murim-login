import unittest

from tools.progress import (
    ModelCall,
    changed_file_facts,
    compact_n,
    copy_facts,
    findings_facts,
    join_bits,
    qa_brief,
    short_model,
    step,
)


class ProgressTest(unittest.TestCase):
    def test_short_model_and_counts(self):
        self.assertEqual(short_model("openai-codex/gpt-5.6-luna:high"), "luna")
        self.assertEqual(short_model("cursor/cursor-grok-4.6:low"), "grok")
        self.assertEqual(compact_n(14765), "14.8k")
        self.assertEqual(compact_n(4984), "4,984")
        self.assertEqual(qa_brief({"passed": True, "errors": [], "warnings": [{}]}), "QA PASS · 1w")
        self.assertEqual(qa_brief({"passed": True, "errors": [], "warnings": []}), "QA PASS")

    def test_translation_fact_helpers(self):
        facts = copy_facts("가" * 100, "Alpha beta gamma " * 20, glossary=12)
        self.assertTrue(any("words" in item for item in facts))
        self.assertTrue(any(item.startswith("×") for item in facts))
        self.assertIn("12 glossary", facts)
        self.assertEqual(
            findings_facts({"findings": [
                {"severity": "major"}, {"severity": "minor"}, {"severity": "minor"},
            ]}),
            ["3 findings", "1 major", "2 minor"],
        )
        files = changed_file_facts([
            "docs/NAMES.md",
            "docs/CONTEXT.json",
            "characters/Jin Taekyung.md",
            "summaries/beats/0371.md",
        ])
        self.assertIn("4 files", files)
        self.assertTrue(any("Jin Taekyung" in item for item in files))

    def test_live_row_stays_on_one_line_then_freezes_with_stats(self):
        painted: list[tuple[str, bool]] = []
        call = ModelCall(
            "draft",
            "openai-codex/gpt-5.6-luna:high",
            960,
            packet_tokens=13101,
            facts=["12 glossary"],
            started=0,
            writer=lambda line, live: painted.append((line, live)),
            tty=True,
            refresh_seconds=0,
        )
        call.start()
        call.on_event({"type": "message_update", "assistantMessageEvent": {"type": "thinking_start"}})
        call.done(
            {"elapsed_seconds": 270, "output_tokens": 14765, "reasoning_tokens": 11609},
            "QA PASS",
            facts=["4,812 words", "×2.10", "12 glossary"],
        )
        self.assertTrue(painted[0][1])
        self.assertIn("draft", painted[0][0])
        self.assertIn("luna", painted[0][0])
        self.assertIn("packet 13.1k", painted[0][0])
        self.assertFalse(painted[-1][1])
        self.assertIn("4m30s", painted[-1][0])
        self.assertIn("14.8k out", painted[-1][0])
        self.assertIn("11.6k think", painted[-1][0])
        self.assertIn("QA PASS", painted[-1][0])
        self.assertIn("4,812 words", painted[-1][0])
        self.assertEqual(sum(1 for _line, live in painted if not live), 1)

    def test_step_prints_note(self):
        from io import StringIO
        from contextlib import redirect_stdout
        buf = StringIO()
        with redirect_stdout(buf):
            step("prepare", facts=["13.1k tok", "12 glossary"])
        text = buf.getvalue()
        self.assertIn("prepare", text)
        self.assertIn("13.1k tok", text)
        self.assertIn("glossary", text.lower())
        self.assertIn("packet", text.lower())


if __name__ == "__main__":
    unittest.main()
