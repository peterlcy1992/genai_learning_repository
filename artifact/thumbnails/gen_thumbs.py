#!/usr/bin/env python3
"""Generate GenAI Evolution Atlas podcast square thumbnails.

Honors the mono-color editorial print skill (yanliudesign/mono-color-skill):
adaptive neutral substrate, <=2 printing inks with assigned plate roles,
halftone/mechanical reproduction, active negative space (25-55% paper),
one focal event per page, one manual-gesture family, terse display type.

Composed as SVG (1000-unit viewBox) and rendered to 3000x3000 PNG.
Square (1:1) is the user-specified ratio for podcast cover art.
"""
import math, os, json, hashlib

OUT = os.path.join(os.path.dirname(__file__), "build")
os.makedirs(OUT, exist_ok=True)

# ---- fonts (installed in this environment) --------------------------------
GROTESK = "'Liberation Sans','Arial','DejaVu Sans',sans-serif"
SERIF   = "'Bitstream Charter','Georgia','DejaVu Serif',serif"
MONO    = "'Liberation Mono','DejaVu Sans Mono',monospace"

M = 76           # outer margin (viewBox units, ~7.6%)
W = 1000

def esc(s): return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

# ---- halftone reproduction layer ------------------------------------------
def halftone(pid, ink, spacing=9.0, r=2.5, angle=15):
    """A rotated dot screen — mechanical print reproduction, not a color wash."""
    c = spacing / 2.0
    return (f'<pattern id="{pid}" width="{spacing}" height="{spacing}" '
            f'patternUnits="userSpaceOnUse" patternTransform="rotate({angle})">'
            f'<circle cx="{c}" cy="{c}" r="{r}" fill="{ink}"/></pattern>')

def line_screen(pid, ink, spacing=8.0, thick=2.4, angle=0):
    return (f'<pattern id="{pid}" width="{spacing}" height="{spacing}" '
            f'patternUnits="userSpaceOnUse" patternTransform="rotate({angle})">'
            f'<rect x="0" y="0" width="{spacing}" height="{thick}" fill="{ink}"/></pattern>')

# ---- type helpers ----------------------------------------------------------
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
    """Consistent series microtype: brand line + stage index + registration mark."""
    y = W - M + 20
    g  = text(M, y, "GENAI EVOLUTION ATLAS", 15.5, dom_ink, MONO, 700, 4.2)
    g += text(W - M, y, index_label, 15.5, dom_ink, MONO, 700, 4.2, anchor="end")
    g += f'<line x1="{M}" y1="{y-27}" x2="{W-M}" y2="{y-27}" stroke="{dom_ink}" stroke-width="1.1" opacity="0.7"/>'
    g += reg_mark(W - M, M - 6, dom_ink)
    return g

def kicker(s, ink, x=M, y=M+18):
    return text(x, y, s, 15.5, ink, MONO, 700, 4.4)

# ---- SVG frame -------------------------------------------------------------
def frame(defs, body, substrate):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="3000" height="3000" '
            f'viewBox="0 0 {W} {W}">'
            f'<defs>{defs}</defs>'
            f'<rect width="{W}" height="{W}" fill="{substrate}"/>'
            f'{body}</svg>')

def html(svg):
    return ('<!doctype html><meta charset="utf-8">'
            '<style>html,body{margin:0;padding:0}svg{display:block}</style>' + svg)

# palette hexes
COBALT="#2148B8"; TERRA="#C65F38"; CHARCOAL="#30343A"; SIGRED="#C83232"
ELECTRIC="#173AE3"; CARBON="#242321"; BOTAN="#008A4B"; OXBLOOD="#8F3434"
ULTRA="#263E99"; SAFETY="#E55D2B"; CYAN="#159DDA"; BRICK="#B64032"
TANGE="#E46C2D"; SLATE="#4773A5"; MINT="#5EB783"; WCHAR="#302D2E"
S_WHITE="#FAFAF7"; S_GRAY="#E9E9E5"; S_BEIGE="#F5F1E8"

