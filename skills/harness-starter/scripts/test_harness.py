#!/usr/bin/env python3
"""Tests for the harness: run with `python3 -m unittest test_harness.py` from this folder. A guard that breaks quietly is worse than no guard."""
import json, os, subprocess, sys, tempfile, time, unittest
HERE = os.path.dirname(os.path.abspath(__file__))
GUARD, QRUN = os.path.join(HERE, "guard.py"), os.path.join(HERE, "qrun.py")


def guard(stdin):
    return subprocess.run([sys.executable, GUARD], input=stdin, capture_output=True, text=True)


def cmd(c):
    return guard(json.dumps({"tool_input": {"command": c}}))


class Guard(unittest.TestCase):
    def test_blocks_what_you_cannot_undo(self):
        for c in ("rm -rf build", "rm -f notes.txt", "git push origin main --force", "git push -f origin main",
                  "git reset --hard HEAD~1", "psql -c 'DROP TABLE users'"):
            r = cmd(c)
            self.assertEqual(r.returncode, 2, c); self.assertIn("Ask the owner first", r.stderr)

    def test_lets_normal_work_through(self):
        for c in ("ls -la", "git status", "git push origin main", "grep -rf patterns.txt src"):
            self.assertEqual(cmd(c).returncode, 0, c)

    def test_broken_input_blocks_instead_of_passing(self):   # a crash that passes is a guard that fails open
        for bad in ("", "not json", "[]", '{"tool_input": 5}'):
            self.assertEqual(guard(bad).returncode, 2, bad)


class Queue(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp(); self.env = dict(os.environ, QRUN_DIR=self.d, QRUN_MIN_FREE="0", QRUN_HEAVY_MAX="1")

    def run_q(self, *job, **kw):
        return subprocess.run([sys.executable, QRUN, "--", *job], env=dict(self.env, **kw), capture_output=True, text=True, timeout=30)

    def test_runs_the_job_and_keeps_its_exit_code(self):
        self.assertEqual(self.run_q(sys.executable, "-c", "raise SystemExit(7)").returncode, 7)

    def test_second_job_waits_for_the_slot(self):
        first = subprocess.Popen([sys.executable, QRUN, "--", sys.executable, "-c", "import time; time.sleep(3)"], env=self.env)
        time.sleep(1); t = time.time()
        self.run_q(sys.executable, "-c", "pass"); first.wait()
        self.assertGreater(time.time() - t, 1.0)

    def test_no_job_starts_while_memory_is_short(self):
        out = os.path.join(self.d, "ran")
        p = subprocess.Popen([sys.executable, QRUN, "--", sys.executable, "-c", f"open({out!r}, 'w')"], env=dict(self.env, QRUN_MIN_FREE="101"))
        time.sleep(2.5); p.kill(); p.wait()
        self.assertFalse(os.path.exists(out))

    def test_refuses_when_it_cannot_read_memory(self):   # never starts blind
        r = self.run_q(sys.executable, "-c", "print('ran')", QRUN_MIN_FREE="30", QRUN_TEST_NO_METER="1")
        self.assertEqual(r.returncode, 3); self.assertNotIn("ran", r.stdout)


if __name__ == "__main__":
    unittest.main()
