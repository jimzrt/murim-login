import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools import profile_retrofit


class ProfileRetrofitTest(unittest.TestCase):
    def test_apply_updates_reviewed_fields_and_rejects_stale_sources(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "characters").mkdir()
            (root / "source").mkdir()
            (root / "translations").mkdir()
            profile = root / "characters" / "Hero.md"
            profile.write_text(
                "# Hero (주인공)\n\n- **Role:** Scout\n- **Personality:** Quiet\n"
                "- **Voice:** Not established.\n- **Relationships:** Leads the group\n"
                "- **Sources:** Chapter 1\n",
                encoding="utf-8",
            )
            source = root / "source" / "0001.txt"
            translation = root / "translations" / "0001.md"
            source.write_text("주인공", encoding="utf-8")
            translation.write_text("# Chapter 1\n\nHero speaks plainly.\n", encoding="utf-8")
            proposal = root / "proposal.json"
            proposal.write_text(json.dumps({
                "version": 1,
                "profile": "Hero.md",
                "profile_sha256": hashlib.sha256(profile.read_bytes()).hexdigest(),
                "chapters": {"1": {
                    "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
                    "translation_sha256": hashlib.sha256(translation.read_bytes()).hexdigest(),
                }},
                "fields": {
                    "Role": "Scout",
                    "Personality": "Quiet and observant.",
                    "Voice": "Direct, plain-spoken, and concise.",
                    "Relationships": "Leads the group.",
                },
            }), encoding="utf-8")
            with (
                patch.object(profile_retrofit, "ROOT", root),
                patch.object(profile_retrofit, "chapter_path", lambda number: source),
                patch.object(profile_retrofit, "translation_path", lambda number: translation),
            ):
                profile_retrofit.apply(proposal)
                updated = profile.read_text(encoding="utf-8")
                self.assertIn("- **Voice:** Direct, plain-spoken, and concise.", updated)
                self.assertIn("Profile retrofit evidence: Chapters 1", updated)
                proposal_data = json.loads(proposal.read_text(encoding="utf-8"))
                proposal_data["profile_sha256"] = hashlib.sha256(profile.read_bytes()).hexdigest()
                proposal.write_text(json.dumps(proposal_data), encoding="utf-8")
                source.write_text("changed", encoding="utf-8")
                with self.assertRaisesRegex(SystemExit, "evidence chapter 1 changed"):
                    profile_retrofit.apply(proposal)

    def test_packet_pairs_only_the_selected_source_and_accepted_translation(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            profile = root / "Hero.md"
            profile.write_text("# Hero (주인공)\n- **Voice:** Not established.\n", encoding="utf-8")
            source = root / "0007.txt"
            translation = root / "0007.md"
            source.write_text("주인공이 묻는다.", encoding="utf-8")
            translation.write_text("Hero asks.", encoding="utf-8")
            with (
                patch.object(profile_retrofit, "chapter_path", return_value=source),
                patch.object(profile_retrofit, "extract_chapter", return_value="주인공이 묻는다.\n"),
                patch.object(profile_retrofit, "translation_path", return_value=translation),
            ):
                packet, refs = profile_retrofit.build_packet(profile, [7])
            self.assertIn("주인공이 묻는다.", packet)
            self.assertIn("Hero asks.", packet)
            self.assertIn("Chapter 7", packet)
            self.assertIn("The only allowed `evidence_chapters` are [7]", packet)
            self.assertEqual(refs["7"]["source_sha256"], hashlib.sha256(source.read_bytes()).hexdigest())

    def test_chapter_floor_excludes_earlier_same_name_person(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            profile = root / "Jang Sam.md"
            profile.write_text("# Jang Sam (장삼)\n", encoding="utf-8")
            translations = root / "translations"
            translations.mkdir()
            (translations / "0546.md").write_text("Accepted.", encoding="utf-8")
            with patch.object(
                profile_retrofit, "translation_path",
                lambda number: translations / f"{number:04d}.md",
            ):
                chapters = profile_retrofit.chapters_for(
                    profile, {4: "장삼은 산적이다.", 546: "어부 장삼이다."}, from_chapter=546,
                )
            self.assertEqual(chapters, [546])

    def test_model_result_accepts_only_matching_nested_evidence(self):
        fields = {
            "Role": "A leader.",
            "Personality": "Reserved.",
            "Voice": "Formal.",
            "Relationships": "Trusted by her mentor.",
        }
        result = {
            "fields": {**fields, "evidence_chapters": [12]},
            "evidence_chapters": [12],
        }
        self.assertEqual(profile_retrofit.validated_model_result(result), (fields, [12]))
        result["fields"]["evidence_chapters"] = [13]
        with self.assertRaisesRegex(SystemExit, "must match"):
            profile_retrofit.validated_model_result(result)

    def test_sampling_spreads_across_chronology(self):
        self.assertEqual(profile_retrofit.sampled_chapters(list(range(20)), 4), [0, 6, 13, 19])


if __name__ == "__main__":
    unittest.main()
