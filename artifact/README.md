# artifact/

The source for the **GenAI Evolution Atlas** — a visual, interactive companion to
this knowledge bank, published as a Claude Artifact.

**Live artifact:** https://claude.ai/code/artifact/41730737-b7b0-4055-9d7f-e0ea1cc34de9

## What it is
A hash-routed **multi-page** field guide to the evolution of generative AI. The
overview (`#/`) is a map of 8 gateway cards; each opens a **dedicated deep page**
(`#/stage/N`) mirroring [`../knowledge_bank/`](../knowledge_bank/) with a full
write-up (problem → mechanism with math → key concepts → checkpoints → annotated
reading list), hand-drawn diagrams (the seq2seq bottleneck, attention, the
Transformer block, the model families, scaling laws, MoE routing, the RLHF
pipeline, diffusion, the agent loop), and reference links to the primary papers
and canonical explainers — plus a **live Daily Digests** panel.

## How the digests work
The Atlas embeds the **latest daily brief** (rendered in-page) plus a prominent
**"All digests on GitHub"** link to [`../digests/`](../digests/), which always has
every day's brief. It does **not** use a runtime connector.

> We first built the digests panel to read `digests/` live via the `mcp`
> capability + the GitHub connector, but the account's GitHub connector is a
> *Web*-type connector that the artifact viewer does not expose to pages
> ("no matching connector found"), so live-fetch isn't possible here. The
> embedded-latest + GitHub-link design is the robust equivalent. To refresh the
> embedded brief, re-publish the artifact; the full archive is always live on
> GitHub regardless.

The **current-stage marker** is a click-to-set picker in the hero; the choice is
saved per-viewer in the browser (`localStorage`) and highlights that stage's
gateway card and page. No connector or repo read involved.

## Podcast thumbnails
Square (1:1, 3000×3000) cover images for the Atlas and each of the nine stages
live in [`thumbnails/`](thumbnails/), generated with the
[mono-color editorial print](https://github.com/yanliudesign/mono-color-skill)
visual system (adaptive substrate, ≤2 inks with assigned plate roles, halftone
reproduction, active negative space, one focal event). The published PNGs are in
[`../docs/thumbnails/`](../docs/thumbnails/); the site cover doubles as the Open
Graph / Twitter social-preview image (wired in by `build_public_html.py`). See
[`thumbnails/README.md`](thumbnails/README.md) for recipes and how to regenerate.

## Notes for maintainers
- `knowledge-bank.html` is the **artifact body** (no `<!doctype>`/`<html>`/`<head>`/
  `<body>` — those are added at publish time), so it won't render standalone by
  double-clicking; it's the source of truth for the published artifact.
- To update the design/content or refresh the embedded latest digest: edit this
  file, then re-publish to the **same URL** (pass it as `url` to the Artifact
  tool, or republish the same path in the originating session).
- No runtime capabilities are declared (`capabilities: {}`); the page is fully
  self-contained apart from the Google Fonts + marked.js CDN loads.
