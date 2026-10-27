---
name: stranger-test
description: Reads every Supabase table with the public key and no login, lists what sent back rows, and closes each with Row Level Security and a rule after your yes. Fixes "I built a Supabase app with an agent, and anyone can read my tables." Use after an agent builds or changes a Supabase app, before launch and whenever you add a table. Also on /stranger-test.
---

# Stranger test

You built a Supabase app with an agent, and anyone can read your tables. The public key ships in your app on purpose; only Row Level Security (RLS) and a rule per table keep strangers out. This skill reads it as a stranger and closes what opened, with you.

## The principles
1. The public key protects nothing. RLS and a per-table rule do.
2. Every table gets RLS and a rule for who may read what. RLS with no rule shuts everyone out. A wrong rule can open it again.
3. Whatever a stranger can read, the world can read.

## Steps
1. Ask for the project URL and the anon or publishable key. Never the secret or service role key: it skips RLS. Test only the owner's projects.
2. Have the owner run these in the SQL editor per exposed schema (usually public):
   `select tablename, rowsecurity from pg_tables where schemaname = 'public';`
   `select table_name, column_name from information_schema.columns where table_schema = 'public';`
   Views skip RLS unless made with security_invoker: test them too.
3. Read each table with that key, no login. Only headers print, never rows:
   `curl -s -o /dev/null -D - "<URL>/rest/v1/<table>" -H "apikey: <key>" -H "Accept-Profile: <schema>" -H "Prefer: count=exact"`
   Content-Range, after the slash, reads:
   - Above 0: open.
   - 0: closed if RLS is on, open but empty if off.
   - 401 or 403: closed. Anything else: not tested.
4. Give the owner the open tables first: RLS on or off, row count, personal-looking columns. That is what opened.
5. Per open table, write one line on who may read it, then its SQL:
   ```
   alter table <t> enable row level security;
   -- each user reads only their own rows
   create policy <t>_owner_read on <t> for select to authenticated using (auth.uid() = user_id);
   ```
   `to authenticated` keeps strangers out; user_id names the owner. Rollback: `alter table <t> disable row level security;` Ask "Apply these?" and change nothing before a yes.
6. Rerun step 3: rows drop to none, or to what the rule allows. Have the owner check the app logged in. Test writes and cross-user reads separately.

## Rules
- An untested table is not closed. Report it as not tested.
- Never print rows, only counts and column names.
- Proof (scripts/rls-run-2026-10-27.txt, scripts/PROOF.md): local Postgres as role anon read 3 fake rows, then 0 after RLS. UpGuard, as reported, found 16,326 readable databases among about 300,000 Supabase domains.
- It does not show a Supabase project tested, personal data everywhere, any copying, or that AI caused it.
