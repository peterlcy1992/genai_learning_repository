# automation/

How the knowledge bank keeps itself up to date and reminds you where you are.

## What runs

A scheduled **Routine** (Claude Code on the web) fires **once per day at 08:00
America/Los_Angeles (16:00 UTC)**. Each firing starts a fresh Claude Code
session against this repository and runs the instruction in
[`daily_update_prompt.md`](daily_update_prompt.md):

1. reads your current stage from [`../PROGRESS.md`](../PROGRESS.md),
2. web-searches for the newest notable GenAI papers, releases, and blog posts,
3. de-duplicates against [`../updates/latest.md`](../updates/latest.md) and
   prepends the best new finds,
4. commits + pushes to `claude/genai-learning-knowledge-bank-rn9s7p`, and
5. **emails you** a brief: your current stage + a next action + the day's
   highlights.

The email is the Routine's **completion notification**, sent to the account
owner (peterlcy1992@gmail.com). No SMTP setup or secrets required.

## The live Routine

- **Name:** `Daily GenAI knowledge-bank update`
- **Trigger ID:** `trig_016nEKMsZ2iG9AbeVBwGne4J`
- **Schedule (cron, UTC):** `0 16 * * *`  (= 08:00 PST)
- **Type:** fresh session per fire, email notification enabled.

> Note on daylight saving: cron runs in fixed UTC, so `16:00 UTC` is 08:00
> during PST and 09:00 during PDT (roughly mid-March to early November). Ask to
> shift it to `0 15 * * *` if you want a steady 08:00 during PDT.

## Changing the automation

You can just ask Claude Code (in a session on this repo) to do any of these, or
do them yourself with the Routines/`claude-code-remote` tools:

- **Change the time:** update the Routine's cron expression (`update_trigger`).
- **Change what it does:** edit [`daily_update_prompt.md`](daily_update_prompt.md)
  *and* update the Routine's `prompt` so the live job matches.
- **Pause it:** disable the Routine (`update_trigger` with `enabled: false`).
- **Resume it:** enable it again.
- **Delete it:** remove the Routine (`delete_trigger`).
- **Run it now (test):** fire the Routine on demand (`fire_trigger`).

To find the Routine later, list your Routines and match the name/trigger ID
above.

## How the system knows your learning progress

It reads the machine-readable YAML block at the top of
[`../PROGRESS.md`](../PROGRESS.md) — specifically `current_stage`. **You** are the
source of truth: when you finish a stage, bump `current_stage` (and tick the
checklist). The daily email greets you at whatever stage that block says. The
automation never changes your stage for you.
