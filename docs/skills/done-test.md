# /done-test

Write the checks before the work. Run them before anyone says "done".

[The skill file](../../skills/done-test/SKILL.md) is 29 lines. You can read all of it in a minute.

## What it fixes

The agent said it was done. It was not.

The problem was not that the agent lied. "Done" meant "I stopped working", not "it works", and nobody had said what "works" means. So the agent picked its own finish line, and it picked one it could reach. This skill writes one to three checks before the work starts, checks a stranger could answer yes or no. When the work ends, the agent runs each check and reports pass, fail or not run, with the evidence next to each one. If it could not run a check, it says so instead of claiming it.

## When to use it

- You are about to hand a task to an agent and come back later.
- The result will be reported to you as "done", "fixed" or "works".
- Part of the result happens somewhere the agent cannot see: your inbox, your phone, your customer.
- Part of the result is taste. Then the check is "the owner says yes to X", and it is never a pass until you say it.

It works the same whether the thing is code, a page, a document, an email or a plan.

## Example

This is a real run on Claude Code (2026-10-13), copied as it came out. The site was one static page for a photographer, with an email address under "Contact".

### Before: the same ask, without the skill

> add a contact form to my site

```
I added a contact form to the Contact section of `index.html`, but it doesn't send messages from the website itself. I haven't opened it in a browser.

**How it works:**
- The form has Name, Email and Message fields, and all three are required.
- When someone clicks **Send**, their own email app opens with a new message to hello@example.com. The subject is "Website inquiry from <name>" and the body has their message, name and email address.
- If the visitor has JavaScript turned off, the browser falls back to a plain `mailto:` link.
- I kept your email address in the text above the form, so people can still write to you directly.

**The limitation:** your site is a single static HTML file with no server. So the visitor still has to send the message from their own email app. If they don't have one set up, which is common on shared or work computers, nothing gets sent.

**For a form that sends without leaving the page**, you'd need a form service like Formspree, Netlify Forms or Web3Forms. It means signing up for an account and changing one line in the form. I can set that up if you tell me which service you'd like.

**Also:** hello@example.com is still a placeholder, both in the text and in the form. Replace it with your real address before going live, or tell me the address and I'll put it in.
```

The agent was honest, and the work is still not done. It chose how messages travel without asking, and it never opened the page. Nothing says what would have to be true for the form to count as working.

### With the skill: the checks come first

> add a contact form to my site

```
The site is a single static page, `index.html`, with no backend. So the main open question is where the messages go once someone hits Send. Here are the checks I'd like to agree on before I start:

**Proposed done-tests**
1. **The form shows up and is usable on a phone.** It replaces or sits under the current "Contact" section, with Name, Email and Message fields and a Send button. It shouldn't scroll sideways at 375px wide. *How I'll check:* open the page at phone width in a headless browser and look at a screenshot.
2. **Empty or invalid fields are blocked.** Clicking Send with a blank field or a bad email address shows an error and sends nothing. *How I'll check:* fill in the form wrong in the headless browser and confirm nothing is sent.
3. **A real test message reaches your inbox.** *How it gets checked:* I can't do this one myself. I can't see your inbox, and it depends on your form service account. You'll need to send one test message from the live site and tell me whether it arrived.

**I need one answer from you: where should messages go?**
- **(a) A form service like Formspree, which is my recommendation.** It's free for low volume and works on any static host. You sign up with the email address you want messages sent to and give me the form ID. Visitors never leave your page.
- **(b) Netlify Forms.** This only applies if the site is hosted on Netlify. It needs no account setup beyond that.
- **(c) A plain `mailto:` link.** It needs no service, but it opens the visitor's own email app instead of sending from the page, and many people don't have one set up. I don't recommend it.

Are these the right checks, and which option do you want? If it's (a), I can build everything now with a placeholder form ID, and you can swap in the real one once you have it.
```

### The answer

> yes, those checks are right. go with (a) and a placeholder id, I'll sign up later

### After: the report

```
I added the contact form to `index.html`. Two of the three checks pass. The third, a real message reaching your inbox, can't run until you have a Formspree ID.

**What I added**
- Name, Email and Message fields with a Send button under "Contact". Your email address is still shown below as a backup.
- The form sends to Formspree without leaving the page, then shows "Thanks! Your message has been sent." If sending fails, it asks the visitor to email you directly.

**Check results**
1. **The form shows up and is usable on a phone: Pass.** At 375px wide the page is exactly 375px across, so nothing scrolls sideways, and all four parts (three fields and the button) are visible. I saved screenshots to `/tmp/cf-check/phone.png` and `/tmp/cf-check/phone-errors.png`, but I didn't get permission to open them, so I haven't looked at them myself. Open them if you want to see the layout.
2. **Empty or invalid fields are blocked: Pass.**
   - An all-blank Send showed an error under each of the three fields.
   - A Send with `not-an-email` in the Email field showed only "Please enter a valid email address."
   - A message made only of spaces showed "Please write a message."
   - None of those attempts sent anything. As a control, a correctly filled Send did go to `formspree.io/f/YOUR_FORM_ID`. It got the "something went wrong" message, which is expected while the ID is a placeholder.
3. **A real test message reaches your inbox: Not run.** It needs your Formspree account. To run it:
   1. Sign up at formspree.io with the email address you want messages sent to, and create a form.
   2. In `index.html`, replace `YOUR_FORM_ID` in the form's `action="https://formspree.io/f/YOUR_FORM_ID"` with the ID they give you.
   3. Publish the site, send yourself one message from the live page, and check that it arrives. Formspree may ask you to confirm your email address the first time.

This isn't done yet: the remaining step is check 3, which you'll need to run once you've signed up.
```

The report does not say "done". It says two checks passed and shows what it saw for each. It also says what it did not see: it never looked at its own screenshots, so it says so. The one check it could not run, the message reaching your inbox, is marked "not run" with the three steps you need to run it yourself. That is the check that matters most, and it is the one an agent is most tempted to skip.

## The principle

The principles:

1. Done is a check, not a feeling. If a stranger cannot answer it yes or no, it is not a check yet.
2. Write the checks before the work. Checks written afterwards describe what was built, not what was wanted.
3. A check you did not run is not a pass. Say it was not run.

The agent can do the work. It does not get to decide, on its own, that the work is done.
