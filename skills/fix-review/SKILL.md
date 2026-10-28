---
name: fix-review
description: Reads the change an agent made to turn a failing check green, asks whether it solves the problem or only moves the number, and adds a check that catches the shortcut. Fixes "the agent fixed the failing check, it's green, and the work got worse." Use whenever an agent says a failing test, gate, lint rule or score now passes, before you accept an automatic fix, when a check turns green faster than you expected, and when the agent touched a test, a threshold or the check itself. Also on /fix-review.
---

# Fix review

Your agent fixed a failing check, and it is green. Before you accept it, look at what it changed to make the check pass.
An agent asked to make a check pass looks for the easiest change that turns it green. That change does not always solve the problem.
This skill reads the fix, asks whether it solved anything, and adds a check that catches the shortcut.

## The principles
1. A green check tells you the number moved. It does not tell you the work got better.
2. Read the change itself, not only the result.
3. Every shortcut you find gets its own check, so it cannot pass a second time.

## Steps
1. When a check that was failing passes after an agent's fix, stop before you accept it. Open the change that turned it green with `git diff` or `git show`.
2. Say in one sentence what the check measures and which problem it is there to catch.
3. Read every changed line and ask: does this change solve the problem, or only move the number? These are signs that it only moved the number:
   - it changed the test, the threshold or the check
   - it added filler to reach a count
   - it made a special case for the test input
   - it skipped or exempted something
   - it piled more of the same onto what was already there
4. Look at the real output the way a user would: watch it, open it or run it. The check does not look for you.
5. If the change only moved the number, say so plainly. Hold the change, and fix the real problem before you report anything.
6. Add a check that catches the shortcut. Write it as a rule a stranger could answer yes or no. Ours: no two animations on one element at the same moment. Run it on the shortcut to show it fails, then run it on the real fix to show it passes.
7. Report four things: what the check measures, what the agent changed, whether that solved the problem or moved the number, and the new check with both of its results.

## Rules
- Never accept "it's green" without the diff next to it.
- If the agent edited a test, a threshold or a check, report that first, and wait for the owner's yes.
- If a check passed and the output looks worse, believe the output.
- The real case is in scripts/june-commits.txt and scripts/PROOF.md. In June 2026 our agent passed a minimum-animation check by stacking extra animations on elements that were already there, all at the same moment. The videos flickered, a person caught it by watching, and that same day we added an anti-flicker check and rewrote the fix. That shows one case, ours. It does not show how often agents game checks in general, and it does not show that the agent did it on purpose.
