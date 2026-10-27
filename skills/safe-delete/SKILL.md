---
name: safe-delete
description: Puts three habits in front of any script that deletes files. It pushes the work to a remote first, runs a dry run that only counts and lists, and rehearses the delete on a copy before the real folder is touched. Fixes "I let the agent clean up, and it deleted my project." Use before an agent writes or runs anything that deletes, cleans or rebuilds a folder, and before an agent works on a project with no remote. Also on /safe-delete.
---

# Safe delete

You let the agent clean up, and it deleted your project. In one reported case, which nobody has independently verified, a Claude Code agent's own cleanup script walked through 614 Windows directory junctions into the live project. It deleted 48,218 project files and the .git folder in 103 seconds, and there was no remote. This skill puts three habits in front of every delete.

## The principles
1. Count before you delete. A dry run only counts and lists. If the count is far from what you expected, stop.
2. Rehearse the delete on a copy first. The real folder comes only after the dry run and the copy pass and the person says yes.
3. Push before the agent starts. A .git folder on the same machine is deleted with the project. A remote such as GitHub is not.

## Steps
1. Run `git status` and `git remote -v`. If there is no remote, or work is not pushed, ask the person to commit and push to GitHub. Wait until it is done.
2. Write down what should be deleted, in words and as a number: "the 3 files in temp/".
3. Before anything else, give the delete script a dry-run mode that only counts and lists, and deletes nothing. Run it.
4. If the count is far from the number in step 2, or a path is outside the folder you meant, stop and show the person.
5. Copy the folder outside the project with links kept as links (`cp -a`), or remove the links from the copy. Check that no path in the copy resolves outside it. Run the delete on the copy without following links, and check that only the right things are gone.
6. Show the person the count, the result on the copy and the push status. Run on the real folder only after their yes.
7. If something is lost anyway, restore it from the remote with `git clone`. Only pushed work comes back.

## Rules
- If the count does not match, stop. Never change the expected number to make it match.
- No delete runs while the work exists only on this machine.
- The real folder is never the first place a delete runs.

## What the proof shows
- `python3 scripts/dryrun.py out.txt` builds a temp folder with 3 files and one link to a 1,200-file project. The dry run counts 1,203 files, 1,200 of them inside the project, and deletes nothing.
- `scripts/restore-run.txt` shows a 1,200-file folder and its .git deleted, then one `git clone` bringing all 1,200 files back in 0.34 seconds.
- What it does not prove: the story is the developer's own account, retold by the press and the AI Incident Database. Our runs were on a Mac, with a symlink standing in for a Windows junction. Our remote was a second folder on the same Mac, not GitHub.
