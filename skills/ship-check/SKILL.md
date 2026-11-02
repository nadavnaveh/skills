---
name: ship-check
description: Compares what you approved with what's about to ship, file by file, and stops the send on any difference. Fixes "I approved the right file, and yesterday's copy was about to go out." Use when you approve files for a later send, when a post, email, upload or release sends from a staging or copy folder, and right before any such send. Also on /ship-check.
---

# Ship check

You approved the right file, and yesterday's copy was about to go out. The send reads from a folder of copies, and a copy does not change when the approved file does, so checks on the package can pass while that folder is stale. This skill compares what you approved with what's about to ship. It sends nothing itself.

## The principles
1. Check the envelope, not the package. What ships is what the send command reads.
2. Yesterday's copy stays yesterday's. A file name proves nothing. A fingerprint does.
3. Compare before you rebuild. A stale file gets shown, not silently overwritten.
4. Any difference after the rebuild stops the send, even one that looks harmless.

## Steps
1. Find the exact files the send command reads. Open the command or script and follow its paths. Do not assume it reads the package. If you cannot tell, stop and say so.
2. At approval, record each approved file, its source path and its fingerprint in one file. Use `shasum -a 256 <file>`, or md5 (`md5 -r <file>` on a Mac, `md5sum <file>` on Linux). Keep to one tool.
3. Right before sending, fingerprint the files at the last stop, the paths from step 1, and compare them with the record. Copy nothing yet.
4. Report every difference now and show both sides: path, fingerprint and modified time. List any file in the sending folder that is not in the record as unapproved.
5. Rebuild the sending folder: copy each approved file from its source over the staged copy. Mark each file that differed in step 4 as "was stale, refreshed". Leave unapproved files in place.
6. Fingerprint the last stop again and compare with the record. Report one line per file: name, approved fingerprint, last-stop fingerprint, match or mismatch. A missing file is a mismatch. So is an unapproved file.
7. On any mismatch, stop the send and show both versions. The owner decides. If every file matches, give the report to whatever does the sending.

## Rules
- Never edit the record to make a mismatch go away. A changed file needs a new yes.
- A comparison you did not run is not a match. Report it as not run.
- Our run: one post. The video matched, but a stale cover sat in the staging folder, caught about six minutes before the slot, and the same stale files were found for the next day's video. A near miss, one run, not a rate. Rebuilding right before sending is a recommendation from that incident, not proven.
