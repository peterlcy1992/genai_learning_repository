# GenAI Learning Knowledge Bank

A self-updating knowledge bank for learning the evolution of Generative AI —
from the pre-transformer era, through *Attention Is All You Need* (2017), all
the way to today's frontier reasoning models and agentic systems — and for
**staying current** as the field keeps moving.

> **📍 Visual companion — the GenAI Evolution Atlas:** an interactive field guide
> with the full curriculum, per-stage deep-dive pages, diagrams, reference links,
> and the latest daily digest. Public web page: [`docs/index.html`](docs/index.html),
> served via GitHub Pages at `https://peterlcy1992.github.io/genai_learning_repository/`
> once enabled. Build source in [`artifact/`](artifact/).

This repository does three things:

1. **Teaches the evolution structurally.** A staged curriculum
   ([`LEARNING_PLAN.md`](LEARNING_PLAN.md)) walks you from foundations to the
   frontier, with a deep-dive note and a curated reading list for each stage in
   [`knowledge_bank/`](knowledge_bank/).
2. **Tracks where you are.** [`PROGRESS.md`](PROGRESS.md) records your current
   learning stage and checklist, so the system (and you) always know what to do
   next.
3. **Keeps you up to date automatically.** A daily job searches for the newest
   papers and technical blog posts, appends them to
   [`updates/latest.md`](updates/latest.md), commits them here, and **emails you
   a reminder** of your current stage plus what's new in the industry.

---

## How to use it

### Learning
1. Open [`LEARNING_PLAN.md`](LEARNING_PLAN.md) and read the overview.
2. Start at **Stage 0** (or wherever your current knowledge sits).
3. For each stage, read the matching note in
   [`knowledge_bank/`](knowledge_bank/) and work through its reading list.
4. As you finish a stage, tick it off in [`PROGRESS.md`](PROGRESS.md) and set
   `current_stage` to the next one. **This file is how the daily email knows
   where you are** — keep it honest and it stays useful.

### Staying current
- Skim [`updates/latest.md`](updates/latest.md) — it's a reverse-chronological
  log of what the daily job found.
- Read the daily email; it summarizes your stage and the day's notable finds.

---

## Repository map

| Path | What it is |
|------|-----------|
| [`LEARNING_PLAN.md`](LEARNING_PLAN.md) | The staged curriculum + how to pace yourself |
| [`PROGRESS.md`](PROGRESS.md) | Your current learning stage and checklist (edit this as you go) |
| [`knowledge_bank/`](knowledge_bank/) | One deep-dive note per stage + glossary + master reading list |
| [`updates/latest.md`](updates/latest.md) | Rolling log of the latest innovations (auto-appended daily) |
| [`digests/`](digests/) | Full, reader-friendly per-day brief (`YYYY-MM-DD.md`) that the daily email links to |
| [`podcasts/`](podcasts/) | Weekly NotebookLM podcast episodes for *The GenAI Evolution Atlas* (audio + manifest) |
| [`automation/`](automation/) | The daily-update and weekly-podcast prompts, and docs on how the automation works |

---

## How the daily automation works (in brief)

A scheduled **Routine** (Claude Code on the web) fires once per day. It spins up
a fresh session against this repository and:

1. Reads [`PROGRESS.md`](PROGRESS.md) to learn your current stage.
2. Searches the web for the newest GenAI papers and technical blog posts.
3. Appends notable, non-duplicate finds to [`updates/latest.md`](updates/latest.md).
4. Writes a full per-day brief to [`digests/`](digests/) (`YYYY-MM-DD.md`).
5. Commits and pushes the update to this repo.
6. Emails you a short brief — *"You're on Stage N — here's what's new today"* —
   that **links straight to the day's digest** (the email body is a fixed
   template, so the full write-up lives in the linked digest).

Full details, and how to change the schedule or pause it, are in
[`automation/README.md`](automation/README.md).

## Weekly podcasts

Two weekly Routines turn the digests into audio for the RSS.com show
**The GenAI Evolution Atlas** (Season 2): a **Wednesday Deep Dive** on the
week's most important innovation, and a **Friday News Roundup** of everything
worth calling out plus commentary and a look ahead. Both are made with
**NotebookLM** (Deep Dive format, Long length), get a mono-color episode cover,
and are prepared as an **unpublished RSS.com draft** for you to review and
publish — the automation never publishes. See
[`automation/podcast_playbook.md`](automation/podcast_playbook.md).
