# Deep-dive podcast prompt (Wednesday episode)

These are the steering instructions passed to NotebookLM's audio hosts to
produce the **weekly Deep Dive** — an in-depth episode on the single most
important innovation of the past week. The sources in the notebook are the
one-to-three articles the week's digests flagged as most important; the weekly
podcast run substitutes their exact titles into the `FEATURED ARTICLES` list
below before handing this file to `notebooklm generate audio --prompt-file`.

- **Format:** Deep Dive · **Length:** Long
- **Sources:** the featured article(s), added to the notebook by URL so you can
  read the primary source yourself.

---

Create a long, in-depth **Deep Dive** podcast about the most important GenAI
innovation of the past week. The sources in this notebook are the article(s)
listed below — **read them in full yourself and ground every claim, number, and
quote in them.** Do not invent facts, figures, or quotes; if a detail is not in
the sources, either omit it or clearly flag it as your own commentary.

FEATURED ARTICLES (this week):
{{FEATURED_ARTICLES}}

If more than one article is listed, treat them as one connected story — explain
how they relate and why, together, they are the week's defining development —
rather than covering them as unrelated items.

Walk through the material in this order:

1. **Why this is the week's biggest deal.** Open by setting the stakes: what
   changed, and why this is the development that matters most out of everything
   that happened this week. Frame it for a curious, technically-literate
   listener who follows AI but is not a specialist.
2. **Background and context.** The problem it addresses, what came before, and
   why the field cared about solving it. Give just enough history to make the
   advance legible.
3. **How it actually works.** Explain the mechanism in accessible terms: name
   the specific models, methods, architectures, datasets, and the key numbers
   and results. Define jargon as you introduce it.
4. **Why it matters / impact.** What it changes in practice — both the results
   already demonstrated and the transferable lessons or second-order effects for
   the rest of the field.
5. **Novelty — how new is this, really?** Separate a genuine advance from good
   engineering of known ideas, and say which parts are which. Compare it to the
   most relevant prior or concurrent work.
6. **Caveats, limitations, and open questions.** Expert-style commentary:
   what's unproven, what could go wrong, what to watch next, and who should
   care most. Clearly flag this section as opinion, distinct from the sources'
   own claims.

Tone: engaging and conversational, but precise and faithful to the sources.
Take the time a Long deep dive allows — go deep, don't rush — but keep every
segment earning its place. Keep opinion and analysis clearly separated from the
articles' factual claims throughout.
