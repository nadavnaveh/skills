---
name: big-archive
description: Splits a big archive (hundreds or thousands of pages) into numbered parts, gives one part to each subagent, reads all parts at the same time, makes every finding cite its page, merges the lists into one with duplicates gone, and spot-checks two cited pages at random. Fixes "I gave it a thousand pages, and it skimmed the start and guessed the rest." Use when you need to find something across a large folder of documents, scans, letters, reports or records, when one session cannot read it all, or when every answer must point to where it came from. Also on /big-archive.
---

# Big archive

You gave it a thousand pages, and it skimmed the start and guessed the rest. One agent cannot hold that much at once, so the late pages get less attention and the findings lose their source. This skill splits the archive into parts, reads them in parallel, makes every finding cite its page, merges the lists and checks two pages by hand.

## The principles
1. One part per agent. Every page is in exactly one part: no gaps, no overlap.
2. A finding without a page is not a finding.
3. The same thing found twice is one finding. Merge before you count.
4. Citations are claims until you open the page. Open two at random.

## Steps
1. Write the question in one sentence: what you are looking for in the archive. Then write what one finding looks like: what was found, the file, the page, and a short exact quote.
2. Split. List the files, count the pages, and cut the archive into numbered parts, one per agent (1/3, 2/3, 3/3). Write the split to a file such as `parts.md`: which part holds which files and pages. Show it and ask "Split like this?" Start only after a yes.
3. Read in parallel. Start one subagent per part, all at the same time. Give each one the question, its part and nothing else, and the finding format. Each one only reads, writes its findings to its own file (`findings-1.md`, `findings-2.md` and so on) and ends by naming the last page it read.
4. Cite the page. Check each list as it comes back. Every finding needs a file, a page and a quote. Send any finding without them back to its agent, or drop it. If an agent did not reach the last page of its part, send it back to finish.
5. Merge. Combine the lists into one. When two agents found the same thing, keep one row and list both pages. Say how many duplicates you removed.
6. Spot-check. Pick two findings at random, not the first ones. Open each cited page yourself and check that the quote is there and says what the finding says. If both match, the list holds. If one fails, check that agent's whole part again.
7. Report: the question, the parts and which agent read each one, the merged list with pages, the number of duplicates removed, and the two spot-checked pages with what you saw on each.

## Rules
- Agents only read. Nobody edits the archive, and each agent writes only its own findings file.
- Never fill in a page from memory. No page, no finding.
- A failed spot-check is about the whole part, not one line. Recheck the part.
- If the archive has no page numbers, use the file name and line number instead, and say so in the report.
