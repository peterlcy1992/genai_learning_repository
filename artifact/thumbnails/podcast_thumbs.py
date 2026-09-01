#!/usr/bin/env python3
"""Generate a single GenAI Evolution Atlas *podcast episode* square cover.

Same visual system as gen_thumbs.py (the mono-color editorial print skill,
yanliudesign/mono-color-skill): adaptive neutral substrate, <=2 printing inks
with assigned plate roles, halftone/mechanical reproduction, active negative
space, one focal event per page, one manual-gesture family (the registration
mark), terse display type. This module is the *parameterized* companion: it
takes an episode's season/number/type/title and emits one cover, so the weekly
podcast Routine can render a fresh cover per episode.

Two episode types, each with a fixed on-brand palette and focal metaphor so the
series reads consistently while the two kinds stay distinguishable:

  deep-dive  — Electric Blue + Carbon, a single aperture zooming onto one idea
               (focus / depth: one thing, examined closely).
  roundup    — Tangerine + Slate Blue, a scanned field of the week's signals
               with a few highlighted (breadth: the whole week at a glance).

Composed as SVG (1000-unit viewBox) and rendered to 3000x3000 PNG by render.js
(point it at this build dir via BUILD_DIR / OUT_DIR).

Usage:
  python3 podcast_thumbs.py \
      --type deep-dive --season 2 --episode 1 --date 2026-09-03 \
      --title "The week's biggest leap" \
      [--subtitle "one line under the title"] \
      [--out-slug S2E01-2026-09-03-deep-dive] \
      [--build-dir podcast_build]

Writes <build-dir>/<slug>.html and <build-dir>/<slug>.svg (deterministic).
Prints the slug on stdout so callers can capture it.
"""
import argparse, math, os, textwrap

# ---- fonts (installed in this environment; match gen_thumbs.py) -----------
GROTESK = "'Liberation Sans','Arial','DejaVu Sans',sans-serif"
SERIF   = "'Bitstream Charter','Georgia','DejaVu Serif',serif"
MONO    = "'Liberation Mono','DejaVu Sans Mono',monospace"

M = 76           # outer margin (viewBox units, ~7.6%)
W = 1000

# palette hexes (subset of gen_thumbs.py)
CARBON="#242321"; ELECTRIC="#173AE3"; TANGE="#E46C2D"; SLATE="#4773A5"
S_WHITE="#FAFAF7"; S_GRAY="#E9E9E5"; S_BEIGE="#F5F1E8"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def halftone(pid, ink, spacing=9.0, r=2.5, angle=15):
    """A rotated dot screen — mechanical print reproduction, not a color wash."""
    c = spacing / 2.0
    return (f'<pattern id="{pid}" width="{spacing}" height="{spacing}" '
            f'patternUnits="userSpaceOnUse" patternTransform="rotate({angle})">'
            f'<circle cx="{c}" cy="{c}" r="{r}" fill="{ink}"/></pattern>')


def text(x, y, s, size, ink, font=GROTESK, weight=700, spacing=0.0,
         anchor="start", opacity=1.0, style="", italic=False):
    it = 'font-style:italic;' if italic else ''
    ls = f'letter-spacing:{spacing}px;' if spacing else ''
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-weight="{weight}" '
            f'font-size="{size}" fill="{ink}" text-anchor="{anchor}" '
            f'opacity="{opacity}" style="{it}{ls}{style}">{esc(s)}</text>')


def reg_mark(x, y, ink, s=11, sw=1.4):
    """Print registration crosshair — the series' single manual-gesture family."""
    return (f'<g stroke="{ink}" stroke-width="{sw}" fill="none">'
            f'<circle cx="{x}" cy="{y}" r="{s*0.55}"/>'
            f'<line x1="{x-s}" y1="{y}" x2="{x+s}" y2="{y}"/>'
            f'<line x1="{x}" y1="{y-s}" x2="{x}" y2="{y+s}"/></g>')


