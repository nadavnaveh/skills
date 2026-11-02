---
name: count-check
description: Makes your agent end every count with its rule, three random rows and how many rows the rule could not read, and stop if more than 10% went unread. Fixes "the count was wrong, and it looked right." Use whenever the agent gives a count or total from a sheet, a CRM, a log or a folder, and before you act on one. Works pasted once into any agent or rules file. Also on /count-check.
---

# Count check

Our agent said 114 of 145 video ideas had no video yet. 74 of those were already in work, and at least 18 were finished that day. A count reads the same whether the rule worked or not. These are instructions you paste into your agent, so it adds these three questions to every count.

## The instructions

Here are the instructions. Paste them into your agent once (or into your rules file, CLAUDE.md / AGENTS.md):

```
Every time you give me a count or a total from a sheet, a CRM, a log or a folder, end your answer with three lines:
1. RULE: the exact rule you counted with, in one sentence (which column, which words or values).
2. SAMPLE: three rows picked at random, each with the cell you read and whether it matched the rule.
3. UNREAD: how many rows the rule could not read or match at all. If UNREAD is more than 10% of the rows, say "the rule may be wrong" and stop before giving a conclusion.
```

## The principles
1. The number alone cannot show the rule behind it.
2. A row the rule could not read is not a no.
3. The unread rows show a wrong rule at once. Ours could not find a piece for exactly the 114 it called new.

## Steps
1. On /count-check, apply the instructions to the last count here, or the next one. To keep them, ask "Add this to your rules file?" and add them word for word after a yes.
2. Sort every row: matched, not matched or unread. Unread means the rule found nothing to judge, or you never reached the row.
3. Write RULE, naming the column and the exact words or values.
4. Write SAMPLE. Pick three rows at random, never the first three, and copy each cell word for word.
5. Write UNREAD as a number out of all the rows. If it is more than 10%, write "the rule may be wrong" and stop. Give no conclusion or plan. Wait for the owner.
6. If the rule changes, count again and write all three lines.

## Rules
- A count without the three lines is not finished.
- Never let unread rows fall into a group like "new" or "other".
- The three lines do not prove a count right.
- Ours looked for "card X" while the sheet's Notes said "episode X". We caught it before anything was drafted.