# ===========================================================================
#  COMPOSITIONS  (one focal event each, 45-80% dominant object, active paper)
# ===========================================================================

def c_site():
    """Overall Atlas cover — Cobalt+Terracotta, editorial cover, focal=milestone arc."""
    dom, acc, sub = COBALT, TERRA, S_WHITE
    defs = halftone("h_site", dom, 9, 2.7)
    b = kicker("A VISUAL FIELD GUIDE", acc)
    b += text(W-M, M+18, "2017 → NOW", 15.5, dom, MONO, 700, 3.2, anchor="end")
    # focal: a shallow arc of milestones across the top — the evolution timeline
    P0, P1, P2 = (120, 440), (500, 150), (880, 440)
    def bez(t):
        u = 1 - t
        return (u*u*P0[0] + 2*u*t*P1[0] + t*t*P2[0],
                u*u*P0[1] + 2*u*t*P1[1] + t*t*P2[1])
    b += f'<path d="M {P0[0]} {P0[1]} Q {P1[0]} {P1[1]} {P2[0]} {P2[1]}" fill="none" stroke="{dom}" stroke-width="6"/>'
    n = 9
    for i in range(n):
        px, py = bez(i/(n-1))
        last = (i == n-1)
        col = acc if last else dom
        rr = 26 if last else (7 + i*1.5)
        b += f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{rr:.1f}" fill="{col}"/>'
        if last:
            b += f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{rr+13:.1f}" fill="none" stroke="{acc}" stroke-width="2.4"/>'
        b += text(px, py-rr-11, f"{i:02d}", 13, dom, MONO, 700, 1, anchor="middle", opacity=0.85)
    # dominant title, in the clear lower field
    b += text(M-3, 600, "GENAI", 134, dom, GROTESK, 800, -2)
    b += text(M-3, 712, "EVOLUTION", 104, dom, GROTESK, 800, -1)
    b += f'<rect x="{M}" y="726" width="330" height="15" fill="{acc}"/>'
    b += text(M-3, 850, "ATLAS", 134, acc, GROTESK, 800, 6)
    b += text(M+2, 896, "the transformer era, mapped stage by stage", 22, dom, SERIF, 400, 0, italic=True)
    b += footer(dom, "SERIES INDEX")
    return frame(defs, b, sub), dict(mode="complementary duotone", ink=f"Cobalt {COBALT} + Terracotta {TERRA}",
        layout="editorial cover", type="grotesk display + serif aside", process="dot halftone / flat plates",
        focal="milestone arc — the whole evolution as one sweep")

