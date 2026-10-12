# News-roundup podcast prompt (Friday episode)

These are the steering instructions passed to NotebookLM's audio hosts for the
weekly **GenAI News Roundup** — a broad, quick tour of the week, then synthesis,
opinion, and a look ahead. Before handing this file to
`notebooklm generate audio`, the run substitutes this week's **dated** item list
into `THIS WEEK'S ITEMS` and the last two roundups' chapter lists into
`ALREADY COVERED`.

- **Format:** Deep Dive · **Length:** Long
- **Sources:** every notable item from this week's daily digests (added by URL),
  dated **inside this episode's week only** — no earlier newsletter editions.

---

Create a long **GenAI News Roundup** covering this week in generative AI.
Deliberately **broad but shallow**: move briskly through every development worth
calling out with a crisp, accessible explanation, not a deep dive on any one.
Read the sources yourself and ground every fact, name, and number in them; do
not invent details.

THIS WEEK'S ITEMS (each line carries its date; cover only these):
{{WEEKLY_ITEMS}}

ALREADY COVERED in the last two roundups — do **not** re-cover these:
{{ALREADY_COVERED}}

Dates: anything dated before this week's window must be given its date and never
called "this week." Do not call any stretch of the week "quiet" without checking
the sources first — say it only if the sources bear it out.

Structure the episode in two movements.

### Part 1 — The roundup (broad)
Open with a short cold open that describes **one** real item accurately — don't
merge separate stories. Then walk the week's developments, grouped sensibly
(model releases, reasoning/agents, efficiency, multimodality, safety/alignment,
tooling). For each: what it is, who did it, the one or two numbers or facts that
make it notable, and why it matters — a sentence or three, then move on. You may
add a genuinely notable item the list missed only if you flag it as your own and
are confident it is real.

Stay precise and faithful to the sources in Part 1: **no claims about motives or
causes here** — save those for Part 2, clearly labeled as opinion. Flag
uncertainty and vendor-reported numbers as such, and say the hedge out loud
every time the item comes up. Double-check basic technical explanations (for
example, attention cost is quadratic in sequence length, and scaling laws are
power laws).

### Part 2 — Synthesis, opinion, and what's next
- **Themes.** The throughlines across the week; where the field is converging or
  diverging, and what the pattern of releases and papers says about where effort
  and money are going.
- **Opinions.** Clearly-labeled takes: what's genuinely significant vs. hype,
  what's under- or over-rated, and the likely second-order effects.
- **What's next.** Close with what's coming — concretely
  (announced-but-unshipped work, obvious next steps from this week's papers) and
  as educated speculation — distinguishing "already announced" from "informed
  guess."

Starting ideas for Part 2 (use what fits; add your own): sparse-MoE + hybrid
attention as the efficiency default; "agentic" as the default framing and its
cost for evaluation and safety; RL post-training and reasoning (returns and
alternatives); long-context / context management; open- vs. closed-weight
dynamics; safety findings (scalable oversight, reward hacking).

Tone: energetic but plain-spoken; avoid hype words and filler replies. Precise
and faithful to the sources in Part 1, with opinion and speculation kept clearly
distinct from reported facts throughout.
