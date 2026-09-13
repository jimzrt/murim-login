import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools import expedition


class ExpeditionTest(unittest.TestCase):
    def test_check_accepts_seeded_expedition(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "docs").mkdir()
            (root / "source").mkdir()
            (root / "summaries" / "beats").mkdir(parents=True)
            (root / "docs" / "expedition.json").write_text(json.dumps({
                "version": 1,
                "mode": "expedition",
                "start_chapter": 374,
                "seed_safe_through": 373,
                "skipped_ranges": [],
                "canonical_anchor": {},
                "pages_repository": "owner/pages",
                "pages_event": "expedition-publish",
                "release_tag": "expedition-ebook",
            }), encoding="utf-8")
            (root / "docs" / "STATE.md").write_text(
                "- Last completed: 373\n- Next chapter: 374\n", encoding="utf-8"
            )
            (root / "docs" / "CONTEXT.json").write_text(
                json.dumps({"safe_through": 373}), encoding="utf-8"
            )
            (root / "docs" / "EXPEDITION.md").write_text("instructions", encoding="utf-8")
            (root / "docs" / "EXPEDITION_SEED.md").write_text("seed", encoding="utf-8")
            (root / "source" / "0374.txt").write_text("source", encoding="utf-8")
            for chapter in (371, 372, 373):
                (root / "summaries" / "beats" / f"{chapter:04d}.md").write_text("beat", encoding="utf-8")
            with patch.object(expedition, "ROOT", root):
                result = expedition.check()
            self.assertEqual(result["start_chapter"], 374)

    def test_check_rejects_wrong_next_chapter(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "docs").mkdir()
            (root / "docs" / "expedition.json").write_text(json.dumps({
                "version": 1, "mode": "expedition", "start_chapter": 374,
                "seed_safe_through": 373, "skipped_ranges": [],
                "canonical_anchor": {}, "pages_repository": "owner/pages",
                "pages_event": "expedition-publish", "release_tag": "expedition-ebook",
            }), encoding="utf-8")
            (root / "docs" / "STATE.md").write_text(
                "- Last completed: 373\n- Next chapter: 375\n", encoding="utf-8"
            )
            with patch.object(expedition, "ROOT", root):
                with self.assertRaisesRegex(SystemExit, "expedition state"):
                    expedition.check()


if __name__ == "__main__":
    unittest.main()
