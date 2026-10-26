"""Address pass: rule extraction, validation, span screening, paths, locks, estimate."""

from __future__ import annotations

import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools import address_pass, run_address_pass
from tools.run_lock import (
    ADDRESS_LOCK_ENV,
    ENTITY_LOCK_ENV,
    FINAL_LOCK_ENV,
    LOCK_ENV,
    MASTER_LOCK_ENV,
    hold_address_lock,
    hold_entity_lock,
    hold_final_lock,
    hold_master_lock,
    hold_run_lock,
    lock_is_live,
)

CFG = {
    "terms": {"소협": "Young Hero"},
    "auto_apply_min_confidence": 0.8,
    "max_changed_chars": 40,
    "edit_window_chars": 24,
    "min_baseline_preserved": 0.97,
}
SOURCE = "“궁 소협, 같이 가자.” 궁 소협이 웃었다. “진 소협, 처음 뵙겠습니다.”"
TEXT = (
    "# Chapter 1\n\n"
    "“Young Hero Gung, let’s go together.”\n\n"
    "Young Hero Gung laughed.\n\n"
    "“Young Hero Jin, it’s an honor to meet you.”\n\n"
    "[^1]: Young Hero Gung is a note.\n"
)


def raw_finding(**overrides) -> dict:
    value = {
        "use": "third_person",
        "current": "Young Hero Gung laughed.",
        "replacement": "Gung Gibang laughed.",
        "korean": "궁 소협이 웃었다",
        "speaker": "narration",
        "addressee": "Gung Gibang",
        "reason": "Narration refers to him; nobody is addressed.",
        "confidence": 0.95,
    }
    value.update(overrides)
    return value


def screened(**overrides) -> dict:
    detection = address_pass.validate_detection({"findings": [raw_finding(**overrides)]}, SOURCE, TEXT, CFG)
    return address_pass.screen(detection["findings"], CFG, TEXT)[0]


class RuleTest(unittest.TestCase):
    def test_rule_comes_from_rules_md_address_section(self):
        rule = address_pass.rule_text()
        self.assertIn("소협", rule)
        self.assertIn("Young Hero Taishan", rule)
        self.assertNotIn("## English and Markdown", rule)

    def test_config_loads_and_names_a_model(self):
        cfg = address_pass.load_config()
        self.assertTrue(cfg["model"])
        self.assertEqual(cfg["terms"], {"소협": "Young Hero"})

    def test_packet_lists_occurrences_and_korean_lines(self):
        packet = address_pass.build_packet(1, SOURCE, TEXT, CFG, [], "(No matching address pairs.)")
        self.assertIn("- line 3: “Young Hero Gung, let’s go together.”", packet)
        self.assertIn("궁 소협이 웃었다", packet)
        self.assertIn("## The rule", packet)


class ValidationTest(unittest.TestCase):
    def test_valid_finding_is_auto(self):
        finding = screened()
        self.assertEqual(finding["status"], "auto", finding.get("reason_status"))
        self.assertTrue(finding["evidence_found"])

    def test_invalid_use_and_hangul_are_rejected(self):
        with self.assertRaises(ValueError):
            address_pass.validate_detection({"findings": [raw_finding(use="style")]}, SOURCE, TEXT, CFG)
        with self.assertRaises(ValueError):
            address_pass.validate_detection({"findings": [raw_finding(replacement="궁 laughed.")]}, SOURCE, TEXT, CFG)
        with self.assertRaises(ValueError):
            address_pass.validate_detection({"findings": [raw_finding(confidence=2)]}, SOURCE, TEXT, CFG)

    def test_repeated_span_goes_to_human(self):
        self.assertIn("occurs", screened(current="Young Hero Gung", replacement="Gung")["reason_status"])

    def test_span_without_address_phrase_goes_to_human(self):
        finding = screened(current="laughed.", replacement="chuckled.")
        self.assertEqual(finding["status"], "human")

    def test_korean_without_address_word_goes_to_human(self):
        self.assertEqual(screened(korean="웃었다")["reason_status"], "Korean evidence has no address word")

    def test_missing_korean_evidence_goes_to_human(self):
        self.assertEqual(screened(korean="궁 소협이 울었다")["reason_status"], "Korean evidence is not in the source")

    def test_low_confidence_goes_to_human(self):
        self.assertIn("below", screened(confidence=0.5)["reason_status"])

    def test_edit_beyond_the_phrase_goes_to_human(self):
        current = "“Young Hero Jin, it’s an honor to meet you.”"
        finding = screened(current=current, replacement="“Jin, it’s an honor to meet you, truly, my friend.”",
                           korean="진 소협")
        self.assertEqual(finding["status"], "human")

    def test_footnote_definition_is_not_touched(self):
        finding = screened(current="[^1]: Young Hero Gung is", replacement="[^1]: Gung is", korean="궁 소협")
        self.assertEqual(finding["reason_status"], "span touches a footnote definition")

    def test_overlapping_findings_both_go_to_human(self):
        detection = address_pass.validate_detection({"findings": [
            raw_finding(),
            raw_finding(current="Young Hero Gung laughed", replacement="Gung laughed"),
        ]}, SOURCE, TEXT, CFG)
        statuses = {item["status"] for item in address_pass.screen(detection["findings"], CFG, TEXT)}
        self.assertEqual(statuses, {"human"})

    def test_edits_local(self):
        pattern = address_pass.phrase_pattern(CFG)
        self.assertTrue(address_pass.edits_local("“Young Hero Gung, you…”", "“Gung, you…”", pattern, 24))
        self.assertFalse(address_pass.edits_local(
            "Young Hero Gung said that the river was cold today.",
            "Young Hero Gung said that the river was warm today.", pattern, 10,
        ))


