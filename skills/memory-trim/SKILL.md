---
name: memory-trim
description: Measures the agent's memory index (MEMORY.md) against what Claude Code loads, lists the rules past the cut, and rebuilds it as one short line per rule, most important first. Fixes "the agent ignores a rule I wrote, as if it never saw it." Use when the agent breaks a rule that is in its memory, when Claude Code warns at session start that MEMORY.md was only partly loaded, or when the index nears 200 lines. Also on /memory-trim.
---

# Memory trim

The agent ignored a rule you wrote. Maybe it never saw it. Claude Code loads only the start of the memory index, so the newest rules at the end are the first to go. This skill counts what loads, shows what was cut, and rebuilds the index so every rule fits.

## The principles
1. A rule that was not loaded cannot be followed. Check that it loaded before asking why it was broken.
2. One short line per rule in the index. The detail lives in topic files that open only when needed.
3. The cut always comes from the end. Put what matters most at the top.

## Steps
1. Find the index: run /memory and open the auto memory folder. If the session opened with a warning that MEMORY.md was only partly loaded, copy it word for word.
2. Count it: `wc -l -c MEMORY.md`. Claude Code loads the first 200 lines or about 25 KB, whichever comes first. To find where the bytes run out, run `head -N MEMORY.md | wc -c` for a few values of N.
3. List every line past the cut by title. These are the rules the agent never saw.
4. Rewrite each entry as one line: the title, the link to its topic file and a hook of a few words, well under 200 characters. Move any longer detail into the topic file.
5. Order the lines by what a miss would cost, every-session rules first. A new entry goes where its weight puts it, not at the bottom.
6. Show the before and after counts and the new order, and ask "Write it like this?" Copy or commit the old file first. Write only after a yes.
7. Count again and leave room under the limit. In a fresh session, check that the warning is gone. If it is not, report the line where it still cuts.

## Rules
- Shorter wording alone is usually not enough. In the real case, cutting every hook to 60 characters still left the index past the cut. The detail has to move out.
- Never delete a rule to make room. Move its detail and keep its line.
- Report every count with the command behind it, and call a limit inferred when it was.
- The worked example is scripts/memory-cut-2026-10-28.md, summed up in scripts/PROOF.md: 205 lines, 24 cut from line 182, among them "Run autonomously" and "Quota stop is 98%". It shows which rules did not load, not what the agent did differently because of it, the exact byte limit (about 25.5 KB, inferred) or that other tools cut the same way.
