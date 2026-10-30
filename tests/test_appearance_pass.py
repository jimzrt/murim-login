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
    def test_verify_drops_unverified_quotes(self):
        chapters = {3: "그는 은발에 푸른 눈동자를 가졌다.", 9: "흰 수염이 길었다."}
        facts = [
            {"fact": "silver hair", "chapter": 3, "quote": "은발에  푸른 눈동자"},
            {"fact": "made up", "chapter": 3, "quote": "붉은 머리카락"},
            {"fact": "beard", "chapter": 9, "quote": "흰 수염이 길었다."},
            {"fact": "x", "chapter": 3, "quote": "눈"},
        ]
        good, dropped = ap.verify(facts, chapters)
        self.assertEqual([f["fact"] for f in good], ["silver hair", "beard"])
        self.assertEqual(len(dropped), 2)

    def test_render_lines(self):
        one = [{"start": 4, "description": "Hero is tall. Tags: tall"}]
        self.assertEqual(ap.render_lines(one), ["- **Appearance (from ch 4):** Hero is tall. Tags: tall"])
        two = one + [{"start": 90, "description": "Hero is old. Tags: old"}]
        self.assertEqual(ap.render_lines(two), [
            "- **Appearance (ch 4–89):** Hero is tall. Tags: tall",
            "- **Appearance (from ch 90):** Hero is old. Tags: old"])
        self.assertEqual(ap.render_lines([]), ["- **Appearance:** not described"])

    def test_parse_json_ignores_trailing_text(self):
        self.assertEqual(ap.parse_json('```json\n{"a": 1}\n```\nNote {x}'), {"a": 1})

    def facts(self):
        return [{"chapter": 2, "fact": "tall"}, {"chapter": 40, "fact": "one-eyed"}, {"chapter": 41, "fact": "eyepatch"}]

    def test_check_ranges_accepts_valid_and_forces_first_start(self):
        result = {"ranges": [
            {"start": 9, "description": "Hero is tall (영웅). Tags: tall", "used": [0]},
            {"start": 40, "description": "Hero is tall and one-eyed. Tags: one eye", "used": [0, 1, 2],
             "difference": "two eyes -> one eye"},
        ]}
        ranges = ap.check_ranges(result, self.facts(), "Hero", first=1, approved={1})
        self.assertEqual([r["start"] for r in ranges], [1, 40])
        self.assertEqual(ranges[0]["description"], "Hero is tall. Tags: tall")

    def test_check_ranges_rejects_leaks_and_bad_starts(self):
        base = {"start": 1, "description": "Hero is tall. Tags: tall", "used": [0]}
        later = {"start": 40, "description": "Hero is one-eyed. Tags: one eye", "used": [1], "difference": "two eyes -> one eye"}
        leak = dict(base, used=[0, 1])
        for bad, message in (
            ([leak, later], "next range start"),
            ([base, dict(later, start=30)], "APPROVED-CHANGE"),
            ([base, dict(later, description="He is one-eyed. Tags: one eye")], "start with the name"),
            ([base, later], "APPROVED-CHANGE"),    # nothing approved: first mention is not a change
        ):
            with self.assertRaisesRegex(ValueError, message):
                ap.check_ranges({"ranges": bad}, self.facts(), "Hero", 1)
        ok = ap.check_ranges({"ranges": [base, later]}, self.facts(), "Hero", 1, approved={1})
        self.assertEqual(len(ok), 2)
        with self.assertRaisesRegex(ValueError, "Tags"):
            ap.check_ranges({"ranges": [dict(base, description="Hero is tall.")]}, self.facts(), "Hero", 1)

    def test_merge_facts_unions_without_duplicates(self):
        a = [{"chapter": 5, "quote": "검은 눈 동자", "fact": "a"}]
        b = [{"chapter": 5, "quote": "검은눈동자", "fact": "dup"}, {"chapter": 2, "quote": "큰 키", "fact": "b"}]
        self.assertEqual([f["fact"] for f in ap.merge_facts(a, b)], ["b", "a"])

    def test_later_range_needs_visible_difference_and_not_described_base(self):
        base = {"start": 1, "description": "Hero is tall. Tags: tall", "used": [0]}
        later = {"start": 40, "description": "Hero is one-eyed. Tags: one eye", "used": [1]}
        with self.assertRaisesRegex(ValueError, "difference"):
            ap.check_ranges({"ranges": [base, later]}, self.facts(), "Hero", 1, approved={1})
        placeholder = {"start": 1, "description": "not described", "used": []}
        ranges = ap.check_ranges(
            {"ranges": [placeholder, dict(later, difference="old man -> youth")]}, self.facts(), "Hero", 1, approved={1})
        self.assertEqual([r["start"] for r in ranges], [40])

    def test_no_visible_difference_is_rejected(self):
        base = {"start": 1, "description": "Hero is tall. Tags: tall", "used": [0]}
        for diff in ("body remade by Bone Transformation (visible effect not stated)", "unclear", "x"):
            later = {"start": 40, "description": "Hero is remade. Tags: x", "used": [1], "difference": diff}
            with self.assertRaisesRegex(ValueError, "difference"):
                ap.check_ranges({"ranges": [base, later]}, self.facts(), "Hero", 1, approved={1})

    def test_manual_facts_and_overrides_are_well_formed(self):
        for name, facts in ap.MANUAL_FACTS.items():
            for fact in facts:
                self.assertTrue(len(ap.norm(fact["quote"])) >= ap.MIN_QUOTE and isinstance(fact["chapter"], int))
        for table in (ap.OVERRIDES, ap.FORCE_APPROVE):
            for name, chapters in table.items():
                self.assertTrue(all(isinstance(c, int) and isinstance(r, str) and r for c, r in chapters.items()))
        self.assertTrue(ap.CHANGE_RE.search("대충 빡빡 밀어 버린 민머리"))

    def test_change_marker_is_deterministic(self):
        chapters = {7: "그는 웃었다.\n노인은 어느덧 새하얀 백발이 되어 버렸다.\n그는 말했다.", 8: "평범한 노인이었다."}
        self.assertTrue(ap.has_marker({"chapter": 7, "quote": "새하얀 백발이 되어 버렸다"}, chapters))
        self.assertFalse(ap.has_marker({"chapter": 8, "quote": "평범한 노인이었다"}, chapters))

    def test_context_marks_quote_with_neighbours(self):
        text = "\n".join(f"문단{i}" for i in range(10)) + "\n"
        ctx = ap.context_for({"chapter": 1, "quote": "문단5"}, {1: text})
        self.assertIn(">>> 문단5 <<<", ctx)
        self.assertIn("문단2", ctx)
        self.assertNotIn("문단1\n", ctx.replace("문단10", ""))

    def test_paragraph_verdicts_are_shared_strictest(self):
        chapters = {1: "눈이 붉었다. 머리가 하얗다.\n다른 문단.\n"}
        facts = [{"chapter": 1, "quote": "눈이 붉었다"}, {"chapter": 1, "quote": "머리가 하얗다"}]
        verdicts = {0: {"this_character": True, "literal_present": True, "lasting_change": True},
                    1: {"this_character": True, "literal_present": False, "lasting_change": False}}
        ap.share_paragraph_verdicts(facts, verdicts, chapters)
        self.assertFalse(verdicts[0]["literal_present"])
        self.assertFalse(verdicts[0]["lasting_change"])

    def test_write_requires_every_fact_used_or_explained(self):
        row = {"english": "Hero", "gender": "male", "first_chapter": 1}
        kept = [{"chapter": 2, "fact": "tall", "quote": "큰 키"}, {"chapter": 3, "fact": "scarf", "quote": "목도리"}]
        answers = iter([
            json.dumps({"ranges": [{"start": 1, "description": "Hero is tall. Tags: tall", "used": [0]}]}),
            json.dumps({"ranges": [{"start": 1, "description": "Hero is tall. Tags: tall", "used": [0]}],
                        "omitted": [{"index": 1, "reason": "one-scene costume"}]}),
        ])
        with patch.object(ap, "claude", lambda model, prompt: next(answers)):
            ranges, conflicts, unused, omitted = ap.write(row, kept, set(), [])
        self.assertEqual((len(ranges), unused, omitted[0]["index"]), (1, [], 1))

    def test_change_hits_use_epithets_and_proximity(self):
        row = {"english": "Jeok Cheongang", "names": ["적천강"], "chapters": [1]}
        near = "＃1화\n노괴가 서 있었다.\n타오르는 붉은 머리카락, 반로환동을 마친 모습이었다.\n"
        far = "＃2화\n" + "가" * 2000 + "\n적천강은 웃었다.\n" + "나" * 2000 + "\n반로환동 이야기는 먼 이야기였다.\n"
        hits = ap.change_hits(row, {1: near, 2: far, 3: "반로환동 한 노인.\n"})
        self.assertEqual([h["chapter"] for h in hits], [1])      # ch2 too far, ch3 names nobody
        self.assertEqual(ap.change_hits(dict(row, english="Other", names=["엉뚱"]), {1: near}), [])   # 노괴 is an epithet only for him

    def test_narrator_change_hits_need_first_person(self):
        row = {"english": "Jin Taekyung", "names": ["진태경"], "chapters": []}
        text = "＃1화\n내 몸이 환골탈태를 거치며 변했다.\n그의 몸이 환골탈태를 거쳤다.\n"
        hits = ap.change_hits(row, {1: text})
        self.assertEqual(len(hits), 1)
        self.assertIn("내 몸", hits[0]["text"])

    def test_beat_sentences_need_name_and_change_vocabulary(self):
        with tempfile.TemporaryDirectory() as folder:
            beats = Path(folder)
            (beats / "0505.md").write_text(
                "# Chapter 505\n\nJeok Cheongang reveals he achieved Returned to Youth. Zhuge Feng frowns.\n"
                "Someone else returned to youth.\n", encoding="utf-8")
            with patch.object(ap, "BEATS", beats):
                found = ap.beat_sentences({"english_names": ["Jeok Cheongang"]})
        self.assertEqual([(b["chapter"], b["text"][:14]) for b in found], [(505, "Jeok Cheongang")])

    def test_timeline_parses_events_and_drops_junk(self):
        answer = json.dumps({"events": [{"chapter": 505, "change": "old -> young", "cause": "enlightenment"},
                                        {"change": "no chapter"}, "junk"]})
        with patch.object(ap, "claude", lambda model, prompt: answer):
            events = ap.timeline({"english": "Hero", "names": ["영웅"]}, [{"chapter": 505, "text": "x"}], [])
        self.assertEqual([(e["chapter"], e["cause"]) for e in events], [(505, "enlightenment")])

    def test_event_hint_only_near_event(self):
        events = [{"chapter": 505, "change": "old -> young", "cause": "enlightenment"}]
        self.assertIn("Timeline hint: ch505", ap.event_hint({"chapter": 506}, events))
        self.assertEqual(ap.event_hint({"chapter": 700}, events), "")

    def test_write_requires_timeline_events_to_open_a_range_or_be_dismissed(self):
        row = {"english": "Hero", "gender": "male", "first_chapter": 1}
        kept = [{"chapter": 2, "fact": "old", "quote": "노인"}, {"chapter": 50, "fact": "young", "quote": "청년"}]
        events = [{"chapter": 50, "change": "old -> young", "cause": "enlightenment"}]
        one = {"ranges": [{"start": 1, "description": "Hero is old. Tags: old", "used": [0, 1]}]}
        two = {"ranges": [{"start": 1, "description": "Hero is old. Tags: old", "used": [0]},
                          {"start": 50, "description": "Hero is young after enlightenment. Tags: young", "used": [1],
                           "difference": "old man -> young man"}]}
        answers = iter([json.dumps(one), json.dumps(two)])
        with patch.object(ap, "claude", lambda model, prompt: next(answers)):
            ranges, *_ = ap.write(row, kept, {1}, [], events)
        self.assertEqual([r["start"] for r in ranges], [1, 50])

    def test_candidates_ignore_profile_safe_through(self):
        row = {"english": "Other", "names": ["영웅"], "safe_through": 300, "chapters": [1, 150, 400]}
        text = "＃1화\n영웅의 얼굴은 하얗고 머리카락은 검었다.\n"
        found = ap.candidates(row, {1: text, 150: text, 400: text})
        self.assertEqual([c["chapter"] for c in found], [1, 150, 400])

    def test_narrator_gets_mirror_paragraphs_without_name(self):
        narrator = {"english": "Jin Taekyung", "names": ["진태경"], "safe_through": 10, "chapters": [1]}
        text = "＃1화\n거울 속에 비친 내 얼굴은 낯설었다. 하얀 피부에 검은 머리카락이었다.\n"
        self.assertEqual(len(ap.candidates(narrator, {1: text, 2: text})), 2)
        other = dict(narrator, english="Other")
        self.assertEqual(ap.candidates(other, {1: text, 2: text}), [])


