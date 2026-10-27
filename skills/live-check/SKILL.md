---
name: live-check
description: Opens the live address itself, reads which version is really running there, and walks one real user path start to end before anyone says production is restored. Fixes "the agent said production was restored, and users still got errors." Use after any deploy, rollback, hotfix or restore, whenever a script, a log or an agent prints "restored", "deployed" or "live", and before you tell anyone the site is back. Also on /live-check.
---

# Live check

The agent wrote "production restored", and users still got errors. The script or the agent printed that line. The site did not, so the line can say "restored" when nothing changed. This skill checks the live address itself before anyone believes the line.

## The principles
1. A status message is a claim, not evidence. Only the live address shows what users get.
2. The version that counts is the one the live site reports. The one you built or meant to ship does not count.
3. Restored means a real user can finish a real path. Until then, it is not restored.

## Steps
1. Write down the claim and who made it: the exact line the script, log or agent printed.
2. Name the live address users really reach, and the version you expect to find there (a version string, a build id, a commit). If you do not know what to expect, find out before you check.
3. Open the live address yourself with curl or a browser. Write down the status code and what the page returns. A 404, a 500 or the old page means not restored.
4. Read the running version from the live site itself: a version string on the page, a build id, or a health endpoint. Compare it with the version you expect. If the site shows no version, say so and suggest adding one.
5. Walk one real user path once, start to end, on the live site. For example: open the home page, sign in, and load the page users came for. Write down each step and what you saw.
6. Report each check as pass, fail or not run, with the evidence: the command, the status code, the version you saw, and the step where the path stopped.
7. Say "restored" only when all three checks passed. If one failed, say "not restored" and show what the live site returned.

## Rules
- Never repeat "restored", "deployed" or "live" from a script or an agent without the three live checks next to it.
- If you cannot reach the live site or walk the path, report "not run" and the exact step the owner can take.
- When a check fails, fix the site, not the message.
- What the proof behind this skill shows, and what it does not: on a small scratch site with a deploy typo we planted, the script printed "Production restored" in 2 of 2 runs while nothing changed, and 3 of 3 live checks showed the old build. That shows a success line is not evidence. It does not show that agents lie on purpose, that they usually skip the check (ours checked), or anything about real production systems.
