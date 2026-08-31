# Stage 2 — The pretraining era

**Goal:** understand the idea that made the Transformer explode in usefulness —
**pretrain once on huge unlabeled text, then transfer** — and learn the three
model families it produced.

---

## The big idea: transfer learning comes to NLP

Before 2018, most NLP models were trained from scratch on each task's (small)
labeled dataset. The breakthrough insight: train a Transformer on a **massive
corpus of raw text** using a *self-supervised* objective (no human labels — the
text supervises itself), so it learns general language structure. Then
**fine-tune** that pretrained model on your specific task with comparatively
little labeled data. This is the recipe that still underlies everything today
(pretraining → post-training).

There are two natural self-supervised objectives, and they define two families.

## Family 1 — Decoder-only, autoregressive: GPT

**GPT-1** (Radford et al., 2018, *Improving Language Understanding by Generative
Pre-Training*) uses the Transformer **decoder** and trains it on plain
**language modeling**: predict the next token given all previous tokens. Because
it only ever looks left (causal masking), it's naturally **generative** — you
can sample from it to produce text.

- Objective: `maximize P(tokenₜ | token₁ … tokenₜ₋₁)`
- Strength: generation, and — as Stage 3 reveals — *in-context learning*.
- This family (decoder-only, autoregressive) becomes the backbone of GPT-2/3/4,
  Claude, Llama, Gemini, and essentially every modern chat LLM.

## Family 2 — Encoder-only, masked: BERT

**BERT** (Devlin et al., 2018, *BERT: Pre-training of Deep Bidirectional
Transformers*) uses the Transformer **encoder** and a different objective:
**masked language modeling (MLM)**. Randomly hide ~15% of tokens and train the
model to fill them in using context from **both directions** at once.

- Objective: predict masked tokens from left *and* right context.
- Strength: rich **bidirectional understanding** — excellent for
  classification, named-entity recognition, retrieval, sentence embeddings.
- Weakness: not generative (it fills blanks, it doesn't continue text).

**ELMo** (Peters et al., 2018) is the transitional figure: it produced
*contextual* word embeddings from a bi-directional LSTM and showed that
context-dependent representations beat static word2vec/GloVe vectors — pointing
the way, just before BERT did it with Transformers.

## Family 3 — Encoder–decoder: T5, BART

**T5** (Raffel et al., 2019, *Text-to-Text Transfer Transformer*) reframed
*every* NLP task as text-in → text-out ("translate English to German: …",
"summarize: …"). **BART** combined a bidirectional encoder with an
autoregressive decoder. This family shines on true sequence-to-sequence tasks.

## The mental model to keep

| Family | Example | Objective | Best at |
|--------|---------|-----------|---------|
| Decoder-only | GPT | Next-token prediction (causal) | **Generation**, few-shot, chat |
| Encoder-only | BERT | Masked LM (bidirectional) | Understanding, classification, embeddings |
| Encoder–decoder | T5, BART | Denoising / span corruption | Translation, summarization |

The field ultimately bet on **decoder-only** for general-purpose assistants,
because a single next-token objective scales beautifully and, at scale, absorbs
"understanding" tasks too (you can just *ask* the model to classify).

---

## Checkpoints — you should be able to explain…
- What "self-supervised pretraining then fine-tuning" means and why it was such
  a leap.
- The difference between GPT's causal LM objective and BERT's masked LM
  objective, and what each is good at.
- Why decoder-only models are naturally generative and encoder-only models are
  not.
- Where T5/encoder–decoder models fit.

## Reading list
- **Primary — Radford et al. (2018), _Improving Language Understanding by
  Generative Pre-Training_ (GPT-1).** OpenAI.
- **Primary — Devlin et al. (2018), _BERT_.** arXiv:1810.04805
- **Peters et al. (2018), _Deep contextualized word representations_ (ELMo).**
  arXiv:1802.05365
- **Raffel et al. (2019), _Exploring the Limits of Transfer Learning with a
  Unified Text-to-Text Transformer_ (T5).** arXiv:1910.10683
- **Explainer — Jay Alammar, _The Illustrated BERT, ELMo, and co._**

## Bridge to Stage 3
GPT-1 was modest. The obvious next experiment was: *keep the architecture, make
it much, much bigger, and feed it far more data.* The results (GPT-2, then
GPT-3) were surprising enough to reorganize the whole industry — and gave us
scaling laws and in-context learning.
