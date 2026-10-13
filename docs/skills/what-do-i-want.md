# /what-do-i-want

Turn a vague want into one statement with a done-test, before the agent starts.

[The skill file](../../skills/what-do-i-want/SKILL.md) is 30 lines. You can read all of it in a minute.

## What it fixes

You asked for something. The agent did exactly that, and it is not what you wanted.

The problem was not the agent. "Make it better" is a feeling with a direction, and nobody wrote down where it ends. The agent guessed, and it guessed confidently. This skill makes the guessing visible, asks the few questions that change the result, and writes down what you want and how you will both know it is done.

## When to use it

- The request has no clear end: "make it better", "clean this up", "something like X", "fix the onboarding".
- Nobody has said who the result is for.
- You could not tell a stranger how to check that it is finished.
- You are about to hand a task to an agent and walk away.

If your request already has a clear end and a test, the skill says so in one line and gets out of the way.

It works the same whether the thing is code, a document, a page, a plan or an email.

## Example

This is a real run of the skill on Claude Code (2026-10-13), copied as it came out.

### Before

> make my landing page better

### Round one: the skill does not start the work

```
Before I touch anything, I need to know what "better" means for your landing page. It could point in a few different directions.

**Three ways to read "better":**
1. **More people act on it.** This assumes the page gets visitors who leave without signing up, buying or booking.
2. **It looks more current and trustworthy.** This assumes the content works but the design feels dated or cheap.
3. **It says the right thing.** This assumes visitors don't quickly understand what you offer or who it's for.

**Three questions that would change the result most:**

**1. Who is the page for?**
- a) New visitors who have never heard of you ← my best guess
- b) People who already know you and come back to buy, book or log in
- c) Investors, partners or press
- or tell me in your own words

**2. What should change for them when it works?**
- a) More of them take the main action (sign up, buy, book a call) ← my best guess
- b) They understand what you do within a few seconds
- c) They trust you enough to get in touch
- or tell me in your own words

**3. What must stay as it is?**
- a) The brand: logo, colours and fonts ← my best guess
- b) The copy and messaging
- c) The tech stack or the page structure
- d) Nothing is off limits
- or tell me in your own words

You can answer with letters ("1a, 2b, 3a") or just describe it. It would also help to have the page's URL or the folder it lives in. Once I have your answers, I'll write a short statement of what you want and how we'll know it's done, and I'll only start the work after you confirm it.
```

### The answer

> 1a, 2a. It's a bakery that does custom cakes. People land from Instagram, scroll, and leave. I want more of them to send an order request. Don't touch the logo or the photos, they're my work.

### After: the statement

```
**I want:** people who land from Instagram (new visitors who've never heard of the bakery) to send an order request for a custom cake instead of scrolling and leaving.

**Done when:**
1. A visitor on a phone coming from Instagram can find how to send an order request without scrolling past the first screen.
2. The share of Instagram visitors who send an order request goes up from today's rate. The target number is still open; see below.
3. You look at the new page and say yes, it still feels like your bakery.

**Not:**
- The logo stays as it is.
- The photos stay as they are, because they're your work.

**Open:**
- **Today's numbers.** I don't know how many Instagram visitors you get or how many send a request. Without that, "more" has no baseline. Do you have analytics, or a rough count of requests per week?
- **How a request is sent.** Is it a form, email, WhatsApp, DMs or a phone call? It changes what "send an order request" means.
- **Where the page lives.** Is it Squarespace, Wix, Shopify or custom code? I'll need the URL or the files.
- **What a request needs.** Does it need a date, size, flavour, budget or a photo for reference? I'll ask before I change any fields.

**Is this what you want?** If yes, send whatever you have on the open points, especially the page URL and how requests come in, and I'll start.
```

"Make my landing page better" could have meant a redesign. It turned out to mean one button on the first screen of a phone, for people coming from Instagram, with the photos left alone. Notice that the skill did not invent a target number. It put the missing baseline under Open.

## The principle

The principles:

1. A want is a feeling with a direction. Understand it before you write a plan.
2. While the want is unclear, do not solve. Show the readings, the tensions, and the one question that changes the picture.
3. Your options are guesses, not the whole space. Say so, and let the person answer in their own words.

The agent can open options. It does not get to decide what you really want.
