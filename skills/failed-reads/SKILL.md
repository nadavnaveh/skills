---
name: failed-reads
description: Makes every automated report list its sources, mark each one read or failed with the real error, keep the failed ones in a file for the next run, and end with one line naming what it could not read. Fixes "My agent said nothing new, and it just couldn't read the source." Use when you build or run a scheduled report, digest, news scan or monitor that reads more than one source, and whenever an agent is about to write "nothing new". Also on /failed-reads.
---

# Failed reads

The agent said nothing new. It just couldn't read the source. A blocked source and a quiet day look the same in a summary, because the agent writes about what it got and stays silent about what it did not get. This skill ends every report with what it could not read.

## The principles
1. A failed read is not a quiet day. Anthropic's blog gives this advice: don't mistake a failed read for a quiet day, and end the brief with one line naming what it couldn't read.
2. "Nothing new" may only be written about sources that were read.
3. If everything failed, it is not a report. It is an outage.

## Steps
1. Open the failed list, `failed-reads.md`, if it exists. Whatever is on it goes first in this run.
2. Read every source. Mark each one read or failed. For a failure, keep the real error as it came back, such as HTTP 404 or JSONDecodeError, not "could not access".
3. If every source failed, stop. Write no digest. Say nothing was read, name each source with its error, and go to step 7.
4. Open the report with the list of sources. Next to each one, write read or failed, and why. In one of our runs, the news agent had 16 sources, 2 failed, and the report's header named both.
5. Write the report from the sources that were read. If they hold nothing new, say so about those sources only, and say how many could not be read.
6. End the report with one line naming what it could not read, with each error. If every source was read, the line says that.
7. Update `failed-reads.md`. Add each source that failed in this run, with the date and the error. Remove each source that was read.

## Rules
- Never write "nothing new", "quiet day" or "no updates" about a source that failed.
- An empty answer or a login page is a failed read.
- Never drop a failed source from the report, even if it fails every run.
- Never fill a failed source from an older run or from a guess.
- A source stays on the failed list until a read succeeds.
