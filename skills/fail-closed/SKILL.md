---
name: fail-closed
description: Makes every guard block the action when it breaks, instead of letting it through. Fixes "the safety check broke, and the agent went ahead anyway." Use when you write or change a hook, report a test result, wait for a yes before a deploy or push, set which commands may run, or find a key or setting missing. Also on /fail-closed.
---

# Fail closed

The safety check broke, and the agent went ahead anyway. A broken guard makes no noise, and no noise looks like a yes. This skill makes every guard lock the door when it fails, so a failure stops the work instead of waving it through.

## The principles
1. When the guard crashes, the door locks. A broken check blocks. It never passes.
2. No run, no pass. A check that did not run has not passed.
3. Silence is no. No answer in time means nothing ships.
4. Unknown means deny. Only what is on the list is allowed.
5. Do not guess what is missing. Stop and ask.

## Steps
1. Hooks. A PreToolUse hook in .claude/settings.json blocks an action only when it exits with code 2. Any other error lets the action go ahead. So run each guard script through a small wrapper with its own time limit: the wrapper runs the script and exits 2 if the script is missing, fails to run, fails or times out. Then break the script on purpose, try the action it guards (for example a push), and show that the action was blocked.
2. Tests. Before you report a result, read how many tests ran. If the runner reports zero tests, or no count can be found, report "not passed: 0 tests ran", never "passed".
3. Questions. Before a deploy, push, send or delete, ask the owner and wait. If no answer comes in time, nothing ships. Report the step as waiting for a yes.
4. Commands. Keep the allowed commands in permissions.allow in .claude/settings.json. When nobody is watching, use dontAsk permission mode, so anything not on the list is refused instead of asked. A command that is not on the list is never run because it looks safe. If it is needed, name it, say why, and ask the owner to add it.
5. Missing keys. If a key, setting or file is missing, stop. Name exactly what is missing and ask the owner. Never invent a value, copy one from another project or fall back to a default.

## Rules
- A guard that lets the action through when it fails is a bug. Fix it before the work goes on.
- Test a guard by breaking it, not by reading it.
- "It probably would have passed" is not a pass.
- Only the owner turns a block into a yes.
