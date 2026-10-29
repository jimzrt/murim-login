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
LINE = "- **Appearance (ch 1–99):** Hero is tall and white-haired. Tags: tall, white hair\n- **Appearance (from ch 100):** Hero has one eye. Tags: one eye"


class AppearanceFieldTest(unittest.TestCase):
    def test_set_inserts_after_relationships_and_replaces(self):
        body = names.set_profile_appearance(PROFILE, LINE)
        lines = body.splitlines()
        first = lines.index(LINE.split("\n")[0])
        self.assertEqual(lines[first - 1].split(":")[0], "- **Relationships")
        self.assertEqual(lines[first + 1], LINE.split("\n")[1])
        self.assertEqual(lines[first + 2], "- **Sources:** Chapter 1")
        self.assertEqual(names.profile_appearance(body), LINE)
        again = names.set_profile_appearance(body, "- **Appearance:** not described")
        self.assertEqual(again.count("Appearance"), 1)
        self.assertEqual(names.appearance_ranges(body), [
            {"start": 1, "end": 99, "text": "Hero is tall and white-haired. Tags: tall, white hair"},
            {"start": 100, "end": None, "text": "Hero has one eye. Tags: one eye"},
        ])
        self.assertEqual(names.appearance_ranges(again), [])
        legacy = PROFILE.replace("- **Sources", "- **Appearance (as of ch 4):** old\n- **Sources")
        self.assertEqual(names.set_profile_appearance(legacy, None), PROFILE)
        self.assertEqual(names.set_profile_appearance(body, None), PROFILE)

    def test_compact_profile_excludes_appearance(self):
        compact = context.compact_profile(names.set_profile_appearance(PROFILE, LINE))
        self.assertNotIn("Appearance", compact)

    def test_compression_preserves_and_never_invents(self):
        original = names.set_profile_appearance(PROFILE, LINE)
        key = "characters/Hero.md"
        kept = compress_context.preserve_appearance((Path(key), original), {key: PROFILE})
        self.assertEqual(names.profile_appearance(kept[key]), LINE)
        rewritten = original.replace("tall and white-haired", "short")
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

    def test_render_lines(self):
        one = [{"start": 4, "description": "Hero is tall."}]
        self.assertEqual(ap.render_lines(one), ["- **Appearance (from ch 4):** Hero is tall."])
        two = one + [{"start": 90, "description": "Hero is old."}]
        self.assertEqual(ap.render_lines(two), [
            "- **Appearance (ch 4–89):** Hero is tall.", "- **Appearance (from ch 90):** Hero is old."])
        self.assertEqual(ap.render_lines([]), ["- **Appearance:** not described"])

    def test_parse_json_ignores_trailing_text(self):
        self.assertEqual(ap.parse_json('```json\n{"a": 1}\n```\nNote {x}'), {"a": 1})

    def facts(self):
        return [{"chapter": 2, "fact": "tall"}, {"chapter": 40, "fact": "one-eyed"}, {"chapter": 41, "fact": "eyepatch"}]

    def test_check_ranges_accepts_valid_and_forces_first_start(self):
        result = {"ranges": [
            {"start": 9, "description": "Hero is tall (영웅).", "used": [0]},
            {"start": 40, "description": "Hero is tall and one-eyed.", "used": [0, 1, 2]},
        ]}
        ranges = ap.check_ranges(result, self.facts(), "Hero", first=1, safe=100)
        self.assertEqual([r["start"] for r in ranges], [1, 40])
        self.assertEqual(ranges[0]["description"], "Hero is tall.")

    def test_check_ranges_rejects_leaks_and_bad_starts(self):
        base = {"start": 1, "description": "Hero is tall.", "used": [0]}
        later = {"start": 40, "description": "Hero is one-eyed.", "used": [1]}
        leak = dict(base, used=[0, 1])
        for bad, message in (
            ([leak, later], "next range start"),
            ([base, dict(later, start=30)], "equal the chapter"),
            ([base, dict(later, description="He is one-eyed.")], "start with the name"),
            ([base, dict(later, start=40)] , None),
        ):
            if message is None:
                self.assertEqual(len(ap.check_ranges({"ranges": bad}, self.facts(), "Hero", 1, 100)), 2)
                continue
            with self.assertRaisesRegex(ValueError, message):
                ap.check_ranges({"ranges": bad}, self.facts(), "Hero", 1, 100)
        with self.assertRaises(ValueError):
            ap.check_ranges({"ranges": [base, dict(later, start=40)]}, self.facts(), "Hero", 1, 39)

    def test_candidates_scan_all_chapters_up_to_safe_through(self):
        row = {"english": "Other", "names": ["영웅"], "safe_through": 300, "chapters": [1, 150, 400]}
        text = "＃1화\n영웅의 얼굴은 하얗고 머리카락은 검었다.\n"
        found = ap.candidates(row, {1: text, 150: text, 400: text})
        self.assertEqual([c["chapter"] for c in found], [1, 150])

    def test_narrator_gets_mirror_paragraphs_without_name(self):
        narrator = {"english": "Jin Taekyung", "names": ["진태경"], "safe_through": 10, "chapters": [1]}
        text = "＃1화\n거울 속에 비친 내 얼굴은 낯설었다. 하얀 피부에 검은 머리카락이었다.\n"
        self.assertEqual(len(ap.candidates(narrator, {1: text, 2: text})), 2)
        other = dict(narrator, english="Other")
        self.assertEqual(ap.candidates(other, {1: text, 2: text}), [])


if __name__ == "__main__":
    unittest.main()
