import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools import expedition


def write_fixture(root: Path, *, start=370, seed=369, completed=369, next_chapter=370):
    (root / "docs").mkdir()
    (root / "source").mkdir()
    (root / "translations").mkdir()
    (root / "docs" / "expedition-parked").mkdir()
    (root / "docs" / "expedition.json").write_text(json.dumps({
        "version": 1,
        "mode": "expedition",
        "start_chapter": start,
        "seed_safe_through": seed,
        "skipped_ranges": [],
        "parked_progress": {
            "from_chapter": 374,
            "through_chapter": 375,
            "context": "docs/expedition-parked/CONTEXT-0375.json",
            "state": "docs/expedition-parked/STATE-0375.md",
        },
        "canonical_anchor": {},
        "pages_repository": "owner/pages",
        "pages_event": "expedition-publish",
        "release_tag": "expedition-ebook",
    }), encoding="utf-8")
    (root / "docs" / "STATE.md").write_text(
        f"- Last completed: {completed}\n- Next chapter: {next_chapter}\n",
        encoding="utf-8",
    )
    (root / "docs" / "CONTEXT.json").write_text(
        json.dumps({"safe_through": seed}), encoding="utf-8"
    )
    (root / "docs" / "EXPEDITION.md").write_text("instructions", encoding="utf-8")
    (root / "docs" / "EXPEDITION_SEED.md").write_text("seed", encoding="utf-8")
    (root / "source" / f"{start:04d}.txt").write_text("source", encoding="utf-8")
    (root / "translations" / "0374.md").write_text("# Chapter 374\n", encoding="utf-8")
    (root / "translations" / "0375.md").write_text("# Chapter 375\n", encoding="utf-8")
    (root / "docs" / "expedition-parked" / "CONTEXT-0375.json").write_text(
        json.dumps({"safe_through": 375}), encoding="utf-8"
    )
    (root / "docs" / "expedition-parked" / "STATE-0375.md").write_text(
        "- Last completed: 375\n- Next chapter: 376\n", encoding="utf-8"
    )


class ExpeditionTest(unittest.TestCase):
    def test_check_accepts_seeded_expedition(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root)
            with patch.object(expedition, "ROOT", root):
                result = expedition.check()
            self.assertEqual(result["start_chapter"], 370)
            self.assertEqual(result["parked_through"], 375)

    def test_check_rejects_wrong_next_chapter(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root, next_chapter=375)
            with patch.object(expedition, "ROOT", root):
                with self.assertRaisesRegex(SystemExit, "expedition state"):
                    expedition.check()

    def test_resume_parked_restores_375_state(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root, completed=373, next_chapter=374)
            for chapter in range(370, 374):
                (root / "translations" / f"{chapter:04d}.md").write_text(
                    f"# Chapter {chapter}\n", encoding="utf-8"
                )
            with patch.object(expedition, "ROOT", root):
                result = expedition.resume_parked()
                self.assertEqual(result["restored_completed"], 375)
                self.assertEqual(result["restored_next"], 376)
                expedition.check()
            state = (root / "docs" / "STATE.md").read_text(encoding="utf-8")
            self.assertIn("Last completed: 375", state)


if __name__ == "__main__":
    unittest.main()
