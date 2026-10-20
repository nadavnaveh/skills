---
name: dogfood-first
description: Runs a new skill, prompt or agent setup on your own real tasks for this week before anyone else gets it. It logs one line for each thing it got wrong, fixes only the miss that keeps coming back, runs the same tasks again to count the misses, and shares the tested version only after it has held up. Fixes "I shared my skill, and it broke the first time someone else used it." Use when you have just written a skill, a prompt, a CLAUDE.md rule or an agent workflow, before you publish it or hand it to your team, and when you are about to share something you have only tried on a demo. Also on /dogfood-first.
---

# Dogfood first

You shared your skill, and it broke the first time someone else used it. It had only ever run on a demo, and the demo was picked because it worked. This skill runs it on your own real work first, counts what it gets wrong, fixes the worst miss, and shares only the tested version.

## The principles
1. Real work, not a demo. A demo shows what you hoped for. This week's tasks show what really happens.
2. A miss that nobody wrote down is forgotten by next week.
3. Fix the miss that keeps coming back, not the one you saw last.
4. Only the same tasks, run again and counted, can show that a fix worked.

## Steps
1. Pick this week's real tasks: three to ten things you actually need done. No made-up examples. Save the list in a file, such as dogfood/tasks.md, so next week can use the same list.
2. Run it on each task. Each time it gets something wrong, add one line to dogfood/misses.md: the date, the task, and the miss in two or three words ("wrong date", "tone too formal"). Write one line for every miss, even if the same miss happened before.
3. At the end of the week, count the misses by kind and show the count, the biggest first: "date x6, tone x2".
4. Fix only the top miss. Find the line in the skill, prompt or CLAUDE.md that caused it, show the change, and ask "Fix it like this?" Make the change only after a yes. Leave the other misses for a later round.
5. Next week, run the same tasks again. Start each one in a fresh session (/clear), so nothing left over from last week's chat helps it along. Log the misses the same way.
6. Compare the weeks side by side: "week 1: 6 misses, week 2: 1". If the top miss is still there, the fix did not work. Say so, and try again before you fix anything else. Repeat steps 3 to 6 each week.
7. Share it only after three tested weeks, with at most one miss left. Commit it with git, and write next to it the miss count from the last run and any miss that is still open.

## Rules
- Never share a version that has not run on real tasks.
- One fix per round, so you know which change helped.
- Never change the task list between weeks to make the count look better.
- A run you did not do is not a pass. Say it was not run.
