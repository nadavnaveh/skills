#!/usr/bin/env python3
"""Run a Claude Code skill like a button: one input in, one checkable line out, a PASS or FAIL per input.

  python3 skill_button.py SKILL INPUTS.txt --pass "word1,word2" [--model haiku] [--cwd DIR]

SKILL       the skill's name, without the slash (it must be installed where --cwd points)
INPUTS.txt  one input per line
--pass      words the one-line answer must contain; PASS when at least one appears (case does not matter)
Prints PASS/FAIL, exit code, seconds, cost and the line for each input. Exits 1 if any input fails, so a schedule or CI can stop on it.
Built from the script in our run (3 of 3 PASS, 2026-11-02)."""
import argparse, json, subprocess, sys, time

ap = argparse.ArgumentParser()
ap.add_argument("skill"); ap.add_argument("inputs")
ap.add_argument("--pass", dest="words", required=True); ap.add_argument("--model", default="haiku"); ap.add_argument("--cwd", default=".")
a = ap.parse_args()
words = [w.strip().lower() for w in a.words.split(",") if w.strip()]
failed = 0
for item in [l for l in open(a.inputs, encoding="utf-8").read().splitlines() if l.strip()]:
    t = time.time()
    r = subprocess.run(["claude", "-p", f"/{a.skill} {item} Return ONLY one line, nothing else.", "--model", a.model, "--output-format", "json"],
                       cwd=a.cwd, capture_output=True, text=True)
    try:
        d = json.loads(r.stdout); lines = (d.get("result") or "").strip().splitlines(); line = lines[-1] if lines else ""
    except ValueError:
        d, line = {}, ""
    ok = r.returncode == 0 and bool(line) and any(w in line.lower() for w in words)
    failed += not ok
    print(f"{'PASS' if ok else 'FAIL'}\texit {r.returncode}\t{time.time() - t:.0f}s\t${d.get('total_cost_usd', 0) or 0:.3f}\t{line or (r.stderr.strip()[:200] or 'no answer')}", flush=True)
sys.exit(1 if failed else 0)
