import unittest

from tools import run_catchup


class RunCatchupTest(unittest.TestCase):
    def test_catchup_ranges(self):
        self.assertEqual(run_catchup.KEEP_LIVE, list(range(2, 9)))
        self.assertEqual(run_catchup.FULL_RESET[:3], [9, 10, 11])
        self.assertEqual(run_catchup.FULL_RESET[-1], 179)
        self.assertNotIn(161, run_catchup.FULL_RESET)
        self.assertNotIn(64, run_catchup.REMASTER)
        self.assertNotIn(1, run_catchup.REMASTER)
        self.assertEqual(run_catchup.LANE_A[0], 2)
        self.assertEqual(run_catchup.LANE_A[-1], 63)
        self.assertEqual(run_catchup.LANE_B, list(range(162, 180)))
        self.assertEqual(run_catchup.REGISTER_ONLY, [1, 64])

    def test_catchup_owns_path(self):
        self.assertTrue(run_catchup.catchup_owns_path("translations/0012.md"))
        self.assertTrue(run_catchup.catchup_owns_path("reviews/mastering/0162/sol.md"))
        self.assertTrue(run_catchup.catchup_owns_path("reviews/metrics/0004.json"))
        self.assertTrue(run_catchup.catchup_owns_path("reviews/retrofit/0009-0063/state.json"))
        self.assertFalse(run_catchup.catchup_owns_path("translations/0180.md"))
        self.assertFalse(run_catchup.catchup_owns_path("docs/STATE.md"))
        self.assertFalse(run_catchup.catchup_owns_path("reviews/metrics/0180.json"))

    def test_classify_audit_paths_ignores_other_catchup_dirt(self):
        allowed, unexpected = run_catchup.classify_audit_paths([
            "translations/0012.md",
            "reviews/retrofit/0009-0063/state.json",
            "reviews/mastering/0002/sol.md",
            "translations/0162.md",
            "docs/STATE.md",
        ])
        self.assertEqual(allowed, ["translations/0012.md", "reviews/retrofit/0009-0063/state.json"])
        self.assertEqual(unexpected, ["docs/STATE.md"])

    def test_should_run_phases(self):
        self.assertTrue(run_catchup.should_run("reset", "reset"))
        self.assertTrue(run_catchup.should_run("audit", "reset"))
        self.assertFalse(run_catchup.should_run("reset", "remaster"))
        self.assertTrue(run_catchup.should_run("register", "remaster"))
        self.assertTrue(run_catchup.should_run("verify", "verify"))


if __name__ == "__main__":
    unittest.main()
