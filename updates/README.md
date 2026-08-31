# updates/

This folder holds the **rolling log of the latest GenAI innovations**.

- [`latest.md`](latest.md) — reverse-chronological log (newest at top). The daily
  automation appends new, de-duplicated finds here and commits them.

## How it's populated
Once per day, a scheduled Routine (see [`../automation/`](../automation/)):
1. searches the web (arXiv, Hugging Face, lab blogs, newsletters) for the newest
   notable papers/releases/posts,
2. filters out anything already in `latest.md`,
3. prepends the best few as new dated entries, and
4. commits + pushes, then emails you a summary.

## Housekeeping
`latest.md` grows over time. That's fine — it's your searchable history. If it
ever gets unwieldy, archive older months into files like `archive/2026-Q3.md`
and keep `latest.md` to the recent window. (The automation is instructed to keep
appending to `latest.md`; archiving is a manual choice for you.)
