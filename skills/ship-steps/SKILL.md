---
name: ship-steps
description: Takes a change from a prompt to a safe merge in five steps. It agrees the plan, builds in a branch, runs the tests, puts the diff in front of you for a second look, and merges only after you say yes. Fixes "The agent changed main, and I never saw what went in." Use when you ask for a feature, a fix or any change to a project kept in git, before the first edit, and whenever the agent is about to commit, push or merge. Also on /ship-steps.
---

# Ship steps

The agent changed main, and nobody saw what went in. It went straight from the prompt to the code, with no plan, no branch, no tests and no second look. This skill takes every change through five steps, from a prompt to a safe merge, and stops for you at each step that needs you.

## The principles
1. Agree on the plan before any code.
2. Main stays clean. The work grows on its own branch.
3. The tests run before review, and the count is shown.
4. Someone looks at the diff, not at the agent's summary of it.
5. A person says yes, and only then does it merge.

## Steps
1. **Plan.** Write the plan as a numbered list of small steps: what changes, which files, and how it will be tested. In Claude Code, plan mode (Shift+Tab) keeps the agent from editing anything yet. Ask "Is this the plan?" and start only after a yes. Tick each step as it is done.
2. **Build in a branch.** Check that main is clean (`git status`). Then make a new branch for this change (`git switch -c <short-name>`). Do all the work and make every commit there. Never commit to main.
3. **Test.** Run the full test suite before review and report the count, like "24 of 24 passed". If any fail, fix them and run the suite again. Zero tests run is not a pass, so say so. If nothing tests this change, write a test first.
4. **Review.** Show the diff against main (`git diff main...HEAD`). Ask a fresh subagent that never saw the work to read the diff and list the problems it finds. Then put the diff in front of the person, with the test count and the reviewer's notes. If they ask for changes, make them, run the tests again and show the new diff.
5. **Merge on a yes.** Ask "Merge this branch into main?" and wait. Merge only after the person says yes to this merge. Then run the tests on main once more and report the count.

## Rules
- No code before the plan has a yes.
- Never commit, push or merge to main without the person's yes for that merge.
- A yes to the plan is not a yes to the merge.
- If the tests failed or did not run, the change does not go to review.
- A diff nobody looked at has not been reviewed.
