# Stage 4 — Efficiency and better building blocks

**Goal:** understand the engineering that made large Transformers *practical* —
faster to train, cheaper to serve, and able to handle long context. This is
where "a model" starts becoming "an engineered system."

The through-line: the vanilla Transformer is **O(n²)** in sequence length and
**dense** (every parameter runs on every token). Both are expensive. This stage
is the responses to those two costs.

---

## 1. The quadratic-attention problem and its answers

Attention compares every token to every other → cost grows with the *square* of
the context length. Two broad strategies emerged:

### a) Approximate / sparse attention
Don't attend to everything. **Longformer**, **BigBird**, and **Reformer** use
sparse or local+global attention patterns to reach near-linear cost. **Linear
attention** variants (Performer, Linformer) approximate the softmax. These trade
some exactness for scalability. Useful to know, but note: they were largely
*leapfrogged* in practice by the next idea.

### b) Make *exact* attention hardware-efficient — FlashAttention
**Dao et al. (2022), _FlashAttention_** (arXiv:2205.14135) is one of the most
important systems papers in modern ML. Key insight: attention is
**memory-bandwidth bound**, not compute-bound — the bottleneck is moving the big
`n×n` attention matrix in and out of GPU high-bandwidth memory. FlashAttention
computes attention **tile-by-tile in fast on-chip SRAM without ever
materializing the full matrix** (using online softmax). Same exact result,
several times faster, far less memory. It's why long context became affordable,
and it's baked into essentially every modern training stack (FlashAttention-2/3
followed).

## 2. Mixture-of-Experts (MoE): decouple parameters from compute

A **dense** model uses all its parameters for every token. **Mixture-of-Experts**
replaces the feed-forward layer with many "expert" MLPs plus a **router** that
sends each token to only a few (e.g. 2 of 64). The result: a model with a huge
*total* parameter count but a small *active* count per token — more capacity
without proportionally more compute per token.

- Lineage: **GShard**, **Switch Transformer** (Fedus et al., 2021) →
  now central to frontier systems. **Mixtral 8x7B** made open MoE mainstream;
  **DeepSeek-V3** and most current frontier models are large MoEs.
- Trade-offs: harder to train (load balancing, routing collapse) and more
  memory to hold all experts, but far cheaper *inference* per quality.

## 3. Positional encodings that enable long context

The original sinusoidal positions (Stage 1) don't extrapolate well beyond
training length. Modern schemes fixed this and are a big reason context windows
grew from 512 tokens to hundreds of thousands or millions:

- **RoPE (Rotary Position Embedding)** — encodes position by *rotating* Q/K
  vectors by an angle proportional to position. Relative by construction and
  extrapolates gracefully (with tricks like **position interpolation** and
  **YaRN**). Used by Llama, most open models, and many closed ones.
- **ALiBi** — adds a distance-based linear bias to attention scores; simple and
  extrapolates to longer sequences than seen in training.

## 4. Serving-side efficiency (worth knowing by name)

Making a trained model cheap to *run* is its own discipline:
- **KV cache** — cache past keys/values so generation is O(n) per token, not
  O(n²) re-computation; the KV cache's *size* is now a primary memory constraint.
- **Multi-Query / Grouped-Query Attention (MQA/GQA)** — share K/V across heads to
  shrink the KV cache. Standard in modern models.
- **Quantization** (INT8/INT4, e.g. GPTQ, AWQ), **speculative decoding**, and
  **PagedAttention / vLLM** for high-throughput serving.
- **Parameter-efficient fine-tuning** — **LoRA / QLoRA** — adapt giant models by
  training tiny low-rank add-ons instead of all the weights.

---

## Checkpoints — you should be able to explain…
- Why attention is O(n²) and the two families of responses (sparse/approximate
  vs. IO-aware exact).
- The core insight of FlashAttention (memory-bandwidth bound; tile in SRAM,
  never materialize the full matrix).
- What Mixture-of-Experts changes: total vs. *active* parameters, and the
  routing trade-offs.
- Why RoPE/ALiBi replaced sinusoidal encodings and how that enabled long context.
- What the KV cache is and why GQA/quantization matter for serving cost.

## Reading list
- **FlashAttention — Dao et al. (2022).** arXiv:2205.14135 (then skim
  FlashAttention-2, arXiv:2307.08691).
- **Switch Transformer — Fedus et al. (2021).** arXiv:2101.03961 (MoE at scale).
- **RoFormer / RoPE — Su et al. (2021).** arXiv:2104.09864
- **ALiBi — Press et al. (2021), _Train Short, Test Long_.** arXiv:2108.12409
- **LoRA — Hu et al. (2021).** arXiv:2106.09685 (and QLoRA, arXiv:2305.14314).
- **Explainer** — the vLLM / PagedAttention blog and paper for the serving side.

## Bridge to Stage 5
Efficiency gave us big, fast, long-context base models — but a raw pretrained
model is a *text-completion engine*, not a helpful, safe assistant. Turning one
into the other is **alignment / post-training**: Stage 5.
