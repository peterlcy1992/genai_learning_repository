# automation/

How the knowledge bank keeps itself up to date and reminds you where you are.

## What runs

A scheduled **Routine** (Claude Code on the web) fires **once per day at 15:00
UTC** — 08:00 Pacific while daylight saving is in effect (PDT). Each firing
starts a fresh Claude Code
session against this repository and runs the instruction in
[`daily_update_prompt.md`](daily_update_prompt.md):

1. reads your current stage from [`../PROGRESS.md`](../PROGRESS.md),
2. web-searches for the newest notable GenAI papers, releases, and blog posts,
3. de-duplicates against [`../updates/latest.md`](../updates/latest.md) and
   prepends the best new finds,
4. writes a full, reader-friendly per-day digest to
   [`../digests/`](../digests/) (`YYYY-MM-DD.md`),
5. (strict, usually nothing) appends a genuinely durable find to the Stage 8
   [Frontier log](../knowledge_bank/08_staying_current.md) via
   [`frontier_log_add.py`](frontier_log_add.py),
6. regenerates the public web page ([`../docs/index.html`](../docs/index.html))
   with today's digest (and any Frontier-log update) embedded,
7. commits + pushes directly to `main`, and
8. **emails you** a brief: your current stage + a next action + the day's
   highlights, with a **direct link to that day's digest**.

The email is the Routine's **completion notification**, sent to the account
owner (peterlcy1992@gmail.com). No SMTP setup or secrets required.

> **About the email body:** the completion notification is a fixed template —
> a short summary plus an "Open session" button — so the full brief can't be
> inlined into it. Instead the summary is front-loaded (stage + top items) and
> **links straight to that day's [`digests/`](../digests/) file**, which GitHub
> renders in full. One click, no session needed. Enable it under
> **claude.ai → Settings → Notifications → "Emails from Claude Code on the web"**
> (this is separate from the push toggle).

## The live Routine

- **Name:** `Daily GenAI knowledge-bank update`
- **Trigger ID:** `trig_016nEKMsZ2iG9AbeVBwGne4J`
- **Schedule (cron, UTC):** `0 15 * * *`  (= 08:00 PDT, current Pacific time)
- **Target:** commits directly to `main` (no pull request).
- **Type:** fresh session per fire, email notification enabled.

> Note on daylight saving: cron runs in fixed UTC, so `15:00 UTC` is 08:00
> during PDT (roughly mid-March to early November) and 07:00 once standard time
> (PST) resumes. Ask to shift it to `0 16 * * *` when winter comes if you want
> to keep the email landing at 08:00 year-round.

## The public web page (GitHub Pages)

The shareable page is [`../docs/index.html`](../docs/index.html) — a standalone
build of the Atlas, intended to be served publicly by GitHub Pages from `/docs`.

- **Build script:** [`../artifact/build_public_html.py`](../artifact/build_public_html.py)
  wraps the Atlas source (`../artifact/knowledge-bank.html`) into a complete HTML
  document at `../docs/index.html`. [`../artifact/refresh_embedded_digest.py`](../artifact/refresh_embedded_digest.py)
  embeds the newest digest before the wrap.
- **Kept current by the daily job:** step 5 above runs both scripts, so the
  published site shows each day's digest automatically — no artifact and no
  interactive session involved.
- **Enable Pages (one-time):** make the repo public, then GitHub → **Settings →
  Pages → Deploy from a branch → `main` / `/docs`**. The URL is
  `https://peterlcy1992.github.io/genai_learning_repository/`.

To rebuild the page by hand: `python3 artifact/build_public_html.py`, then commit
`docs/index.html`.

> A private artifact version of the Atlas also exists
> (`https://claude.ai/code/artifact/41730737-b7b0-4055-9d7f-e0ea1cc34de9`). Its
> source is `../artifact/knowledge-bank.html`, but the published artifact no
> longer auto-updates — the public page above is the maintained, shareable copy.

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

## The weekly podcasts

On top of the daily job, **two weekly Routines** turn the digests into audio
episodes for the RSS.com show **The GenAI Evolution Atlas** (Season 2):

- **Wednesday — Deep Dive:** an in-depth episode on the single most important
  innovation of the past week (usually one article, at most three).
- **Friday — News Roundup:** a broad tour of everything worth calling out that
  week, then synthesis, opinion, and a look ahead.

Both are generated with **NotebookLM** (Deep Dive format, Long length) via
[`notebooklm-py`](https://github.com/teng-lin/notebooklm-py), given a mono-color
episode cover, and prepared for upload to RSS.com as an **unpublished draft** for
you to review and publish. The automation never publishes.

The authoritative procedure is [`podcast_playbook.md`](podcast_playbook.md).
Supporting files:

| File | What it is |
|------|-----------|
| [`podcast_playbook.md`](podcast_playbook.md) | The full weekly procedure (both episodes), end to end. |
| [`podcast_deepdive_prompt.md`](podcast_deepdive_prompt.md) | NotebookLM steering prompt for the Wednesday Deep Dive. |
| [`podcast_roundup_prompt.md`](podcast_roundup_prompt.md) | NotebookLM steering prompt for the Friday News Roundup. |
| [`rss_upload.py`](rss_upload.py) | Creates the RSS.com episode as an unpublished draft (X-API-Key; run with the key present). |
| [`../podcasts/`](../podcasts/) | The episode manifest (`episodes.json`) + generated audio + per-episode copy. |
| [`../artifact/thumbnails/podcast_thumbs.py`](../artifact/thumbnails/podcast_thumbs.py) | Parameterized mono-color episode cover generator. |

**Requirements.** The podcast Routines must run in an environment that has the
`NOTEBOOKLM_MASTER_TOKEN_JSON` secret **and** Google egress (the environment
`env_017Ev8YD93Ey36h3gyP68kyH` already does). The RSS.com draft upload
additionally needs `RSS_API_KEY` (an RSS.com **Network** plan) and egress to
`api.rss.com`; when that isn't present, the episode is still fully prepared and
left ready for a manual or local upload. See the playbook for details.

> **Schedule:** the two Routines are created separately (Wed + Fri). Until they
> are, generate an episode on demand by following `podcast_playbook.md` in a
> session on this repo, or ask Claude Code to create/fire the Routines.

## How the system knows your learning progress

It reads the machine-readable YAML block at the top of
[`../PROGRESS.md`](../PROGRESS.md) — specifically `current_stage`. **You** are the
source of truth: when you finish a stage, bump `current_stage` (and tick the
checklist). The daily email greets you at whatever stage that block says. The
automation never changes your stage for you.