def c_stage0():
    """Foundations — Charcoal+Signal Red, focal=recurrence loop into a bottleneck."""
    dom, acc, sub = CHARCOAL, SIGRED, S_GRAY
    defs = halftone("h0", dom, 9, 2.6)
    b = kicker("STAGE 00", acc)
    b += text(W-M, M+18, "PRE-2017", 15.5, dom, MONO, 700, 3, anchor="end")
    # focal: chain of recurrent cells feeding a single narrow bottleneck
    y = 470
    xs = [150, 250, 350, 450]
    for i, x in enumerate(xs):
        b += f'<rect x="{x-34}" y="{y-34}" width="68" height="68" rx="6" fill="url(#h0)"/>'
        b += f'<rect x="{x-34}" y="{y-34}" width="68" height="68" rx="6" fill="none" stroke="{dom}" stroke-width="2.2"/>'
        # recurrent self-loop arrow (charcoal)
        b += f'<path d="M {x+18} {y-34} q 40 -46 -18 -52 q -50 -4 -30 34" fill="none" stroke="{dom}" stroke-width="2.4"/>'
        if i < len(xs)-1:
            b += f'<line x1="{x+34}" y1="{y}" x2="{xs[i+1]-34}" y2="{y}" stroke="{dom}" stroke-width="3"/>'
    # the bottleneck: everything squeezes through one fixed vector (red = the fix)
    bx = 560
    b += f'<line x1="{xs[-1]+34}" y1="{y}" x2="{bx-14}" y2="{y}" stroke="{dom}" stroke-width="3"/>'
    b += f'<path d="M {bx-14} {y-60} L {bx+40} {y} L {bx-14} {y+60} Z" fill="{dom}"/>'
    b += f'<circle cx="{bx+90}" cy="{y}" r="26" fill="{acc}"/>'
    b += text(bx+90, y+8, "c", 30, sub, SERIF, 700, 0, anchor="middle", italic=True)
    # attention as the fix: red fan reconnecting the decoder to every cell
    for x in xs:
        b += f'<path d="M {bx+112} {y-6} Q {(x+bx)/2} {y-150} {x} {y-46}" fill="none" stroke="{acc}" stroke-width="1.8" opacity="0.9"/>'
    b += text(760, y-150, "attention", 22, acc, SERIF, 400, 0, anchor="middle", italic=True)
    # title
    b += text(M-2, 720, "BEFORE", 118, dom, MONO, 700, 2)
    b += text(M-2, 835, "ATTENTION", 118, dom, MONO, 700, 2)
    b += text(M+3, 300, "one hidden state carried the whole sentence.", 21, dom, SERIF, 400, 0, italic=True)
    b += footer(dom, "00 / 08")
    return frame(defs, b, sub), dict(mode="chromatic + black", ink=f"Charcoal {CHARCOAL} + Signal Red {SIGRED}",
        layout="ruled information poster", type="mono structure + serif aside", process="dot halftone cells",
        focal="the sequence bottleneck, with attention fanning back in red")

