import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools import illustrate as il

PROFILE = (
    "# Hero (영웅)\n\n"
    "- **Safe through:** Chapter 900\n"
    "- **Gender:** male\n"
    "- **Role:** Secret heir who later becomes emperor.\n"
    "- **Appearance (ch 1–99):** Hero is an old man with white hair. Tags: old man, white hair, clear eyes\n"
    "- **Appearance (from ch 100):** Hero has a bald head and one eye. Tags: bald head, one eye, grey eyes\n"
    "- **Sources:** Chapter 1\n"
)
GHOST = "# Ghost\n\n- **Gender:** male\n- **Appearance:** not described\n"
ROWS = [
    {"rank": 1, "english": "Hero", "profile": "characters/Hero.md", "text": PROFILE},
    {"rank": 2, "english": "Ghost", "profile": "characters/Ghost.md", "text": GHOST},
]
OVERRIDES = {"Hero": {"identity": "a square jaw", "ranges": {"100": {"fill_ins": {"clothing": "a grey robe"}}}}}


class PromptTest(unittest.TestCase):
    def setUp(self):
        self.entries = il.build_prompts(ROWS, OVERRIDES)
        self.by_id = {entry["id"]: entry for entry in self.entries}

    def test_one_prompt_per_range_and_not_described_skipped(self):
        self.assertEqual(sorted(self.by_id), ["hero-1", "hero-100"])
        self.assertEqual((self.by_id["hero-1"]["from"], self.by_id["hero-1"]["to"]), (1, 99))
        self.assertIsNone(self.by_id["hero-100"]["to"])

    def test_style_block_verbatim(self):
        style = il.STYLE.format(setting=il.MURIM_SETTING)
        for entry in self.entries:
            self.assertIn(f"Style/medium: {style}\n", entry["prompt"])
            self.assertTrue(entry["prompt"].startswith("Use case: illustration-story\n"))
            self.assertIn("Avoid: text, watermark", entry["prompt"])

    def test_non_murim_setting_replaces_only_the_setting_phrase(self):
        entry = il.build_prompts(ROWS[:1], {"Hero": {"setting": "modern Seoul hunter setting"}})[0]
        self.assertNotIn("wuxia", entry["prompt"])
        self.assertIn(il.STYLE.format(setting="modern Seoul hunter setting"), entry["prompt"])

    def test_range_isolation(self):
        early, late = self.by_id["hero-1"]["prompt"], self.by_id["hero-100"]["prompt"]
        self.assertIn("white hair", early)
        self.assertNotIn("bald", early)
        self.assertNotIn("grey robe", early)
        self.assertNotIn("emperor", early + late)
        self.assertIn("bald head", late)
        self.assertNotIn("white hair", late)
        anchor = "Identity anchor (identical in every portrait of this character; do not redesign the face): a square jaw."
        self.assertIn(anchor, early)
        self.assertIn(anchor, late)

    def test_anti_comedy_guard_for_exaggerated_features(self):
        giant = PROFILE.replace("Tags: old man, white hair, clear eyes", "Tags: giant, big round bulging eyes")
        rows = [{**ROWS[0], "text": giant}]
        guarded = {entry["id"]: entry for entry in il.build_prompts(rows, {})}
        self.assertTrue(guarded["hero-1"]["serious"])
        self.assertIn("Tone: serious and grounded, not comic", guarded["hero-1"]["prompt"])
        self.assertIn("cartoonish or chibi proportions", guarded["hero-1"]["prompt"])
        self.assertFalse(guarded["hero-100"]["serious"])
        self.assertNotIn("Tone:", guarded["hero-100"]["prompt"])
        forced = il.build_prompts(ROWS[:1], {"Hero": {"serious": True, "framing": "scale",
                                                      "fill_ins": {"scale": "a tiny doorway"}}})[0]
        self.assertIn("Scale reference: a tiny doorway.", forced["prompt"])
        self.assertIn("low camera angle", forced["prompt"])

    def test_age_and_build_basis_split(self):
        overrides = {"Hero": {"ranges": {"1": {"age": "looks about 80", "build": {"text": "short", "basis": "오척단구 (ch 5)"},
                                                "continuity": "same face as before", "avoid": ["handsome face"]}}}}
        entry = il.build_prompts(ROWS[:1], overrides)[0]
        self.assertIn("Subject: Hero, male, looks about 80:", entry["prompt"])
        self.assertIn("Build: short.", entry["prompt"])
        self.assertEqual(entry["source_facts"]["build"]["basis"], "오척단구 (ch 5)")
        self.assertEqual(entry["fill_ins"]["age"], "looks about 80")
        self.assertIn("glamour retouching, handsome face.", entry["prompt"])

    def test_eyes_named_as_irises_and_clear_is_not_pale(self):
        self.assertIn("dark brown irises", self.by_id["hero-1"]["prompt"])
        self.assertIn("strikingly clear, bright and sharp", self.by_id["hero-1"]["prompt"])
        self.assertIn("grey irises", self.by_id["hero-100"]["prompt"])

    def test_source_facts_and_fill_ins_kept_apart(self):
        late = self.by_id["hero-100"]
        self.assertIn("Tags: bald head", late["source_facts"]["line"])
        self.assertEqual(late["source_facts"]["eyes"]["basis"], "profile tag: grey eyes")
        self.assertEqual(late["fill_ins"]["clothing"], "a grey robe")
        self.assertIn("expression", late["fill_ins"])
        self.assertIn("eyes", self.by_id["hero-1"]["fill_ins"])

    def test_curated_flag_and_deterministic_hash(self):
        self.assertTrue(self.by_id["hero-1"]["curated"])
        self.assertFalse(il.build_prompts(ROWS, {})[0]["curated"])
        self.assertEqual(il.build_prompts(ROWS, OVERRIDES), self.entries)

    def test_repo_prompts_are_isolated(self):
        """Tags exclusive to another range of the same character never leak into a prompt."""
        entries = il.build_prompts()
        groups: dict[str, list[dict]] = {}
        for entry in entries:
            if not entry.get("skip"):
                groups.setdefault(entry["character"], []).append(entry)
        for character, items in groups.items():
            for entry in items:
                own = {tag.casefold() for tag in entry["source_facts"]["tags"]}
                for other in items:
                    for tag in other["source_facts"]["tags"]:
                        tag_cf = tag.casefold()
                        if len(tag) > 6 and tag_cf not in entry["source_facts"]["line"].casefold() \
                                and not any(tag_cf in mine or mine in tag_cf for mine in own):
                            self.assertNotIn(tag.casefold(), entry["prompt"].casefold(), (entry["id"], tag))
        self.assertNotIn("asmodeus", {entry["slug"] for entry in entries})
        self.assertNotIn("lord-of-heaven", {entry["slug"] for entry in entries})


class GenerateTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.patches = [patch.object(il, name, root / rel) for name, rel in (
            ("ROOT", "."), ("WORK", ".work/illustrations"), ("ORIGINALS", ".work/illustrations/originals"),
            ("PUBLIC", "reader/public/characters"), ("READER_DATA", "reader/src/data/ci.json"),
            ("MANIFEST", "reviews/illustrations/manifest.json"), ("CODEX_IMAGES", "codex-images"))]
        for item in self.patches:
            item.start()
        il.ROOT = root
        self.root = root
        self.entries = il.build_prompts(ROWS, OVERRIDES)
        self.calls = []

    def tearDown(self):
        for item in self.patches:
            item.stop()
        self.tmp.cleanup()

    def fake_codex(self, thread="t1", images=2, stdout_extra="", stderr=""):
        def runner(command, **kwargs):
            self.calls.append((command, kwargs))
            self.assertIs(kwargs["stdin"], subprocess.DEVNULL)
            if images:
                from PIL import Image
                folder = il.CODEX_IMAGES / thread
                folder.mkdir(parents=True, exist_ok=True)
                for index in range(images):
                    Image.new("RGB", (1024, 1280), (index * 90, 10, 10)).save(folder / f"exec-{index}.png")
            lines = [json.dumps({"type": "thread.started", "thread_id": thread}), stdout_extra,
                     json.dumps({"type": "turn.completed", "usage": {"input_tokens": 100, "output_tokens": 5}})]
            return subprocess.CompletedProcess(command, 0 if images else 1, "\n".join(lines), stderr)
        return runner

    def test_generate_records_manifest_and_reader_data(self):
        manifest = {"version": 1, "items": {}}
        record = il.generate_one(self.entries[0], manifest, self.entries, runner=self.fake_codex())
        self.assertEqual(record["thread_id"], "t1")
        self.assertEqual(record["generations"], 2)
        self.assertEqual(record["prompt_hash"], self.entries[0]["prompt_hash"])
        from PIL import Image
        with Image.open(self.root / record["original"]) as image:
            self.assertEqual(image.getpixel((0, 0))[0], 90)  # newest PNG in the thread dir
        with Image.open(il.PUBLIC / "hero-1.webp") as image:
            self.assertEqual(image.size, (512, 640))
        saved = json.loads(il.MANIFEST.read_text())
        self.assertEqual(saved["items"]["hero-1"]["status"], "done")
        data = json.loads(il.READER_DATA.read_text())
        self.assertEqual(data, {"Hero": [{"from": 1, "to": 99, "image": "characters/hero-1.webp",
                                          "alt": self.entries[0]["alt"]}]})
        command = self.calls[0][0]
        self.assertIn("--json", command)
        self.assertIn("exactly one image", command[-1])

    def test_select_skips_done_and_stale_and_uncurated(self):
        manifest = {"items": {"hero-1": {"status": "done", "prompt_hash": "old"}}}
        self.assertEqual([e["id"] for e in il.select(self.entries, manifest, [], False, False)], ["hero-100"])
        self.assertEqual(il.state(self.entries[0], manifest["items"]["hero-1"]), "stale")
        self.assertEqual(il.state(self.entries[0], {"status": "done", "prompt_hash": "old", "keep": True}), "done")
        self.assertEqual(len(il.select(self.entries, manifest, [], True, False)), 2)
        manifest["items"]["hero-1"] = {"status": "failed", "prompt_hash": "x"}
        self.assertEqual(len(il.select(self.entries, manifest, [], False, False)), 2)
        uncurated = il.build_prompts(ROWS, {})
        self.assertEqual(il.select(uncurated, {"items": {}}, [], False, False), [])
        with self.assertRaises(SystemExit):
            il.select(uncurated, {"items": {}}, ["hero-1"], False, False)
        self.assertEqual(len(il.select(uncurated, {"items": {}}, [], False, True)), 2)
        skipping = il.build_prompts(ROWS, {"Hero": {"ranges": {"100": {"skip": "vision, not a lasting change"}}}})
        self.assertEqual([e["id"] for e in il.select(skipping, {"items": {}}, [], False, False)], ["hero-1"])
        with self.assertRaises(SystemExit):
            il.select(skipping, {"items": {}}, ["hero-100"], False, False)

    def test_variant_keeps_main_record_and_reader_data(self):
        manifest = {"version": 1, "items": {}}
        il.generate_one(self.entries[0], manifest, self.entries, runner=self.fake_codex("t1"))
        il.generate_one(self.entries[0], manifest, self.entries, Path("/ref.png"), self.fake_codex("t2"), "ref")
        self.assertIn("hero-1~ref", manifest["items"])
        self.assertTrue((il.ORIGINALS / "hero-1~ref.png").exists())
        self.assertFalse((il.PUBLIC / "hero-1~ref.webp").exists())
        self.assertEqual(len(json.loads(il.READER_DATA.read_text())["Hero"]), 1)
        self.assertIn("--image=/ref.png", self.calls[1][0])
        self.assertIn("only as an art-style reference", self.calls[1][0][-1])

    def test_quota_failure_is_blocked_and_stops(self):
        error = json.dumps({"type": "error", "message": "You've hit your usage limit. Try again later."})
        with self.assertRaises(il.Blocked):
            il.run_codex(self.entries[0], runner=self.fake_codex(images=0, stdout_extra=error))
        with self.assertRaises(il.Failed):
            il.run_codex(self.entries[0], runner=self.fake_codex(images=0, stderr="boom"))

    def test_command_stops_at_first_failure_and_resumes(self):
        prompts = self.root / "prompts.json"
        prompts.write_text(json.dumps({"prompts": self.entries}))
        args = il.argparse.Namespace(ids=[], max=5, force=False, allow_uncurated=False, reference=None, variant=None)
        with patch.object(il, "PROMPTS", prompts), \
                patch.object(il, "run_codex", side_effect=il.Blocked(json.dumps({"error": "rate limit exceeded"}))) as run:
            self.assertEqual(il.command_generate(args), 3)
            self.assertEqual(run.call_count, 1)
        manifest = json.loads(il.MANIFEST.read_text())
        self.assertEqual(manifest["items"]["hero-1"]["status"], "blocked")
        runner = self.fake_codex()
        real = il.run_codex
        with patch.object(il, "PROMPTS", prompts), \
                patch.object(il, "run_codex", side_effect=lambda entry, reference=None, _=None: real(entry, reference, runner)):
            self.assertEqual(il.command_generate(args), 0)
        manifest = json.loads(il.MANIFEST.read_text())
        self.assertEqual({key: value["status"] for key, value in manifest["items"].items()},
                         {"hero-1": "done", "hero-100": "done"})


if __name__ == "__main__":
    unittest.main()


class KeyArtTest(unittest.TestCase):
    def test_title_verbatim_and_cast_uses_early_ranges(self):
        spec = {"title": "Murim Login", "style": "webtoon",
                "scenes": {"art-1": {"idea": "i", "cast": [["Hero", 1]], "scene": "s", "composition": "c",
                                     "title_placement": "top"}}}
        entry = il.keyart_prompts(spec, OVERRIDES | {"Hero": {"identity": "a square jaw",
                                                               "ranges": {"1": {"appearance": "an old man"},
                                                                          "100": {"appearance": "a bald man"}}}})[0]
        self.assertIn('Text (verbatim): "Murim Login" (spelled M-U-R-I-M L-O-G-I-N), exactly once', entry["prompt"])
        self.assertIn("- Hero: an old man; face (keep exactly): a square jaw", entry["prompt"])
        self.assertNotIn("bald", entry["prompt"])

    def test_repo_keyart_cast_is_spoiler_free(self):
        for entry in il.keyart_prompts():
            for later in ("red hair", "bald", "monk", "iron-hard", "skull"):
                self.assertNotIn(later, entry["prompt"])
