import unittest

from tools.audit_range import apply_patchset, blocks, split_chapter_group, subset_review


class AuditRangeTest(unittest.TestCase):
    def test_blocks_preserve_order_and_remainder(self):
        self.assertEqual(blocks(list(range(8)), 5), [list(range(5)), [5, 6, 7]])

    def test_exact_patch_is_applied_once(self):
        patchset = {"patches": [{"chapter": 1, "finding_ids": ["R1"], "old": "shook his head", "new": "nodded"}]}
        result = apply_patchset(patchset, {1: "He shook his head."})
        self.assertEqual(result[1], "He nodded.")

    def test_ambiguous_patch_is_rejected(self):
        patchset = {"patches": [{"chapter": 1, "finding_ids": ["R1"], "old": "head", "new": "face"}]}
        with self.assertRaises(ValueError):
            apply_patchset(patchset, {1: "His head met the head."})

    def test_subset_review_keeps_named_chapters(self):
        data = {"findings": [{"chapter": 9, "id": "a"}, {"chapter": 10, "id": "b"}]}
        self.assertEqual([item["id"] for item in subset_review(data, [10])["findings"]], ["b"])

    def test_split_chapter_group_keeps_a_fitting_block(self):
        from unittest.mock import patch
        review = {"findings": [{"chapter": 9}, {"chapter": 10}]}
        with patch("tools.audit_range.build_refine_packet", return_value="x"), patch(
            "tools.audit_range.estimated_tokens", return_value=1000
        ):
            self.assertEqual(split_chapter_group([9, 10], review, 80000), [[9, 10]])

    def test_split_chapter_group_halves_an_oversize_block(self):
        from unittest.mock import patch
        review = {"findings": [{"chapter": 9}, {"chapter": 10}]}
        with patch("tools.audit_range.build_refine_packet", return_value="x"), patch(
            "tools.audit_range.estimated_tokens", side_effect=[90000, 1000, 1000]
        ):
            self.assertEqual(split_chapter_group([9, 10], review, 80000), [[9], [10]])


class AuditRangeTest(unittest.TestCase):
    def test_blocks_preserve_order_and_remainder(self):
        self.assertEqual(blocks(list(range(8)), 5), [list(range(5)), [5, 6, 7]])

    def test_exact_patch_is_applied_once(self):
        patchset = {"patches": [{"chapter": 1, "finding_ids": ["R1"], "old": "shook his head", "new": "nodded"}]}
        result = apply_patchset(patchset, {1: "He shook his head."})
        self.assertEqual(result[1], "He nodded.")

    def test_ambiguous_patch_is_rejected(self):
        patchset = {"patches": [{"chapter": 1, "finding_ids": ["R1"], "old": "head", "new": "face"}]}
        with self.assertRaises(ValueError):
            apply_patchset(patchset, {1: "His head met the head."})


if __name__ == "__main__":
    unittest.main()
