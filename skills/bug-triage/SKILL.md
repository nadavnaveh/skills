---
name: bug-triage
description: Checks a list of bug findings and keeps only the real ones. It reproduces each one, has a second agent try to disprove it, merges findings with one cause, writes what a user sees when it breaks, and starts each fix with a failing test. Fixes "the agent found ten bugs, and most of them were not real." Use when a review, an audit or an agent hands you a list of findings, before you fix any of them, or when several reports look alike. Also on /bug-triage.
---

# Bug triage

The agent found ten bugs. Some were guesses, and three were the same bug. A finding reads like a fact, so it gets fixed like one. This skill checks every finding first and keeps only the bugs that survive.

## The principles
1. No repro, no bug. A finding you cannot make happen is a guess.
2. A second agent argues it is not a bug. What survives is real.
3. One cause is one bug, however many reports point at it.
4. Harm sets the order: what a user sees, not what the code does.
5. Every real bug gets a test that fails before the fix and passes after.

## Steps
1. Number every finding, with the file it points at and the claim in one line.
2. Write the smallest repro for each: a script, a command or steps to click through. Run it. Mark it **reproduced**, with the output, or **not reproduced**, with what happened instead. Drop the second kind, or send it back to ask for steps.
3. For each reproduced finding, start a subagent as the skeptic. Give it the finding, the repro and the output, and one job: argue it is not a bug (expected behavior, bad input, a path no user reaches). If it proves the case, mark it **not a bug** and drop it.
4. Fold findings with one cause (the same null user, the same missing check) into the first one, and keep the count: "bug 1 (x3)".
5. For each bug left, write three steps or fewer to make it happen, what the user sees (an error page, a wrong total) and a severity from that harm: blocks users, gives wrong results, or annoys.
6. Show the table: each finding as real, not a bug, merged or not reproduced, with the reason. Ask "Fix these, in this order?" and start only after a yes.
7. For each bug, in severity order, write a test named for it (test_bug_2). Run it and show it fail. Fix the bug, show the same test pass, then run the full test suite.

## Rules
- Never fix a finding that was not reproduced.
- The skeptic gets the evidence, not your opinion.
- A test that passes before the fix does not test the bug.
- No finding ends as "looks fine". It is real, not a bug, merged or not reproduced.
