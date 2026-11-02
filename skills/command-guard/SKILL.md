---
name: command-guard
description: Adds a hook that blocks the dangerous shell commands on its list (rm -rf, force push, git reset --hard, DROP TABLE) before they run in Claude Code, sends the reason back to the agent, and tests it on four commands. Fixes "I told the agent to be careful, and that was the only thing stopping it." Use before you give an agent full access or leave it to run alone, or when a rule like "never force push" lives only in a prompt. Also on /command-guard.
---

# Command guard

You told the agent to be careful, and that line was the only thing stopping it. A prompt can be misread or dropped, so it is only a request. This skill puts a hook in front of every shell command, and the hook stops the commands on its list before they run. The idea comes from @kloss_xyz on X.

## The principles
1. A prompt is a request, not a boundary. A prompt line asks, a hook blocks.
2. The guard stops only what is on its list. Everything else still runs.
3. A blocked command goes back to the agent with the reason, and the next step is to ask the owner.
4. A guard you have not tested is not a guard yet. If it breaks or cannot read a command, it blocks, by design.

## Steps
1. Ask where the guard applies: this project (`.claude/settings.json`) or every project (`~/.claude/settings.json`). Copy scripts/guard.py to `~/.claude/hooks/guard.py`, where the shipped settings expect it. If you keep it inside one project instead, put its absolute path in "command".
2. Show what it blocks: `rm` with `-r` or `-f`, `git push` with `--force` or `-f`, `git reset --hard`, `DROP TABLE` and `DROP DATABASE`. It matches text anywhere, so a search for "drop table" is blocked too.
3. Ask "What else can you not undo?" (a deploy, a database reset). Add each answer as a narrow new pattern in the BAD list, and keep the four shipped ones.
4. Merge the PreToolUse entry from scripts/settings.hook.json into the settings file, and keep any hooks already there. Write it only after a yes. Its `onFailure` setting needs Claude Code 2.1.295 or newer, so check `claude --version`.
5. Test four commands the way the hook receives them. Save each one as a small file, because a live hook blocks a shell line that contains these words. A file looks like `{"tool_input":{"command":"rm -rf build"}}`. Run `python3 ~/.claude/hooks/guard.py < test.json; echo $?`.
   - `rm -rf build` and `git push origin main --force` must print BLOCKED and exit 2.
   - `ls -la` and `git status` must exit 0.
6. Optional extra evidence, on a throwaway folder only: the hook loads in a new session or after a review in `/hooks`. Then ask the agent to run `rm -rf` on that folder. It should be blocked, and the folder should still be there. If skipped, say not run.
7. Report each test as blocked or passed, with the output.

## Rules
- Never edit the guard or the settings to get a blocked command through. The owner runs it.
- Never say "it is safe now". Name what is blocked, and say what is not caught: `rm --recursive`, `rm -i -r`, `rm dir -rf`, `find -delete`, `git clean`, `truncate` and scripts that delete.
- If any test gives an unexpected result, the guard is not working. Say so.
- Run the four tests again after every change to the list.
