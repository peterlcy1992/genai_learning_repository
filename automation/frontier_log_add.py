#!/usr/bin/env python3
"""Append one durable, high-signal item to the Stage 8 "Frontier log".

Writes the SAME markdown entry (newest-first, deduped by URL) into both places
that hold the log, between their <!-- FRONTIER_LOG_START --> / _END --> markers:
  - knowledge_bank/08_staying_current.md   (the canonical knowledge-bank page)
  - artifact/knowledge-bank.html           (the Atlas page-8 embedded block)

After running this, run artifact/build_public_html.py so docs/index.html picks
up the Atlas change.

Usage:
  python3 automation/frontier_log_add.py DATE TITLE URL WHY STAGE
Example:
  python3 automation/frontier_log_add.py 2026-09-02 "DeepSeek-R2" \
      "https://arxiv.org/abs/XXXX.XXXXX" "Open RLVR recipe, reproduced at 3B." "Stage 5 + 7"

Only add items that clear Stage 8's bar (durable, broad, well-evidenced) — most
days add nothing. Exit 0 on add or dedup-skip; 1 on error.
"""
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
TARGETS = [REPO / "knowledge_bank" / "08_staying_current.md",
           REPO / "artifact" / "knowledge-bank.html"]
START = "<!-- FRONTIER_LOG_START -->"
END = "<!-- FRONTIER_LOG_END -->"


def update_file(path: Path, entry: str, url: str) -> str:
    if not path.exists():
        return f"skip (missing): {path.name}"
    text = path.read_text(encoding="utf-8")
    m = re.search(re.escape(START) + r"(.*?)" + re.escape(END), text, re.DOTALL)
    if not m:
        return f"skip (no markers): {path.name}"
    body = m.group(1)
    if url and url in body:
        return f"dup: {path.name}"
    # drop the placeholder line(s), keep real existing entries
    kept = [ln for ln in body.splitlines() if ln.strip() and "_No entries yet" not in ln]
    new_body = "\n" + entry + ("\n" + "\n".join(kept) if kept else "") + "\n"
    path.write_text(text[:m.start(1)] + new_body + text[m.end(1):], encoding="utf-8")
    return f"added: {path.name}"


def main(argv) -> int:
    if len(argv) < 5:
        print("usage: frontier_log_add.py DATE TITLE URL WHY STAGE", file=sys.stderr)
        return 1
    date, title, url, why, stage = argv[0], argv[1], argv[2], argv[3], argv[4]
    if "</script>" in why.lower() or "</script>" in title.lower():
        print("error: reserved token in input", file=sys.stderr)
        return 1
    entry = f"- **{date}** · **{title}** — {why} ([source]({url})) · _{stage}_"
    for path in TARGETS:
        print(update_file(path, entry, url))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
