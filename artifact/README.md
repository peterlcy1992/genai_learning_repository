# artifact/

The source for the **GenAI Evolution Atlas** — a visual, interactive companion to
this knowledge bank, published as a Claude Artifact.

**Live artifact:** https://claude.ai/code/artifact/41730737-b7b0-4055-9d7f-e0ea1cc34de9

## What it is
A single-page field guide to the evolution of generative AI: the 8 stages from
[`../knowledge_bank/`](../knowledge_bank/) with expanded write-ups, hand-drawn
diagrams (attention, the model families, scaling laws, MoE routing, the RLHF
pipeline, diffusion, the agent loop), and reference links to the primary papers
and canonical explainers — plus a **live Daily Digests** panel.

## How the live digests work
The Atlas reads your [`../digests/`](../digests/) folder **directly from GitHub**
at open time, using the `mcp` runtime capability with your GitHub connector
(`get_file_contents`). New daily digests therefore appear automatically — no
re-publish needed. It also reads [`../PROGRESS.md`](../PROGRESS.md) to mark your
current stage ("You are here"). If the GitHub connector isn't available in a
given view, the panel degrades gracefully to an embedded snapshot plus a link to
the digests folder on GitHub.

Because it reads your connected data, the artifact is **private to you** and can't
be publicly shared (a constraint of connector-backed artifacts).

## Notes for maintainers
- `knowledge-bank.html` is the **artifact body** (no `<!doctype>`/`<html>`/`<head>`/
  `<body>` — those are added at publish time), so it won't render standalone by
  double-clicking; it's the source of truth for the published artifact.
- To update the design/content: edit this file, then re-publish to the **same
  URL** (pass it as `url` to the Artifact tool, or republish the same path in the
  originating session). The digests update themselves live and do **not** require
  a republish.
- Declared capability: `mcp` → server `github`, tool `get_file_contents`.
