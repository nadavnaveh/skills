---
name: team-roles
description: Splits a job into five roles (the planner, the builder, the tester, the reviewer and you), gives each role one job, and keeps the merge for your yes. Fixes "one agent planned it, built it, tested it and approved it, and nobody caught the mistake." Use when a change is bigger than one quick edit, when you are about to let one agent take a job from goal to merge, when you want tests and a second look before anything lands, or when you start more than one agent on the same change. Also on /team-roles.
---

# Team roles

One agent planned the work, wrote the code, tested it and approved it. Nobody else looked, so its mistakes went straight in. An agent that plays every role checks its work against what it meant to build, not against what it actually built. This skill gives each role one job, puts a fresh agent on the review, and leaves the last word to you.

## The principles
1. One role, one job. The planner does not build, the tester does not fix, and the builder does not approve.
2. The agent that wrote the code never judges it.
3. Agents check the work. You say yes. No agent merges.

## Steps
1. **The planner.** Write the goal in one sentence. In plan mode (Shift+Tab), with no edits, break it into numbered steps. Each step is small enough to build and test on its own, and names the files it touches and how it will be checked. Show the steps and ask "Build it in these steps?" Start only after a yes.
2. **The builder.** Give one step at a time to a builder subagent, working on a branch and never on main. Its brief is the step number, the files it may touch and what must not change. It writes the code for that step and nothing else.
3. **The tester.** Run the tests after each step. Report how many passed and how many failed, with the output of each failure. A failure goes back to the builder with the exact error. The tester flags the failure. It does not fix it.
4. **The reviewer.** Start a fresh subagent that did not see the building. Give it only the step, the builder's diff and the test results. It writes each note with the file and line, then approves or sends the step back. The builder fixes the notes and the tester runs again.
5. Repeat steps 2 to 4 for every step in the plan. If a step has not passed after three rounds, stop and bring it to the person.
6. **You.** When every test passes and the reviewer has approved, show the person the diff summary, the test results and each reviewer note with how it was handled. Ask "Merge?" Merge only after a yes.

## Rules
- No agent checks its own work.
- A step that was not tested or not reviewed is not done. Say which one is missing.
- Only the person's yes merges into main.
- If a step keeps failing, go back to the plan instead of trying a fourth fix.
