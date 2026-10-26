"""Entity consistency pass: prefilter, validation, escalation, apply, paths, locks."""

from __future__ import annotations

import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools import entity_pass, run_entity_pass
from tools.run_lock import (
    ADDRESS_LOCK_ENV,
    ENTITY_LOCK_ENV,
    FINAL_LOCK_ENV,
    LOCK_ENV,
    hold_address_lock,
    hold_entity_lock,
    hold_final_lock,
    hold_run_lock,
    lock_is_live,
)

CFG = {
    "escalate_below_confidence": 0.9,
    "auto_apply_min_confidence": 0.9,
    "max_changed_chars": 120,
    "min_baseline_preserved": 0.97,
}
SOURCE = "그녀는 활을 당겼다. 궁성이 웃었다. 진태경이 말했다."
TEXT = "# Chapter 1\n\nThe Bow Saint drew his bow.\n\nJin Taekyung spoke.\n"
CARDS = [
    {"english": "Bow Saint", "english_names": ["Bow Saint"], "korean_names": ["궁성"], "gender": "female"},
    {"english": "Jin Taekyung", "english_names": ["Jin Taekyung", "Taekyung"], "korean_names": ["진태경"], "gender": "male"},
]


def raw_finding(**overrides) -> dict:
    value = {
        "category": "gender",
        "current": "drew his bow",
        "replacement": "drew her bow",
        "korean": "그녀는 활을 당겼다",
        "explanation": "The Bow Saint is a woman.",
        "confidence": 0.95,
    }
    value.update(overrides)
    return value


class PrefilterTest(unittest.TestCase):
    def test_opposite_pronoun_near_name_is_flagged(self):
        flags = entity_pass.pronoun_conflicts(TEXT, CARDS)
        self.assertEqual([flag["character"] for flag in flags], ["Bow Saint"])
        self.assertEqual(flags[0]["pronouns"], ["his"])

    def test_matching_pronoun_is_not_flagged(self):
        text = "The Bow Saint drew her bow.\n"
        self.assertEqual(entity_pass.pronoun_conflicts(text, CARDS), [])

    def test_window_naming_another_character_is_skipped(self):
        text = "The Bow Saint watched Jin Taekyung raise his sword.\n"
        self.assertEqual(entity_pass.pronoun_conflicts(text, CARDS), [])

    def test_quoted_speech_is_ignored(self):
        text = "The Bow Saint said, “He is late.”\n"
        self.assertEqual(entity_pass.pronoun_conflicts(text, CARDS), [])

    def test_noise_patterns_are_not_flagged(self):
        for text in (
            "Jin Taekyung gave her a sheepish smile.",
            "Jin Taekyung called one of them over and began speaking to her in Chinese.",
            "At the Bow Saint’s words, the leader bowed his head.",
            "Unlike the Bow Saint, he already knew everything.",
            "The Bow Saint’s gaze followed his hand.",
            "The Bow Saint understood how he felt.",
            "The Bow Saint watched the old man raise his cup.",
            "The Bow Saint smiled at Lee Cheonbaek as he left.",
        ):
            self.assertEqual(entity_pass.pronoun_conflicts(text, CARDS), [], text)

    def test_following_subject_pronoun_is_flagged(self):
        flags = entity_pass.pronoun_conflicts("The Bow Saint nodded. He smiled.", CARDS)
        self.assertEqual(flags[0]["pronouns"], ["he"])

    def test_unknown_gender_is_never_flagged(self):
        cards = [{**CARDS[0], "gender": "unknown"}]
        self.assertEqual(entity_pass.pronoun_conflicts(TEXT, cards), [])

    def test_name_variant_and_absent_term_flags(self):
        entries = [
            {"korean": "파이 첸", "english": "Faye Chen", "kind": "person", "variants": ["Pai Chen"]},
            {"korean": "남천마교", "english": "Southern Heaven Demonic Cult", "kind": "ledger", "variants": []},
        ]
        source = "파이 첸이 남천마교를 봤다."
        text = "Pai Chen looked at the cult.\n"
        report = entity_pass.prefilter(source, text, cards=[], entries=entries)
        self.assertEqual(report["counts"]["name_variant"], 1)
        self.assertEqual(report["counts"]["term_absent"], 1)
        self.assertTrue(report["flagged"])


