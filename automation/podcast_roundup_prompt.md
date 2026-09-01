# News-roundup podcast prompt (Friday episode)

These are the steering instructions passed to NotebookLM's audio hosts to
produce the **weekly GenAI News Roundup** — a broad, quick-hit tour of
everything worth calling out from the past week, followed by synthesis, opinion,
and a look ahead. The sources in the notebook are all of the past week's digest
items (added by URL). The weekly podcast run substitutes the week's item list
into `THIS WEEK'S ITEMS` below before handing this file to
`notebooklm generate audio --prompt-file`.

- **Format:** Deep Dive · **Length:** Long
- **Sources:** every notable item from the past week's daily digests, added to
  the notebook by URL.

---

Create a long **GenAI News Roundup** podcast covering the past week in
generative AI. This episode is deliberately **broad but shallow**: move quickly
through every development worth calling out, giving each a crisp, accessible
explanation, rather than going deep on any single one. Read the sources in this
notebook yourself and ground the facts, names, and numbers in them; do not
invent details.

THIS WEEK'S ITEMS:
{{WEEKLY_ITEMS}}

Structure the episode in two movements:

### Part 1 — The roundup (broad)
Go through the week's developments, grouped sensibly (e.g. model releases,
reasoning/agents, efficiency, multimodality, safety/alignment, tooling). For
each item: what it is, who did it, the one or two numbers or facts that make it
notable, and why a listener should care — in a sentence or three, then move on.
Keep the pace brisk and the connections clear. It is fine to add a genuinely
notable item you know about that the list missed, as long as you flag it as your
own addition and are confident it is real.

### Part 2 — Synthesis, opinion, and what's next
After the tour, shift gears and step back:

- **Themes & synthesis.** What are the throughlines across this week's news?
  Where is the field converging or diverging? What does the pattern of releases
  and papers say about where effort and money are going?
- **Opinions & commentary.** Offer clearly-labeled opinions: which developments
  are genuinely significant vs. hype, what's underrated, what's overrated, and
  what the second-order effects might be. Flag these as opinion, not fact.
- **What to look forward to.** Close with what's coming next — both concretely
  (announced-but-not-yet-released work, obvious next steps from this week's
  papers) and as educated speculation about where the field is heading in the
  coming weeks and months. Distinguish the "already known / announced" from the
  "informed guess."

Some starting ideas for Part 2 (use what fits, and add your own relevant points
where you see fit — don't feel limited to this list):
- The steady convergence on sparse-MoE + hybrid-attention recipes for efficient
  frontier-class models.
- "Agentic" becoming the default framing for frontier releases, and what that
  means for evaluation, safety, and reliability.
- RL post-training and reasoning models — where the returns are, and the
  emerging alternatives to "just do more RL."
- Long-context and context-management techniques as a distinct frontier.
- Open-weight vs. closed-model dynamics, and what licensing/openness signals.
- Safety and alignment findings — scalable oversight, reward hacking, emergent
  multi-agent behavior.

Tone: energetic, curious, and opinionated in Part 2, but always precise and
faithful to the sources in Part 1. Take the time a Long episode allows to cover
the week thoroughly and then reflect, but keep it skimmable and well-paced —
this is the listener's weekly catch-up on the whole field. Keep opinion and
speculation clearly distinct from the reported facts throughout.