if __name__ == "__main__":
    unittest.main()


class VisionGuardTest(unittest.TestCase):
    CHAPTER = ("평범한 문단이다.\n\n"
               "얼굴에 흉터가 가득하고, 한쪽 팔을 잃어버린 최 팀장이 술잔을 비운다.\n\n"
               "백발이 된 노인이 웃었다.")

    def fact(self, text, quote, chapter=830):
        return {"chapter": chapter, "fact": text, "quote": quote, "kind": "change"}

    def test_vision_and_same_paragraph_facts_are_rejected(self):
        facts = [
            self.fact("Face covered in scars (later timeline)", "얼굴에 흉터가 가득하고"),
            self.fact("Lost one arm", "한쪽 팔을 잃어버린 최 팀장이"),
            self.fact("Hair turned white", "백발이 된 노인이 웃었다"),
        ]
        verdicts = {1: {"reason": "Lost arm is a lasting change, shown here for the first time."}}
        self.assertEqual(ap.vision_facts(facts, verdicts, {830: self.CHAPTER}), {0, 1})

    def test_judge_reason_alone_marks_a_vision(self):
        facts = [self.fact("Has one eye", "백발이 된 노인이 웃었다")]
        self.assertEqual(ap.vision_facts(facts, {0: {"reason": "seen in a dream of the future"}}, {830: self.CHAPTER}), {0})
        self.assertEqual(ap.vision_facts(facts, {0: {"reason": "permanent injury"}}, {830: self.CHAPTER}), set())

    def test_prompts_treat_visions_like_flashbacks(self):
        self.assertIn("Visions, dreams, prophecies", ap.JUDGE_PROMPT)
        self.assertIn("vision, dream, prophecy", ap.EXTRACT_PROMPT)
