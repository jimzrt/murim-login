import unittest

from tools.model_io import (
    apply_review_replacements,
    blocking_dispositions,
    extract_reading_copy,
    parse_json_object,
    validate_patchset,
    validate_range_review,
    validate_review,
    validate_durable_update,
)


class ModelIoTest(unittest.TestCase):
    def review(self):
        return validate_review({
            "summary": "One problem.",
            "findings": [{
                "id": "F01", "severity": "major", "source": "원문",
                "current": "Current.", "defect": "Wrong subject.",
                "replacement": "Corrected.", "rationale": "Grammar.", "confidence": 0.9,
            }],
        })

    def test_fenced_json_is_accepted_but_normalized(self):
        value = parse_json_object('```json\n{"findings": [], "summary": "No actionable findings"}\n```')
        self.assertEqual(validate_review(value)["findings"], [])

    def test_json_embedded_in_prose_is_extracted(self):
        value = parse_json_object('Here is the review.\n{"findings": [], "summary": "No actionable findings"}\n')
        self.assertEqual(value["summary"], "No actionable findings")

    def test_empty_response_names_the_failure(self):
        with self.assertRaises(ValueError) as error:
            parse_json_object("   ")
        self.assertIn("empty response", str(error.exception))

    def test_review_replacements_apply_without_rewriting_unchanged_text(self):
        revised = apply_review_replacements("# Chapter 1\n\nCurrent. Keep.\n", self.review())
        self.assertEqual(revised, "# Chapter 1\n\nCorrected. Keep.\n")

    def test_review_replacement_requires_a_unique_current_span(self):
        with self.assertRaisesRegex(ValueError, "occurs 2 times"):
            apply_review_replacements("Current. Current.", self.review())
    def test_paired_findings_replace_repeated_paragraphs(self):
        quote = "“Do you remember the promise you made me long ago?”"
        review = {"findings": [
            {
                "id": "F07",
                "source": "“오래전, 나와 했던 약속을 기억하느냐?”",
                "current": quote,
                "replacement": "“Do you remember the promise we made long ago?”",
            },
            {
                "id": "F08",
                "source": "“오래전, 노부와 했던 약속을 기억하느냐?”",
                "current": quote,
                "replacement": "“Do you remember the promise we made long ago?”",
            },
        ]}
        text = f"# Chapter 974\n\n{quote}\n\nMiddle.\n\n{quote}\n\n"
        revised = apply_review_replacements(text, review)
        replacement = "“Do you remember the promise we made long ago?”"
        self.assertEqual(revised, f"# Chapter 974\n\n{replacement}\n\nMiddle.\n\n{replacement}\n")

    def test_review_replacement_preserves_blockquote_prefixes(self):
        current = "Quest **[Desert Mirage]** successfully completed!  \nQuest rewards have been granted!  \nGained a large amount of EXP and Fame!  \nA new linked Quest has been generated upon completion of **[Desert Mirage]**."
        replacement = "Quest **Desert Mirage** successfully completed!  \nQuest rewards have been granted!  \nGained a large amount of EXP and Fame!  \nA new linked Quest has been generated upon completion of **Desert Mirage**."
        text = "> " + current.replace("\n", "\n> ")
        review = {"findings": [{"id": "F06", "current": current, "replacement": replacement}]}
        revised = apply_review_replacements(text, review)
        self.assertEqual(revised, "> " + replacement.replace("\n", "\n> ") + "\n")

    def test_review_replacement_prefers_unique_full_paragraph(self):
        review = {"findings": [{
            "id": "F01",
            "current": "Shao Yang.",
            "replacement": "Xiao Yang.",
        }]}
        revised = apply_review_replacements(
            "# Chapter 1\n\nShao Yang.\n\nChairman Shao Yang.\n", review
        )
        self.assertEqual(
            revised, "# Chapter 1\n\nXiao Yang.\n\nChairman Shao Yang.\n"
        )


    def test_overlapping_review_replacements_keep_the_stronger_span(self):
        review = self.review()
        review["findings"].append({
            "id": "F02",
            "severity": "minor",
            "source": "원문",
            "current": "rent.",
            "replacement": "vised.",
            "defect": "Overlap.",
            "rationale": "Cannot apply atomically.",
            "confidence": 0.8,
        })
        revised = apply_review_replacements("Current.", review)
        self.assertEqual(revised, "Corrected.\n")

    def test_duplicate_review_spans_are_applied_once(self):
        quote = "I would prefer it this way."
        review = {"findings": [
            {
                "id": "F07",
                "severity": "major",
                "current": quote,
                "replacement": "I'd actually prefer it this way.",
                "confidence": 0.95,
            },
            {
                "id": "F08",
                "severity": "major",
                "current": quote,
                "replacement": "I'd actually prefer it this way.",
                "confidence": 0.0,
            },
            {
                "id": "F09",
                "severity": "major",
                "current": quote,
                "replacement": "I'd actually prefer it this way.",
                "confidence": 0.0,
            },
        ]}
        revised = apply_review_replacements(f"# Chapter 1\n\n{quote}\n", review)
        self.assertEqual(revised, "# Chapter 1\n\nI'd actually prefer it this way.\n")

    def test_durable_update_rejects_multiline_profile_patch(self):
        value = {
            "chapter": 4,
            "beat": {"plot": ["Plot."], "continuity": [], "translation_decisions": []},
            "context": {
                "version": 1,
                "safe_through": 4,
                "continuity_sources": [4],
                "active_continuity": ["Fact."],
                "open_questions": ["Question?"],
                "temporary_decisions": [],
            },
            "names": [],
            "profile_updates": [{
                "path": "characters/Hero.md",
                "current": "- **Role:** Old\n- **Voice:** Old",
                "replacement": "- **Role:** New",
            }],
            "profile_creations": [],
        }
        with self.assertRaisesRegex(ValueError, "one complete line"):
            validate_durable_update(value, 4)

    def test_durable_update_accepts_spaced_korean_address_endpoints(self):
        value = {
            "chapter": 4,
            "beat": {"plot": ["Plot."], "continuity": [], "translation_decisions": []},
            "context": {
                "version": 1,
                "safe_through": 4,
                "continuity_sources": [4],
                "active_continuity": ["Fact."],
                "open_questions": ["Question?"],
                "temporary_decisions": [],
            },
            "names": [],
            "address_pairs": [{
                "speaker": "최 팀장",
                "addressee": "진태경",
                "kinship": "team_leader_to_hunter",
                "normal_address": "Mr. Jin Taekyung",
                "speech_level": "formal-but-urgent",
                "notes": "Emergency.",
            }],
            "profile_updates": [],
            "profile_creations": [],
        }
        update = validate_durable_update(value, 4)
        self.assertEqual(update["address_pairs"][0]["speaker"], "최 팀장")

    def test_durable_update_accepts_digit_titles_in_address_pairs(self):
        value = {
            "chapter": 92,
            "beat": {"plot": ["Plot."], "continuity": [], "translation_decisions": []},
            "context": {
                "version": 1,
                "safe_through": 92,
                "continuity_sources": [92],
                "active_continuity": ["Fact."],
                "open_questions": ["Question?"],
                "temporary_decisions": [],
            },
            "names": [],
            "address_pairs": [{
                "speaker": "1팀장",
                "addressee": "임춘수",
                "kinship": "team_leader_to_guild_master",
                "normal_address": "Guild Master",
                "speech_level": "formal-deferential",
                "notes": "Uses 길드장님.",
            }],
            "profile_updates": [],
            "profile_creations": [],
        }
        update = validate_durable_update(value, 92)
        self.assertEqual(update["address_pairs"][0]["speaker"], "1팀장")

    def test_durable_update_rejects_romanized_address_endpoints(self):
        value = {
            "chapter": 92,
            "beat": {"plot": ["Plot."], "continuity": [], "translation_decisions": []},
            "context": {
                "version": 1,
                "safe_through": 92,
                "continuity_sources": [92],
                "active_continuity": ["Fact."],
                "open_questions": ["Question?"],
                "temporary_decisions": [],
            },
            "names": [],
            "address_pairs": [{
                "speaker": "Team 1 Leader",
                "addressee": "임춘수",
                "kinship": "team_leader_to_guild_master",
                "normal_address": "Guild Master",
                "speech_level": "formal-deferential",
                "notes": "Bad romanization.",
            }],
            "profile_updates": [],
            "profile_creations": [],
        }
        with self.assertRaisesRegex(ValueError, "must be Korean"):
            validate_durable_update(value, 92)

    def test_durable_update_resolves_profile_english_address_endpoints(self):
        value = {
            "chapter": 4,
            "beat": {"plot": ["Plot."], "continuity": [], "translation_decisions": []},
            "context": {
                "version": 1,
                "safe_through": 4,
                "continuity_sources": [4],
                "active_continuity": ["Fact."],
                "open_questions": ["Question?"],
                "temporary_decisions": [],
                "extra": "dropped",
            },
            "names": [],
            "address_pairs": [{
                "speaker": "Hyuk Mujin",
                "addressee": "Jin Taekyung (진태경)",
                "kinship": "subordinate to squad leader",
                "normal_address": "Captain",
                "speech_level": "deferential",
                "notes": "Uses 조장님.",
            }],
            "profile_updates": [],
            "profile_creations": [],
        }
        update = validate_durable_update(value, 4)
        self.assertEqual(update["address_pairs"][0]["speaker"], "혁무진")
        self.assertEqual(update["address_pairs"][0]["addressee"], "진태경")
        self.assertNotIn("extra", update["context"])

    def test_durable_update_accepts_address_pairs(self):
        value = {
            "chapter": 4,
            "beat": {"plot": ["Plot."], "continuity": [], "translation_decisions": []},
            "context": {
                "version": 1,
                "safe_through": 4,
                "continuity_sources": [4],
                "active_continuity": ["Fact."],
                "open_questions": ["Question?"],
                "temporary_decisions": [],
            },
            "names": [],
            "address_pairs": [{
                "speaker": "진태경",
                "addressee": "진무경",
                "kinship": "younger_to_older_brother",
                "normal_address": "hyung",
                "speech_level": "casual-but-junior",
                "notes": "Greeting.",
            }],
            "profile_updates": [],
            "profile_creations": [],
        }
        update = validate_durable_update(value, 4)
        self.assertEqual(update["address_pairs"][0]["normal_address"], "hyung")

    def test_durable_update_defaults_missing_address_pairs(self):
        value = {
            "chapter": 4,
            "beat": {"plot": ["Plot."], "continuity": [], "translation_decisions": []},
            "context": {
                "version": 1,
                "safe_through": 4,
                "continuity_sources": [4],
                "active_continuity": ["Fact."],
                "open_questions": ["Question?"],
                "temporary_decisions": [],
            },
            "names": [],
            "profile_updates": [],
            "profile_creations": [],
        }
        update = validate_durable_update(value, 4)
        self.assertEqual(update["address_pairs"], [])

    def test_unresolved_major_checkpoint_finding_blocks_acceptance(self):
        review = self.review()
        dispositions = {
            "dispositions": [
                {"finding_id": "F01", "status": "unresolved", "reason": "Ambiguous."}
            ]
        }
        self.assertEqual(blocking_dispositions(review, dispositions), ["F01"])

    def test_trailing_prose_after_json_is_ignored(self):
        value = parse_json_object(
            '{"findings": [], "summary": "No actionable findings"}\nPlease continue reviewing.\n{"findings": []}'
        )
        self.assertEqual(value["summary"], "No actionable findings")

    def test_range_review_requires_chapter_and_patch_coverage(self):

        value = self.review()
        value["findings"][0]["chapter"] = 3
        review = validate_range_review(value, {3, 4})
        patchset = validate_patchset({
            "summary": "Fixed.",
            "patches": [{"chapter": 3, "finding_ids": ["F01"], "old": "Current.", "new": "Corrected."}],
            "dispositions": [{"finding_id": "F01", "status": "applied", "reason": "Corrected."}],
        }, review)
        self.assertEqual(patchset["patches"][0]["chapter"], 3)


class ReadingCopyExtractTest(unittest.TestCase):
    def test_extract_reading_copy_strips_same_line_preamble(self):
        raw = "Checking the chapter workflow and source so the final pass stays faithful.# Chapter 28\n\n*Hoo.*\n"
        self.assertEqual(extract_reading_copy(raw, 28), "# Chapter 28\n\n*Hoo.*\n")

    def test_extract_reading_copy_rejects_missing_heading(self):
        with self.assertRaises(ValueError):
            extract_reading_copy("No heading here.", 28)