def footer(dom_ink, index_label):
    """Consistent series microtype: brand line + episode index + registration mark."""
    y = W - M + 20
    g = text(M, y, "GENAI EVOLUTION ATLAS", 15.5, dom_ink, MONO, 700, 4.2)
    g += text(W - M, y, index_label, 15.5, dom_ink, MONO, 700, 4.2, anchor="end")
    g += (f'<line x1="{M}" y1="{y-27}" x2="{W-M}" y2="{y-27}" '
          f'stroke="{dom_ink}" stroke-width="1.1" opacity="0.7"/>')
    g += reg_mark(W - M, M - 6, dom_ink)
    return g


def kicker(s, ink, x=M, y=M+18):
    return text(x, y, s, 15.5, ink, MONO, 700, 4.4)


def frame(defs, body, substrate):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="3000" height="3000" '
            f'viewBox="0 0 {W} {W}">'
            f'<defs>{defs}</defs>'
            f'<rect width="{W}" height="{W}" fill="{substrate}"/>'
            f'{body}</svg>')


def html(svg):
    return ('<!doctype html><meta charset="utf-8">'
            '<style>html,body{margin:0;padding:0}svg{display:block}</style>' + svg)


def _wrap_title(s, width):
    """Greedy wrap a display title into up to 3 lines for the given char width."""
    lines = textwrap.wrap(s, width=width, break_long_words=False) or [s]
    return lines[:3]


def _title_block(lines, ink_main, ink_accent, font, size, y0, weight=800,
                 lh=None, italic=False):
    """Render up to three stacked title lines; the last line takes the accent ink."""
    lh = lh or int(size * 1.02)
    out = ""
    n = len(lines)
    for i, ln in enumerate(lines):
        ink = ink_accent if i == n - 1 else ink_main
        out += text(M - 3, y0 + i * lh, ln, size, ink, font, weight, 0,
                    italic=italic)
    return out


def _bottom_block(title, subtitle, ink_main, ink_accent, sub_ink, font,
                  size, lh, wrap_w, sub_font=SERIF):
    """Bottom-anchored title + optional subtitle, laid out clear of the footer.

    Titles wrap to at most three lines; a subtitle is shown only when the title
    fits in one or two lines, so a full three-line title never crowds the
    footer. Returns the SVG string."""
    lines = _wrap_title(title, wrap_w)
    if len(lines) >= 3:
        show_sub, bottom = False, 878
    else:
        show_sub = bool(subtitle)
        bottom = 858 if show_sub else 888
    y0 = bottom - (len(lines) - 1) * lh
    out = _title_block(lines, ink_main, ink_accent, font, size=size,
                       weight=(700 if font == SERIF else 800), y0=y0, lh=lh)
    if show_sub:
        out += text(M + 3, 900, subtitle, 20, sub_ink, sub_font, 400, 0,
                    italic=True)
    return out


def cover_deepdive(season, episode, date, title, subtitle):
    """Deep Dive cover — Electric Blue + Carbon, focal = an aperture onto one idea."""
    dom, acc, sub = ELECTRIC, CARBON, S_WHITE
    defs = halftone("h_dd", dom, 9, 2.6)
    b = kicker("DEEP DIVE", acc)
    b += text(W - M, M + 18, date, 15.5, dom, MONO, 700, 2.4, anchor="end")

    # focal: concentric aperture rings converging on one dense core — "one idea,
    # examined closely." Screened outer rings, solid focal center.
    cx, cy = 500, 388
    for i, rr in enumerate((196, 158, 120)):
        op = 0.30 + i * 0.16
        b += (f'<circle cx="{cx}" cy="{cy}" r="{rr}" fill="none" '
              f'stroke="{dom}" stroke-width="{3 + i*1.2:.1f}" opacity="{op:.2f}"/>')
    b += f'<circle cx="{cx}" cy="{cy}" r="150" fill="url(#h_dd)" opacity="0.5"/>'
    # aperture blades (a few short chords) — mechanical, print-y
    for k in range(6):
        a = math.radians(k * 60 + 12)
        x1, y1 = cx + 86*math.cos(a), cy + 86*math.sin(a)
        x2, y2 = cx + 118*math.cos(a + 0.5), cy + 118*math.sin(a + 0.5)
        b += (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
              f'stroke="{dom}" stroke-width="3"/>')
    b += f'<circle cx="{cx}" cy="{cy}" r="70" fill="{acc}"/>'
    b += f'<circle cx="{cx}" cy="{cy}" r="70" fill="none" stroke="{dom}" stroke-width="3"/>'

    # title (serif, focused voice), bottom-anchored clear of the footer
    b += _bottom_block(title, subtitle, dom, acc, acc, SERIF,
                       size=74, lh=80, wrap_w=20)
    b += footer(dom, f"S{season} · E{episode:02d}")
    return frame(defs, b, sub)


