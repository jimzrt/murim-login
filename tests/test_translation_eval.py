import unittest

from tools.translation_eval import evaluate_text


BASELINE = """# Chapter 10

It’s not like I’ve ever used anything like that before…

Successful attempts (2 / 100)

They say you only know what something is like once you’ve experienced it.

“Acquire item.”

This is the life of a gold spoon. The God-Spoon System is realistic.

The courtesans called him the Night King.

The training cave was enormous.
"""


class TranslationEvaluationTest(unittest.TestCase):
    def test_accepted_chapter_ten_anchors_pass(self):
        result = evaluate_text(BASELINE)
        self.assertTrue(result["passed"])
        self.assertEqual(result["passed_checks"], result["total_checks"])

    def test_semantically_equivalent_wording_is_not_pinned_to_baseline_prose(self):
        equivalent = BASELINE.replace(
            "It’s not like I’ve ever used anything like that before…",
            "I’d never had anything like this to draw on before.",
        ).replace(
            "you only know what something is like once you’ve experienced it",
            "experience was everything",
        ).replace(
            "first hung its signboard",
            "first hung out its shingle",
        ).replace("“Acquire item.”", "“Acquire Item.”")
        self.assertTrue(evaluate_text(equivalent)["passed"])

    def test_known_regression_anchors_fail(self):
        candidate = BASELINE.replace(
            "It’s not like I’ve ever used anything like that before…",
            "I should have tried using that from the beginning…",
        ).replace(
            "Successful attempts (2 / 100)",
            "Remaining successful attempts (2 / 100)",
        ).replace(
            "you only know what something is like once you’ve experienced it",
            "you only know the value of meat once you’ve tasted it",
        ).replace("“Acquire item.”", "“Item Acquired.”")
        result = evaluate_text(candidate)
        failed = {item["id"] for item in result["checks"] if not item["passed"]}
        self.assertEqual(
            failed,
            {"internal_energy_realization", "counter_direction", "idiom_function", "inventory_command"},
        )


if __name__ == "__main__":
    unittest.main()
