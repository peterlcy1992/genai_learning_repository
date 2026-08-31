# Stage 7 — Frontier systems and the engineered stack

**Goal:** understand how the field moved from "a model" to "an engineered
system," and grasp the current frontier: long context, retrieval, tool use,
agents, and — the defining shift of 2024–2025 — **reasoning ("thinking")
models** trained with reinforcement learning on verifiable rewards.

This is the living edge of the field. The deep-dive below is your map;
[`updates/latest.md`](../updates/latest.md) and the daily email keep it current.

---

## 1. The model landscape (as of early 2026)

- **Closed frontier:** OpenAI's GPT-4 → GPT-4o (natively multimodal) → the
  **o1/o3 reasoning line** → **GPT-5**; Anthropic's **Claude** family (Opus /
  Sonnet / Haiku, with extended "thinking"); Google's **Gemini** (long context,
  multimodal). Google's **Gemini** notably pushed context windows into the
  **1M+ token** range.
- **Open-weight ecosystem:** Meta's **Llama** series made strong open models
  mainstream; **Mistral / Mixtral** (open MoE); **DeepSeek** (**V3**, a large
  efficient MoE, and **R1**, an open reasoning model); **Qwen**, **Gemma**, and
  others. Open weights closed much of the gap with closed frontier models.

The architectural common denominator is still a decoder-only Transformer — now
usually a **large Mixture-of-Experts** (Stage 4), multimodal (Stage 6), aligned
via post-training (Stage 5), with long context (RoPE + interpolation, Stage 4).
The *deltas* that define the frontier are mostly in **post-training and
inference-time systems**, below.

## 2. Long context

Context windows grew from 2K (GPT-3) to **128K–1M+ tokens**. Enablers: RoPE +
position interpolation / YaRN, FlashAttention, GQA, and ring/sequence
parallelism. It changes what's possible (whole codebases, books, long
transcripts in one prompt) — but "context rot" (degraded use of the middle of
long contexts, the "lost in the middle" effect) means long context complements
rather than replaces retrieval.

## 3. Retrieval-Augmented Generation (RAG)

Rather than bake all knowledge into weights, **retrieve** relevant documents at
query time and put them in the context. Pipeline: embed your corpus into a
**vector database** → embed the query → fetch nearest chunks → feed them to the
LLM to ground its answer. Benefits: fresh/proprietary knowledge, fewer
hallucinations, citations. It remains the standard pattern for
knowledge-intensive apps, now often combined with long context and reranking.
Origin: **Lewis et al. (2020), RAG** (arXiv:2005.11401).

## 4. Tool use / function calling

LLMs are bad at arithmetic, can't see live data, and can't act on the world — so
let them **call tools**. The model emits a structured call (e.g. JSON) to a
function — search, calculator, code interpreter, an API — receives the result,
and continues. **Toolformer** (2023) showed models can learn to do this.
**Model Context Protocol (MCP)** (Anthropic, 2024) emerged as an open standard
for connecting models to tools/data sources. Tool use turns a text predictor
into something that can *do* things — the foundation of agents.

## 5. Agents

An **agent** is an LLM in a loop: it plans, calls tools, observes results, and
iterates toward a goal with some autonomy. Building blocks:
- **ReAct** (Yao et al., 2022) — interleave reasoning traces and actions.
- **Chain-of-Thought** (Wei et al., 2022) — "let's think step by step" elicits
  multi-step reasoning; the conceptual seed of reasoning models.
- **Memory, planning, reflection**, and multi-agent orchestration.
Agentic coding assistants (like Claude Code itself), computer-use agents, and
research agents are the fastest-moving application area. The hard problems are
reliability, error recovery, and long-horizon coherence.

## 6. The reasoning-model shift (the big recent leap)

Through ~2023, progress came mostly from **scaling pretraining**. The
2024–2025 shift moved a major axis of progress to **inference-time compute** and
**RL on verifiable rewards**:

- **OpenAI o1 / o3** (2024–2025) are trained to produce long internal
  **chains of thought** before answering, and to spend more *test-time compute*
  on harder problems. Accuracy on math/coding/science jumped sharply.
- **DeepSeek-R1** (2025, arXiv:2501.12948) showed **openly** that
  large-scale **RL with verifiable rewards (RLVR)** — rewarding *correct final
  answers* on math/code, with formats like GRPO — can induce sophisticated
  reasoning (self-checking, backtracking) with minimal supervised data. Its
  open recipe was a landmark.
- The new scaling story: **"test-time / inference-time scaling"** — let the model
  think longer — is a distinct lever from pretraining scale, and it reopened
  rapid progress just as pretraining returns were flattening.

Frontier assistants now expose this as **"extended thinking"** / reasoning modes.
Expect much of the near-term news in [`updates/latest.md`](../updates/latest.md)
to be about reasoning, agents, RL post-training, efficiency, and multimodality.

## 7. Cross-cutting themes to keep watching
- **Efficiency & small models** — distillation, quantization, and strong small
  models (Phi, Gemma, small Qwen) running on-device.
- **Data** — the scarce resource; synthetic data, data quality, and filtering.
- **Evaluation** — benchmarks saturate fast (MMLU → GPQA → frontier math/coding/
  agentic evals like SWE-bench); "evals are the new unit tests."
- **Safety & alignment at scale** — interpretability, oversight, jailbreak
  robustness, and governance.

---

## Checkpoints — you should be able to explain…
- Why the frontier is now defined more by post-training + inference systems than
  by raw architecture changes.
- What RAG is and when you'd reach for it vs. long context vs. fine-tuning.
- How tool use and the agent loop turn an LLM into something that acts.
- What changed with reasoning models: test-time compute and RL on verifiable
  rewards (RLVR), and why DeepSeek-R1 was significant.

## Reading list
- **RAG — Lewis et al. (2020).** arXiv:2005.11401
- **Chain-of-Thought — Wei et al. (2022).** arXiv:2201.11903
- **ReAct — Yao et al. (2022).** arXiv:2210.03629
- **Toolformer — Schick et al. (2023).** arXiv:2302.04761
- **DeepSeek-R1 (2025).** arXiv:2501.12948 — the open reasoning-model recipe.
- **GPT-4 Technical Report (2023).** arXiv:2303.08774
- **Llama papers** (Touvron et al., 2023) for the open-model reference design.
- **Surveys/explainers** — Lilian Weng's *LLM Powered Autonomous Agents*; the
  *Model Context Protocol* docs; Sebastian Raschka's and Anthropic's engineering
  blogs for reasoning/agents.

## You've reached the frontier
From here, learning is continuous, not staged. Keep
[`PROGRESS.md`](../PROGRESS.md) at Stage 7, read the daily updates, and go deep
on whichever thread (agents, reasoning, efficiency, multimodality, safety) pulls
you. The [`updates/`](../updates/) log is now your primary curriculum.
