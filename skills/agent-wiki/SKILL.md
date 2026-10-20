---
name: agent-wiki
description: Keeps a wiki folder the agent writes to as it reads. It makes one page per topic, gives every claim a link to its source, edits the right page when a new source arrives, keeps an index.md that lists every page, and runs a weekly review that deletes what went stale. Fixes "The agent read it last week, and today it knows nothing about it." Use when you hand the agent an article, a document, a paper or a link to learn from, when you research one topic over several sessions, when a notes file has grown too long to use, and once a week for the review. Also on /agent-wiki.
---

# Agent wiki

The agent read it last week, and today it knows nothing about it. What it learned stayed in a session that ended, or went into one giant notes file that nobody can search. This skill files what the agent learns into a wiki of topic pages, with a source for every line, and keeps the wiki current.

## The principles
1. One page per topic, not one giant notes file.
2. Every claim links its source. A line without a source is a guess.
3. A new source edits the page it belongs to. It does not start a new pile.
4. A wiki that is never pruned starts to say things that are no longer true. Stale pages go.

## Steps
1. Set up the folder. Make `wiki/` with an `index.md` in it. Add one line to CLAUDE.md: "Before answering about a topic, read wiki/index.md and the page it points to." That way every new session finds the wiki.
2. Read the source. When you are handed an article, a file or a link, read all of it. List what it says that is new, as short claims.
3. File each claim on its topic page. If the topic already has a page, edit that page: add the new finding, and change any line the source proves wrong. If it has no page, make one, numbered in the order the pages are made: `01-caching.md`, `02-search.md`.
4. Cite every line. Each claim ends with a number like [1]. Under the claims, a Sources list gives each number its source: the title, the link or file, and the date it was read. Then check the page: every claim has a number, and every number has a source. If a check fails, fix the page before you go on.
5. Update index.md. Give each page one line: its name, one sentence on what it covers, and the date it last changed. Then check that every page in `wiki/` is listed and every listed page exists.
6. Report what changed: which pages were made or edited, and each new finding with its number.
7. Once a week, review. A page is stale when it has not changed in the time the owner set (for example, three months), when its sources are gone, or when a newer page says the opposite. Show the stale pages with the reason for each one. Delete them only after the owner says yes, then take them out of index.md. The other pages stay.

## Rules
- Never write a claim you cannot cite. Say it is not known instead.
- Edit the page that exists. Never make a second page for a topic that already has one.
- Commit the wiki to git after each change, so a deleted page can be brought back.