class DiffTest(unittest.TestCase):
    def test_diff_shows_old_and_new_lines(self):
        finding = screened()
        new = TEXT.replace("Young Hero Gung laughed.", "Gung Gibang laughed.")
        text = address_pass.diff_markdown(1, TEXT, new, [finding])
        self.assertIn("- Young Hero Gung laughed.", text)
        self.assertIn("+ Gung Gibang laughed.", text)
        self.assertIn("**A01** third_person", text)


class PathsTest(unittest.TestCase):
    def test_address_owns_only_its_chapter(self):
        self.assertTrue(address_pass.address_owns_path("translations/0012.md", 12))
        self.assertTrue(address_pass.address_owns_path("reviews/address/0012/result.json", 12))
        self.assertFalse(address_pass.address_owns_path("reviews/address/0013/result.json", 12))
        self.assertFalse(address_pass.address_owns_path("reviews/entity/0012/result.json", 12))

    def test_unexpected_paths_refuse_other_harness_files(self):
        dirty = [
            "translations/0012.md",
            "reviews/address/0012/state.json",
            "translations/0099.md",
            "docs/NAMES.md",
            "tools/scratch.py",
        ]
        with patch("tools.address_pass.foreign_address_paths", return_value=set()), \
                patch("tools.entity_pass.foreign_entity_paths", return_value=set()), \
                patch("tools.run_next.foreign_master_paths", return_value=set()), \
                patch("tools.final_touches.foreign_final_paths", return_value=set()):
            self.assertEqual(run_address_pass.allowed_paths(12, dirty),
                             {"translations/0012.md", "reviews/address/0012/state.json"})
            self.assertEqual(run_address_pass.unexpected_paths(12, dirty), ["translations/0099.md", "docs/NAMES.md"])

    def test_selection_skips_unfinished_and_entity_in_flight(self):
        with patch.object(run_address_pass, "load_state", return_value={"stage": "NOT_STARTED"}), \
                patch.object(run_address_pass, "final_promoted", side_effect=lambda n: n != 2), \
                patch.object(run_address_pass, "entity_in_flight", side_effect=lambda n: n == 3):
            chosen, notes = run_address_pass.select_chapters([1, 2, 3], [])
        self.assertEqual(chosen, [1])
        self.assertEqual(len(notes), 2)


class LockRefusalTest(unittest.TestCase):
    KEYS = (LOCK_ENV, MASTER_LOCK_ENV, FINAL_LOCK_ENV, ENTITY_LOCK_ENV, ADDRESS_LOCK_ENV)

    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.saved = {key: os.environ.pop(key, None) for key in self.KEYS}

    def tearDown(self):
        for key, value in self.saved.items():
            os.environ.pop(key, None)
            if value is not None:
                os.environ[key] = value
        self.temporary.cleanup()

    def test_refuses_while_any_work_lock_is_live(self):
        run_address_pass.refuse_live_locks(self.root)
        for hold in (hold_entity_lock, hold_final_lock, hold_run_lock, hold_master_lock):
            with hold(self.root, holder="test"):
                with self.assertRaises(SystemExit):
                    run_address_pass.refuse_live_locks(self.root)
            run_address_pass.refuse_live_locks(self.root)

    def test_address_lock_is_exclusive(self):
        with hold_address_lock(self.root, holder="test"):
            self.assertTrue(lock_is_live(self.root, "address.lock"))
        self.assertFalse(lock_is_live(self.root, "address.lock"))


class EstimateTest(unittest.TestCase):
    def test_estimate_is_one_call_per_chapter(self):
        records = [{"packet_tokens": 10000, "korean": 2, "english": 2, "final_promoted": True} for _ in range(10)]
        est = address_pass.estimate(records, {"estimate": {"usd_per_1k_packet_tokens": [0.003, 0.006],
                                                           "seconds_per_chapter": 36}}, workers=2)
        self.assertEqual(est["model_calls"], 10)
        self.assertEqual(est["usd"], [0.3, 0.6])
        self.assertEqual(est["hours"], 0.1)


if __name__ == "__main__":
    unittest.main()
