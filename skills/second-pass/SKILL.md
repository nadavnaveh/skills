---
name: second-pass
description: Adds the second pass to every coding task. After the agent writes code, it lists the odd cases the request implies, writes a check for each, runs those checks and the project's tests, fixes and reruns for up to three rounds, then reports what was checked, what passed and what was not checked. Fixes "the code worked on the normal case and broke on the first odd one." Use after writing or changing any code and before you report a coding task as finished. Also on /second-pass.
---

# Second pass

The code worked on the normal case, then broke on the first odd one. One pass writes what the request says, and the cases it only implies never get tried. This skill adds the second pass: list the odd cases, check each one, fix, and say plainly what was not checked.

## The principles
1. Writing the code is the first pass. Trying to break it is the second.
2. A check counts only if it ran. Reading the code is not a check.
3. A failing test means fix the code, not the test.
4. It matters most where the rules are tricky. In our small test (eight tricky functions, one small model, three runs each), writing in one go scored 20, 20 and 19 out of 20 hidden checks. The second pass scored 20 every time, for about 23% more cost. On an easier set, both scored 20 every time.

## Steps
1. Write the code the request asked for.
2. Reread the request and list the odd cases it implies. Go through each kind:
   - **Empty**: no input, one item, a missing value.
   - **Boundaries**: zero, negatives, the first and last allowed value, one step past them.
   - **Separators**: commas inside quotes, extra spaces, hyphens, slashes.
   - **Dates**: month and year ends, leap years, week numbers.
   - **Rounding**: money, exact halves, tiny fractions.
   If a kind cannot apply, say why in one line.
3. For each odd case, write one check: the input and the expected answer. Take the answer from the request, not from what the code does now. If the request does not settle the answer, do not guess. Put the case on the not-checked list.
4. Run every check, plus the project's tests if it has any. If no tests ran, say so. That is not a pass.
5. Fix the code for each failure, then rerun everything. Stop when all pass or after three rounds.
6. Report in plain words:
   - **Checked**: each odd case and test run.
   - **Passed**: what passed, with the output.
   - **Failed**: what still fails after three rounds, and what happened instead.
   - **Not checked**: what was left out, and why.

## Rules
- Never edit, skip or delete a test to make it pass. This includes your own checks. If a test looks wrong, tell the person why and let them decide.
- Three rounds is the limit. After that, hand back to the person with what still fails.
- Never say "it works" without the report next to it.
- "All passed" covers only what is listed. Always include the not-checked list, even when it is short.
