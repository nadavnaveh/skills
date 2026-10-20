---
name: automate-questions
description: Asks five questions before a task is automated (does it repeat, can you check it, what if it fails, who owns it, is the data ready) and builds the job only when every one has an answer. Fixes "I automated it, and now I spend more time fixing it than doing it." Use before you set up a scheduled job, a script that runs on its own, a hook or a recurring agent run, whenever someone says "let's automate this" or "do this for me every week", and before you turn a task you did once into a job. Also on /automate-questions.
---

# Automate questions

You automated the task, and now you fix it more often than you used to do it.
It ran on bad data, it failed with nobody watching, and nobody could say if a run worked.
This skill asks five questions before anything is automated, and builds the job only when each one has an answer.

## The principles
1. Automate what comes back. A task that happened once is not a job.
2. A job you cannot check is a guess that runs on a timer.
3. Every job fails some day. Decide now how the mistake is caught and who hears about it.
4. Automating bad inputs repeats the mistake on every run. Clean them first.

## Steps
1. Write the task in one sentence: what goes in, what comes out, and how often.
2. **Does it repeat?** Ask how often it happened in the last month. It is worth automating if it comes back weekly or more. If not, do it by hand this time and say why.
3. **Can you check it?** Write one check that tells you the run worked, for example a `check.sh` that finds the output file, counts the rows or compares it to a known result. It must answer pass or fail without a person reading the output. If you cannot write one, stop here and say so.
4. **What if it fails?** Plan how a mistake gets caught. The check runs after every run. A fail stops the job before it sends or changes anything more, and an alert goes out to a named place (an email, a chat message, a notification).
5. **Who owns it?** Name one person who gets the alert and keeps watch. Not "the team". Write the name next to the job.
6. **Is the data ready?** Open the real inputs, for example `inputs.csv`. Look for empty fields, duplicates, wrong formats and rows that do not belong. Show every bad row, and with the owner's yes, fix the inputs or the step that makes them.
7. Show the five answers in a short table and ask "Automate it like this?" Build only after a yes. Then run it once while you watch, run the check, and show the result.

## Rules
- A question without an answer means no automation yet. Say which one is missing.
- Never delete or change an input row without the owner's yes.
- A job with no alert is not finished. "It should be fine" is not a plan for failure.
- Write the check, the alert and the owner down where the job lives, so the next person finds them.
