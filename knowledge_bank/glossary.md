# Glossary

Quick, plain-language definitions of terms you'll meet repeatedly. Grouped
roughly by stage. Not exhaustive — a companion to the deep-dive notes.

## Foundations & architecture
- **Token** — the unit a model reads/generates (a word piece, via a tokenizer
  like BPE). Models predict tokens, not characters or words.
- **Embedding** — a dense vector representing a token/word/image where geometry
  encodes meaning.
- **RNN / LSTM / GRU** — recurrent networks that process sequences step by step;
  the pre-Transformer standard. Sequential (slow) and weak at long range.
- **seq2seq** — encoder→decoder architecture that maps one sequence to another.
- **Attention** — a learned weighted lookup: score candidates against a query,
  softmax to weights, return the weighted sum of values.
- **Self-attention** — attention where a sequence attends to itself.
- **Q / K / V (Query / Key / Value)** — the three projections each token gets;
  attention = softmax(QKᵀ/√dₖ)·V.
- **Multi-head attention** — several attention computations in parallel, each in
  its own subspace, concatenated.
- **Positional encoding** — information about token order injected into the model
  (sinusoidal → **RoPE**, **ALiBi**).
- **Transformer** — the attention-based architecture from *Attention Is All You
  Need* (2017); the backbone of modern GenAI.
- **Encoder-only / Decoder-only / Encoder–decoder** — the three model families
  (BERT / GPT / T5). Decoder-only won for general assistants.
- **Residual connection / LayerNorm** — stabilizers that let deep stacks train.

## Training & scaling
- **Pretraining** — self-supervised training on huge unlabeled data (e.g.
  next-token prediction).
- **Self-supervised learning** — the data supplies its own labels (predict the
  next/masked token).
- **Fine-tuning** — further training of a pretrained model on a narrower task.
- **Autoregressive / Causal LM** — generate the next token from prior tokens
  (GPT-style).
- **Masked LM (MLM)** — predict hidden tokens from both sides (BERT-style).
- **In-context learning** — the model performs a task from examples in the
  prompt, with no weight updates.
- **Zero-/one-/few-shot** — how many in-prompt examples you give.
- **Scaling laws** — power-law relationship of loss to parameters, data, and
  compute.
- **Chinchilla-optimal** — the compute-optimal parameter:token ratio; scale data
  and parameters together (data is the scarce resource).
- **Emergent abilities** — capabilities that appear sharply with scale (a
  contested framing — partly a metric artifact).

## Efficiency
- **O(n²) attention** — attention cost grows with the square of context length.
- **FlashAttention** — IO-aware exact attention; tiles computation in fast SRAM,
  never materializes the full matrix.
- **Mixture-of-Experts (MoE)** — many expert MLPs + a router; huge *total* but
  small *active* parameters per token.
- **RoPE / ALiBi** — modern positional schemes enabling long-context
  extrapolation.
- **KV cache** — cached past keys/values so generation is O(n) per token; a major
  memory cost.
- **MQA / GQA** — share K/V across heads to shrink the KV cache.
- **Quantization** — lower-precision weights (INT8/INT4) for cheaper inference.
- **LoRA / QLoRA** — parameter-efficient fine-tuning via small low-rank adapters.
- **Distillation** — train a small model to mimic a big one.
- **Speculative decoding** — a small model drafts tokens a big model verifies, to
  speed generation.

## Alignment & post-training
- **Post-training** — everything after pretraining (SFT, RLHF, DPO…) that turns a
  base model into an assistant.
- **SFT / Instruction tuning** — supervised fine-tuning on (instruction,
  response) pairs.
- **RLHF** — Reinforcement Learning from Human Feedback: SFT → reward model →
  RL (PPO) against human preferences.
- **Reward model (RM)** — model trained to predict human preference as a scalar.
- **PPO** — the RL algorithm classically used in RLHF.
- **KL penalty** — keeps the RL-tuned policy close to the reference model.
- **DPO** — Direct Preference Optimization; optimizes preferences with a simple
  loss, no reward model or RL loop.
- **RLAIF / Constitutional AI** — feedback from an AI judge guided by written
  principles, replacing much human labeling.
- **RLVR** — RL from Verifiable Rewards; reward correct answers on checkable
  tasks (math/code). Engine of reasoning models.
- **Reward hacking / specification gaming** — satisfying the reward's letter, not
  its intent.
- **Sycophancy** — telling users what they want to hear (an RLHF side-effect).
- **HHH** — Helpful, Harmless, Honest.

## Multimodal & generation
- **CLIP** — contrastively trains image+text encoders into a shared embedding
  space.
- **Contrastive learning** — pull matching pairs together, push mismatches apart.
- **Diffusion model** — generate by learning to reverse a gradual noising
  process.
- **Latent diffusion** — run diffusion in a compressed latent space (Stable
  Diffusion).
- **Classifier-free guidance** — strengthens prompt adherence in diffusion.
- **U-Net / DiT** — diffusion backbones (convolutional U-Net → Diffusion
  Transformer).
- **Multimodal LLM / VLM** — an LLM that also takes images (and audio/video),
  e.g. LLaVA, GPT-4o, Gemini.

## Frontier systems
- **Long context** — very large context windows (128K–1M+ tokens).
- **"Lost in the middle" / context rot** — degraded use of information in the
  middle of long contexts.
- **RAG** — Retrieval-Augmented Generation; fetch relevant docs at query time to
  ground answers.
- **Vector database** — stores embeddings for nearest-neighbor retrieval.
- **Tool use / function calling** — the model invokes external functions/APIs.
- **MCP (Model Context Protocol)** — open standard for connecting models to
  tools and data.
- **Agent** — an LLM in a plan→act→observe loop with tools and some autonomy.
- **ReAct** — interleaving reasoning and actions.
- **Chain-of-Thought (CoT)** — step-by-step reasoning elicited in the output.
- **Reasoning / "thinking" model** — trained to reason at length before
  answering (o1/o3, DeepSeek-R1, extended-thinking modes).
- **Test-time / inference-time scaling** — spending more compute *at inference*
  (thinking longer) to improve answers.
- **Hallucination** — confident, fluent, but false output.
- **Eval / benchmark** — standardized capability tests (MMLU, GPQA, SWE-bench,
  etc.).
