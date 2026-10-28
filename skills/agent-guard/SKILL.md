---
name: agent-guard
description: Sets three guards before an agent works near your files. Delete commands wait for your approval, the agent works only inside the project folder, and what matters is saved in git and in a separate backup. Fixes "I asked the agent to tidy a folder, and years of my files were gone." Use before an agent cleans up, moves or deletes files, when you open an agent near personal files, and when auto-run is on. Also on /agent-guard.
---

# Agent guard

You asked the agent to tidy a folder, and years of files were gone. A terminal delete skips the Recycle Bin and the checkpoints. This skill sets three guards, so the agent runs alone and a delete waits for you.

## The principles
1. Guard the delete commands, not one spelling. A deny rule on `rm -rf` stopped 1 of 4 spellings; ask rules on the commands stopped 4 of 4 (scripts/deny-test-2026-10-27.txt, scripts/ask-test-2026-10-27.txt).
2. Never open the agent in a folder with personal files. It works in the project folder, and the computer enforces that.
3. Checkpoints do not undo a file only a shell command changed (scripts/docs-quotes.md). Git and a separate backup do.

## Steps
1. **Deletes wait for approval.** Show the owner these lines for `.claude/settings.json` in the project, and add them after a yes, keeping what is there:
   ```json
   {"permissions": {"ask": ["Bash(rm:*)", "Bash(rmdir:*)", "Bash(find:*)"]}}
   ```
   Every `find` will ask too. In Cursor, its staff advise switching auto-run to Ask every time.
2. **Test it.** Make a throwaway folder in the project. The owner opens a new session, asks the agent to run `rm -r -f` on it, and expects a prompt. Say no. It passes if the folder is still there. No prompt = report "not tested".
3. **Only the project folder.** Run `pwd`. If it is a home folder, a desktop or a whole drive, stop and ask the owner to open the agent in the project. Then offer `"sandbox": {"enabled": true, "allowUnsandboxedCommands": false}` in the same file. Shell commands then write only in the project and the temp folder. A delete outside failed with it on and ran with it off (scripts/sandbox-test-2026-10-28.txt). Native Windows has no sandbox: use WSL2.
4. **What matters is saved.** Ask where the backup is and how old it may be, and write both in CLAUDE.md. Before every risky run (a cleanup, a delete, a move), check `git status` shows nothing uncommitted, and `ls -l` the backup path for its date. If either fails, or the agent cannot read the backup, stop and ask.
5. Report each guard as set, not set or not tested.

## Rules
- Never say yes to your own delete, and never turn a guard off yourself.
- The ask rules match the command text, so `/bin/rm`, `git clean`, `mv` or a script can get past them. The sandbox fences shell commands; Edit and Write follow permission rules.
- Our tests ran each spelling once, on one small model, in print mode (`claude -p`). The live prompt, Cursor and Windows were not tested.
