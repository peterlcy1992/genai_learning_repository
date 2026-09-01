# Podcast episode covers

Per-episode square (3000×3000) cover art for **The GenAI Evolution Atlas**
podcast, one PNG per Season 2 episode. These are generated fresh for each
episode by the weekly podcast Routine using
[`../../../artifact/thumbnails/podcast_thumbs.py`](../../../artifact/thumbnails/podcast_thumbs.py)
(the mono-color editorial-print system, same as the stage thumbnails) and
rendered to PNG with headless Chromium via
[`../../../artifact/thumbnails/render.js`](../../../artifact/thumbnails/render.js).

Files are named `S<season>E<NN>-<YYYY-MM-DD>-<type>.png` (e.g.
`S2E01-2026-09-03-deep-dive.png`). Because GitHub Pages serves this repo from
`/docs`, each cover is also reachable publicly at
`https://peterlcy1992.github.io/genai_learning_repository/thumbnails/podcast/<file>.png`.
