---
name: checkpoints
description: Commits a clean point before a long job starts, keeps a progress.md file that says what is done, what runs now and what is next, and works on a branch with one commit per step. If the job crashes, it starts again at the step that crashed. If a step breaks things, one git command takes the work back to the last good step. Fixes "it ran for an hour, crashed halfway, and I had to start over." Use before any job with many steps or a long run time (a migration, a big refactor, a change across many files, an overnight run), when a session crashed or was cut off and you want to pick up where it stopped, and when a step has just broken something. Also on /checkpoints.
---

# Checkpoints

The job ran for an hour, crashed at step 6, and the only way back was to start over. Nothing was saved along the way, so nobody knew what was done or which change broke things. This skill saves a clean point before the job, writes progress to a file as it goes and commits every step, so a crash costs one step and not the whole job.

## The principles
1. Commit before the long job. A clean point is the way back.
2. Progress lives in a file, not in the session. A new session can read a file.
3. One step, one commit. A step with its own commit can be undone on its own.

## Steps
1. Before the job, run `git status`. If anything is uncommitted, commit it and note the short commit id (for example a81f). Start only when the tree is clean.
2. Create a branch for the job (`git checkout -b <job-name>`), so main stays as it was.
3. Split the job into numbered steps. Write them to progress.md under three headings: Done, Now and Next. Commit the file.
4. Run one step at a time. After each step, run its check, move it to Done with its commit id, put the next step under Now, and commit the work and progress.md together as "step 3: <what changed>".
5. If the job crashes or the session ends, start a fresh session. Read progress.md and compare it with `git log` and `git status`. If the crashed step left half-done changes, show them and ask before you throw them away. Then resume at the step under Now, not at step 1.
6. If a step breaks things, go back to the last good step with `git reset --hard <commit id of that step>`. Ask first, because it deletes every change made after that commit. Then redo the step in smaller pieces, or stop and ask.
7. When every step is done, report each step with its commit id, any step that was rolled back and why, and the branch that is ready to merge.

## Rules
- Never start a long job when the tree has uncommitted changes.
- A step goes under Done only after its check passes.
- Reset only on the job branch, never on main, and only after a yes.
- If progress.md and `git log` disagree, trust `git log` and fix the file.
