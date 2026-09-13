import tempfile
import unittest
from pathlib import Path

from tools import benchmark


class BenchmarkTest(unittest.TestCase):
    def test_load_and_score_accepted_translations(self):
        items = benchmark.load_items()
        self.assertGreaterEqual(len(items), 25)
        report = benchmark.score_items(items)
        self.assertEqual(report["counts"]["fail"], 0)
        self.assertEqual(report["counts"]["missing"], 0)
        self.assertGreater(report["counts"]["pass"], 0)

    def test_forbidden_span_fails_an_item(self):
        item = {
            "id": "ML-064-anaphora-01",
            "chapter": 64,
            "category": "zero_anaphora",
            "source": "아직 안 끝났다.",
            "constraint": "Situational reading.",
            "origin": "test",
            "required": ["It’s not over yet."],
            "forbidden": ["I’m not finished"],
        }
        result = benchmark.score_item(item, "# Chapter 64\n\n“I’m not finished.”\n")
        self.assertEqual(result["status"], "fail")
        self.assertEqual(result["forbidden_hits"], ["I’m not finished"])

    def test_missing_translation_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "translations").mkdir()
            items = [{
                "id": "ML-001-test-01",
                "chapter": 1,
                "category": "idiom",
                "source": "테스트",
                "constraint": "Placeholder.",
                "origin": "test",
                "required": ["Hello"],
                "forbidden": [],
            }]
            report = benchmark.score_items(items, root=root)
        self.assertEqual(report["counts"]["missing"], 1)
        self.assertEqual(report["results"][0]["status"], "missing")
