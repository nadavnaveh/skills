---
name: check-ways
description: Checks an agent's work in five ways before you trust it. It runs the tests, has a second agent review the work, sets a gate the work must pass before it counts as done, reads the diff line by line, and tries the result the way a user would. Fixes "I trusted the agent's work, and it broke the first time someone used it." Use when an agent says a task is done, before you commit, merge, ship or send its work, before you report your own work as finished, and whenever the change touches sign-up, payments, data or anything a user sees. Also on /check-ways.
---

# Check ways

The agent said it works. You trusted it, and it broke the first time someone used it. The agent that did the work is a poor judge of it, because it checks what it meant to build, not what it built. This skill checks the work in five ways that do not depend on the agent's word.

## The principles
1. The agent's word is not a check. Only something outside the agent can pass the work.
2. The tests decide. Not the agent, and not a feeling.
3. Fresh eyes catch what the author cannot see.
4. Done is a gate, not a claim. Nothing gets through while a check fails.

## Steps
1. **Tests.** Run the test command from CLAUDE.md or the README, and report a count, for example "12 of 12 passed". If any fail, the work is not done. If the change has no test, write one that fails without the change and passes with it.
2. **Review.** Start a subagent with a fresh window. Give it only the diff and one line on what the change should do, not the conversation. Ask it to find what is wrong. It either approves or names the exact line and the problem. Fix that and send the work back to it.
3. **A gate.** Ask the owner before adding a git pre-commit hook that runs the tests and refuses the commit while any test fails. If the project already has a gate, keep it on.
4. **The diff.** Run `git diff` and read every changed line. Look for what nobody asked for: a deleted check, a test changed so it passes, a hard-coded value, a file outside the task. Point the owner to the lines that touch money, data or sign-in.
5. **As a user.** Use it the way a real user would, step by step, with test data: open /signup, sign up, pay with a test card, see the receipt. Write down each step and what you saw. If you cannot do this yourself, write the exact steps for the owner.
6. Report all five checks as passed, failed or not run, each with its evidence. Call the work done only when every check that ran has passed and the owner knows which ones did not run.

## Rules
- Fix a failing test in the code. Change the test only if the owner agrees the test was wrong.
- The reviewer sees the work, never the author's reasoning.
- Never use `--no-verify` or turn a gate off to get a commit through.
- For work that is not code, your written checks are the tests and the reader is the user.
- Real money, real accounts and real emails stay out of the user test.
