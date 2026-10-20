---
name: tests-as-spec
description: Ports code to a new language, framework or version by using the old test suite as the spec. It freezes the suite green, ports one module at a time, runs the same tests against the new code, compares old and new answers on the same input, and stops the agent if it edits a test. Fixes "the agent ported the code, said it works, and it behaves differently." Use before any rewrite, migration or port (a new language, a new framework, a major version upgrade, moving off old code), when the agent offers to rewrite everything at once, and whenever a test fails during a port. Also on /tests-as-spec.
---

# Tests as spec

The agent ported the code, said it works, and it behaves differently. It checked that the new code looked right, not that it does what the old code did. This skill makes the old tests the spec. The port is done when the new code passes the same tests and gives the same answers, and the tests never change to fit it.

## The principles
1. The old tests are the spec. If they are not green before the port, there is no spec yet.
2. Port one module at a time, so a failure points at one place.
3. A port passes on proof (the same tests, the same answers), not on the agent's word.
4. The tests do not move to meet the code. The code moves to meet the tests.

## Steps
1. Freeze the tests. Run the old suite on the old code and write down the result, for example "312 of 312 pass". If any test fails, stop and settle it with the owner before the port starts. Commit the tests so any later change shows up in git.
2. List the modules (for example parser, router, db) and the order to port them. Show the list and ask "Port in this order?" Start only after a yes.
3. Port one module. Leave the others as they are.
4. Run the same tests against the new code. Report the count next to the old one: "old 312, new 301, 11 fail". Name each failing test. Fix the code until the counts match.
5. Compare. Send the same inputs to the old and the new code (requests, files, sample data) and put the answers side by side: status, output, errors. Any difference is a fail, even when the tests pass.
6. Lock the tests. Before each commit, run git diff on the tests folder. If the agent changed a test, stop, undo the change with git, and fix the code instead. You can also add a deny rule for edits to the tests folder in .claude/settings.json.
7. Mark the module done only when every test passes and every compared answer matches. Then go to the next module.

## Rules
- Never edit, skip or delete a test to make the port pass. If a test looks wrong, stop and ask the owner.
- Report counts as "new X of old Y", never "most tests pass".
- A module with a failing test is not done, and the next module waits.
- If the old code cannot be run to compare, say so and name what was not compared.
