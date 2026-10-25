---
name: user-path-test
description: Writes one yes/no test with you, before the agent starts, that walks a real user's whole path against the running app, and holds "done" until it passes. Fixes "the agent's tests were green, and a user still could not get in." Use before an agent fixes a bug or changes something users go through (sign-up, log-in, checkout, a form, an API call), when a bug report names only one kind of user, and whenever the agent is about to say done because the tests it wrote itself are green. Also on /user-path-test.
---

# User-path test

The agent's tests were green, and a user still could not get in. The agent wrote the code and the tests, so the tests check what it fixed, not the user it never thought about. This skill writes one test with you before the work starts. The test walks a real user's whole path, and "done" waits until it passes.

## The principles
1. The agent's tests guard what it fixed. Your test guards the user nobody reported.
2. Test the whole path against the real running app, the way a user goes through it.
3. A test that cannot fail proves nothing.
4. Done means the promise to the user passes, yes or no.

## Steps
1. Before the agent writes anything, write the promise to the user in one line, for example "a user who signed up can log in".
2. List the users the bug report did not mention. Ask who already uses this today, and who has old data, a different spelling or a saved setting. Pick the one most likely to be left out, for example an existing user.
3. Turn that user into one yes/no test across the whole path: "an existing user types the email exactly as it was saved, and gets in, yes or no". Run it against the real running app or server, not against one function inside it. It must give the same answer every time it runs.
4. Show the promise, the user and the test, and ask "Is this the user and the promise?" Start the work only after a yes.
5. Let the agent work. It keeps its own tests. It does not say done until your test passes, and it never edits your test to make it pass.
6. When everything is green, undo one line of the fix on purpose and run all the tests again. If your test stays green, it does not cover the path, so fix the test. Then put the line back.
7. Report each test as pass or fail, with the output.

## Rules
- Do not build this test for an internal function that no user goes through. Its own tests are enough.
- Never change the user-path test quietly. If it is wrong, say so and agree a new one.
- Green tests the agent wrote are its claim, not your pass.
- What this rests on: one small run of ours, a sign-up and log-in API with a planted bug. The agent fixed it six times out of six. When we then undid one line on purpose, its own tests stayed green three times out of three, and the user-path test failed three times out of three. That holds for those runs only. It does not show that agents ship broken code, how often this happens, that unit tests are useless, or anything about tests that click through a browser.
