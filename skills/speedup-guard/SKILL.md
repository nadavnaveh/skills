---
name: speedup-guard
description: Checks a speedup before you approve it: runs old and new code on the same inputs, edges included, finds where the fast version stops being correct, and guards those bounds with the original. Fixes "the agent made the code much faster, and it gave wrong answers on inputs nobody tried." Use whenever an agent rewrites code to run faster (a new formula, a cache, a rewritten loop), before you approve or merge it. Also on /speedup-guard.
---

# Speedup guard

The agent made the code much faster, and you approved it. Fast code is often correct only inside a range of sizes, types or values, and outside it returns a wrong answer with no error. This skill compares old and new, names the bounds, and guards them.

## The principles
1. Faster means nothing until old and new give the same output.
2. Every speedup has bounds where it stops being correct. Name them.
3. Outside the bounds, the slow and correct original runs.

## Steps
1. Keep the original. Put the new version next to it under a new name.
2. Pick normal inputs plus the edges: largest, smallest, empty, zero, negative, every type that can arrive. First say what "same" means: exact or a stated decimal tolerance, whether order counts, the same error, the same records written.
3. Run both on every input. Report how many you tried, how many did not match, and each mismatch. Time both once.
4. Ask what size, type or range the speedup needs (a number that can overflow, a sorted list). Write each bound as a check, such as "0 <= n <= 3037000500".
5. Test one step past each bound against the original. `scripts/maxdemo.py` shows this once on doubleAI's Maxwell example (about 70 seconds, no need to rerun): the loops and n*(n-1)/2 in 64-bit match for n from 0 to 2000, and one past the bound the formula goes negative while the guarded version is exact.
6. Add the guard: fast inside the bounds, original outside. Rerun the comparison through it, past each bound too, and time it. If the original would take days there, use a scaled-down case or an independent exact method, and say the real original was not run.
7. Report inputs tried, mismatches, old, new and guarded speed, each bound, and what was not tested. Ask "Approve with the guard?"

## Rules
- Never write "same result, faster" without the comparison output next to it.
- Never remove the original while the guard can still call it.
- No bound found or tested past means no approval. Say the speedup is unverified.
- Matching on many inputs is evidence, not proof.
- The demo falls back to exact math, which matches the loops only for n >= 0. A real guard calls the real original, and negatives are compared against it. It shows a bound is real, not that the vendor has this bug or that their speed figures hold.
