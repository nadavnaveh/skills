---
name: write-skills
description: Writes your team's know-how down as skills, one SKILL.md per job (how we test, how we deploy, our code style, how to review, writing a ticket), so every agent follows the same steps without being told again. Fixes "I explain the same thing to every agent, and each one does it its own way." Use when you explain a process to an agent for the second time, when two sessions did the same job two different ways, when a new person or agent joins a project, or when you set up a new repo. Also on /write-skills.
---

# Write skills

You explain the same thing to every agent, and each one does it its own way. The know-how lives in your head or in an old chat, and a new session never saw either one. This skill writes each job down once as a skill, so every agent reads the same steps.

## The principles
1. Write it once. Every agent knows it.
2. One skill, one job. A skill that tries to cover everything gets skimmed.
3. Write down what you really do, taken from real runs, not what you wish you did.
4. A skill is not finished until a fresh session uses it and gets the job right.

## Steps
1. Pick the jobs you keep explaining. Start from these five and keep only the ones you have:
   - **How we test**: which tests to run, and when.
   - **How we deploy**: the steps to ship, in order.
   - **Our code style**: names, patterns, and limits.
   - **How to review**: what a good review looks for.
   - **Writing a ticket**: the same clear parts in every ticket.
2. For each job, gather what is real: the commands in the project files and past runs, the last few tickets and reviews, and the corrections you keep making. Ask the owner only what you cannot find. Never invent a command.
3. Write one folder per job at `.claude/skills/<name>/SKILL.md` inside the project, so it travels with the code. At the top, give it a `name` and a `description` that says what it does and when to use it, in the words someone would actually type. Then short numbered steps, then the rules.
4. Keep each one short and exact: real commands, real names, real numbers ("functions under 50 lines", "unit tests after every edit, all tests before a merge"). Cut anything an agent would do anyway.
5. Show the owner each skill and ask "Is this how we really do it?" Save it only after a yes.
6. Test each skill in a fresh session (run /clear first). Give it a real task and see whether the agent picks up the skill, or type /<name>. If it skipped a step or guessed, fix the skill, not the output.
7. Commit the skills to git. When the way you work changes, change the skill in the same commit.

## Rules
- One job per skill. If the description needs "and also", split it into two.
- Every step is something an agent can do or check, never "be careful".
- Never put keys, passwords or tokens in a skill.
- A skill that disagrees with how the team works now is fixed or deleted, never left to go stale.
