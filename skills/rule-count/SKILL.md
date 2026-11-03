---
name: rule-count
description: Runs one small real task three times with your CLAUDE.md and three times without it, in a throwaway copy of the repo, and counts from the logs which lines changed what the agent did. Fixes "I wrote the rules, and I can't tell which ones it follows." Use when you add or rewrite lines in CLAUDE.md, when a rule seems ignored, when the file has grown long, or before you share a CLAUDE.md with a team. Also on /rule-count.
---

# Rule count

You wrote rules in CLAUDE.md, and you cannot tell which ones the agent follows. Some lines it would follow anyway, some it skips, and in a single session the two look the same. This skill runs the count on your file: the same task with the file and without it, checked line by line.

## The principles
1. Phrase every rule as a result you can see in the answer.
2. Run the same task three times with the file and three times without, and count what changed.
3. Rewrite any rule that changed nothing as a result you can see.

## Steps
1. Read the project's CLAUDE.md and list each line as a check. A visible line (a line in the answer, a file, a test run) is checked from the final answer. A process line (an order of steps, a file read first) is checked from the tool log.
2. Pick one small real task from this project with the user, one that touches what the rules talk about. Ask "Run this task six times?" and start only after a yes.
3. Copy the repo to a temp folder, including CLAUDE.md if it is not committed. Never run in the user's working tree.
4. In the copy, run the task 3 times with CLAUDE.md. Then move it aside and run the task 3 times without it. Use `claude -p "<task>" --output-format stream-json --verbose` for every run, with the same model and settings each time, and save each log to its own file. Both sets of runs still load the user's global CLAUDE.md, so say so in the report.
5. Count each check from the logs: the answer text for visible lines, and the tool calls in order for process lines. Print one table: the line, kept n of 3 with the file, n of 3 without, and the evidence (the answer line, or the tool calls in order).
6. If a line was kept as often without the file as with it, it changed nothing measurable here. Say so in those words.
7. Suggest a visible rewrite for every such line and every line under 3 of 3, with the old line and the new one side by side. Change nothing in CLAUDE.md without the user's yes.

Example, from our run: a discount bug, Haiku, three lines. The line asking the agent to end with a "Not checked:" line was kept 3 of 3 with the file and 0 of 3 without. "Before changing a function, read its test file first." was kept 3 of 3 with the file and 3 of 3 without, so it changed nothing. "Change one file only." was kept 3 of 3 in both. The bug was fixed in all 6 runs.

## Rules
- Count from the logs, never from the agent's own report.
- Three runs is a quick check, not a measurement.
- Quote a rule only in its exact words, and check what those words ask, not a stricter version.
