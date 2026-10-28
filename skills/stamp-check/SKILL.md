---
name: stamp-check
description: Saves a fingerprint (hash) of the files each check judged. Before anything ships, it compares that fingerprint with the files as they are now, so any edit made after the check makes the check expire and run again. Fixes "I approved the agent's change, and it edited one more line after." Use when a test run, a review or your approval stands between the work and a commit, merge, send, render or release, whenever the agent edits anything after a check passed, and right before you ship. Also on /stamp-check.
---

# Stamp check

You approved the agent's change, and then it edited one more line. Your approval still looks valid, but the files you said yes to no longer exist. This skill stamps every check with a fingerprint of the files it judged, so the check expires by itself the moment one of them changes.

## The principles
1. A check covers the exact files it judged, not the files as they are now.
2. When a check passes, it saves a fingerprint (hash) of those files.
3. If anything changed since then, the check has expired and runs again. No assumptions.

## Steps
1. List the checks that must pass before anything ships (the tests, a review, the owner's yes) and the files each one judges. If a check has no clear list of files, ask before you go on.
2. When a check passes, write a stamp: the check's name, the time, and one hash per file, for example from `shasum -a 256 <files>`. Save it in a stamps file in the project, such as `stamps/<check>.txt`. If the files are committed and git status is clean, the commit hash can be the stamp.
3. Before anything ships (a commit, merge, send, render or publish), hash the same files again and compare each one with the stamp.
4. If every hash matches, report "stamp holds" with the check's name and time.
5. If any hash differs, the check has expired. Stop before the next step. Name the file, show the old and new hash, and run the check again. If the check was a person's approval, show them what changed and ask again.
6. If the owner wants this every time, put the compare inside the step that ships (a script or a git pre-commit hook), so it refuses without the agent having to remember. Test it both ways: change one word and see it refuse, then restore the word and see it pass.

## Rules
- A missing stamp, a missing file or a hash command that fails counts as expired, never as a pass.
- Never update a stamp without running the check it belongs to.
- A stamp only forces a re-check. It does not find bugs by itself, and a check that was wrong stays wrong.
- The proof is in scripts/PROOF.md and scripts/expire-run.txt. In our video pipeline, changing one word changed the file's md5, the copy gate check expired and the render stopped. Restoring the word brought the PASS back. The Claude Code team writes that an approval covers one specific commit and has to be given again when new commits land. That quote shows their rule, not how they build it, and our run says nothing about GitHub or any other tool.
