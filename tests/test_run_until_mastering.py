import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools import run_until_mastering


class RunUntilMasteringTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        (self.root / "translations").mkdir()
        self.root_patch = patch.object(run_until_mastering, "ROOT", self.root)
        self.root_patch.start()

    def tearDown(self):
        self.root_patch.stop()
        self.temporary.cleanup()

    def touch_translation(self, number: int) -> None:
        (self.root / "translations" / f"{number:04d}.md").write_text(
            f"# Chapter {number}\n", encoding="utf-8"
        )

    def test_plans_unmastered_chapters_through_until(self):
        for number in (41, 42, 43, 44):
            self.touch_translation(number)
        with (
            patch.object(run_until_mastering, "next_mastering_chapter", return_value=41),
            patch.object(
                run_until_mastering,
                "needs_mastering",
                side_effect=lambda n: n in {41, 42, 44},
            ),
            patch.object(
                run_until_mastering,
                "accepted_translation_numbers",
                return_value=[41, 42, 43, 44],
            ),
        ):
            self.assertEqual(run_until_mastering.planned_chapters(44), [41, 42, 44])
            self.assertEqual(run_until_mastering.planned_chapters(42), [41, 42])
            self.assertEqual(run_until_mastering.planned_chapters(40), [])

    def test_dry_run_prints_plan_without_running(self):
        with (
            patch.object(run_until_mastering, "planned_chapters", return_value=[41, 42]),
            patch.object(run_until_mastering, "next_mastering_chapter", return_value=41),
            patch.object(run_until_mastering, "run_next_mastering_chapter") as runner,
            patch("sys.argv", ["run_until_mastering.py", "42", "--dry-run"]),
        ):
            self.assertEqual(run_until_mastering.main(), 0)
        runner.assert_not_called()
        self.assertFalse((self.root / ".work" / "master.lock").exists())

    def test_runs_each_chapter_and_stops_on_failure(self):
        remaining = {41, 42, 43}

        def fake_next():
            return min(remaining) if remaining else None

        def fake_needs(number: int) -> bool:
            return number in remaining

        def fake_run():
            current = fake_next()
            if current == 42:
                return 7
            remaining.remove(current)
            return 0

        with (
            patch.object(run_until_mastering, "next_mastering_chapter", side_effect=fake_next),
            patch.object(run_until_mastering, "needs_mastering", side_effect=fake_needs),
            patch.object(
                run_until_mastering,
                "accepted_translation_numbers",
                return_value=[41, 42, 43],
            ),
            patch.object(run_until_mastering, "run_next_mastering_chapter", side_effect=fake_run),
            patch("sys.argv", ["run_until_mastering.py", "43"]),
        ):
            self.assertEqual(run_until_mastering.main(), 7)
        self.assertEqual(remaining, {42, 43})

    def test_existing_master_lock_blocks_run_until_mastering(self):
        import subprocess
        import sys
        import time
        from tools.run_lock import read_payload, lock_path

        repo = Path(__file__).resolve().parents[1]
        holder = subprocess.Popen(
            [
                sys.executable,
                "-c",
                "import sys, time\n"
                "from pathlib import Path\n"
                "sys.path.insert(0, sys.argv[1])\n"
                "from tools.run_lock import hold_master_lock\n"
                "with hold_master_lock(Path(sys.argv[2]), holder='run_next_mastering', chapter=12, stage='workflow'):\n"
                "    time.sleep(30)\n",
                str(repo),
                str(self.root),
            ],
            cwd=repo,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            text=True,
        )
        try:
            deadline = time.time() + 5
            payload = {}
            while time.time() < deadline:
                payload = read_payload(lock_path(self.root, "master.lock"))
                if payload.get("holder") == "run_next_mastering":
                    break
                if holder.poll() is not None:
                    self.fail(holder.stderr.read())
                time.sleep(0.05)
            self.assertEqual(payload.get("holder"), "run_next_mastering")
            with (
                patch.object(run_until_mastering, "planned_chapters", return_value=[41]),
                patch.object(run_until_mastering, "next_mastering_chapter", return_value=41),
                patch.object(run_until_mastering, "run_next_mastering_chapter") as runner,
                patch("sys.argv", ["run_until_mastering.py", "41"]),
            ):
                with self.assertRaises(SystemExit) as error:
                    run_until_mastering.main()
            runner.assert_not_called()
            self.assertIn("already in progress", str(error.exception))
            self.assertIn("run_next_mastering", str(error.exception))
        finally:
            holder.terminate()
            holder.wait(timeout=5)
            if holder.stderr:
                holder.stderr.close()


if __name__ == "__main__":
    unittest.main()