class ValidationTest(unittest.TestCase):
    def test_valid_detection_is_numbered_and_annotated(self):
        result = entity_pass.validate_detection({"findings": [raw_finding()], "uncertain": False}, SOURCE, TEXT)
        finding = result["findings"][0]
        self.assertEqual(finding["id"], "E01")
        self.assertEqual(finding["span_count"], 1)
        self.assertTrue(finding["evidence_found"])

    def test_invalid_findings_raise(self):
        for bad in (
            raw_finding(category="style"),
            raw_finding(confidence=1.5),
            raw_finding(confidence=True),
            raw_finding(replacement="drew his bow"),
            raw_finding(replacement="drew 그녀 bow"),
            raw_finding(korean=""),
        ):
            with self.assertRaises(ValueError):
                entity_pass.validate_detection({"findings": [bad]}, SOURCE, TEXT)

    def test_uncertain_must_be_boolean(self):
        with self.assertRaises(ValueError):
            entity_pass.validate_detection({"findings": [], "uncertain": "maybe"}, SOURCE, TEXT)

    def test_escalation_requires_one_decision_per_id(self):
        with self.assertRaises(ValueError):
            entity_pass.validate_escalation({"decisions": [], "added": []}, ["E01"], SOURCE, TEXT)
        with self.assertRaises(ValueError):
            entity_pass.validate_escalation(
                {"decisions": [{"id": "E01", "verdict": "amend", "confidence": 0.9}], "added": []},
                ["E01"], SOURCE, TEXT,
            )
        value = entity_pass.validate_escalation(
            {"decisions": [{"id": "E01", "verdict": "confirm", "confidence": 0.96, "reason": "explicit"}],
             "added": [raw_finding(current="Jin Taekyung spoke", replacement="The Bow Saint spoke",
                                   category="referent", korean="궁성이 웃었다")]},
            ["E01"], SOURCE, TEXT,
        )
        self.assertEqual(value["added"][0]["id"], "S01")


class EscalationTest(unittest.TestCase):
    def detection(self, *findings, uncertain=False):
        return entity_pass.validate_detection({"findings": list(findings), "uncertain": uncertain}, SOURCE, TEXT)

    def test_only_low_confidence_or_unlocatable_findings_escalate(self):
        detection = self.detection(
            raw_finding(),
            raw_finding(current="Jin Taekyung spoke", replacement="The Bow Saint spoke",
                        category="referent", confidence=0.6),
            raw_finding(current="his missing bow", replacement="her missing bow"),
            raw_finding(current="Jin Taekyung spoke", replacement="Jin Wikyung spoke", category="name",
                        korean="없는 말"),
        )
        self.assertEqual(entity_pass.select_escalation(detection, CFG), ["E02", "E03", "E04"])

    def test_escalate_all_findings_sends_every_finding(self):
        detection = self.detection(raw_finding())
        cfg = {**CFG, "escalate_all_findings": True}
        self.assertEqual(entity_pass.select_escalation(detection, cfg), ["E01"])
        self.assertFalse(entity_pass.needs_escalation(self.detection(), cfg))

    def test_uncertain_chapter_escalates_everything(self):
        detection = self.detection(raw_finding(), uncertain=True)
        self.assertEqual(entity_pass.select_escalation(detection, CFG), ["E01"])
        self.assertTrue(entity_pass.needs_escalation(self.detection(uncertain=True), CFG))
        self.assertFalse(entity_pass.needs_escalation(self.detection(raw_finding()), CFG))

    def test_resolve_applies_verdicts(self):
        detection = self.detection(
            raw_finding(),
            raw_finding(current="Jin Taekyung spoke", replacement="The Bow Saint spoke",
                        category="referent", korean="진태경이 말했다", confidence=0.5),
        )
        escalation = {"decisions": [{"id": "E02", "verdict": "reject", "confidence": 0.9, "reason": "fine"}],
                      "added": []}
        findings = entity_pass.resolve(detection, escalation, ["E02"], CFG, SOURCE, TEXT)
        self.assertEqual([item["status"] for item in findings], ["auto", "rejected"])

    def test_amended_finding_uses_new_span(self):
        detection = self.detection(raw_finding(current="his bow", replacement="her bow", confidence=0.5))
        escalation = {"decisions": [{"id": "E01", "verdict": "amend", "confidence": 0.95, "reason": "x",
                                     "current": "drew his bow", "replacement": "drew her bow"}], "added": []}
        findings = entity_pass.resolve(detection, escalation, ["E01"], CFG, SOURCE, TEXT)
        self.assertEqual((findings[0]["status"], findings[0]["current"]), ("auto", "drew his bow"))