def c_stage1():
    """Transformer — Electric Blue+Carbon, focal=self-attention all-to-all matrix."""
    dom, acc, sub = ELECTRIC, CARBON, S_WHITE
    defs = halftone("h1", dom, 8.5, 2.5)
    b = kicker("STAGE 01", acc)
    b += text(W-M, M+18, "2017", 15.5, acc, MONO, 700, 3, anchor="end")
    # focal: all-to-all attention — tokens on an arc, every pair linked
    cx, cy, R = 500, 430, 250
    N = 7
    pts = [(cx + R*math.cos(2*math.pi*i/N - math.pi/2),
            cy + R*math.sin(2*math.pi*i/N - math.pi/2)) for i in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            b += f'<line x1="{pts[i][0]:.1f}" y1="{pts[i][1]:.1f}" x2="{pts[j][0]:.1f}" y2="{pts[j][1]:.1f}" stroke="{dom}" stroke-width="1.1" opacity="0.45"/>'
    # one query row highlighted in carbon (accent role: the focused head)
    q = 0
    for j in range(1, N):
        b += f'<line x1="{pts[q][0]:.1f}" y1="{pts[q][1]:.1f}" x2="{pts[j][0]:.1f}" y2="{pts[j][1]:.1f}" stroke="{acc}" stroke-width="2.6"/>'
    for i,(px,py) in enumerate(pts):
        col = acc if i==q else dom
        b += f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{22 if i==q else 17}" fill="{col}"/>'
    b += f'<circle cx="{pts[q][0]:.1f}" cy="{pts[q][1]:.1f}" r="35" fill="none" stroke="{acc}" stroke-width="2.2"/>'
    # title — interlocked caps crossing the field
    b += text(M-3, 760, "ATTENTION", 128, dom, GROTESK, 800, -1)
    b += text(M-3, 872, "IS ALL", 128, acc, GROTESK, 800, 2)
    b += text(W-M, 872, "—", 128, dom, GROTESK, 800, 0, anchor="end")
    b += text(M+3, 655, "no recurrence. every token sees every other, at once.", 20, acc, SERIF, 400, 0, italic=True)
    b += footer(acc, "01 / 08")
    return frame(defs, b, sub), dict(mode="chromatic + black", ink=f"Electric Blue {ELECTRIC} + Carbon {CARBON}",
        layout="type-led declaration", type="cultural grotesk + serif aside", process="thin plate line-work",
        focal="the all-to-all attention field, one query head in carbon")

def c_stage2():
    """Pretraining era — Botanical Green+Oxblood, focal=three model families, transfer arrow."""
    dom, acc, sub = BOTAN, OXBLOOD, S_BEIGE
    defs = halftone("h2", dom, 9, 2.6)
    b = kicker("STAGE 02", acc)
    b += text(W-M, M+18, "2018", 15.5, acc, MONO, 700, 3, anchor="end")
    # three stacked-layer specimens: encoder / decoder / enc-dec
    labels = ["ENCODER", "DECODER", "ENC–DEC"]
    subl = ["BERT", "GPT", "T5"]
    x0, gap, w = 150, 250, 150
    ytop, layers, lh = 250, 5, 34
    for k in range(3):
        x = x0 + k*gap
        for L in range(layers):
            yy = ytop + L*(lh+9)
            fillp = "url(#h2)" if L % 2 else dom
            b += f'<rect x="{x-w/2}" y="{yy}" width="{w}" height="{lh}" rx="4" fill="{fillp}"/>'
            b += f'<rect x="{x-w/2}" y="{yy}" width="{w}" height="{lh}" rx="4" fill="none" stroke="{dom}" stroke-width="1.6"/>'
        b += text(x, ytop-18, labels[k], 17, dom, GROTESK, 700, 1.5, anchor="middle")
        b += text(x, ytop+layers*(lh+9)+30, subl[k], 27, acc, SERIF, 700, 0, anchor="middle")
    # transfer arrow (oxblood accent role): pretrain -> fine-tune sweeping across
    ay = ytop + layers*(lh+9) + 70
    b += f'<path d="M {x0-40} {ay} C 360 {ay+66}, 640 {ay+66}, {x0+2*gap+40} {ay}" fill="none" stroke="{acc}" stroke-width="3"/>'
    b += f'<path d="M {x0+2*gap+40} {ay} l -22 -12 l 4 14 l -14 6 z" fill="{acc}"/>'
    b += text(500, ay+108, "pretrain once, transfer everywhere", 21, acc, SERIF, 400, 0, anchor="middle", italic=True)
    # title
    b += text(M-3, 770, "Pretrain", 118, dom, SERIF, 700, 0)
    b += text(M-3, 878, "& Transfer", 118, acc, SERIF, 700, 0)
    b += footer(dom, "02 / 08")
    return frame(defs, b, sub), dict(mode="complementary duotone", ink=f"Botanical Green {BOTAN} + Oxblood {OXBLOOD}",
        layout="specimen annotation / archival plate", type="literary serif + grotesk labels", process="dot halftone layers",
        focal="three pretraining families, one transfer arrow in oxblood")

def c_stage3():
    """Scale & emergence — Ultramarine+Safety Orange, focal=extreme scale jump."""
    dom, acc, sub = ULTRA, SAFETY, S_WHITE
    defs = halftone("h3", dom, 9, 2.7)
    b = kicker("STAGE 03", acc)
    b += text(W-M, M+18, "2019–20", 15.5, dom, MONO, 700, 3, anchor="end")
    # focal: one giant circle dwarfing a ramp of tiny ones (the size jump)
    xs = [150, 205, 275, 365]
    rs = [7, 12, 20, 33]
    baseline = 470
    for x, r in zip(xs, rs):
        b += f'<circle cx="{x}" cy="{baseline}" r="{r}" fill="{dom}"/>'
    big_cx, big_cy, big_r = 660, 435, 210
    b += f'<circle cx="{big_cx}" cy="{big_cy}" r="{big_r}" fill="url(#h3)"/>'
    b += f'<circle cx="{big_cx}" cy="{big_cy}" r="{big_r}" fill="none" stroke="{dom}" stroke-width="3"/>'
    # emergent spark (accent role): the ability that appears at scale
    b += f'<circle cx="{big_cx}" cy="{big_cy}" r="30" fill="{acc}"/>'
    for a in range(8):
        t = a*math.pi/4
        b += f'<line x1="{big_cx+38*math.cos(t):.1f}" y1="{big_cy+38*math.sin(t):.1f}" x2="{big_cx+62*math.cos(t):.1f}" y2="{big_cy+62*math.sin(t):.1f}" stroke="{acc}" stroke-width="4"/>'
    b += f'<path d="M {xs[0]} {baseline+40} C 300 {baseline+40}, 380 {big_cy+big_r-6}, {big_cx-big_r} {big_cy+big_r-6}" fill="none" stroke="{acc}" stroke-width="2" stroke-dasharray="3 6"/>'
    b += text(big_cx, big_cy+big_r+40, "10¹¹ parameters", 20, dom, MONO, 700, 1, anchor="middle")
    # title
    b += text(M-3, 740, "SCALE", 150, dom, GROTESK, 800, -2)
    b += text(M-3, 858, "CHANGES", 96, acc, GROTESK, 800, 1)
    b += text(M+540, 858, "IT ALL", 96, dom, GROTESK, 800, 1)
    b += text(M+3, 300, "same recipe — far bigger.", 22, dom, SERIF, 400, 0, italic=True)
    b += text(M+3, 335, "and new abilities appear.", 22, acc, SERIF, 400, 0, italic=True)
    b += footer(dom, "03 / 08")
    return frame(defs, b, sub), dict(mode="overprint duotone", ink=f"Ultramarine {ULTRA} + Safety Orange {SAFETY}",
        layout="type-led declaration", type="assertive grotesk + mono label", process="dot halftone mass",
        focal="extreme scale jump — one giant screened circle, emergence spark in orange")

def c_stage4():
    """Efficiency — Brick Red+Cyan, focal=repeated experts (object field), one router + long context."""
    dom, acc, sub = BRICK, CYAN, S_GRAY
    defs = halftone("h4", dom, 8.5, 2.5)
    b = kicker("STAGE 04", acc)
    b += text(W-M, M+18, "2020–22", 15.5, dom, MONO, 700, 3, anchor="end")
    # object field: a grid of expert blocks, only a few routed (cyan) — sparse MoE
    cols, rows = 5, 3
    gx, gy, cell = 150, 250, 118
    active = {(0,1),(2,0),(3,2),(4,1)}
    for r in range(rows):
        for c in range(cols):
            x = gx + c*cell; y = gy + r*cell
            on = (c, r) in active
            fillp = acc if on else "url(#h4)"
            b += f'<rect x="{x}" y="{y}" width="{cell-20}" height="{cell-20}" rx="7" fill="{fillp}"/>'
            b += f'<rect x="{x}" y="{y}" width="{cell-20}" height="{cell-20}" rx="7" fill="none" stroke="{dom}" stroke-width="1.8"/>'
    # router node feeding the active experts
    rxr, ryr = gx-4, gy + rows*cell/2 - 10
    b += f'<circle cx="{rxr}" cy="{ryr}" r="16" fill="{dom}"/>'
    for (c, r) in sorted(active):
        tx = gx + c*cell; ty = gy + r*cell + (cell-20)/2
        b += f'<path d="M {rxr+14} {ryr} Q {(rxr+tx)/2} {ty} {tx} {ty}" fill="none" stroke="{acc}" stroke-width="2.4"/>'
    # long-context bar crossing under the field
    cyb = gy + rows*cell + 34
    b += f'<rect x="{gx}" y="{cyb}" width="{cols*cell-20}" height="16" rx="8" fill="url(#h4)"/>'
    b += f'<rect x="{gx}" y="{cyb}" width="120" height="16" rx="8" fill="{acc}"/>'
    b += text(gx, cyb+46, "longer context, fewer FLOPs per token", 20, dom, SERIF, 400, 0, italic=True)
    # title
    b += text(M-3, 780, "FASTER", 100, dom, GROTESK, 800, 0)
    b += text(M-3, 878, "LONGER, CHEAPER", 70, acc, GROTESK, 800, 0.5)
    b += footer(dom, "04 / 08")
    return frame(defs, b, sub), dict(mode="overprint duotone", ink=f"Brick Red {BRICK} + Cyan {CYAN}",
        layout="object field", type="grotesk caps + serif aside", process="dot halftone blocks",
        focal="a field of experts, only a sparse few routed in cyan")

def c_stage5():
    """Alignment — pure one-ink Signal Red, focal=preference bend toward a target."""
    dom, sub = SIGRED, S_WHITE
    defs = halftone("h5", dom, 9, 2.6) + halftone("h5l", dom, 11, 1.7)
    b = kicker("STAGE 05", dom)
    b += text(W-M, M+18, "2022", 15.5, dom, MONO, 700, 3, anchor="end")
    # focal: raw next-token path (pale screen) bent by preference toward a target
    sx, sy = 150, 300
    b += f'<path d="M {sx} {sy} C 330 240, 380 560, 560 540" fill="none" stroke="url(#h5l)" stroke-width="20" opacity="0.9"/>'
    tx, ty = 780, 430
    b += f'<path d="M {sx} {sy} C 360 300, 520 360, {tx} {ty}" fill="none" stroke="{dom}" stroke-width="9"/>'
    b += f'<path d="M {tx} {ty} l -20 -8 l 5 12 l -12 7 z" fill="{dom}"/>'
    # the target / reward (bullseye) — density change, still one ink
    b += f'<circle cx="{tx+30}" cy="{ty}" r="46" fill="none" stroke="{dom}" stroke-width="4"/>'
    b += f'<circle cx="{tx+30}" cy="{ty}" r="26" fill="url(#h5)"/>'
    b += f'<circle cx="{tx+30}" cy="{ty}" r="9" fill="{dom}"/>'
    # ranked preferences (thin ruled band) — the human signal
    for i, yy in enumerate([210, 240]):
        b += f'<line x1="{sx}" y1="{yy}" x2="{sx+150}" y2="{yy}" stroke="{dom}" stroke-width="{6 if i==0 else 2}"/>'
    b += text(sx, 175, "A ≻ B", 22, dom, MONO, 700, 2)
    b += text(sx, 600, "reward, not just likelihood, shapes the reply", 20, dom, SERIF, 400, 0, italic=True)
    # title — civic stacked caps
    b += text(M-3, 760, "ALIGN", 132, dom, GROTESK, 800, 1)
    b += text(M-3, 878, "THE ASSISTANT", 74, dom, GROTESK, 800, 1)
    b += footer(dom, "05 / 08")
    return frame(defs, b, sub), dict(mode="pure one-ink", ink=f"Signal Red {SIGRED}",
        layout="type-led declaration", type="civic grotesk + serif aside", process="single-plate density / halftone",
        focal="a preference bending the path onto the reward target")

def c_stage6():
    """Multimodality — Tangerine+Slate Blue, focal=diffusion denoise resolving into an aperture."""
    dom, acc, sub = TANGE, SLATE, S_WHITE
    defs = halftone("h6", dom, 9, 2.6)
    b = kicker("STAGE 06", acc)
    b += text(W-M, M+18, "2021–23", 15.5, acc, MONO, 700, 3, anchor="end")
    # focal: noise field (left) resolving into a clean lens/aperture (right)
    import random
    rnd = random.Random(6)
    for _ in range(150):
        x = rnd.uniform(120, 470); y = rnd.uniform(230, 560)
        r = rnd.uniform(1.2, 5.5) * (1 - (x-120)/380)  # denser noise at the left
        b += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{max(0.6,r):.1f}" fill="{dom}" opacity="0.8"/>'
    ex, ey = 640, 400
    b += f'<circle cx="{ex}" cy="{ey}" r="150" fill="url(#h6)"/>'
    b += f'<circle cx="{ex}" cy="{ey}" r="150" fill="none" stroke="{dom}" stroke-width="3"/>'
    b += f'<circle cx="{ex}" cy="{ey}" r="66" fill="{sub}"/>'
    b += f'<circle cx="{ex}" cy="{ey}" r="66" fill="none" stroke="{acc}" stroke-width="6"/>'   # lens = vision, in accent
    b += f'<circle cx="{ex}" cy="{ey}" r="24" fill="{acc}"/>'
    b += f'<path d="M 470 400 L 555 400" stroke="{acc}" stroke-width="3" stroke-dasharray="4 7"/>'
    # a language bracket joining the visual stream
    b += f'<path d="M {ex+180} {ey-120} q 26 0 26 26 v 68 q 0 26 26 26" fill="none" stroke="{acc}" stroke-width="3"/>'
    b += text(ex+250, ey+8, "text", 24, acc, SERIF, 400, 0, italic=True)
    b += text(M+3, 615, "noise resolves into an image; pixels learn to read", 22, acc, SERIF, 400, 0, italic=True)
    # title — large playful typographic
    b += text(M-3, 770, "SEEING", 132, dom, GROTESK, 800, -1)
    b += text(M-3, 885, "& MAKING", 132, acc, GROTESK, 800, 0)
    b += footer(acc, "06 / 08")
    return frame(defs, b, sub), dict(mode="complementary duotone", ink=f"Tangerine {TANGE} + Slate Blue {SLATE}",
        layout="editorial cover", type="large typographic + serif aside", process="stochastic dot denoise",
        focal="diffusion noise resolving into a vision aperture")

def c_stage7():
    """Frontier systems — Cobalt+Terracotta, focal=reasoning loop with tool/agent branches."""
    dom, acc, sub = COBALT, TERRA, S_GRAY
    defs = halftone("h7", dom, 9, 2.6)
    b = kicker("STAGE 07", acc)
    b += text(W-M, M+18, "2023–26", 15.5, dom, MONO, 700, 3, anchor="end")
    # focal: a bold reasoning loop (two chasing arcs) around a central model node
    cx, cy, R = 470, 420, 165
    b += f'<path d="M {cx} {cy-R} A {R} {R} 0 1 1 {cx-R*math.sin(0.5):.1f} {cy-R*math.cos(0.5):.1f}" fill="none" stroke="{dom}" stroke-width="9"/>'
    ax = cx - R*math.sin(0.5); ay = cy - R*math.cos(0.5)
    b += f'<path d="M {ax:.1f} {ay:.1f} l -2 -22 l 18 10 z" fill="{dom}"/>'
    b += f'<circle cx="{cx}" cy="{cy}" r="72" fill="url(#h7)"/>'
    b += f'<circle cx="{cx}" cy="{cy}" r="72" fill="none" stroke="{dom}" stroke-width="3"/>'
    # tool / agent branches (terracotta accent role)
    tools = [("retrieve", -38), ("tools", 34), ("act", 122)]
    for name, deg in tools:
        t = math.radians(deg)
        x1, y1 = cx + 84*math.cos(t), cy + 84*math.sin(t)
        x2, y2 = cx + 210*math.cos(t), cy + 210*math.sin(t)
        b += f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{acc}" stroke-width="3"/>'
        b += f'<circle cx="{x2:.1f}" cy="{y2:.1f}" r="15" fill="{acc}"/>'
        b += text(x2+ (24 if math.cos(t)>=0 else -24), y2+6, name, 18, dom, MONO, 700, 1,
                  anchor=("start" if math.cos(t)>=0 else "end"))
    # title
    b += text(M-3, 772, "The Thinking", 96, dom, SERIF, 700, 0)
    b += text(M-3, 880, "Frontier", 120, acc, SERIF, 700, 0)
    b += text(M+3, 686, "a model becomes a system: retrieval, tools, agents, reasoning", 19, dom, SERIF, 400, 0, italic=True)
    b += footer(dom, "07 / 08")
    return frame(defs, b, sub), dict(mode="complementary duotone", ink=f"Cobalt {COBALT} + Terracotta {TERRA}",
        layout="editorial cover", type="literary serif + mono labels", process="dot halftone core",
        focal="a reasoning loop with tool/agent branches in terracotta")

def c_stage8():
    """Staying current — Mint Green+Warm Charcoal, focal=refresh loop over the daily log."""
    dom, acc, sub = MINT, WCHAR, S_BEIGE
    defs = halftone("h8", dom, 9, 2.7)
    b = kicker("STAGE 08", acc)
    b += text(W-M, M+18, "ONGOING", 15.5, acc, MONO, 700, 3, anchor="end")
    # focal: a bold circular refresh loop
    cx, cy, R = 470, 415, 175
    b += f'<path d="M {cx+R} {cy} A {R} {R} 0 1 1 {cx} {cy-R}" fill="none" stroke="{dom}" stroke-width="11"/>'
    b += f'<path d="M {cx} {cy-R} l -22 -6 l 12 20 z" fill="{dom}"/>'
    b += f'<path d="M {cx-R} {cy} A {R} {R} 0 0 1 {cx-6} {cy+R-2}" fill="none" stroke="{dom}" stroke-width="3" opacity="0.5"/>'
    # the daily log stack inside the loop (repeated rhythm) — charcoal accent
    for i in range(4):
        yy = cy - 46 + i*30
        w = 150 - i*8
        b += f'<line x1="{cx-w/2}" y1="{yy}" x2="{cx+w/2}" y2="{yy}" stroke="{acc}" stroke-width="{7 if i==0 else 3}"/>'
        b += f'<circle cx="{cx-w/2-16}" cy="{yy}" r="4.5" fill="{dom}"/>'
    b += text(cx, cy+96, "curate → integrate → prune", 18, acc, MONO, 700, 1, anchor="middle")
    # title — journal serif, lowercase
    b += text(M-3, 780, "the loop", 118, dom, SERIF, 700, 0, italic=True)
    b += text(M-3, 888, "never ends", 118, acc, SERIF, 700, 0, italic=True)
    b += text(M+3, 300, "at the frontier, learning turns into keeping up.", 20, acc, SERIF, 400, 0, italic=True)
    b += footer(acc, "08 / 08")
    return frame(defs, b, sub), dict(mode="chromatic + black", ink=f"Mint Green {MINT} + Warm Charcoal {WCHAR}",
        layout="editorial journal", type="literary serif + mono label", process="dot halftone loop",
        focal="a refresh loop enclosing the daily log stack")

# ===========================================================================
ITEMS = [
    ("00-atlas-site",       "GenAI Evolution Atlas (site cover)",       c_site),
    ("01-stage00-foundations", "Stage 0 — Foundations",                 c_stage0),
    ("02-stage01-transformer", "Stage 1 — The Transformer",             c_stage1),
    ("03-stage02-pretraining", "Stage 2 — The Pretraining Era",         c_stage2),
    ("04-stage03-scale",       "Stage 3 — Scale & Emergence",           c_stage3),
    ("05-stage04-efficiency",  "Stage 4 — Efficiency & Building Blocks", c_stage4),
    ("06-stage05-alignment",   "Stage 5 — Alignment & Post-training",   c_stage5),
    ("07-stage06-multimodal",  "Stage 6 — Multimodality",               c_stage6),
    ("08-stage07-frontier",    "Stage 7 — Frontier Systems",            c_stage7),
    ("09-stage08-staying-current", "Stage 8 — Staying Current",         c_stage8),
]

recipes = []
for slug, title, fn in ITEMS:
    svg, rec = fn()
    with open(os.path.join(OUT, slug + ".html"), "w") as f:
        f.write(html(svg))
    with open(os.path.join(OUT, slug + ".svg"), "w") as f:
        f.write(svg)
    rec["slug"] = slug; rec["title"] = title
    recipes.append(rec)
    print("built", slug)

with open(os.path.join(OUT, "recipes.json"), "w") as f:
    json.dump(recipes, f, indent=2)
print("done:", len(recipes), "thumbnails")
