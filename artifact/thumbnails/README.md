# Podcast thumbnails — GenAI Evolution Atlas

Square (1:1) cover images for the Atlas as a whole and for each of its nine
learning stages, sized **3000 × 3000 px** (above the 1400 px minimum and at the
3000 px size recommended by Apple Podcasts / Spotify).

The published PNGs live in [`../../docs/thumbnails/`](../../docs/thumbnails/) so
they are served by GitHub Pages alongside the site; the site cover
(`00-atlas-site.png`) is also wired in as the Open Graph / Twitter social-preview
image by [`../build_public_html.py`](../build_public_html.py).

## Visual system

Generated with the **mono-color editorial print** skill
([yanliudesign/mono-color-skill](https://github.com/yanliudesign/mono-color-skill)):
an adaptive neutral substrate, **no more than two printing inks** with a distinct
role assigned to each plate, halftone/mechanical reproduction (not a color wash),
25–55 % active negative space, one clearly identifiable focal event per page, a
single manual-gesture family (here, a print registration mark), and terse
display typography.

This environment has no diffusion image-generation model, so — per the skill's
prompt-only fallback — each poster is composed deterministically as SVG (honoring
the same recipe manifest) and rendered to PNG with headless Chromium, rather than
diffusion-generated. The series is held together by a shared microtype line
(`GENAI EVOLUTION ATLAS`), a stage index, the registration mark, and consistent
ink/plate logic; distinctiveness comes from a subject-appropriate palette,
layout family, type voice, and focal metaphor per stage.

## Recipes

| File | Stage | Mode | Inks (plate roles) | Substrate | Layout | Focal event |
|------|-------|------|--------------------|-----------|--------|-------------|
| `00-atlas-site.png` | Atlas (site cover) | complementary duotone | Cobalt `#2148B8` + Terracotta `#C65F38` | Neutral White | editorial cover | milestone arc — the whole evolution as one sweep |
| `01-stage00-foundations.png` | 0 · Foundations | chromatic + black | Charcoal `#30343A` + Signal Red `#C83232` | Cool Gray | ruled information poster | the sequence bottleneck, with attention fanning back in red |
| `02-stage01-transformer.png` | 1 · The Transformer | chromatic + black | Electric Blue `#173AE3` + Carbon `#242321` | Neutral White | type-led declaration | the all-to-all attention field, one query head in carbon |
| `03-stage02-pretraining.png` | 2 · Pretraining Era | complementary duotone | Botanical Green `#008A4B` + Oxblood `#8F3434` | Pale Beige | specimen / archival plate | three pretraining families, one transfer arrow in oxblood |
| `04-stage03-scale.png` | 3 · Scale & Emergence | overprint duotone | Ultramarine `#263E99` + Safety Orange `#E55D2B` | Neutral White | type-led declaration | extreme scale jump — one giant screened circle, emergence spark |
| `05-stage04-efficiency.png` | 4 · Efficiency | overprint duotone | Brick Red `#B64032` + Cyan `#159DDA` | Cool Gray | object field | a field of experts, only a sparse few routed in cyan |
| `06-stage05-alignment.png` | 5 · Alignment | pure one-ink | Signal Red `#C83232` | Neutral White | type-led declaration | a preference bending the path onto the reward target |
| `07-stage06-multimodal.png` | 6 · Multimodality | complementary duotone | Tangerine `#E46C2D` + Slate Blue `#4773A5` | Neutral White | editorial cover | diffusion noise resolving into a vision aperture |
| `08-stage07-frontier.png` | 7 · Frontier Systems | complementary duotone | Cobalt `#2148B8` + Terracotta `#C65F38` | Cool Gray | editorial cover | a reasoning loop with tool / agent branches in terracotta |
| `09-stage08-staying-current.png` | 8 · Staying Current | chromatic + black | Mint Green `#5EB783` + Warm Charcoal `#302D2E` | Pale Beige | editorial journal | a refresh loop enclosing the daily log stack |

The machine-readable version is in [`recipes.json`](recipes.json).

## Reproducing

```bash
# from this directory (artifact/thumbnails/)
python3 gen_thumbs.py     # writes build/<slug>.html + .svg and recipes.json
npm i playwright          # or use the pre-installed Chromium on Claude Code on the web
node render.js            # writes png/<slug>.png at 3000x3000
cp png/*.png ../../docs/thumbnails/
```

`render.js` uses whatever Chromium Playwright finds; set `CHROMIUM_PATH` to point
at a specific binary. It renders every `*.html` in `BUILD_DIR` (default `build/`)
to a same-named PNG in `OUT_DIR` (default `png/`) — both are overridable via
those environment variables. Output is deterministic — the same recipe
reproduces the same poster. The editable SVGs are in [`svg/`](svg/).

## Podcast episode covers

[`podcast_thumbs.py`](podcast_thumbs.py) is the *parameterized* companion used by
the weekly podcast automation: it emits **one** episode cover in the same
mono-color system, given the episode's season/number/type/title. Two episode
types, each with a fixed on-brand palette and focal metaphor:

| Type | Inks (plate roles) | Substrate | Focal event |
|------|--------------------|-----------|-------------|
| `deep-dive` | Electric Blue `#173AE3` + Carbon `#242321` | Neutral White | an aperture converging on one dense core — one idea, examined closely |
| `roundup` | Slate Blue `#4773A5` + Tangerine `#E46C2D` | Pale Beige | a scanned field of the week's signals, a sparse few promoted to the accent ink |

```bash
# from this directory (artifact/thumbnails/)
python3 podcast_thumbs.py \
    --type deep-dive --season 2 --episode 1 --date 2026-09-03 \
    --title "Short display title" --subtitle "optional one-liner"
# -> podcast_build/S2E01-2026-09-03-deep-dive.{html,svg}

BUILD_DIR=podcast_build OUT_DIR=../../docs/thumbnails/podcast node render.js
# -> ../../docs/thumbnails/podcast/S2E01-2026-09-03-deep-dive.png (3000x3000)
```

The title wraps to at most three lines; keep display titles short (the subtitle
is dropped automatically when a title needs all three lines). `podcast_build/`
is an ephemeral scratch dir (git-ignored); the published PNGs live in
[`../../docs/thumbnails/podcast/`](../../docs/thumbnails/podcast/).
