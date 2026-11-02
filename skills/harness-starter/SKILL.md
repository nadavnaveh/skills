---
name: harness-starter
description: Installs the ready kit for your own harness in a Claude Code project, a hook before every command you can't undo, a queue for heavy jobs, and tests for that code itself. Fixes "I want my own harness, and all I have is rules in a prompt." Use when you want a harness and don't know where to start, when an agent ran something you could not undo, when heavy jobs run your machine out of memory, or when you have guards nobody ever tested. Also on /harness-starter.
---

# Harness starter

You want your own harness, and all you have is rules in a prompt. A rule is a request, and the agent can skip it. This skill installs the ready kit: a hook before every command you can't undo, a queue for heavy jobs, and tests for that code itself.

## The principles
1. A check that runs outside the agent is harder to skip. A line in the prompt is only asked.
2. A guard that breaks quietly is worse than no guard, so a broken guard blocks.
3. Harness code is code, so it gets its own tests.

## Steps
1. Show what will be installed and where: `guard.py` and `qrun.py` into `.claude/harness/`, plus one hook in `.claude/settings.json`. If a file is already there, ask before replacing it.
2. Copy `scripts/guard.py` and `scripts/qrun.py` into `.claude/harness/` as they are.
3. Show the exact block from `scripts/settings.hook.json` and ask "Add this hook to .claude/settings.json?" Only after a yes, add it. If the file is missing, create it with just this block. If a `PreToolUse` list exists, append to it. Keep every other hook and setting. Without a yes, leave the file alone and say the hook is off.
4. From the `scripts` folder, run `python3 -m unittest test_harness.py` and show the result. Pass is 7 tests, OK. They test the skill's copies, identical to the installed files. If any fail, stop, take the hook back out and say it is off.
5. Prove the hook once on a harmless example. Nothing runs, the guard only reads the text:
   `printf '{"tool_input":{"command":"rm -%s build"}}' rf | python3 .claude/harness/guard.py; echo "exit $?"`
   Pass is "BLOCKED by guard" and exit 2. The `%s` keeps the live hook from blocking this line. Never test with a real destructive command.
6. Run one harmless job and show the output: `python3 .claude/harness/qrun.py -- echo ok`. Real use is `python3 .claude/harness/qrun.py -- <heavy command>`. `QRUN_HEAVY_MAX` sets the slots (default 2), `QRUN_MIN_FREE` the percent of free memory needed to start (default 30).
7. Report each piece as installed, passed or not done. If the hook does not fire, start a new session.

## Rules
- The hook's patterns are a short list and can be got around. It does not catch `rm --recursive`, `rm -i -r`, `rm dir -rf`, `find -delete`, `git clean`, `git branch -D`, `git checkout -- .`, `git stash drop`, `truncate`, `dd`, `mv` and scripts that delete. Add your own. It watches the Bash tool only.
- `settings.hook.json` sets `onFailure` to `block` (Claude Code 2.1.295 or newer), so a hook that crashes blocks. `guard.py` also blocks on input it can't read.
- The queue reads free memory on macOS and Linux and refuses if it can't. It only holds jobs sent through it.
- This kit does not replace permissions or backups.
- Our numbers: four commands, two blocked; a job waited over half an hour; the kit's own 7 tests.
