---
name: memory-queue
description: Sends every heavy job (builds, tests, renders) through one small queue script that caps how many run at once and waits until at least thirty percent of memory is free before each one starts. Fixes "I run five agents at once, and my Mac runs out of memory, so jobs crash or crawl." Use when you run several agents in parallel on one Mac, when builds, tests or renders slow the Mac down or die halfway, or when a "wait for free memory" rule in the prompt keeps getting broken. Also on /memory-queue.
---

# Memory queue

You run five agents at once. Each one starts a build, a test or a render, and the Mac runs out of memory, so jobs crawl or die halfway.
A "wait for free memory" rule in the prompt gets broken, because agents forget it.
This skill moves the rule into one small script that every heavy job passes through.

## The principles
1. A limit in code holds. A limit in the prompt is only a request.
2. Every heavy job goes through one door, so no agent can skip the queue.
3. A job starts only when it has a free slot and room to run.

## Steps
1. List the heavy jobs (builds, test runs, renders) and ask "Are these the heavy ones?"
2. Copy scripts/qrun.py into the project. Run `memory_pressure -Q` once and check that it prints "free percentage". The script reads that line, so it works only on a Mac.
3. Set the limits. The slot cap is `QRUN_HEAVY_MAX` (default two jobs at once). The memory floor is `QRUN_MIN_FREE` (default thirty percent free). Renders can queue apart with `--pool render`, capped by `QRUN_RENDER_MAX`.
4. Put `python3 scripts/qrun.py --` in front of each heavy command inside the build, test and render scripts the agents already call. If agents can still call the raw tool, add a PreToolUse hook that refuses it without qrun in front.
5. Test it. Start three jobs with a cap of two and check that the third waits. Run one job with `QRUN_MIN_FREE=101`, check that it never starts, then stop it with Ctrl+C.
6. Report each wait: which job, and how long it waited (qrun prints "qrun: waited Ns"). Then say what the queue did not prove.

## Rules
- Memory is checked only before a job starts. A job that grows later can still fill the Mac.
- If the script cannot read free memory, it lets the job start. Repeat the check in step 2 on every new Mac.
- Our proof is one Mac, one night: six tests passed, the longest job waited over six minutes and started at thirty percent free, and a render waited almost three minutes. It does not show that no job ever died, and it gives no speed-up number.
- Never raise the cap or lower the floor to make a wait go away without the owner's yes.
