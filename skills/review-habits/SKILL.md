---
name: review-habits
description: Reviews code an agent wrote with five habits: keep the change small, read the diff, run it yourself, try empty, huge and odd inputs, and list what no test covers. Fixes "I approved the agent's code after a quick look, and it broke later." Use before you accept, commit or merge any change an agent made, when an agent says a feature or fix is finished, when a pull request is waiting for your review, or when a change looks too big to read in one sitting. Also on /review-habits.
---

# Review habits

You approved the agent's code after a quick look, and it broke later. Agent code looks clean and sure of itself, so it gets skimmed instead of read. This skill reviews it with five habits, in order, and reports what each one found.

## The principles
1. Small changes get real reviews. A 40-line change gets read; a 2,000-line change gets skimmed.
2. The diff is the truth. Review what changed, not what the agent says changed.
3. Seeing it run beats reading that it works.
4. Bugs hide at the edges and in the gaps no test covers.

## Steps
1. Check the size. Run `git diff --stat`. If the change is more than about 400 lines or mixes several jobs, stop. Propose how to split it into small changes, one job each, and review them one at a time.
2. Read the diff. Run `git diff` (or `git diff main...HEAD` for a branch) and read every added and removed line. For each file, say in one line what changed and why. Flag any change the task did not ask for, any check or test that was deleted, and any file nobody named.
3. Run it yourself. Start the app the way the project does (for example `npm run dev`) and walk through the change as a user would. Say what you did and what you saw. If you cannot run it, say so and give the owner the exact steps to run it on their machine.
4. Check the edges. For each new input, try three kinds: empty (nothing, null, an empty list), huge (a very long text, thousands of rows) and odd (special characters, a negative number, the wrong type, a date in the wrong format). Write down what happened for each one.
5. Find what is untested. Run the tests, then list each new function, branch and error path the change added, and mark whether a test covers it. Use the project's coverage tool if it has one. For each gap, write a test or name the gap in the report.
6. Report each habit as pass, fail or not run, with the evidence: the output, the line, what you saw. Put every failure at the top, with its file and line.

## Rules
- Never approve a change you have not read line by line.
- "The agent said it works" is not evidence. Running it is.
- An edge that breaks the code is a finding, not a detail. Fix it with a test that fails first.
- A gap in the tests is reported, never hidden behind a coverage number.
- If a change is too big to read, it is too big to approve.
