# Stage 1 — The Transformer

**Primary text:** Vaswani et al. (2017), *Attention Is All You Need*
(arXiv:1706.03762). This is the paper the entire field pivots on. Read the deep
dive below, then read the paper once quickly and once slowly.

---

## The core bet

Recurrence made sequence models slow (Stage 0). The Transformer's bet: **replace
recurrence entirely with attention.** No time-stepping, so the whole sequence is
processed in parallel — which is exactly what GPUs want, and what makes training
at massive scale possible. Everything else in this course follows from that
unlock.

## The building blocks

### 1. Scaled dot-product attention
Every token is projected into three vectors: a **query (Q)**, a **key (K)**, and
a **value (V)**. To compute a token's new representation:

```
Attention(Q, K, V) = softmax( QKᵀ / √dₖ ) · V
```

- `QKᵀ` scores how much each token should attend to every other token (dot
  product = similarity).
- Divide by `√dₖ` (the "scaled" part) to keep the dot products from growing too
  large and pushing softmax into tiny-gradient regions.
- `softmax` turns scores into weights that sum to 1.
- Multiply by `V` to get a weighted average of values.

It's the exact query/score/softmax/weighted-sum pattern from Stage 0 — now
computed for *every token attending to every other token* in one matrix
multiply. This is **self-attention**: the sequence attends to itself.

### 2. Multi-head attention
Do the above `h` times in parallel with different learned projections
("heads"), then concatenate. Each head can specialize — one tracks syntax,
another tracks coreference, etc. Multiple **representation subspaces** at once.

### 3. Positional encoding
Attention is **permutation-invariant** — it has no built-in notion of order.
Since we threw away recurrence (which encoded order implicitly), we must *inject*
position. The original paper adds fixed **sinusoidal** position vectors to the
embeddings. (Stage 4 covers the modern successors — RoPE and ALiBi — that made
long context practical.)

### 4. The rest of the block
Each layer also has:
- a **position-wise feed-forward network** (an MLP applied to each token),
- **residual connections** (add the input back — helps gradients flow),
- **layer normalization**.

Stack `N` of these blocks and you have an encoder (or a decoder).

## The full architecture

The original is an **encoder–decoder** built for translation:
- The **encoder** reads the source with bidirectional self-attention.
- The **decoder** generates the target one token at a time, using **masked**
  self-attention (a token can't attend to future tokens — that would be
  cheating at next-token prediction) plus **cross-attention** into the encoder's
  output.

This encoder / decoder distinction matters enormously for Stage 2, where the
field splits into three families:
- **Encoder-only** (BERT) — great for understanding/classification.
- **Decoder-only** (GPT) — great for generation; **this family wins** and
  becomes the template for essentially every modern LLM.
- **Encoder–decoder** (T5, original Transformer) — great for seq2seq tasks like
  translation and summarization.

## Why it mattered
1. **Parallelism → scale.** Training throughput no longer bottlenecked by
   sequence length dependencies.
2. **Better long-range modeling.** Any token can attend directly to any other in
   one step (path length O(1) vs. O(n) for RNNs).
3. **A uniform, scalable primitive.** The same block, stacked and enlarged, kept
   getting better as you added data and parameters (Stage 3).

## The one caveat (sets up Stage 4)
Self-attention is **O(n²)** in sequence length — every token attends to every
other. Doubling context quadruples the attention compute and memory. Much of
Stage 4 is the field's long war on this quadratic cost.

---

## Checkpoints — you should be able to explain…
- What Q, K, and V are and how scaled dot-product attention combines them.
- Why we divide by √dₖ.
- Why positional encodings are necessary at all.
- The difference between the encoder, the decoder, and why decoder-only models
  came to dominate.
- Why the architecture is O(n²) in sequence length.

## Reading list
- **Primary — Vaswani et al. (2017), _Attention Is All You Need_.**
  arXiv:1706.03762
- **Explainer — Jay Alammar, _The Illustrated Transformer_.** The single best
  visual walkthrough; read it alongside the paper.
- **Explainer — _The Annotated Transformer_ (Harvard NLP).** The paper
  reimplemented line-by-line in PyTorch — invaluable if you learn by code.
- **Deep dive — Andrej Karpathy, _Let's build GPT: from scratch, in code,
  spelled out_** (video) and the `nanoGPT` repo. Builds a working decoder-only
  Transformer; the best way to make it concrete.

## Bridge to Stage 2
The Transformer is an architecture, not yet a "language model you talk to." The
next leap was learning that you could **pretrain** one of these on a mountain of
unlabeled text and then transfer it to many tasks — the move that created GPT
and BERT.
