#!/usr/bin/env python3
"""Refresh the embedded "latest digest" inside the GenAI Evolution Atlas artifact.

Reads the newest digests/<YYYY-MM-DD>.md and swaps its raw markdown into the
hidden <script id="latest-digest"> block of artifact/knowledge-bank.html, between
the LATEST_DIGEST_START / LATEST_DIGEST_END markers.

Usage:  python3 artifact/refresh_embedded_digest.py
Then republish the artifact (needs an interactive session with the Artifact tool)
and commit knowledge-bank.html.

Exit codes: 0 = updated (or already current), 1 = nothing to do / error.
"""
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
HTML = REPO / "artifact" / "knowledge-bank.html"
DIGESTS = REPO / "digests"
START = "<!-- LATEST_DIGEST_START -->"
END = "<!-- LATEST_DIGEST_END -->"
DATED = re.compile(r"^\d{4}-\d{2}-\d{2}\.md$")


def newest_digest() -> Path | None:
    files = [p for p in DIGESTS.glob("*.md") if DATED.match(p.name)]
    return max(files, key=lambda p: p.name) if files else None


def main() -> int:
    if not HTML.exists():
        print(f"error: {HTML} not found", file=sys.stderr)
        return 1
    digest = newest_digest()
    if digest is None:
        print("error: no dated digests found", file=sys.stderr)
        return 1

    md = digest.read_text(encoding="utf-8").strip()
    # Safety: the raw markdown must not break out of the <script> block.
    if "</script>" in md.lower() or END in md or START in md:
        print("error: digest contains a reserved marker or </script>; aborting", file=sys.stderr)
        return 1

    html = HTML.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    if not pattern.search(html):
        print("error: markers not found in knowledge-bank.html", file=sys.stderr)
        return 1

    replacement = f"{START}\n{md}\n{END}"
    new_html = pattern.sub(lambda _m: replacement, html, count=1)
    if new_html == html:
        print(f"already current: {digest.name}")
        return 0
    HTML.write_text(new_html, encoding="utf-8")
    print(f"embedded latest digest: {digest.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
