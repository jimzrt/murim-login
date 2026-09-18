import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools import run_next_mastering
from tools import workflow


class RunNextMasteringTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        (self.root / "translations").mkdir()
        (self.root / "docs").mkdir()
        self.root_patch = patch.object(run_next_mastering, "ROOT", self.root)
        self.workflow_root = patch.object(workflow, "ROOT", self.root)
        self.root_patch.start()
        self.workflow_root.start()

    def tearDown(self):
        self.workflow_root.stop()
        self.root_patch.stop()
        self.temporary.cleanup()

    def write_primary(self, number: int, stage: str) -> None:
        folder = self.root / ".work" / f"{number:04d}"
        folder.mkdir(parents=True)
        (folder / "workflow.json").write_text(
            json.dumps({"chapter": number, "stage": stage, "artifacts": {}}),
            encoding="utf-8",
        )

    def write_overlay(self, number: int, stage: str, qa_passed: bool = True) -> None:
        folder = self.root / "reviews" / "mastering" / f"{number:04d}"
        folder.mkdir(parents=True)
        (folder / "state.json").write_text(
            json.dumps({"chapter": number, "stage": stage, "qa_passed": qa_passed}),
            encoding="utf-8",
        )

    def test_picks_oldest_committed_unpromoted_chapter(self):
        (self.root / "translations" / "0003.md").write_text("# Chapter 3\n", encoding="utf-8")
        (self.root / "translations" / "0004.md").write_text("# Chapter 4\n", encoding="utf-8")
        self.write_primary(3, "COMMITTED")
        self.write_primary(4, "COMMITTED")
        self.write_overlay(3, "PROMOTED", True)
        with patch.object(run_next_mastering, "state_for", side_effect=lambda n: json.loads(
            (self.root / "reviews" / "mastering" / f"{n:04d}" / "state.json").read_text(encoding="utf-8")
            if (self.root / "reviews" / "mastering" / f"{n:04d}" / "state.json").exists()
            else json.dumps({"stage": "NOT_STARTED"})
        )):
            self.assertEqual(run_next_mastering.next_mastering_chapter(), 4)

    def test_skips_already_promoted_committed_chapters(self):
        (self.root / "translations" / "0003.md").write_text("# Chapter 3\n", encoding="utf-8")
        self.write_primary(3, "COMMITTED")
        self.write_overlay(3, "PROMOTED", True)
        with patch.object(run_next_mastering, "state_for", return_value={"stage": "PROMOTED", "qa_passed": True}):
            self.assertIsNone(run_next_mastering.next_mastering_chapter())

    def test_resumes_mastered_primary_transaction(self):
        (self.root / "translations" / "0005.md").write_text("# Chapter 5\n", encoding="utf-8")
        self.write_primary(5, "MASTERED")
        self.assertEqual(run_next_mastering.next_mastering_chapter(), 5)

    def test_mastered_is_not_a_translation_in_flight_blocker(self):
        self.write_primary(0, "MASTERED")
        self.write_primary(66, "ACCEPTED")
        self.assertEqual(workflow.incomplete_chapter(), 66)
        self.assertEqual(workflow.incomplete_mastering_chapter(), 0)

    def test_blocks_when_translation_checkpoint_window_owns_the_file(self):
        (self.root / "translations" / "0005.md").write_text("# Chapter 5\n", encoding="utf-8")
        self.write_primary(5, "COMMITTED")
        with (
            patch.object(run_next_mastering, "incomplete_chapter", return_value=9),
            patch.object(run_next_mastering, "incomplete_mastering_chapter", return_value=None),
            patch.object(run_next_mastering, "needs_mastering", return_value=True),
            patch.object(
                run_next_mastering,
                "translation_window_paths",
                return_value={"translations/0005.md"},
            ),
        ):
            with self.assertRaisesRegex(SystemExit, "write window"):
                run_next_mastering.next_mastering_chapter()

    def test_require_repository_ignores_sibling_active_overlays(self):
        self.write_overlay(2, "SNAPSHOTTED")
        self.write_overlay(166, "SNAPSHOTTED")
        dirty = [
            "translations/0002.md",
            "reviews/mastering/0002/state.json",
            "translations/0166.md",
            "reviews/mastering/0166/baseline.md",
        ]
        with (
            patch.object(run_next_mastering, "git"),
            patch.object(run_next_mastering, "changed_paths", return_value=dirty),
        ):
            run_next_mastering.require_repository(180, resume=False)


if __name__ == "__main__":
    unittest.main()
