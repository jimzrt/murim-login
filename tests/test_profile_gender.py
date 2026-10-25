"""Profile Gender field: parsing, writing, compact packets, and update rules."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools import compress_context, context, model_io, names

PROFILE = (
    "# Faye Chen (파이 첸)\n\n"
    "- **Safe through:** Chapter 773\n"
    "- **Aliases:** None\n"
    "- **Role:** S-rank Hunter.\n"
    "- **Personality:** Not established.\n"
    "- **Voice:** Not established.\n"
    "- **Relationships:** Felix's comrade.\n"
)


class ProfileGenderTest(unittest.TestCase):
    def test_missing_or_invalid_gender_is_unknown(self):
        self.assertEqual(names.profile_gender(PROFILE), "unknown")
        self.assertEqual(names.profile_gender(PROFILE + "- **Gender:** robot\n"), "unknown")
        self.assertEqual(names.normalize_gender(None), "unknown")

    def test_gender_line_is_parsed_case_insensitively(self):
        body = PROFILE.replace("- **Role:**", "- **Gender:** Female\n- **Role:**")
        self.assertEqual(names.profile_gender(body), "female")

    def test_set_gender_inserts_after_aliases_and_replaces_existing(self):
        body = names.set_profile_gender(PROFILE, "female")
        lines = body.splitlines()
        self.assertEqual(lines[lines.index("- **Aliases:** None") + 1], "- **Gender:** female")
        self.assertTrue(body.endswith("\n"))
        again = names.set_profile_gender(body, "male")
        self.assertEqual(again.count("- **Gender:**"), 1)
        self.assertEqual(names.profile_gender(again), "male")

    def test_spaced_korean_heading_joins_profile_names(self):
        self.assertEqual(names.profile_koreans(PROFILE), ["파이 첸"])
        alias = PROFILE.replace("- **Aliases:** None", "- **Aliases:** Old Chen (늙은 첸)")
        self.assertEqual(names.profile_koreans(alias), ["파이 첸", "늙은 첸"])

    def test_ledger_keeps_spaced_korean_keys(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "docs").mkdir()
            (root / "docs" / "NAMES.md").write_text(
                "| Korean | English | Notes |\n|---|---|---|\n| 매직 존슨 | **Magic Johnson** | Grand Mage |\n",
                encoding="utf-8",
            )
            with patch.object(names, "ROOT", root):
                entries = names.ledger_for_source("매직 존슨이 웃었다.")
        self.assertEqual([item["english"] for item in entries], ["**Magic Johnson**"])

    def test_compact_profile_keeps_gender(self):
        body = names.set_profile_gender(PROFILE, "female")
        compact = context.compact_profile(body + "- **Sources:** Chapter 385\n")
        self.assertIn("- **Gender:** female", compact)
        self.assertNotIn("Sources", compact)

    def test_compression_preserves_established_gender(self):
        original = names.set_profile_gender(PROFILE, "female")
        replacement = {"characters/Faye Chen.md": PROFILE}
        kept = compress_context.preserve_gender((Path("characters/Faye Chen.md"), original), replacement)
        self.assertEqual(names.profile_gender(kept["characters/Faye Chen.md"]), "female")
        untouched = compress_context.preserve_gender((Path("x.md"), PROFILE), replacement)
        self.assertEqual(untouched, replacement)


class ProfileCreationGenderTest(unittest.TestCase):
    def update(self, **creation: object) -> dict:
        return {
            "chapter": 1,
            "beat": {"plot": ["p"], "continuity": [], "translation_decisions": []},
            "context": {
                "version": 1,
                "safe_through": 1,
                "continuity_sources": [1],
                "active_continuity": [],
                "open_questions": [],
                "temporary_decisions": [],
            },
            "names": [],
            "address_pairs": [],
            "profile_updates": [],
            "profile_creations": [{
                "filename": "Faye Chen.md",
                "korean": "파이 첸",
                "english": "Faye Chen",
                "aliases": [],
                "role": "Hunter",
                "personality": "Calm",
                "voice": "Not established",
                "relationships": "Felix",
                **creation,
            }],
        }

    def validate(self, value: dict) -> dict:
        with patch.object(context, "workflow_config", return_value={
            "continuity_source_limit": 2, "context_max_bytes": 16384,
        }):
            return model_io.validate_durable_update(value, 1)

    def test_creation_gender_defaults_to_unknown_and_validates(self):
        self.assertEqual(self.validate(self.update())["profile_creations"][0]["gender"], "unknown")
        self.assertEqual(
            self.validate(self.update(gender="Female"))["profile_creations"][0]["gender"], "female"
        )
        with self.assertRaises(ValueError):
            self.validate(self.update(gender="woman"))


if __name__ == "__main__":
    unittest.main()
