---
name: stale-memory
description: Goes through the agent's rules file, memory notes and index and flags what is no longer true, as one list of MISSING, CONFLICT and UNDATED lines. Changes nothing until you decide. Fixes "my agent's memory points to files that are gone and rules I already replaced." Use when the agent names a file that is not there, follows a rule you replaced, warns that memory was only partly loaded, or when memory has grown for months without a review. Works pasted into any agent. Also on /stale-memory.
---

# Stale memory

These are instructions you paste into your agent, so it flags what in its memory is no longer true. Memory is a copy of your project, and nothing syncs it when the project moves. Use it in Claude Code, Codex, Cursor or any agent that can read your files, or on /stale-memory. The check changes nothing. You decide what goes.

## The principles
1. Memory is a copy of the world. A copy goes stale unless someone syncs it.
2. A memory line is a claim from the day it was written. Check it before you trust it.
3. Nothing marks which of two opposite rules won. The owner decides.
4. A line that never loads cannot help, however true it is.

## Steps
1. Open the rules file (CLAUDE.md or AGENTS.md), every memory or notes file and any index. Read only.
2. Mark MISSING. For each line that names a file, folder or command, test whether it still exists. Look a command up, never run it. Count how many are named and how many are missing. List what you could not test as not checked.
3. Mark CONFLICT. Find two lines, rules or decisions, that cannot both be followed. Mark both and show them side by side with their dates, from the line or the file's last change. A later file change is only a hint, not proof, of which rule is newer.
4. Mark UNDATED: any line with no date of its own.
5. Check the cut. If the session opened with a warning that memory was only partly loaded, copy it word for word and list the lines past the cut. If you saw the session start with no warning, write "no cut reported". If you cannot see it (for example the session is over), write "cut not checked".
6. Report one list: MISSING, CONFLICT, UNDATED, with the cut result on top. Each row has the line, where it lives, the evidence and one proposed fix. Then stop. Nothing has changed.
7. The owner decides what goes. For the rows they pick, copy the old memory files to a backup folder (or commit them if the project is in git), ask "Apply these?" and write only after a yes.

## Rules
- Never guess a new path. Show the search that found it, or call the file gone.
- Never pick the winner between two rules yourself, even when one is newer.
- MISSING proves the line is stale, not that the agent acted on it.
- Clean means clean for what you checked. Name what you did not check.
- Our real run found 8 of 44 named files gone, a June rule next to the October rule that replaced it, and 33 index lines cut. That was one memory on one day, not a rate for yours.
