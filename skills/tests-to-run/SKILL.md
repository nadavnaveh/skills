---
name: tests-to-run
description: Runs five tests before an agent says a code task is done (unit tests, a type check, lint, one real user flow, and a test for every fixed bug), then reports each one as pass, fail or not run, with the output. Fixes "it said the code was done, and nothing had been tested." Use before you report any code change as finished, right after you fix a bug, before a commit or a pull request, and when a project has no test commands written down yet. Also on /tests-to-run.
---

# Tests to run

The agent said the code was done, and nothing had been run. It read its own change, and the change looked right. This skill runs five tests, from one small function up to a real person's clicks, and shows the result of each before anyone says "done".

## The principles
1. Small pieces are checked alone. A unit test gives one function a known input and expects a known answer.
2. The parts must still fit together. A change in one file can break a call in another, and a type check finds it.
3. Simple mistakes cost least when they are caught early. Lint catches them before a person does.
4. Users do not call functions. They click through pages, so one test must do the same.
5. A bug that was fixed once stays fixed only if a test checks it every time.

## Steps
1. Find the project's commands for tests, type check and lint. Look in CLAUDE.md first, then in the package.json scripts or the project's own equivalent. If one is missing, say so and suggest one (for example `npx tsc --noEmit` or `npx eslint .`). Add it only after the owner says yes. Then write the confirmed commands into CLAUDE.md.
2. Unit tests: every function you changed needs a test that checks it on its own, with a normal input, an edge case and a bad input. Write any that are missing, then run them all.
3. Type check: run it, and fix every error in code you touched. Run it again until it reports 0 errors.
4. Lint: run it on the files you changed. Fix what it finds, such as an unused variable, and run it again.
5. Real user flow: pick the flow your change touches most, for example sign up, fill in the form, see the welcome page. If the project has browser tests, run that flow there. If not, start the app and click through it yourself. Write down each step and what you saw.
6. Bug as a test: if the task fixed a bug, first write a test that repeats the bug, and watch it fail. Then fix the bug and watch the test pass. Name the test after the bug (for example bug_42) and keep it in the suite, so it runs on every change after this one.
7. Report all five tests. Mark each one **Pass** with the output ("12 tests passed", "0 errors"), **Fail** with what broke, or **Not run** with the reason and the exact command the owner can run.

## Rules
- A test you did not run is not a pass.
- Zero tests found is not a pass.
- Never delete, skip or weaken a test to make it pass. If a test looks wrong, say so and ask.
- Say "done" only when every test passed, or when the owner has agreed to each one that was not run.