class ScopeTest(unittest.TestCase):
    def scope(self, **overrides):
        return entity_pass.validate_detection({"findings": [raw_finding(**overrides)]}, SOURCE, TEXT)["findings"][0]

    def test_pronoun_and_speaker_fixes_are_in_scope(self):
        self.assertEqual(self.scope()["scope"], "entity")
        swap = self.scope(category="referent", current="I won’t let go!", replacement="You won’t let go!")
        self.assertEqual(swap["scope"], "entity")
        agreement = self.scope(category="referent", current="ever since you were young",
                               replacement="ever since I was young")
        self.assertEqual(agreement["scope"], "entity")

    def test_term_and_title_renames_are_out_of_scope(self):
        for overrides in (
            {"category": "title", "current": "Novice Trainee", "replacement": "Beginner Trainee"},
            {"category": "term", "current": "Novice Trainee", "replacement": "Beginner Trainee"},
            {"category": "name", "current": "the Universal Language Pack", "replacement": "the Unified Language Pack"},
            {"category": "referent", "current": "Jin Wikyung, the Lesser Family Head",
             "replacement": "Jin Wikyung, the Young Sect Leader"},
            {"category": "gender", "current": "drew his bow", "replacement": "drew her longbow"},
            {"category": "name", "current": "The masked man smiled", "replacement": "The Masked Man smiled"},
        ):
            self.assertEqual(self.scope(**overrides)["scope"], "term", overrides)

    def test_identity_needs_a_different_person_or_known_variant(self):
        other = self.scope(category="name", current="Jin Taekyung answered", replacement="Jin Wikyung answered")
        self.assertEqual(other["scope"], "entity")
        source = "파이 첸이 웃었다."
        value = {"findings": [raw_finding(category="identity", current="Pai Chen smiled",
                                          replacement="Faye Chen smiled", korean="파이 첸이 웃었다")]}
        variant = entity_pass.validate_detection(value, source, "Pai Chen smiled.")["findings"][0]
        self.assertEqual(variant["scope"], "entity")

    def test_term_findings_are_reported_never_applied_or_escalated(self):
        detection = entity_pass.validate_detection({"findings": [
            raw_finding(category="title", current="Novice Trainee", replacement="Beginner Trainee", confidence=0.5),
        ]}, SOURCE, "Novice Trainee " + TEXT)
        self.assertEqual(entity_pass.select_escalation(detection, CFG), [])
        findings = entity_pass.resolve(detection, None, [], CFG, SOURCE, "Novice Trainee " + TEXT)
        self.assertEqual(findings[0]["status"], "term")
        report = entity_pass.report_markdown(1, findings, detection, None, {"flags": []}, False)
        self.assertIn("## Term mismatch (not applied) (1)", report)


class ScreenAndApplyTest(unittest.TestCase):
    def finding(self, identifier="E01", **overrides):
        value = {**raw_finding(), "id": identifier, "status": "auto", "reason": "", "evidence_found": True}
        value.update(overrides)
        return value

    def test_gender_fix_without_gendered_korean_goes_to_human(self):
        findings = entity_pass.screen([self.finding(korean="궁성이 웃었다")], CFG, TEXT)
        self.assertEqual(findings[0]["status"], "human")

    def test_footnote_definition_only_takes_gender_or_name(self):
        text = TEXT + "\n[^1]: The Bow Saint is his elder.\n"
        kinship = self.finding(category="kinship", current="his elder", replacement="his junior")
        gender = self.finding(identifier="E02", current="is his elder", replacement="is her elder")
        findings = entity_pass.screen([kinship], CFG, text)
        self.assertEqual(findings[0]["status"], "human")
        findings = entity_pass.screen([gender], CFG, text)
        self.assertEqual(findings[0]["status"], "auto")

    def test_footnote_reference_must_survive(self):
        text = "He drew his bow[^1].\n"
        finding = self.finding(current="his bow[^1]", replacement="her bow")
        self.assertEqual(entity_pass.screen([finding], CFG, text)[0]["status"], "human")

    def test_large_rewrite_goes_to_human(self):
        finding = self.finding(current="The Bow Saint drew his bow.",
                               replacement="Something else entirely happened in this scene, at great length, " * 3)
        self.assertEqual(entity_pass.screen([finding], CFG, TEXT)[0]["status"], "human")

    def test_overlapping_findings_both_go_to_human(self):
        findings = entity_pass.screen(
            [self.finding(), self.finding("E02", current="his bow", replacement="her bow")], CFG, TEXT,
        )
        self.assertEqual([item["status"] for item in findings], ["human", "human"])

    def test_apply_is_atomic(self):
        good = self.finding()
        other = self.finding("E02", current="Jin Taekyung spoke", replacement="The Bow Saint spoke")
        self.assertIn("drew her bow", entity_pass.apply_findings(TEXT, [good, other]))
        self.assertIn("The Bow Saint spoke", entity_pass.apply_findings(TEXT, [good, other]))
        for bad in (
            [good, self.finding("E02", current="nowhere")],
            [good, self.finding("E02", current="o")],
            [good, self.finding("E02", current="his bow", replacement="her bow")],
        ):
            with self.assertRaises(ValueError):
                entity_pass.apply_findings(TEXT, bad)

    def test_qa_blocks_only_new_errors(self):
        baseline = "# Chapter 1\n\n" + "The hall was quiet. " * 10 + "\n"
        source = "가" * 120
        same = entity_pass.entity_qa(1, source, baseline, baseline.replace("hall", "room", 1), [], CFG)
        self.assertTrue(same["passed"])
        broken = entity_pass.entity_qa(1, source, baseline, baseline + '\n"straight"\n', [], CFG)
        self.assertFalse(broken["passed"])


