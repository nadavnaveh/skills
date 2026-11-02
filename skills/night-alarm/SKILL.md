---
name: night-alarm
description: Lists what can stop a night run (free disk, credits or quota, permissions) with each current value and the line at which it matters, writes a check, schedules it every thirty minutes so it wakes the agent in charge, and tests it once by tripping a line. Fixes "the run stopped at night, and the report waited until morning." Use before any overnight or unattended run, when you leave agents working while you sleep, or after a run stopped and nobody knew. Also on /night-alarm.
---

# Night alarm

The run stopped at night. A report said so, and nobody read it until morning. This skill sets up an alarm before your next night run.

In our run, a report waited 7 hours. The next day the alarm rang under 12 GB, cleared what it could and handed over one command, and 2 hours later we were back. That is one real catch so far, not a rate.

## The principles
1. A report only waits to be read. An alarm wakes someone.
2. Every stop has a number. Write its line before the run.
3. The alarm fixes only what the owner allowed. The owner gets one exact command for the rest.
4. An alarm that never rang in a test is not an alarm yet.

## Steps
1. List what can stop this run: free disk, credits or quota, permissions, and anything else it needs. Show each current value and its line, set early enough to leave time to act. Ours was 12 GB, above a 10 GB floor. Read each value with the same tool and scale as the thing that enforces the floor, and note any difference. Read credits from the service's own balance call or error.
2. Ask the owner two things: what the alarm may fix alone, as exact commands (for example clearing regenerable caches), and the one place they look first (for example a phone notification).
3. Write one check script that reads every value and fails when one crosses its line.
4. Schedule it every thirty minutes on the machine whose disk you are watching, and keep that machine awake. Use a Claude Code scheduled task, or the system's cron calling `claude -p` by its full path, with `--allowedTools` limited to the check and the approved fixes. Each firing wakes one agent with one prompt: run the check, and on a breach follow step 5. A session-only schedule, like /loop, dies with the session.
5. On a breach, the agent runs only the allowed fixes and reads the value again. If it is still past the line, it sends the owner one exact command to the place from step 2, with the value, the line and what the command will do.
6. Test it once. Set one line where it must trip, wait for the next scheduled firing, and show the result: what it read, what it fixed, the command it sent. Put the line back. If nothing woke, the alarm is not set.

## Rules
- Never delete anything that isn't regenerable. When unsure, leave it for the owner.
- A value the check cannot read counts as a breach, not a pass.
- One command for the owner, not a list of options.
- An alarm does not prevent a stop. It shortens the wait, so never call it solved.
