import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools import appearance_pass as ap
from tools import compress_context, context, names, workflow

PROFILE = (
    "# Hero (영웅)\n\n"
    "- **Safe through:** Chapter 50\n"
    "- **Aliases:** None\n"
    "- **Gender:** male\n"
    "- **Role:** Lead.\n"
    "- **Personality:** Calm.\n"
    "- **Voice:** Plain.\n"
    "- **Relationships:** Ally.\n"
    "- **Sources:** Chapter 1\n"
)
LINE = "- **Appearance (as of ch 12):** Tall, white-haired. Tags: tall, white hair"


class AppearanceFieldTest(unittest.TestCase):
    def test_set_inserts_after_relationships_and_replaces(self):
        body = names.set_profile_appearance(PROFILE, LINE)
        lines = body.splitlines()
        self.assertEqual(lines[lines.index(LINE) - 1].split(":")[0], "- **Relationships")
        self.assertEqual(lines[lines.index(LINE) + 1], "- **Sources:** Chapter 1")
        again = names.set_profile_appearance(body, "- **Appearance:** not described")
        self.assertEqual(again.count("Appearance"), 1)
        self.assertEqual(names.set_profile_appearance(body, None), PROFILE)

    def test_compact_profile_excludes_appearance(self):
        compact = context.compact_profile(names.set_profile_appearance(PROFILE, LINE))
        self.assertNotIn("Appearance", compact)

    def test_compression_preserves_and_never_invents(self):
        original = names.set_profile_appearance(PROFILE, LINE)
        key = "characters/Hero.md"
        kept = compress_context.preserve_appearance((Path(key), original), {key: PROFILE})
        self.assertEqual(names.profile_appearance(kept[key]), LINE)
        rewritten = original.replace("Tall, white-haired", "Short")
        kept = compress_context.preserve_appearance((Path(key), original), {key: rewritten})
        self.assertEqual(names.profile_appearance(kept[key]), LINE)
        none = compress_context.preserve_appearance((Path(key), PROFILE), {key: PROFILE})
        self.assertIsNone(names.profile_appearance(none[key]))

    def test_compression_budget_ignores_appearance(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "characters").mkdir()
            body = names.set_profile_appearance(PROFILE, "- **Appearance:** " + "x" * 300)
            (root / "characters" / "Hero.md").write_text(body, encoding="utf-8")
            limit = len(PROFILE.encode()) + 10
            with patch.object(compress_context, "ROOT", root), patch.object(
                compress_context, "workflow_config", return_value={"profile_compress_trigger_bytes": limit}
            ):
                self.assertEqual(compress_context.oversized_profiles(), [])

    def test_update_path_cannot_edit_appearance_and_creation_merge_keeps_it(self):
        self.assertNotIn("Appearance", workflow.PROFILE_UPDATE_FIELDS)
        body = names.set_profile_appearance(PROFILE, LINE)
        merged = workflow.merge_existing_profile_creation(body, {
            "role": "New role", "personality": "p", "voice": "v", "relationships": "r", "aliases": [],
        })
        self.assertIn(LINE, merged)
        self.assertIn("- **Role:** New role", merged)


class AppearancePipelineTest(unittest.TestCase):
    def test_verify_drops_unverified_and_late_quotes(self):
        chapters = {3: "그는 은발에 푸른 눈동자를 가졌다.", 9: "흰 수염이 길었다."}
        facts = [
            {"fact": "silver hair", "chapter": 3, "quote": "은발에  푸른 눈동자"},
            {"fact": "made up", "chapter": 3, "quote": "붉은 머리카락"},
            {"fact": "beard", "chapter": 9, "quote": "흰 수염이 길었다."},
            {"fact": "x", "chapter": 3, "quote": "눈"},
        ]
        good, dropped = ap.verify(facts, chapters, safe_through=5)
        self.assertEqual([f["fact"] for f in good], ["silver hair"])
        self.assertEqual(len(dropped), 3)

    def test_render_line_bound_and_not_described(self):
        used = [{"chapter": 4}, {"chapter": 11}]
        self.assertEqual(ap.render_line("Tall (長身).", used), "- **Appearance (as of ch 11):** Tall.")
        self.assertEqual(ap.render_line("not described", used), "- **Appearance:** not described")
        self.assertEqual(ap.render_line("Tall.", []), "- **Appearance:** not described")

    def test_parse_json_ignores_trailing_text(self):
        self.assertEqual(ap.parse_json('```json\n{"a": 1}\n```\nNote {x}'), {"a": 1})

    def test_candidates_respect_safe_through_and_span(self):
        row = {"names": ["영웅"], "safe_through": 5, "chapters": [1, 3, 8]}
        text = "＃1화\n영웅의 얼굴은 하얗고 머리카락은 검었다.\n"
        chapters = {1: text, 3: text, 8: text}
        found = ap.candidates(row, chapters)
        self.assertEqual([c["chapter"] for c in found], [1, 3])


if __name__ == "__main__":
    unittest.main()
