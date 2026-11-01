---
name: batch-judge
description: Turns an AI judge that runs many checks on the same text, one call per check, into one call that answers every check in one JSON answer, with the files pasted in, and proves the verdicts did not change on examples you already know before you switch. Fixes "my AI checks are slow, and every check reads the same text again." Use when an LLM judge, grader, reviewer or eval asks several questions about the same input, when the checks feel slow or cost too much, and when you add a new check to a judge you already have. Also on /batch-judge.
---

# Batch judge

Your AI judge runs ten checks on the same text, one call each. Every call reads the same text again and reads the same files again, so you wait and pay for the same reading many times. On a judge that runs on every piece of work, that waiting and that cost add up every day. This skill puts the checks into one call, and it proves the verdicts stayed the same before you switch.

## The principles
1. One input, one read. Questions about the same text go in the same call.
2. Paste, don't point. Each file the judge opens on its own is another round of waiting.
3. Faster means nothing until the verdicts match on examples you already know.

## Steps
1. List every check the judge runs on one input, with its exact wording. Keep the old judge as it is, under its own name, so you can still run it.
2. Write one prompt: the input once, then every check, word for word as before. End it with "Return ONLY one JSON object" and one key per check, for example `{"H1": {"v": "yes|no", "quote": "..."}, "H2": ...}`.
3. Paste every file the checks need into the prompt, between clear markers, and tell the judge not to open any file. If your runner lets you remove the file tools from the call, remove them. If it does not, run one input and count the requests: more than one means the judge is still opening files, so find what it opened and paste that in too.
4. Read the JSON in code, not by eye. A missing key, or a value that is not yes or no, is a failed read: retry it once, and never fill it in with a guess.
5. Pick a few inputs you already know, some good and some bad, and write down the right verdict for each before any run. Run the old judge and the new one on them. Report, for each input, the old verdict, the new verdict, the seconds and the number of calls. Then say how many verdicts matched out of the total.
6. If any verdict differs, stop and show the checks that differ, with both answers. The owner decides. If all match, show the table and ask "Switch to one call?" Switch only after a yes.
7. After any change to the prompt, the checks or the model, run the same known inputs again and compare before you trust the new verdicts.

## Rules
- Never switch on "it looks the same". Only the comparison counts.
- Keep the check wording identical. A reworded check is a new check and needs its own comparison.
- A failed read is a failure, never a pass.
- Faster with different verdicts is not an improvement. Say so and stop.
