import tempfile
import unittest
from pathlib import Path

from tools import ledgers


ADDRESS = """# Established Address Pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Greeting. |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공. |
"""

RISKS = """# Korean Danger Register

| Korean | Category | Constraint | Forbidden English |
| ------ | -------- | ---------- | ----------------- |
| 피식 | polysemy | Short laugh, not necessarily a smirk. | smirk |
| 당장은 | polysemy | Right away, not anytime soon. | anytime soon |
"""


class LedgerTest(unittest.TestCase):
    def test_address_pairs_require_both_endpoints(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "ADDRESS.md"
            path.write_text(ADDRESS, encoding="utf-8")
            pairs = ledgers.load_address_pairs(path)
        matched = ledgers.matching_address_pairs("진무경이 웃었다.", {"진태경"}, pairs)
        self.assertEqual([item["addressee"] for item in matched], ["진무경"])
        self.assertEqual(matched[0]["normal_address"], "hyung")
        self.assertEqual(ledgers.matching_address_pairs("진무경이 웃었다.", set(), pairs), [])

    def test_risks_match_exact_korean_and_parse_forbidden(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "RISKS.md"
            path.write_text(RISKS, encoding="utf-8")
            risks = ledgers.load_risks(path)
        matched = ledgers.matching_risks("진무경이 피식 웃었다.", risks)
        self.assertEqual([item["korean"] for item in matched], ["피식"])
        self.assertEqual(matched[0]["forbidden"], ["smirk"])
        self.assertEqual(ledgers.matching_risks("당장은 볼 수 없다.", risks)[0]["korean"], "당장은")
        self.assertIn("No matching risk notes", ledgers.risks_text([]))
        self.assertIn("피식", ledgers.risks_text(matched))

    def test_project_ledgers_load(self):
        pairs = {(item["speaker"], item["addressee"]) for item in ledgers.load_address_pairs()}
        self.assertIn(("진태경", "진무경"), pairs)
        risks = {item["korean"]: item for item in ledgers.load_risks()}
        self.assertIn("시침 뚝 떼", risks)
        self.assertEqual(risks["피식"]["forbidden"], ["smirk"])
        self.assertTrue(ledgers.matching_risks("지금은 시침 뚝 떼고 웃었다.", list(risks.values())))
