"""QA and queue selection for the final-touches pass."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools import final_qa, final_touches, run_final_batch, run_next_final


def chapter(body: str) -> str:
    return f"# Chapter 1\n\n{body}\n"


class FinalQaTest(unittest.TestCase):
    def setUp(self):
        self.source = "가" * 120
        self.baseline = chapter("The hall was quiet. " * 10)

    def assess(self, candidate: str, baseline: str | None = None) -> dict:
        return final_qa.assess(
            1,
            self.source,
            baseline if baseline is not None else self.baseline,
            candidate,
            min_baseline_preserved=0.8,
        )

    def test_matching_copy_passes(self):
        qa = self.assess(self.baseline)
        self.assertTrue(qa["passed"], qa["errors"])

    def test_footnote_on_unchanged_prose_passes(self):
        candidate = chapter(
            ("The hall was quiet. " * 9)
            + "The hall was a pyeong.[^1]\n\n"
            + "[^1]: A pyeong is about 3.31 square meters (35.6 square feet)."
        )
        qa = self.assess(candidate)
        self.assertTrue(qa["passed"], qa["errors"])
        self.assertGreaterEqual(qa["metrics"]["baseline_preserved"], 0.8)

    def test_straight_quotes_fail(self):
        candidate = chapter('He said "hello" and the hall was quiet. ' * 6)
        qa = self.assess(candidate, candidate)
        self.assertFalse(qa["passed"])
        self.assertTrue(any(item["code"] == "straight_quotes" for item in qa["errors"]))

    def test_system_chat_and_thought_formats(self):
        good = chapter(
            "> **System**\n>\n> - You have joined.\n\n" + ("The hall was quiet. " * 8)
        )
        qa = self.assess(good, good)
        self.assertFalse(any(item["code"] == "system_format" for item in qa["errors"]), qa["errors"])

        bad_system = chapter("**System**\n\n" + ("The hall was quiet. " * 8))
        qa = self.assess(bad_system, bad_system)
        self.assertTrue(any(item["code"] == "system_format" for item in qa["errors"]))

        bad_chat = chapter("└ Hello there.\n\n" + ("The hall was quiet. " * 8))
        qa = self.assess(bad_chat, bad_chat)
        self.assertTrue(any(item["code"] == "chat_format" for item in qa["errors"]))

        bad_thought = chapter("*“Not again.”*\n\n" + ("The hall was quiet. " * 8))
        qa = self.assess(bad_thought, bad_thought)
        self.assertTrue(any(item["code"] == "thought_format" for item in qa["errors"]))

    def test_warning_heading_must_stay(self):
        baseline = chapter(
            "> **Warning**\n>\n> - The player cannot log out at will.\n\n"
            + ("The hall was quiet. " * 8)
        )
        dropped = chapter(
            "> - The player cannot log out at will.\n\n" + ("The hall was quiet. " * 8)
        )
        qa = self.assess(dropped, baseline)
        self.assertTrue(any(item["code"] == "panel_heading" for item in qa["errors"]))

    def test_rewritten_prose_fails(self):
        candidate = chapter("A wholly different scene about another person. " * 8)
        qa = self.assess(candidate)
        self.assertTrue(any(item["code"] == "prose_drift" for item in qa["errors"]))

    def test_packet_includes_project_rates(self):
        packet = final_touches.build_packet(
            4,
            "source",
            "# Chapter 4\n\nHello.\n",
            [],
            {"currency": {"krw_per_usd": 1400, "krw_per_eur": 1550}},
        )
        self.assertIn("1 US dollar = 1400 Korean won", packet)
        self.assertIn("1 euro = 1550 Korean won", packet)
        self.assertIn("# Chapter 4", packet)
        self.assertIn("same marker", packet.casefold())


class NextFinalChapterTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        (self.root / "translations").mkdir()
        self.patches = [
            patch.object(run_next_final, "ROOT", self.root),
            patch.object(final_touches, "ROOT", self.root),
            patch.object(run_next_final, "translation_blocked", return_value=None),
        ]
        for item in self.patches:
            item.start()

    def tearDown(self):
        for item in reversed(self.patches):
            item.stop()
        self.temporary.cleanup()

    def write_translation(self, number: int) -> None:
        (self.root / "translations" / f"{number:04d}.md").write_text(
            f"# Chapter {number}\n", encoding="utf-8"
        )

    def write_final(self, number: int, stage: str, qa_passed: bool = True) -> None:
        folder = self.root / "reviews" / "final" / f"{number:04d}"
        folder.mkdir(parents=True)
        (folder / "state.json").write_text(
            json.dumps({"chapter": number, "stage": stage, "qa_passed": qa_passed}),
            encoding="utf-8",
        )

    def test_waits_when_the_oldest_chapter_is_not_mastered(self):
        for number in (1, 2, 3):
            self.write_translation(number)
        with patch.object(run_next_final, "mastering_done", side_effect=lambda number: number > 1):
            self.assertIsNone(run_next_final.next_final_chapter(dirty=[]))

    def test_picks_the_oldest_mastered_chapter(self):
        for number in (1, 2):
            self.write_translation(number)
        with patch.object(run_next_final, "mastering_done", return_value=True):
            self.assertEqual(run_next_final.next_final_chapter(dirty=[]), 1)

    def test_skips_a_promoted_chapter(self):
        for number in (1, 2):
            self.write_translation(number)
        self.write_final(1, "PROMOTED")
        with patch.object(run_next_final, "mastering_done", return_value=True):
            self.assertEqual(run_next_final.next_final_chapter(dirty=[]), 2)

    def test_resumes_the_oldest_when_several_are_unfinished(self):
        for number in (1, 2):
            self.write_translation(number)
            self.write_final(number, "QA_FAILED", qa_passed=False)
        with patch.object(run_next_final, "mastering_done", return_value=True):
            self.assertEqual(run_next_final.next_final_chapter(dirty=[]), 1)

    def test_foreign_paths_cover_an_in_flight_chapter(self):
        self.write_final(4, "READY_TO_COMMIT")
        foreign = final_touches.foreign_final_paths(
            [
                "reviews/final/0004/state.json",
                "translations/0004.md",
                "translations/0005.md",
            ]
        )
        self.assertEqual(
            foreign,
            {"reviews/final/0004/state.json", "translations/0004.md"},
        )


class FinalBatchTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        (self.root / "translations").mkdir()
        self.patches = [
            patch.object(run_final_batch, "ROOT", self.root),
            patch.object(final_touches, "ROOT", self.root),
            patch.object(run_final_batch, "translation_blocked", return_value=None),
        ]
        for item in self.patches:
            item.start()

    def tearDown(self):
        for item in reversed(self.patches):
            item.stop()
        self.temporary.cleanup()

    def write_translation(self, number: int) -> None:
        (self.root / "translations" / f"{number:04d}.md").write_text(
            f"# Chapter {number}\n", encoding="utf-8"
        )

    def write_final(self, number: int, stage: str) -> None:
        folder = self.root / "reviews" / "final" / f"{number:04d}"
        folder.mkdir(parents=True)
        (folder / "state.json").write_text(
            json.dumps({"chapter": number, "stage": stage, "qa_passed": True}),
            encoding="utf-8",
        )

    def test_skips_unmastered_and_keeps_later_chapters(self):
        for number in (3, 4, 5):
            self.write_translation(number)
        with patch.object(run_final_batch, "mastering_done", side_effect=lambda number: number != 4):
            chosen, notes = run_final_batch.select_batch(3, 5)
        self.assertEqual(chosen, [3, 5])
        self.assertEqual(notes, ["chapter 4: not mastered"])

    def test_skips_a_finished_chapter_and_a_blocked_one(self):
        for number in (6, 7, 8):
            self.write_translation(number)
        self.write_final(6, "PROMOTED")

        def blocked(number: int) -> str | None:
            return "busy" if number == 8 else None

        with patch.object(run_final_batch, "mastering_done", return_value=True):
            with patch.object(run_final_batch, "translation_blocked", side_effect=blocked):
                chosen, notes = run_final_batch.select_batch(6, 8)
        self.assertEqual(chosen, [7])
        self.assertEqual(notes, ["chapter 8: still in translation or mastering"])


if __name__ == "__main__":
    unittest.main()