class PathsAndLocksTest(unittest.TestCase):
    def test_entity_owns_only_its_chapter(self):
        self.assertTrue(entity_pass.entity_owns_path("translations/0012.md", 12))
        self.assertTrue(entity_pass.entity_owns_path("reviews/entity/0012/result.json", 12))
        self.assertFalse(entity_pass.entity_owns_path("reviews/entity/0013/result.json", 12))
        self.assertFalse(entity_pass.entity_owns_path("reviews/metrics/0012.json", 12))

    def test_unexpected_paths_refuse_other_harness_files(self):
        dirty = [
            "translations/0012.md",
            "reviews/entity/0012/state.json",
            "translations/0099.md",
            "docs/NAMES.md",
            "tools/scratch.py",
        ]
        with patch.object(run_entity_pass, "foreign_entity_paths", return_value=set()), \
                patch("tools.run_next.foreign_master_paths", return_value=set()), \
                patch("tools.final_touches.foreign_final_paths", return_value=set()):
            self.assertEqual(run_entity_pass.allowed_paths(12, dirty),
                             {"translations/0012.md", "reviews/entity/0012/state.json"})
            self.assertEqual(run_entity_pass.unexpected_paths(12, dirty), ["translations/0099.md", "docs/NAMES.md"])

    def test_other_queues_ignore_entity_paths(self):
        with patch.object(entity_pass, "active_entity_chapters", return_value=[7]):
            foreign = entity_pass.foreign_entity_paths(
                ["reviews/entity/0005/state.json", "translations/0007.md", "translations/0008.md"]
            )
        self.assertEqual(foreign, {"reviews/entity/0005/state.json", "translations/0007.md"})

    def test_selection_skips_unfinalized_and_done_chapters(self):
        with patch.object(run_entity_pass, "final_promoted", side_effect=lambda n: n != 2), \
                patch.object(run_entity_pass, "load_state",
                             side_effect=lambda n: {"stage": "COMMITTED" if n == 3 else "NOT_STARTED"}):
            chosen, notes = run_entity_pass.select_chapters(1, 4, [])
        self.assertEqual(chosen, [1, 4])
        self.assertEqual(notes, ["chapter 2: final touches not PROMOTED"])


class LockRefusalTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.saved = {key: os.environ.pop(key, None) for key in (LOCK_ENV, FINAL_LOCK_ENV, ENTITY_LOCK_ENV, ADDRESS_LOCK_ENV)}

    def tearDown(self):
        for key, value in self.saved.items():
            os.environ.pop(key, None)
            if value is not None:
                os.environ[key] = value
        self.temporary.cleanup()

    def test_refuses_while_final_translation_or_address_lock_is_live(self):
        run_entity_pass.refuse_live_locks(self.root)
        for hold in (hold_final_lock, hold_run_lock, hold_address_lock):
            with hold(self.root, holder="test"):
                with self.assertRaises(SystemExit):
                    run_entity_pass.refuse_live_locks(self.root)
            run_entity_pass.refuse_live_locks(self.root)

    def test_entity_lock_is_exclusive(self):
        with hold_entity_lock(self.root, holder="test"):
            self.assertTrue(lock_is_live(self.root, "entity.lock"))
        self.assertFalse(lock_is_live(self.root, "entity.lock"))


class EstimateTest(unittest.TestCase):
    def test_estimate_scales_with_chapters_and_escalation(self):
        records = [{"packet_tokens": 10000, "flagged": index < 5} for index in range(10)]
        cfg = {"estimate": {"escalation_rate_scenarios": [0.2]}}
        est = entity_pass.estimate(records, cfg, workers=2)
        self.assertEqual(est["detector_usd"], [0.03, 0.06])
        rates = {row["escalation_rate"]: row for row in est["scenarios"]}
        self.assertEqual(rates[0.5]["escalated_chapters"], 5)
        self.assertEqual(rates[0.5]["usd_low"], 0.33)


if __name__ == "__main__":
    unittest.main()
