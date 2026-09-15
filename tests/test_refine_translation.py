import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from types import SimpleNamespace

from tools import refine_translation


class RefineTranslationTest(unittest.TestCase):
    def test_finds_exact_quote_and_counts_occurrences(self):
        with tempfile.TemporaryDirectory() as directory:
            translations = Path(directory)
            (translations / "0001.md").write_text("# Chapter 1\n\nSame line.\n", encoding="utf-8")
            (translations / "0002.md").write_text("# Chapter 2\n\nSame line. Same line.\n", encoding="utf-8")
            (translations / "notes.md").write_text("Same line.", encoding="utf-8")
            matches = refine_translation.find_quote("Same line.", translations)
        self.assertEqual([(number, count) for number, _path, count in matches], [(1, 1), (2, 2)])

    def test_archived_context_uses_current_rules_without_draft_instruction(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "RULES.md").write_text("CURRENT RULES", encoding="utf-8")
            (root / "POLISH.md").write_text("CURRENT POLISH", encoding="utf-8")
            packet = root / ".work" / "0007" / "context.md"
            packet.parent.mkdir(parents=True)
            packet.write_text(
                "# Draft Task — Chapter 7\n\nTranslate the whole chapter.\n\n"
                "## Bounded active continuity\n\nSAFE HISTORY\n\n"
                "## Korean source\n\n한국어\n",
                encoding="utf-8",
            )
            reference = refine_translation.reference_context(7, root)
        self.assertIn("CURRENT RULES", reference)
        self.assertIn("CURRENT POLISH", reference)
        self.assertIn("SAFE HISTORY", reference)
        self.assertIn("한국어", reference)
        self.assertNotIn("Translate the whole chapter", reference)

    def test_prompt_allows_evidence_based_cross_chapter_edits(self):
        with patch.object(refine_translation, "ROOT", Path("/repo")):
            prompt = refine_translation.build_prompt(
                7,
                Path("/repo/translations/0007.md"),
                "# Chapter 7\n\nAwkward title.",
                "Awkward title.",
                "this title sounds wrong",
                "Korean and context",
            )
        self.assertIn("do not limit the diagnosis or edit scope", prompt)
        self.assertIn("spanning the chapter or multiple finalized chapters", prompt)
        self.assertIn("matching `source/NNNN.txt`", prompt)
        self.assertIn("apply that strategy everywhere the evidence supports it", prompt)
        self.assertIn("`docs/NAMES.md`", prompt)
        self.assertIn("`docs/ADDRESS.md`", prompt)
        self.assertIn("`compendium.md`", prompt)
        self.assertIn('Proofreader note: \"this title sounds wrong\"', prompt)

    def test_main_launches_for_repeated_anchor_with_broad_tools(self):
        path = refine_translation.ROOT / "translations" / "0066.md"
        captured = {}

        def fake_run(command, cwd):
            captured["command"] = command
            captured["cwd"] = cwd
            captured["prompt"] = Path(command[-1][1:]).read_text(encoding="utf-8")
            return SimpleNamespace(returncode=0)

        with (
            patch("sys.argv", ["refine_translation.py", "Step. Step."]),
            patch("builtins.input", return_value="too repetitive"),
            patch.object(refine_translation, "find_quote", return_value=[(66, path, 2)]),
            patch.object(refine_translation, "reference_context", return_value="SAFE REFERENCE"),
            patch.object(refine_translation.subprocess, "run", side_effect=fake_run),
        ):
            result = refine_translation.main()

        self.assertEqual(result, 0)
        self.assertEqual(captured["cwd"], refine_translation.ROOT)
        self.assertIn(refine_translation.MODEL, captured["command"])
        self.assertIn("read,grep,edit,ask", captured["command"])
        self.assertIn("Step. Step.", captured["prompt"])
        self.assertIn("too repetitive", captured["prompt"])


if __name__ == "__main__":
    unittest.main()
