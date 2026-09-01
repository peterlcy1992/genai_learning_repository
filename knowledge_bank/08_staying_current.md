# Stage 8 — Staying current: the refresh loop

**Goal:** turn the endless stream of daily updates into a small set of *durable*
improvements to your understanding. Stage 7 got you to the frontier; Stage 8 is
the discipline that keeps you there without drowning. It is the only stage that
is never "finished" — it's a **loop you run for the rest of the field's life.**

The daily job ([`updates/latest.md`](../updates/latest.md) and the
[`digests/`](../digests/)) is a firehose: 3–7 items a day, most of them
incremental. Reading everything is neither possible nor useful. The skill worth
building here is **curation** — deciding what actually matters and folding only
that back into your mental model.

---

## 📜 Frontier log — auto-curated

An automatically maintained shortlist of the *durable, high-signal* developments
the daily scout flags — the small fraction that scores high on the rubric in §3
(durability · breadth · evidence). Newest first, deduped. Treat it as the
machine's "maybe worth a permanent note" pile; you still decide what to genuinely
integrate (§2).

<!-- FRONTIER_LOG_START -->
_No entries yet — the daily job appends genuinely durable developments here._
<!-- FRONTIER_LOG_END -->

---

## 1. Why this stage exists

A learning plan that ends at Stage 7 rots within months: models, records, and
even "best practices" turn over fast. But the opposite failure — trying to read
every paper — burns you out and teaches nothing durable, because you never stop
to integrate. Stage 8 is the middle path: a **repeatable triage** that spends
your scarce attention on the few things that change how you'd build or reason,
and lets the rest wash past.

The mantra: **most news is noise; a little of it is a genuine improvement. Your
job is to find that little, and actually absorb it.**

## 2. The refresh loop

Run this on a cadence — daily skim, **weekly** curate, monthly prune:

1. **Skim (daily, 2 min).** The digest already did first-pass filtering. Read the
   one-line "why it matters" per item; open nothing yet unless it's obviously
   seismic.
2. **Triage (weekly, ~30 min).** Re-read the week's digests together and pick the
   **1–3 most critical items** using the rubric in §3. A week's remove from the
   hype makes the signal much easier to see than it was on the day.
3. **Integrate (weekly).** For each chosen item, do the work that makes it
   *yours*: read the primary source, then **write the change down** — a line in
   the right `knowledge_bank/*.md` note or reading list, and a sentence on *what
   it changes* about how you'd build or think. If it doesn't change anything, it
   wasn't critical — drop it.
4. **Prune (monthly).** Remove or annotate what's been **superseded**. A current
   bank is worth more than a complete one; additive-only notes decay into a
   museum. Mark the old approach as "was state-of-the-art until X."

## 3. What counts as a "critical improvement" — the rubric

Score a candidate on four axes; the ones worth integrating score high on most:

- **Durability** — is this a *paradigm shift* or an *increment*? A new training
  regime (RLVR) or capability class (reasoning models) outranks another point on
  a benchmark. Ask: "will this still matter in a year?"
- **Breadth** — how many downstream things does it change? A cheaper attention
  kernel or a new post-training recipe touches everything; one lab's model
  release touches less.
- **Evidence** — reproduced, open, and measured beats a press release. Prefer an
  arXiv paper with a method and ablations, or an open-weights release, over a
  demo or a leaderboard screenshot. **Discount hype; wait for the replication.**
- **Proximity** — does it touch *your* goals and current stage? A retrieval
  advance matters more if you build RAG systems; a diffusion result matters less
  if you never touch images. Relevance is allowed to break ties.

A useful test: **would you change a sentence in the knowledge bank because of
it?** If yes, it's probably critical. If it's "another model, slightly better,"
it's log-and-move-on.

## 4. How this rides on the automation

The daily Routine is your **scout**, not your curator. It surfaces candidates
(searches, de-dupes, links, tags each with a "Relates to: Stage N"), archives a
per-day digest, and nudges you. Stage 8 is the **human-in-the-loop** step on top:
the machine can rank *recency and relevance*, but only you decide what durably
updates your model of the field. Keep the division of labour clear — let the job
gather; you curate.

When `PROGRESS.md` sits at `current_stage: 8`, treat the daily email less as
"what did I miss" and more as "is there anything here worth a permanent change?"
— the answer is usually no, and that's fine.

## 5. Habits that make it stick

- **Small and regular beats big and rare.** A 30-minute weekly pass sustains for
  years; a monthly binge doesn't.
- **Write to remember.** An idea you can't summarise in a sentence you don't yet
  understand. The act of updating a note *is* the learning.
- **Follow threads, not feeds.** Pick two or three arcs (say reasoning, agents,
  efficiency) and go deep; let the rest stay peripheral.
- **Let benchmarks age.** Records fall weekly; the *methods* behind them are what
  endures. Integrate techniques, not scores.
- **It's fine to skip a week.** The digests are archived; nothing is lost. The
  loop tolerates gaps — that's the point of writing things down.

---

## Checkpoints — you should be able to explain…
- Why "read everything" and "stop at Stage 7" are both failure modes, and what
  the refresh loop does instead.
- The four criticality axes (durability, breadth, evidence, proximity) and how
  you'd use them to pick this week's 1–3 items from a stack of digests.
- Why integration means *writing the change down and pruning what it replaces*,
  not just bookmarking.
- The division of labour between the daily automation (scout) and you (curator).

## Reading list
Stage 8 has no fixed papers — its "reading list" is your own live sources, and
the practice of working them. Anchor points:
- **This repo's stream** — [`updates/latest.md`](../updates/latest.md) and
  [`digests/`](../digests/): the raw material you curate.
- **Ongoing sources** — see the *"Ongoing sources"* section of
  [`reading_list.md`](reading_list.md) (arXiv, lab blogs, explainers,
  newsletters). These are where the scout looks and where you browse too.
- **On curation itself** — Nathan Lambert's *Interconnects* and Jack Clark's
  *Import AI* are useful models of *what a good weekly filter looks like*: they
  select and contextualise rather than list.

## This stage never closes
There's no "next" page — Stage 8 loops back into the daily stream. Keep
[`PROGRESS.md`](../PROGRESS.md) at Stage 8 once you've worked through 0–7, run
the weekly pass, and let the knowledge bank stay a living document rather than a
finished one.
