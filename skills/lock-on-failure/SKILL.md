---
name: lock-on-failure
description: Lists every hook in your Claude Code settings, sorts the guards from the hooks that only report, adds onFailure "block" to each guard after your yes, then makes each guard fail once on purpose in a throwaway project and checks that the action stopped. Fixes "my guard crashed, and the command ran anyway with no error." Use when you rely on hooks to stop dangerous actions, after you add or change a hook, when you ask what happens if a guard crashes, or before you leave an agent running alone. Also on /lock-on-failure.
---

# Lock on failure

The guard crashed. Did the door stay open? A hook that fails lets the action through unless you set it to block, and the agent may see no error. This skill makes every guard lock when it fails, then makes it fail once to check.

Our test: two projects, a hook that crashes on purpose with exit 1. Without the setting, the command ran and the agent saw no error. With it, the command was blocked and the file was not created.

## The principles
1. A guard that cannot run blocks the action.
2. A hook that only reports stays open, so it does not stop work it is not guarding.
3. If you never saw it fail, you do not know what it does then.

## Steps
1. Run `claude --version`. You need 2.1.295 or newer. If it is older, stop and tell the owner to update.
2. Read `.claude/settings.json`, `.claude/settings.local.json` and `~/.claude/settings.json`. List every hook: its file, event, matcher, type, what it runs and whether it already sets `onFailure`. Say which files do not exist.
3. Sort each hook as **guards a dangerous action** (it exists to stop something, like a delete, a force push or a send) or **only reports** (it logs, notifies or formats). Read the script, not only its name. If unsure, ask the owner.
4. For every guard, show the exact change and ask "Add this?" Write it only after a yes. Leave every hook that only reports as it is.
   ```json
   { "type": "command", "command": "your-guard.sh", "onFailure": "block" }
   ```
   Only command and HTTP hooks take this setting. List any other guard as not covered.
5. Make each guard fail once. In a new throwaway project, copy its entry into `.claude/settings.json` and change the command to `exit 1`. Keep the matcher and `onFailure`. Then use `claude -p` with `--allowedTools Bash` to ask a fresh session to run a harmless command the matcher covers, such as `echo hello > out.txt`.
6. Check that the action stopped: the file is missing and the session saw a block message. A missing file alone may only mean the command was never allowed.
7. Report each guard as **Locked**, **Still open** or **Not run**, with what you saw. An HTTP guard cannot `exit 1`, so report it as not run unless you made it fail and watched.

## Rules
- Never change a settings file before the owner's yes.
- State only what was tested: exit 1. For the rest, quote the changelog: a hook that "can't start, times out, or exits with an unexpected code" blocks the action.
- Never claim a crash can never let a command through.
- A guard that catches its own errors and exits 0 looks like a success, so this setting will not fire. Flag it to the owner.
