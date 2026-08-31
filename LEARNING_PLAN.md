# The Generative AI Learning Plan

A structured path through the evolution of generative AI, from the ideas that
predate the Transformer to the frontier systems of today. The goal is not to
memorize architectures but to understand **why each change happened** — what
problem it solved, and what it made possible next.

Each stage has:
- a **deep-dive note** in [`knowledge_bank/`](knowledge_bank/) explaining the
  key ideas in plain language,
- a **curated reading list** (the seminal paper(s) plus one or two accessible
  explainers), and
- **checkpoints** — questions you should be able to answer before moving on.

> **How to pace yourself:** aim for one stage every 1–2 weeks if you're doing
> this alongside a job. Read the deep-dive note first (30–60 min), then the
> primary paper (skim → careful reread), then an explainer to consolidate. Don't
> chase completeness — chase the *intuition* behind each leap. Update
> [`PROGRESS.md`](PROGRESS.md) as you finish each stage.

---

## The arc at a glance

```
Pre-2017   RNNs / LSTMs / seq2seq / attention-as-an-add-on
  2017     ── Attention Is All You Need ──  the Transformer
  2018     Pretraining + transfer: ELMo, GPT-1, BERT
  2019-20  Scale: GPT-2, GPT-3, scaling laws, in-context learning
  2020-22  Efficiency & better building blocks: MoE, FlashAttention, RoPE
  2022     Alignment: InstructGPT / RLHF, then DPO, Constitutional AI
  2021-23  Multimodality: CLIP, diffusion, vision-language models
  2023-26  Frontier systems: GPT-4/5, Claude, Gemini, Llama; long context,
           retrieval, tool use, agents, and reasoning ("thinking") models
```

---

## The stages

### Stage 0 — Foundations: before the Transformer
*Why "attention" was invented in the first place.*
Sequence modeling with RNNs/LSTMs, the seq2seq encoder–decoder, the
information-bottleneck problem, and attention as a fix (Bahdanau 2014). Word
embeddings (word2vec, GloVe) and what "distributed representations" buys you.
→ [`knowledge_bank/00_foundations.md`](knowledge_bank/00_foundations.md)

### Stage 1 — The Transformer
*Attention Is All You Need (2017).*
Self-attention, multi-head attention, positional encodings, the
encoder–decoder stack, and why removing recurrence unlocked parallel training
at scale. This is the pivot the whole field turns on.
→ [`knowledge_bank/01_transformer.md`](knowledge_bank/01_transformer.md)

### Stage 2 — The pretraining era
*Transfer learning arrives in NLP.*
ELMo, GPT-1 (decoder-only, generative pretraining), and BERT (encoder-only,
masked language modeling). The split between encoder, decoder, and
encoder–decoder families and what each is good at.
→ [`knowledge_bank/02_pretraining_era.md`](knowledge_bank/02_pretraining_era.md)

### Stage 3 — Scale and emergence
*GPT-2 → GPT-3, scaling laws, in-context learning.*
What happens when you make the same architecture much bigger: few-shot / prompt
learning, the Kaplan and Chinchilla scaling laws, and the debate over "emergent
abilities."
→ [`knowledge_bank/03_scaling_laws.md`](knowledge_bank/03_scaling_laws.md)

### Stage 4 — Efficiency and better building blocks
*Making Transformers faster, longer, and cheaper.*
The quadratic-attention problem and responses to it: sparse/linear attention,
FlashAttention (IO-aware exact attention), Mixture-of-Experts, and modern
positional schemes (RoPE, ALiBi) that enable long context.
→ [`knowledge_bank/04_efficiency_architecture.md`](knowledge_bank/04_efficiency_architecture.md)

### Stage 5 — Alignment and post-training
*Turning a next-token predictor into a helpful assistant.*
Instruction tuning, RLHF (InstructGPT), reward models, and the newer, simpler
alternatives — DPO and friends — plus Constitutional AI / RLAIF. Why
post-training, not pretraining, defines the assistant you actually talk to.
→ [`knowledge_bank/05_alignment_rlhf.md`](knowledge_bank/05_alignment_rlhf.md)

### Stage 6 — Multimodality and generation beyond text
*Images, audio, video, and joint vision–language.*
CLIP and contrastive pretraining, diffusion models (DDPM → latent diffusion →
Stable Diffusion), and how vision-language models bolt perception onto LLMs.
→ [`knowledge_bank/06_multimodal.md`](knowledge_bank/06_multimodal.md)

### Stage 7 — Frontier systems and the engineered stack
*From "a model" to "a system."*
GPT-4/4o/5, Claude, Gemini, Llama and the open-weight ecosystem; long context,
retrieval-augmented generation (RAG), tool use / function calling, agents, and
the shift to **reasoning / "thinking" models** trained with RL on verifiable
rewards (o1/o3-style, and the DeepSeek-R1 line). This is the current frontier —
and where [`updates/latest.md`](updates/latest.md) keeps you moving.
→ [`knowledge_bank/07_frontier_systems.md`](knowledge_bank/07_frontier_systems.md)

---

## Supporting material
- **Glossary** of the terms you'll keep meeting → [`knowledge_bank/glossary.md`](knowledge_bank/glossary.md)
- **Master reading list**, everything in one place, grouped by stage →
  [`knowledge_bank/reading_list.md`](knowledge_bank/reading_list.md)

---

## A note on prerequisites
You'll get the most from this if you're comfortable with: basic linear algebra
(vectors, matrix multiplication), the idea of gradient-descent training, and
softmax/probabilities. If any of that is rusty, the Stage 0 note points to quick
refreshers. You do **not** need to be able to derive backprop by hand.
