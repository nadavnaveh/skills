---
name: batch-judge
description: Speeds up an AI judge that reads the same text many times. It keeps every check in one prompt with one JSON answer, pastes the files in, and cuts the repeat reads only after old and new give the same verdicts on examples you already know. Fixes "my AI judge is slow, and it keeps reading the same text and files again." Use when an LLM judge, grader, reviewer or eval makes several calls on the same input, opens the same files on each call, feels slow, or is about to get more checks. Also on /batch-judge.
---

# Batch judge

Your AI judge makes many calls on the same text. Each call reads that text again and opens the same files again, so you wait and pay for the same reading many times. This skill gets the judge down to one read with the files pasted in, and it switches only after proof that the verdicts did not change.

## The principles
1. One input, one prompt. Every question goes in it, with one JSON answer.
2. Paste, don't point. Each file the judge opens on its own is another round of waiting.
3. One read is not always enough. The comparison decides that, not the speed.

## Steps
1. Look at what the judge does today: how many calls per input, what each call asks, and which files it opens. Do not assume. Keep the old judge runnable, under its own name.
2. Write one prompt: the input once, then every check, word for word as before. End it with "Return ONLY one JSON object" and one key per check, for example `{"H1": {"v": "yes|no", "quote": "..."}, "H2": ...}`.
3. Paste every file the checks need into the prompt, between clear markers, and tell the judge not to open any file.
4. Build a known set: good and bad examples, with the right verdict for each written down before any run.
5. Run the old judge and the new one on every example, three times each. For each input, report the known verdict, the old verdict, the new verdict, the seconds and the calls. Take the majority of three as each judge's verdict. Then give the matches both ways, for example "6 of 6 by majority of three runs, 17 of 18 by single run".
6. If every majority verdict matches, show the table and ask "Cut the repeats?" Switch only after a yes. If any verdict differs, stop and show the checks that differ, with both answers. The owner decides, and may keep more than one read.

## Rules
- Never switch on "it looks the same". Only the comparison counts.
- Faster with different verdicts is not an improvement. Say so and stop.
- A broken JSON answer is a failed read, never a pass. After any change to the prompt, the checks or the model, run the comparison again.
- Keep the old judge runnable after the switch.
- Our run: six known scripts went from 394 seconds, at 5 to 15 reads a script, to between 100 and 123 seconds at one read. Verdicts matched on all six by majority of three runs, and a single run matched 17 of 18. Your judge needs its own comparison.