def cover_roundup(season, episode, date, title, subtitle):
    """Roundup cover — Tangerine + Slate, focal = a scanned field of the week's signals."""
    dom, acc, sub = SLATE, TANGE, S_BEIGE
    defs = halftone("h_ru", dom, 9, 2.6)
    b = kicker("NEWS ROUNDUP", acc)
    b += text(W - M, M + 18, date, 15.5, dom, MONO, 700, 2.4, anchor="end")

    # focal: a scan field — a grid of the week's signals (bars of varying weight),
    # a sparse few promoted to the accent ink. Breadth at a glance.
    gx0, gy0 = M + 6, 250
    cols, rows = 7, 5
    cw, chh = (W - 2*M - 12) / cols, 30
    accent_cells = {(1, 0), (4, 1), (2, 3), (5, 4), (0, 2)}
    for r in range(rows):
        for c in range(cols):
            x = gx0 + c * cw
            y = gy0 + r * (chh + 16)
            # deterministic "signal strength" per cell
            h = 8 + ((c * 7 + r * 13 + 5) % 5) * 6
            is_acc = (c, r) in accent_cells
            ink = acc if is_acc else dom
            op = 1.0 if is_acc else (0.28 + ((c + r) % 3) * 0.12)
            b += (f'<rect x="{x:.1f}" y="{y + (chh - h):.1f}" '
                  f'width="{cw - 12:.1f}" height="{h}" fill="{ink}" opacity="{op:.2f}"/>')
            if is_acc:
                b += (f'<circle cx="{x + (cw-12)/2:.1f}" cy="{y - 8:.1f}" '
                      f'r="4.5" fill="{acc}"/>')

    # title (assertive grotesk, broad voice), bottom-anchored clear of the footer
    b += _bottom_block(title, subtitle, dom, acc, dom, GROTESK,
                       size=78, lh=84, wrap_w=18)
    b += footer(dom, f"S{season} · E{episode:02d}")
    return frame(defs, b, sub)


BUILDERS = {"deep-dive": cover_deepdive, "roundup": cover_roundup}


def main():
    ap = argparse.ArgumentParser(description="Generate one podcast episode cover.")
    ap.add_argument("--type", required=True, choices=sorted(BUILDERS))
    ap.add_argument("--season", type=int, default=2)
    ap.add_argument("--episode", type=int, required=True)
    ap.add_argument("--date", required=True, help="YYYY-MM-DD shown on the cover")
    ap.add_argument("--title", required=True, help="short display title")
    ap.add_argument("--subtitle", default="", help="optional one-line subtitle")
    ap.add_argument("--out-slug", default=None,
                    help="output basename (default S{season}E{episode}-{date}-{type})")
    ap.add_argument("--build-dir", default="podcast_build",
                    help="dir (relative to this file) for the .html/.svg")
    args = ap.parse_args()

    slug = args.out_slug or f"S{args.season}E{args.episode:02d}-{args.date}-{args.type}"
    build = os.path.join(os.path.dirname(os.path.abspath(__file__)), args.build_dir)
    os.makedirs(build, exist_ok=True)

    svg = BUILDERS[args.type](args.season, args.episode, args.date,
                              args.title, args.subtitle)
    with open(os.path.join(build, slug + ".html"), "w") as f:
        f.write(html(svg))
    with open(os.path.join(build, slug + ".svg"), "w") as f:
        f.write(svg)
    print(slug)


if __name__ == "__main__":
    main()
