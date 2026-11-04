import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def ignored(path: str) -> bool:
    result = subprocess.run(
        ["git", "check-ignore", "-q", "--no-index", path], cwd=ROOT, check=False
    )
    return result.returncode == 0


class SourceNotCommittedTest(unittest.TestCase):
    def test_files_embedding_korean_source_are_ignored(self):
        for path in (
            "source/0001.txt",
            "reviews/packets/update-0001.md",
            "reviews/packets/summary-0001-0005.md",
            "reviews/packets/checkpoint-0001-0005.md",
            "reviews/mastering/0001/omp/master.jsonl",
            "reviews/mastering/0001/omp/adjudicator.jsonl",
            "reviews/mastering/0001/omp/fidelity-gate.jsonl",
            "reviews/final/0001/omp/final.jsonl",
            "reviews/entity/0001/omp/detect.jsonl",
            "reviews/address/0001/omp/address.jsonl",
            "reviews/retrofit/0001-0005/refine-packet-0001-0005.md",
        ):
            self.assertTrue(ignored(path), path)

    def test_state_the_tools_depend_on_stays_tracked(self):
        for path in (
            "reviews/mastering/0001/state.json",
            "reviews/final/0001/state.json",
            "reviews/entity/0001/state.json",
            "reviews/address/0001/state.json",
            "reviews/metrics/0001.json",
            "reviews/illustrations/keyart.json",
        ):
            self.assertFalse(ignored(path), path)


if __name__ == "__main__":
    unittest.main()
