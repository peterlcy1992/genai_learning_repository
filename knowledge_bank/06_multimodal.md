# Stage 6 — Multimodality and generation beyond text

**Goal:** understand the parallel revolution outside of text — contrastive
vision-language pretraining (CLIP), diffusion models for image/audio/video
generation, and how modern LLMs gained eyes and ears. These ideas merge back
into the frontier systems of Stage 7.

---

## 1. CLIP — connecting images and text

**CLIP** (Radford et al., 2021, *Learning Transferable Visual Models From
Natural Language Supervision*, arXiv:2103.00020) trained an image encoder and a
text encoder **jointly** on 400M (image, caption) pairs from the web, with a
**contrastive** objective: pull the embeddings of matching image–text pairs
together and push mismatched pairs apart.

Why it mattered:
- It learned a **shared embedding space** for images and text — you can compare a
  picture to a sentence directly.
- It enabled **zero-shot image classification**: classify by comparing an image
  to text prompts like "a photo of a cat" vs. "a photo of a dog," no fine-tuning.
- That shared space became the **bridge** used by text-to-image generators and,
  later, by vision-language models to feed images into LLMs.

## 2. Diffusion models — the engine of image/video generation

The dominant paradigm for high-quality image generation is **diffusion**.

**The idea (DDPM — Ho et al., 2020, arXiv:2006.11239):**
- **Forward process:** gradually add Gaussian noise to an image over many steps
  until it's pure noise.
- **Reverse process:** train a neural network (a U-Net, later a Transformer) to
  *undo* one step of noising — to predict and remove a bit of noise.
- **Generation:** start from pure noise and run the learned denoiser step by
  step to produce a clean image.

**Latent Diffusion / Stable Diffusion** (Rombach et al., 2021, arXiv:2112.10752)
made this efficient and famous: run the diffusion process in a compressed
**latent space** (via an autoencoder) instead of raw pixels — dramatically
cheaper — and condition on text via cross-attention to a CLIP text encoder. This
is what put open text-to-image generation in everyone's hands.

**Beyond images:**
- **Classifier-free guidance** — the standard trick to make outputs follow the
  prompt more strongly.
- **DiT (Diffusion Transformers)** replaced the U-Net backbone with a
  Transformer — the basis of modern high-end image/video systems.
- **Video** (e.g. the Sora line and successors) extends diffusion to
  spacetime. **Audio** (music, speech) uses diffusion and related methods too.
- *Alternative lineages worth knowing by name:* **GANs** (the pre-diffusion
  state of the art), **VAEs**, and **autoregressive image models**.

## 3. Multimodal LLMs — giving language models perception

The frontier trend: bolt perception onto a strong LLM so it can *see* (and hear).

- **Flamingo** (DeepMind, 2022) and **BLIP-2** (2023) pioneered feeding visual
  features into a frozen LLM via lightweight bridging modules.
- **LLaVA** (2023) popularized a simple, effective open recipe: a vision encoder
  (CLIP) → a projection layer → an LLM, instruction-tuned on image–text data.
- **Frontier models are now natively multimodal** — GPT-4o, Claude, and Gemini
  accept images (and increasingly audio/video) in the same context as text,
  trained multimodally from early on rather than stitched together late.

The mental model: a modern multimodal LLM **encodes each modality into tokens/
embeddings in a shared space**, then lets the Transformer attend across all of
them at once. CLIP-style alignment is what makes those spaces compatible.

---

## Checkpoints — you should be able to explain…
- CLIP's contrastive objective and why a shared image–text embedding space is so
  useful (zero-shot classification; conditioning image generators).
- The forward/reverse process of a diffusion model in words.
- What "latent diffusion" changed to make Stable Diffusion practical.
- How a vision-language model like LLaVA connects an image encoder to an LLM.

## Reading list
- **CLIP — Radford et al. (2021).** arXiv:2103.00020
- **DDPM — Ho, Jain, Abbeel (2020).** arXiv:2006.11239
- **Latent Diffusion / Stable Diffusion — Rombach et al. (2021).**
  arXiv:2112.10752
- **LLaVA — Liu et al. (2023), _Visual Instruction Tuning_.** arXiv:2304.08485
- **Explainer — Lilian Weng, _What are Diffusion Models?_** (lilianweng.github.io)
  — the best single technical explainer.
- **Explainer — Jay Alammar, _The Illustrated Stable Diffusion_.**

## Bridge to Stage 7
You now have all the pieces: scalable Transformers, alignment, efficiency, and
multimodality. Stage 7 is where they combine into engineered **systems** —
long-context, retrieval, tool use, agents, and the reasoning-model shift that
defines the current frontier.
