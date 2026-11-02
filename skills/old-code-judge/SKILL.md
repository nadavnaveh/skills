---
name: old-code-judge
description: Makes the old code the judge of a rewrite. It saves the old code's exact output on real inputs, runs the new code on the same inputs, compares them byte for byte and fixes the new code until there are 0 differences. Fixes "the agent rewrote my code, and I can't prove it still does the same thing." Use before an agent rewrites or ports code, moves a program to a new language or framework, replaces an old script, or tells you a rewrite behaves the same. Works pasted into any agent. Also on /old-code-judge.
---

# Old code judge

These are the instructions you paste into your agent, inside the project, before it rewrites or ports any code. The agent says the new version does the same thing, but it only checked what it thinks the old code did. Here the old code decides. Use it in any agent that can run your code, or on /old-code-judge.

## The principles
1. The old code is the judge. The agent's opinion is not evidence.
2. Real inputs come first. Made-up inputs can miss what your real ones hit.
3. Save the answers before the new code exists, and never touch them after.
4. Similar is not the same.

## Steps
Before you rewrite this code, make the old version the judge:
1. Collect real inputs the code handles today (files, requests, rows, logs) into rewrite-check/inputs/. Say how many and from where. If there are few or none, say so plainly: 0 differences will then cover very little.
2. Run the OLD code on each input; save the exact output (stdout, stderr, files, exit code) in rewrite-check/expected/. Don't change the old code. If a run would send, pay or change live data, ask the owner first.
3. Write the new version.
4. Run the NEW code on each input and diff against expected/, byte for byte. Similar is not the same.
5. For each difference, show input, old output, new output, then fix the new code. Never edit expected/.
6. Add edge inputs (empty, huge, odd characters, broken files), judged by the old code.
7. End with: real inputs, differences (must be 0), edge inputs, and anything you could not reproduce.

## Rules
- Real inputs may hold private data (customer names, login details). Ask the owner before copying them into rewrite-check/inputs/.
- If the old code gives different output on the same input (a date, a random id), list it under could not reproduce. Never loosen the diff to hide it.
- Zero differences covers the inputs you ran. It proves nothing about inputs you never had.
- Our real run: one Python-to-Rust port, 0 differences on 615 real scripts. That is not a rate for yours.
