#!/usr/bin/env python3
"""Build a standalone, publicly shareable HTML page from the Atlas source.

The Atlas source (artifact/knowledge-bank.html) is authored in "artifact body"
form — it has a <title>, <style>, content and <script>s but no <!doctype>/<html>/
<head>/<body> (those are added by the Artifact host at publish time). This script
wraps that body into a complete standalone HTML document at site/index.html, which
renders anywhere: opened locally, hosted on any static host, or served by GitHub
Pages. It is self-contained apart from the Google Fonts + marked.js CDN loads the
page already uses.

Usage:  python3 artifact/build_public_html.py
"""
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SRC = REPO / "artifact" / "knowledge-bank.html"
OUT = REPO / "docs" / "index.html"
DESCRIPTION = ("A field guide to the evolution of generative AI — 8 dedicated stage "
               "deep-dives with diagrams and reference links, plus the latest daily digest.")


def main() -> int:
    if not SRC.exists():
        print(f"error: {SRC} not found", file=sys.stderr)
        return 1
    body = SRC.read_text(encoding="utf-8")

    m = re.search(r"<title>(.*?)</title>", body, re.IGNORECASE | re.DOTALL)
    title = m.group(1).strip() if m else "GenAI Evolution Atlas"
    # Remove the title from the body so the document has exactly one, in <head>.
    body = re.sub(r"<title>.*?</title>\s*", "", body, count=1, flags=re.IGNORECASE | re.DOTALL)

    doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<meta name="description" content="{DESCRIPTION}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{DESCRIPTION}">
<meta property="og:type" content="website">
<title>{title}</title>
<style>
  html{{color-scheme:light dark}}
  body{{margin:0}}
  img{{max-width:100%}}
  [hidden]{{display:none!important}}
</style>
</head>
<body>
{body.strip()}
</body>
</html>
"""
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(doc, encoding="utf-8")
    print(f"wrote {OUT.relative_to(REPO)} ({len(doc):,} bytes) — title: {title!r}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
