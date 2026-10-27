---
name: save-points
description: Commits a save point before the agent starts work and before you close the laptop, accepts the agent's pending edits in Cursor, and runs git status when you open the project, so emptied files come back with git restore. Fixes "I opened my project, and my files were empty." Use before you hand an agent a task, before you close the laptop, when you open a project after a break, and when files you did not touch look changed or empty. Also on /save-points.
---

# Save points

You opened the project, and your files were empty. A tool changed them while you were away, and nothing uncommitted had a copy to come back from. This skill commits at the right moments, so a wipe costs one command, not your work.

## The principles
1. Only what is committed can come back.
2. Save before you hand off work and before you leave.
3. When you come back, check before anything else runs.
4. Restoring the files does not remove the cause.

## Steps
1. Before you hand the agent a task, run `git status` and commit any changes as "save point before <task>". Ask first unless the person said commits are fine.
2. Before the laptop closes, commit again, even half-done work.
3. In Cursor, do not leave the agent's edits waiting for review. Click Keep All, not Undo All. Cursor staff said edits never accepted or rejected are kept as pending records and applied again at launch, and that emptied the files.
4. When the project opens, run `git status` first. Look for files nobody touched that changed, and run `git diff --stat` to spot emptied ones.
5. If committed files changed or emptied, show the person the list and ask. Then run `git restore .` (or `git restore <file>`), run `git status` again and report how many files came back.
6. Say plainly what could not come back: anything never committed. If the wipe repeats, the pending records are still there. Click Keep All, then restore again.
7. To show why, run `python3 scripts/zero_run.py out.txt`. In a temp folder it commits 210 files, adds one uncommitted edit, empties every file and restores. In our run all 210 came back in 0.73 seconds, and the uncommitted line was gone.

## Rules
- `git restore .` throws away uncommitted changes in those files. Commit or ask first.
- The wipe numbers are one developer's report on the Cursor forum (3 October 2026): 25 wipes in 17 days, about 210 files each, 412 at most, nothing committed lost. It is not a measured rate.
- The script empties the files itself, so it does not reproduce the Cursor bug. The proof does not show how many people hit the bug or whether later versions still do, and git alone does not stop the wipe from coming back.
- Never call the project safe while `git status` shows changes nobody made.
