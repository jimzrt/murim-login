import re
import unittest
from pathlib import Path

TRANSLATIONS = Path(__file__).resolve().parents[1] / "translations"


class TranslationFormatTest(unittest.TestCase):
    def test_ellipses_use_a_single_character(self):
        for path in sorted(TRANSLATIONS.glob("[0-9][0-9][0-9][0-9].md")):
            text = path.read_text(encoding="utf-8")
            self.assertNotIn("……", text, path.name)
            self.assertNotIn("...", text, path.name)
            self.assertIsNone(re.search(r"…\.(?!\.)", text), path.name)

    def test_every_footnote_reference_has_a_definition(self):
        for path in sorted(TRANSLATIONS.glob("[0-9][0-9][0-9][0-9].md")):
            text = path.read_text(encoding="utf-8")
            references = set(re.findall(r"\[\^(\d+)\](?!:)", text))
            definitions = set(re.findall(r"^\[\^(\d+)\]:", text, re.M))
            self.assertLessEqual(references, definitions, path.name)


if __name__ == "__main__":
    unittest.main()
