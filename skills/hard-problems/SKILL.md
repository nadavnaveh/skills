---
name: hard-problems
description: Attacks a problem nobody has solved yet. It writes many guesses down, runs one cheap test per guess, logs every try (failures included), keeps only the guesses that survived and proves the answer with a result someone else can rerun. Fixes "The agent tried one idea after another, and we are still stuck." Use when a bug or question has beaten the first two fixes, when nobody knows the cause, when the agent keeps saying "this should fix it", or when a session is going in circles. Also on /hard-problems.
---

# Hard problems

The agent tried one idea, then another, and you are still where you started. It chased the first guess, forgot what had failed and called the last try the answer. This skill makes it work like a lab: guesses written down, one cheap test each, every try logged, and a result someone else can rerun.

## The principles
1. A guess in the head gets chased. A guess on paper gets tested.
2. One cheap test per guess. A test that cannot fail tells you nothing.
3. Failed tries are data. A try that is not logged gets tried again.
4. Keep what survived the tests, not what you hoped for.
5. It is solved only when someone else can rerun it and get the same result.

## Steps
1. Write the problem in one sentence: what you see and what you expected to see.
2. Write down every guess about the cause as H1, H2, H3 and on. Write at least five before you test any.
3. For each guess, write one cheap test and the result that would kill it. Cheap means minutes: a log line, a small input, one setting changed, one older git commit checked out. Run the cheapest tests first.
4. Log every try in a file such as tries.md, one line each: number, guess, what you did, what happened, killed or open. Failed tries go in too. Read the log before each new try so nothing runs twice.
5. Narrow down. Cross out the killed guesses. If several are left, design one test that tells them apart. If none is left, write new guesses from what the log shows and go back to step 3.
6. Prove the survivor. Write the exact steps and the command that show the result. Then someone else reruns it: a fresh session, a subagent that gets only the written steps, or a person. It counts only if they get the same output.
7. Report the guess that survived, the test that proves it, how many tries it took, and each killed guess with the try that killed it.

## Rules
- Never write "found it" or "fixed" before the rerun matched.
- Change one thing per try, so each result points to one guess.
- If ten tries in a row kill no guess, stop and ask the person before the next one.
- Keep the log after the problem is solved. The next hard problem may start there.
