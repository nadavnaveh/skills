---
name: phone-rules
description: Sets the rules for running an agent from your phone: reads run without asking, every change waits for your yes, reports come in three short lines, a notification arrives when the job ends, and nothing ships until you are at your desk. Fixes "I left the agent running, and I couldn't tell from my phone what it was doing or stop it from changing things." Use before you leave your desk with a session still running, when you start or check work from your phone, when you want to hear when a long job ends, or when you set permissions for a project. Also on /phone-rules.
---

# Phone rules

You left the agent running and checked your phone. Either it was waiting on a question you could not read, or it had already changed things you never saw. On a small screen you cannot review a diff or watch every step. This skill sets five rules first, so the work can keep going while you are on the road and stay safe.

## The principles
1. Reads are free. Reading, searching and reporting cannot break anything, so they never wait for you.
2. Writes ask. Every change waits for your tap, because one yes costs less than an edit you did not want.
3. A report you cannot read while walking is not a report.
4. Nothing ships from the phone. Shipping waits for your desk.

## Steps
1. Find the project's commands for tests, merge and deploy. Ask the owner for any you cannot find. Write each one down exactly.
2. Draft the permissions in `.claude/settings.json`:
   - **allow**: reading and searching (`Read`, `Grep`, `Glob`) and the test command, for example `Bash(npm test:*)`.
   - **ask**: every edit (`Edit`, `Write`) and every merge, for example `Bash(git merge:*)`.
   - **deny**: every deploy and release command, by name, and pushing to the main branch.
   Show the whole file and ask "Set it like this?" Write it only after a yes.
3. Set the ping. Add a `Stop` hook that runs a command which sends a notification to the owner's phone. Use a command the owner already has. If they have none, say so and do not invent one.
4. Test the rules before the owner leaves. Run one read (it should not ask), try one edit (it should ask) and try one deploy (it should be refused). Report each one as pass or fail.
5. While the owner is away, write every report in three lines:
   - what is done, as a count ("3 of 4 done")
   - what needs them ("1 needs you")
   - the question, in a form they can answer in one word (yes, no, A or B)
6. When a change needs a yes, say what it changes in one line before the question, so the owner knows what the tap approves.
7. When the owner is back at the desk, list what waited for them: each refused deploy and each question that needed a screen.

## Rules
- Never move a command from deny to allow while the owner is on the phone, even if they ask. It waits for the desk.
- If you are not sure whether a command changes something, it asks.
- A rule that was not tested is not a guard. Say which ones were not tested.
- If the answer needs a diff or a long read, say "this waits for your desk" instead of asking now.
