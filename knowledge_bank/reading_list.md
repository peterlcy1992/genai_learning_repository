# Master reading list

Everything from the stage notes in one place, plus a few extras. **Bold** =
start here for that stage. arXiv IDs let you find the exact paper
(`arxiv.org/abs/<id>`).

Legend: 📄 paper · ✍️ blog/explainer · 🎥 video/course

---

## Stage 0 — Foundations
- 📄 **Bahdanau, Cho, Bengio (2014)** — *Neural Machine Translation by Jointly
  Learning to Align and Translate* — arXiv:1409.0473 (attention is born)
- 📄 Sutskever, Vinyals, Le (2014) — *Sequence to Sequence Learning* — arXiv:1409.3215
- 📄 Mikolov et al. (2013) — *word2vec* — arXiv:1301.3781
- ✍️ **Christopher Olah** — *Understanding LSTM Networks* (colah's blog)
- ✍️ Jay Alammar — *Visualizing A Neural Machine Translation Model (Seq2seq with
  Attention)*

## Stage 1 — The Transformer
- 📄 **Vaswani et al. (2017)** — *Attention Is All You Need* — arXiv:1706.03762
- ✍️ **Jay Alammar** — *The Illustrated Transformer*
- ✍️ *The Annotated Transformer* (Harvard NLP) — paper as runnable code
- 🎥 **Andrej Karpathy** — *Let's build GPT: from scratch, in code, spelled out*
  + the `nanoGPT` repo

## Stage 2 — The pretraining era
- 📄 **Radford et al. (2018)** — *Improving Language Understanding by Generative
  Pre-Training* (GPT-1)
- 📄 **Devlin et al. (2018)** — *BERT* — arXiv:1810.04805
- 📄 Peters et al. (2018) — *ELMo* — arXiv:1802.05365
- 📄 Raffel et al. (2019) — *T5* — arXiv:1910.10683
- ✍️ Jay Alammar — *The Illustrated BERT, ELMo, and co.*

## Stage 3 — Scale and emergence
- 📄 **Brown et al. (2020)** — *Language Models are Few-Shot Learners* (GPT-3) —
  arXiv:2005.14165
- 📄 Kaplan et al. (2020) — *Scaling Laws for Neural Language Models* — arXiv:2001.08361
- 📄 **Hoffmann et al. (2022)** — *Training Compute-Optimal LLMs* (Chinchilla) —
  arXiv:2203.15556
- 📄 Wei et al. (2022) — *Emergent Abilities of LLMs* — arXiv:2206.07682
- 📄 Schaeffer et al. (2023) — *Are Emergent Abilities a Mirage?* — arXiv:2304.15004

## Stage 4 — Efficiency & building blocks
- 📄 **Dao et al. (2022)** — *FlashAttention* — arXiv:2205.14135 (+ FlashAttention-2, arXiv:2307.08691)
- 📄 Fedus et al. (2021) — *Switch Transformer* (MoE) — arXiv:2101.03961
- 📄 Su et al. (2021) — *RoFormer / RoPE* — arXiv:2104.09864
- 📄 Press et al. (2021) — *ALiBi* — arXiv:2108.12409
- 📄 Hu et al. (2021) — *LoRA* — arXiv:2106.09685 (+ QLoRA, arXiv:2305.14314)
- ✍️ vLLM / *PagedAttention* paper + blog (serving)

## Stage 5 — Alignment & post-training
- 📄 **Ouyang et al. (2022)** — *InstructGPT* — arXiv:2203.02155
- 📄 Christiano et al. (2017) — *Deep RL from Human Preferences* — arXiv:1706.03741
- 📄 **Rafailov et al. (2023)** — *Direct Preference Optimization (DPO)* — arXiv:2305.18290
- 📄 Bai et al. (2022) — *Constitutional AI* — arXiv:2212.08073
- ✍️ Hugging Face — *Illustrating RLHF*

## Stage 6 — Multimodality
- 📄 **Radford et al. (2021)** — *CLIP* — arXiv:2103.00020
- 📄 Ho, Jain, Abbeel (2020) — *DDPM* — arXiv:2006.11239
- 📄 **Rombach et al. (2021)** — *Latent Diffusion / Stable Diffusion* — arXiv:2112.10752
- 📄 Liu et al. (2023) — *LLaVA (Visual Instruction Tuning)* — arXiv:2304.08485
- ✍️ **Lilian Weng** — *What are Diffusion Models?*
- ✍️ Jay Alammar — *The Illustrated Stable Diffusion*

## Stage 7 — Frontier systems
- 📄 Lewis et al. (2020) — *RAG* — arXiv:2005.11401
- 📄 **Wei et al. (2022)** — *Chain-of-Thought Prompting* — arXiv:2201.11903
- 📄 Yao et al. (2022) — *ReAct* — arXiv:2210.03629
- 📄 Schick et al. (2023) — *Toolformer* — arXiv:2302.04761
- 📄 **DeepSeek-AI (2025)** — *DeepSeek-R1* — arXiv:2501.12948
- 📄 OpenAI (2023) — *GPT-4 Technical Report* — arXiv:2303.08774
- 📄 Touvron et al. (2023) — *Llama / Llama 2*
- ✍️ **Lilian Weng** — *LLM Powered Autonomous Agents*
- ✍️ *Model Context Protocol* docs (Anthropic)

---

## Stage 8 — Staying current
No fixed papers — the "reading" is your own live stream, worked on a cadence.
- 📄 This repo's [`updates/latest.md`](../updates/latest.md) and [`digests/`](../digests/) — the raw material you curate.
- ✍️ **Nathan Lambert** — *Interconnects* — a model of a good weekly filter (selects and contextualises).
- ✍️ **Jack Clark** — *Import AI* — another curation exemplar.
- 🧭 The refresh-loop method itself → [`08_staying_current.md`](08_staying_current.md), then the ongoing sources below.

## Ongoing sources (for staying current — Stage 8)

**Where the daily automation looks, and where you should browse too:**

- **arXiv** — cs.CL, cs.LG, cs.AI (new submissions); *arxiv-sanity* / *alphaXiv*
  for filtering.
- **Hugging Face** — Daily Papers, model releases, blog.
- **Lab blogs** — OpenAI, Anthropic, Google DeepMind, Meta AI, Mistral,
  DeepSeek, Qwen.
- **Engineering/explainer blogs** — Lilian Weng, Sebastian Raschka (*Ahead of
  AI*), Jay Alammar, The Gradient, Answer.AI.
- **Newsletters** — *Import AI* (Jack Clark), *The Batch* (DeepLearning.AI),
  *Ahead of AI*, *Interconnects* (Nathan Lambert).
- **Community** — r/MachineLearning, r/LocalLLaMA, Papers with Code, AI
  researchers on X.

## Courses (optional, for depth)
- 🎥 Stanford **CS224N** (NLP with Deep Learning) — the canonical course.
- 🎥 Stanford **CS336** (Language Modeling from Scratch) — build an LLM end to end.
- 🎥 Andrej Karpathy — *Neural Networks: Zero to Hero* (incl. building GPT).
- 🎥 Hugging Face **NLP Course** / **LLM Course** — practical and free.
