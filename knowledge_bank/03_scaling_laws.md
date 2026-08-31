# Stage 3 — Scale and emergence

**Goal:** understand what happened when the field took the decoder-only
Transformer and made it *enormous* — and the science (scaling laws) and surprises
(in-context learning, "emergence") that came out of it.

---

## GPT-2: scale starts to look qualitatively different

**GPT-2** (Radford et al., 2019) was the same GPT architecture scaled up to 1.5B
parameters on a larger, cleaner web corpus (WebText). It could generate
strikingly coherent long-form text and do some tasks **zero-shot** — with no
task-specific training — just by being prompted. This hinted that a good enough
language model is implicitly a multi-task learner.

## GPT-3 and in-context learning

**GPT-3** (Brown et al., 2020, *Language Models are Few-Shot Learners*) scaled to
175B parameters and revealed the phenomenon that reoriented the field:
**in-context learning**. You can give the model a few examples of a task **in
the prompt itself** — no weight updates — and it performs the task:

```
English: sea otter    French: loutre de mer
English: cheese       French: ___
```

- **Zero-shot / one-shot / few-shot** prompting all become possible.
- The model wasn't *trained* to do this specific task; the capability *emerged*
  from scale + next-token prediction over diverse data.
- This is the birth of **prompt engineering** and of "the model as a general
  interface."

## Scaling laws: it's a science, not luck

**Kaplan et al. (2020), _Scaling Laws for Neural Language Models_** showed that
loss falls as a smooth **power law** in three quantities — parameters, data, and
compute — over many orders of magnitude. Performance became *predictable*: you
could forecast a bigger model's loss before training it. This turned "make it
bigger" from a hunch into a research program with budgets attached.

**Chinchilla** (Hoffmann et al., 2022, *Training Compute-Optimal Large Language
Models*) then corrected the recipe. Kaplan-era models were **oversized and
undertrained**. For a fixed compute budget, Chinchilla showed you should scale
parameters and training **tokens roughly in equal proportion** — a 70B model
trained on far more data beat the 175B-class models. "Chinchilla-optimal"
became the reference point, and it reframed **data**, not just parameters, as
the scarce resource. (Later practice pushes even further past compute-optimal —
training smaller models on *more* tokens because it makes them cheaper to *serve*.)

## "Emergent abilities" — and the caveat

**Wei et al. (2022), _Emergent Abilities of Large Language Models_** cataloged
capabilities (multi-step arithmetic, certain reasoning tasks) that are near-zero
in small models and jump sharply above some scale. This "emergence" framing was
influential — and then contested: **Schaeffer et al. (2023), _Are Emergent
Abilities a Mirage?_** argued some jumps are artifacts of harsh, discontinuous
metrics rather than genuine phase transitions. Hold both ideas: scale reliably
buys capability, but "sudden emergence" claims deserve a skeptical look at how
the metric was defined.

## What to take away
- Scale is not a detail; for years it was *the* dominant driver of capability.
- The same architecture + more compute/data + a next-token objective yields
  general-purpose, promptable behavior nobody explicitly trained in.
- Scaling laws made this an engineering discipline with predictable returns —
  and Chinchilla made **data** central. (Stage 7 covers where the pure-scaling
  story starts hitting limits and reasoning/RL post-training takes over as the
  new axis of progress.)

---

## Checkpoints — you should be able to explain…
- What in-context (few-shot) learning is and why it was surprising.
- What a scaling law is, in words, and what the three ingredients are.
- The Chinchilla correction: what changed about the optimal
  parameter-to-data ratio, and why data became the bottleneck.
- Why "emergent abilities" is both a real observation and a contested framing.

## Reading list
- **Primary — Brown et al. (2020), _Language Models are Few-Shot Learners_
  (GPT-3).** arXiv:2005.14165
- **Kaplan et al. (2020), _Scaling Laws for Neural Language Models_.**
  arXiv:2001.08361
- **Hoffmann et al. (2022), _Training Compute-Optimal LLMs_ (Chinchilla).**
  arXiv:2203.15556
- **Wei et al. (2022), _Emergent Abilities of Large Language Models_.**
  arXiv:2206.07682
- *Counterpoint* — Schaeffer et al. (2023), _Are Emergent Abilities a Mirage?_
  arXiv:2304.15004

## Bridge to Stage 4
Scaling ran headlong into the Transformer's costs: O(n²) attention, memory
limits, and the price of serving huge dense models. Stage 4 is the wave of
engineering — FlashAttention, Mixture-of-Experts, better positional encodings —
that made big models faster, longer-context, and cheaper.
