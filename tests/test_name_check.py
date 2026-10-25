"""Precise proper-name checks, the drift scanner, and their final-QA wiring."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tools import final_qa, name_check, name_drift


def write_root(root: Path) -> None:
    (root / "docs").mkdir(parents=True)
    (root / "characters").mkdir()
    (root / "docs" / "NAMES.md").write_text(
        "# Names\n\n| Korean | Preferred English | Notes |\n| --- | --- | --- |\n"
        "| 파이 첸 | **Faye Chen** | S-rank Hunter. |\n"
        "| 진태 | **Jintae** | Five Gates scion. |\n"
        "| 상태 | **Status** | System window. |\n"
        "| 기세 | **aura** / **momentum** | |\n"
        "| 지크프리트 바스만 | **Siegfried Wassmann** | Grand Mage. |\n",
        encoding="utf-8",
    )
    (root / "docs" / "NAME_VARIANTS.md").write_text(
        "| Korean | Preferred English | Wrong variants |\n| --- | --- | --- |\n"
        "| 파이 첸 | Faye Chen | Pai Chen; Pie Chen |\n",
        encoding="utf-8",
    )
    (root / "characters" / "Jin Taekyung.md").write_text(
        "# Jin Taekyung (진태경)\n\n- **Safe through:** Chapter 1\n- **Aliases:** None\n"
        "- **Gender:** male\n- **Role:** Narrator.\n",
        encoding="utf-8",
    )
    (root / "characters" / "Faye Chen.md").write_text(
        "# Faye Chen (파이 첸)\n\n- **Safe through:** Chapter 1\n- **Aliases:** None\n"
        "- **Gender:** female\n- **Role:** S-rank Hunter.\n",
        encoding="utf-8",
    )


def chapter(body: str) -> str:
    return f"# Chapter 1\n\n{body}\n"


class NameBoundaryTest(unittest.TestCase):
    def test_short_key_inside_longer_name_does_not_match(self):
        self.assertFalse(name_check.name_at_boundary("진태경이 웃었다.", "진태"))
        self.assertTrue(name_check.name_at_boundary("진태가 웃었다.", "진태"))
        self.assertTrue(name_check.name_at_boundary("“진태 형님!”", "진태"))

    def test_spaced_name_with_particles_and_honorifics(self):
        self.assertTrue(name_check.name_at_boundary("파이 첸은 웃었다.", "파이 첸"))
        self.assertTrue(name_check.name_at_boundary("파이 첸이라고 했다.", "파이 첸"))
        self.assertTrue(name_check.name_at_boundary("파이 첸 씨는 웃었다.", "파이 첸"))
        self.assertFalse(name_check.name_at_boundary("상태창을 열었다.", "상태"))

    def test_proper_name_classification(self):
        self.assertTrue(name_check.is_proper_name("**Faye Chen**"))
        self.assertTrue(name_check.is_proper_name("**Eighteen Strongholds of Green Forest**"))
        self.assertFalse(name_check.is_proper_name("**grappling technique**"))
        self.assertFalse(name_check.is_proper_name("**aura** / **momentum**"))


class NameCheckTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        write_root(self.root)
        self.entries = name_check.proper_name_entries(self.root)

    def tearDown(self):
        self.temporary.cleanup()

    def check(self, source: str, translation: str) -> dict:
        return name_check.check_names(source, translation, self.entries)

    def test_entries_include_spaced_keys_and_people(self):
        by_korean = {item["korean"]: item for item in self.entries}
        self.assertEqual(by_korean["파이 첸"]["kind"], "person")
        self.assertEqual(by_korean["파이 첸"]["variants"], ["Pai Chen", "Pie Chen"])
        self.assertEqual(by_korean["지크프리트 바스만"]["english"], "Siegfried Wassmann")
        self.assertNotIn("기세", by_korean)

    def test_known_wrong_variant_is_an_error(self):
        result = self.check("파이 첸이 웃었다.", "Pai Chen smiled. Pai Chen’s hand rose.")
        self.assertEqual([item["code"] for item in result["errors"]], ["name_variant"])
        self.assertEqual(result["errors"][0]["details"]["found"], ["Pai Chen"])

    def test_known_variant_without_korean_name_is_ignored(self):
        result = self.check("그녀가 웃었다.", "Pai Chen smiled.")
        self.assertEqual(result, {"errors": [], "warnings": []})

    def test_preferred_rendering_passes(self):
        result = self.check("파이 첸이 웃었다.", "Faye Chen smiled. Faye Chen’s hand rose.")
        self.assertEqual(result, {"errors": [], "warnings": []})

    def test_uncurated_similar_spelling_is_a_suspect_warning(self):
        result = self.check("파이 첸이 웃었다.", "S-rank Hunter Pi Chen smiled.")
        self.assertEqual(result["errors"], [])
        self.assertEqual([item["code"] for item in result["warnings"]], ["name_variant_suspect"])
        self.assertEqual(result["warnings"][0]["details"]["found"], ["Pi Chen"])

        result = self.check("지크프리트 바스만이 웃었다.", "Siegfried Bassman smiled.")
        self.assertEqual(result["warnings"][0]["details"]["found"], ["Siegfried Bassman"])

    def test_common_word_and_plural_are_not_drift(self):
        result = self.check("상태가 좋다. 진태경이 웃었다.", "The States are fine. Jin Taekyung smiled.")
        self.assertEqual(result, {"errors": [], "warnings": []})

    def test_absent_profiled_name_is_a_warning(self):
        result = self.check("진태경이 웃었다.", "He smiled.")
        self.assertEqual([item["code"] for item in result["warnings"]], ["name_absent"])

    def test_name_corrections_lists_baseline_variants(self):
        corrections = name_check.name_corrections("파이 첸이 웃었다.", "Pie Chen smiled.", self.entries)
        self.assertEqual(corrections, [{"korean": "파이 첸", "preferred": "Faye Chen", "found": ["Pie Chen"]}])


class FinalQaNameTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        write_root(self.root)
        self.entries = name_check.proper_name_entries(self.root)
        self.source = "파이 첸이 웃었다. 상태창이 떴다. " * 8

    def tearDown(self):
        self.temporary.cleanup()

    def assess(self, candidate: str) -> dict:
        return final_qa.assess(
            1,
            self.source,
            candidate,
            candidate,
            [("상태", "**Status**"), ("파이 첸", "**Faye Chen**")],
            min_baseline_preserved=0.8,
            name_entries=self.entries,
        )

    def test_wrong_variant_blocks_final_qa(self):
        qa = self.assess(chapter("Pai Chen smiled at the window. " * 10))
        self.assertFalse(qa["passed"])
        self.assertTrue(any(item["code"] == "name_variant" for item in qa["errors"]))

    def test_noisy_terminology_warning_is_replaced(self):
        qa = self.assess(chapter("Faye Chen smiled at the window. " * 10))
        self.assertTrue(qa["passed"], qa["errors"])
        self.assertFalse(any(item["code"] == "terminology" for item in qa["warnings"]))
        self.assertFalse(any(item["code"].startswith("name_") for item in qa["warnings"]))


class NameDriftScanTest(unittest.TestCase):
    def test_scan_groups_chapters_by_name_and_variant(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            write_root(root)
            (root / "source").mkdir()
            (root / "translations").mkdir()
            for number, english in ((1, "Faye Chen"), (2, "Pai Chen"), (3, "Pai Chen"), (4, "Pi Chen")):
                (root / "source" / f"{number:04d}.txt").write_text("파이 첸이 웃었다.", encoding="utf-8")
                (root / "translations" / f"{number:04d}.md").write_text(
                    chapter(f"{english} smiled."), encoding="utf-8"
                )
            (root / "translations" / "0002_v2.md").write_text("Pie Chen", encoding="utf-8")
            final = root / "reviews" / "final" / "0002"
            final.mkdir(parents=True)
            (final / "state.json").write_text(
                json.dumps({"stage": "PROMOTED", "qa_passed": True}), encoding="utf-8"
            )
            report = name_drift.scan(root)
        self.assertEqual(report["chapters_scanned"], 4)
        variant = report["groups"]["name_variant"]
        self.assertEqual(len(variant), 1)
        self.assertEqual(variant[0]["chapters"], [2, 3])
        self.assertEqual(variant[0]["pending_final"], [3])
        suspect = report["groups"]["name_variant_suspect"]
        self.assertEqual([(row["found"], row["chapters"]) for row in suspect], [(["Pi Chen"], [4])])
        text = name_drift.render(report)
        self.assertIn("| 파이 첸 | Faye Chen | Pai Chen | 2, 3 | 3 |", text)


if __name__ == "__main__":
    unittest.main()
