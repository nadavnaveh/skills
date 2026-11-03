---
name: skill-button
description: Runs a Claude Code skill from a script like a button. One input in, one line back, and code marks each input PASS or FAIL and exits 1 if any fails, so a schedule or CI can stop. Fixes "I run my skill by hand and read a long answer every time." Use when a skill runs often on new inputs, or when you want it on a schedule or in CI. Also on /skill-button.
---

# Skill button

You run the skill and judge a long answer by eye, so it only runs while you watch. This skill gives you our script, with the check: one line back, checked by code, and a stop when it fails.

## The principles
1. A skill that runs often should run from a script, a short code file that runs on its own.
2. Ask for one line back, because code can check one line on its own.
3. The code checks that line, marks each input PASS or FAIL and exits 1 if any fails, so a schedule or CI can stop.

## Steps
1. Check the fit: the skill runs often, and its answer can be one checkable line. If a good answer needs a page, keep typing it.
2. Write the inputs in a text file, one per line.
3. Write the pass rule as `--pass "w1,w2"`. One word, in any case, even inside a longer word ("claim" matches "claims"), is a pass. A word match is a weak check, so read a known wrong answer and pick words only a good line contains: "unverified" for a claims skill, never "the".
4. Test it both ways: your words give PASS, and a word no answer contains, such as zzqqxx, gives FAIL and exit 1.
5. Run it from the project where the skill is installed, using the full path to this skill's scripts folder, or pass --cwd DIR:
   `python3 scripts/skill_button.py SKILL INPUTS.txt --pass "w1,w2" [--model haiku] [--cwd DIR]`
   SKILL is the name without the slash. Each input prints PASS or FAIL, exit code, seconds, cost and the line.
6. Schedule it with cron or a Claude Code scheduled task. Exit 1 is the stop, but only if the job reacts to it, such as running the next step only after a pass. In cron, use full paths to python3 and the inputs file, and a PATH that includes claude.
7. On a FAIL, read the line. A FAIL also comes when claude errors or returns nothing, shown as the error or "no answer". Fix the skill or input and run again.

Our run: our vendor-claims skill from a script on 3 claims, 3 of 3 PASS, 9 to 27 seconds each, about 5 cents in all (API-equivalent). Called the long way, its answers ran 452 to 567 words and 43 to 56 seconds.

## Rules
- One line back. Never parse a long answer. The script reads only the last line.
- The script stops the run. It does not fix anything.
- No API keys in the script. It runs `claude -p` under your Claude Code login.
- A PASS means the words were there, not that the line is true.
