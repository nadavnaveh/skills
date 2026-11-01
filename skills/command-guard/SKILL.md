---
name: command-guard
description: Adds a hook that blocks dangerous shell commands (rm -rf, force push, git reset --hard, DROP TABLE) before they run in Claude Code, sends the reason back to the agent, and tests it on four commands. Fixes "I told the agent to be careful, and that was the only thing stopping it." Use before you give an agent full access or leave it to run alone, or when a rule like "never force push" lives only in a prompt. Also on /command-guard.
---

# Command guard

You told the agent to be careful, and that line was the only thing stopping it. The agent weighs a prompt on every turn, so the prompt is a request it can get wrong. This skill puts a hook in front of every shell command, and the hook stops the commands on its list before they run.

## The principles
1. A prompt is a request, not a boundary. A hook runs every time, whatever the prompt said.
2. The guard stops only what is on its list. Everything else still runs.
3. A blocked command goes back to the agent with the reason, and the next step is to ask the owner.
4. A guard you have not tested is not a guard yet. A guard script that crashes blocks nothing.

## Steps
1. Ask where the guard applies: this project (`.claude/settings.json`) or every project (`~/.claude/settings.json`). Copy scripts/guard.py unchanged to a fixed place, such as `~/.claude/hooks/guard.py`.
2. Show what it blocks: `rm` with `-r` or `-f`, `git push` with `--force`, `DROP TABLE` or `DROP DATABASE`, and `git reset --hard`. It matches text anywhere in the command, so `rm -f` and even a search for "drop table" are blocked too. Ask "Is there anything else you never want run without you?" Add each answer as a new, narrow line in the BAD list, and keep the four shipped lines.
3. In scripts/settings.hook.json, change the path in "command" to your guard.py. Merge its PreToolUse entry into the settings file and keep any hooks already there. Write it only after a yes.
4. Test the script with four commands, sent the way the hook receives them: `echo '{"tool_input":{"command":"rm -rf build"}}' | python3 ~/.claude/hooks/guard.py; echo $?`. `rm -rf build` and `git push origin main --force` must print BLOCKED and exit 2. `ls -la` and `git status` must exit 0. Any other result, or an error, means the guard blocks nothing.
5. If the owner can start a new session, do a live check: confirm the hook is listed in `/hooks`, then ask the agent to run `rm -rf` on a throwaway folder. It should be blocked, and the folder should still be there. The owner may skip this. If skipped, say so.
6. Report each test as blocked or passed, with the output.

## Rules
- Never edit the guard or the settings to get a blocked command through. The owner runs it.
- Never say "it is safe now". Name what is blocked, and say that `git push -f`, `rm --recursive`, `find -delete` and scripts that delete are not caught.
- If any test gives an unexpected result, the guard is not working. Say so.
- Run the four tests again after every change to the list.
