#!/usr/bin/env python3
"""
Generate Unified 300 DPI Composite Visual Cards for the Keynote Presentation.
Combines Theoretical Algorithmic Proofs with Real Live Web GUI Telemetry Cards.
"""

import os
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "presentation", "assets")
CROPS_DIR = os.path.join(ASSETS_DIR, "gui_crops")
COMPOSITES_DIR = os.path.join(ASSETS_DIR, "composites")
os.makedirs(COMPOSITES_DIR, exist_ok=True)

# Canvas Dimensions: 2220 x 1580 px (equivalent to 7.4" x 5.26" at 300 DPI)
W_CANVAS = 2220
H_CANVAS = 1580
BG_COLOR = (11, 16, 32)       # #0B1020
CARD_BG = (18, 26, 47)        # #121A2F
BORDER_COLOR = (30, 44, 72)   # #1E2C48
CYAN = (0, 217, 255)          # #00D9FF
GREEN = (0, 230, 118)         # #00E676

def create_base_canvas():
    return Image.new("RGB", (W_CANVAS, H_CANVAS), BG_COLOR)

def draw_header_pill(draw, text, x, y, w, h, outline_color=BORDER_COLOR, text_color=CYAN):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=8, fill=CARD_BG, outline=outline_color, width=2)
    # Simple centered text
    draw.text((x + 15, y + 8), text, fill=text_color)

# -----------------------------------------------------------------------------
# SLIDE 1: Hero Architecture + Live Telemetry Banner
# -----------------------------------------------------------------------------
def make_slide1_composite():
    canvas = create_base_canvas()
    draw = ImageDraw.Draw(canvas)

    # Top: Architecture Schematic (Height: ~1050 px)
    arch_path = os.path.join(ASSETS_DIR, "slide1_system_architecture.png")
    if os.path.exists(arch_path):
        arch_im = Image.open(arch_path).convert("RGB")
        arch_im = arch_im.resize((W_CANVAS, 1060), Image.Resampling.LANCZOS)
        canvas.paste(arch_im, (0, 0))

    # Bottom Banner Container: Live Web GUI Telemetry Banner
    tel_path = os.path.join(CROPS_DIR, "ui_telemetry_banner.png")
    if os.path.exists(tel_path):
        tel_im = Image.open(tel_path).convert("RGB")
        # Resize nicely to fit bottom
        tw, th = W_CANVAS - 40, 460
        tel_im = tel_im.resize((tw, th), Image.Resampling.LANCZOS)
        # Add subtle container border
        draw.rounded_rectangle([18, 1090, 18 + tw + 4, 1090 + th + 4], radius=10, fill=CARD_BG, outline=BORDER_COLOR, width=2)
        canvas.paste(tel_im, (20, 1092))

    out_p = os.path.join(COMPOSITES_DIR, "slide1_composite.png")
    canvas.save(out_p, quality=95)
    print("[+] Created slide1_composite.png")

# -----------------------------------------------------------------------------
# SLIDE 3: Recurrence Trees + Live Sorting Workbench Card
# -----------------------------------------------------------------------------
def make_slide3_composite():
    canvas = create_base_canvas()
    draw = ImageDraw.Draw(canvas)

    # Left: Recurrence Trees (Width: ~1250 px)
    rec_path = os.path.join(ASSETS_DIR, "slide3_recurrence_trees.png")
    if os.path.exists(rec_path):
        rec_im = Image.open(rec_path).convert("RGB")
        rec_im = rec_im.resize((1280, H_CANVAS), Image.Resampling.LANCZOS)
        canvas.paste(rec_im, (0, 0))

    # Right: Live GUI Sorting Workbench Card
    sort_path = os.path.join(CROPS_DIR, "ui_sorting_workbench.png")
    if os.path.exists(sort_path):
        sort_im = Image.open(sort_path).convert("RGB")
        sw, sh = 880, 1480
        sort_im = sort_im.resize((sw, sh), Image.Resampling.LANCZOS)
        draw.rounded_rectangle([1300, 45, 1300 + sw + 4, 45 + sh + 4], radius=12, fill=CARD_BG, outline=BORDER_COLOR, width=2)
        canvas.paste(sort_im, (1302, 47))

    out_p = os.path.join(COMPOSITES_DIR, "slide3_composite.png")
    canvas.save(out_p, quality=95)
    print("[+] Created slide3_composite.png")

# -----------------------------------------------------------------------------
# SLIDE 4: KMP State Automaton + Live 4-Matcher GUI Scanner Card
# -----------------------------------------------------------------------------
def make_slide4_composite():
    canvas = create_base_canvas()
    draw = ImageDraw.Draw(canvas)

    # Top: KMP DFA Automaton
    str_path = os.path.join(ASSETS_DIR, "slide4_string_automaton.png")
    if os.path.exists(str_path):
        str_im = Image.open(str_path).convert("RGB")
        str_im = str_im.resize((W_CANVAS, 850), Image.Resampling.LANCZOS)
        canvas.paste(str_im, (0, 0))

    # Bottom: Live String Matcher UI Card
    mat_path = os.path.join(CROPS_DIR, "ui_string_matcher_card.png")
    if os.path.exists(mat_path):
        mat_im = Image.open(mat_path).convert("RGB")
        mw, mh = W_CANVAS - 40, 680
        mat_im = mat_im.resize((mw, mh), Image.Resampling.LANCZOS)
        draw.rounded_rectangle([18, 875, 18 + mw + 4, 875 + mh + 4], radius=10, fill=CARD_BG, outline=BORDER_COLOR, width=2)
        canvas.paste(mat_im, (20, 877))

    out_p = os.path.join(COMPOSITES_DIR, "slide4_composite.png")
    canvas.save(out_p, quality=95)
    print("[+] Created slide4_composite.png")

# -----------------------------------------------------------------------------
# SLIDE 5: Attack Topology Graph + Live Min-Cut Quarantine Card
# -----------------------------------------------------------------------------
def make_slide5_composite():
    canvas = create_base_canvas()
    draw = ImageDraw.Draw(canvas)

    # Left: Attack Topology Graph
    top_path = os.path.join(ASSETS_DIR, "slide5_attack_topology.png")
    if os.path.exists(top_path):
        top_im = Image.open(top_path).convert("RGB")
        top_im = top_im.resize((1260, H_CANVAS), Image.Resampling.LANCZOS)
        canvas.paste(top_im, (0, 0))

    # Right: Live GUI Min-Cut Card
    cut_path = os.path.join(CROPS_DIR, "ui_mincut_card.png")
    if os.path.exists(cut_path):
        cut_im = Image.open(cut_path).convert("RGB")
        cw, ch = 900, 1480
        cut_im = cut_im.resize((cw, ch), Image.Resampling.LANCZOS)
        draw.rounded_rectangle([1290, 45, 1290 + cw + 4, 45 + ch + 4], radius=12, fill=CARD_BG, outline=BORDER_COLOR, width=2)
        canvas.paste(cut_im, (1292, 47))

    out_p = os.path.join(COMPOSITES_DIR, "slide5_composite.png")
    canvas.save(out_p, quality=95)
    print("[+] Created slide5_composite.png")

# -----------------------------------------------------------------------------
# SLIDE 6: State Space Tree + Live Knapsack B&B Card
# -----------------------------------------------------------------------------
def make_slide6_composite():
    canvas = create_base_canvas()
    draw = ImageDraw.Draw(canvas)

    # Left: State Space Search Tree
    sst_path = os.path.join(ASSETS_DIR, "slide6_state_space_tree.png")
    if os.path.exists(sst_path):
        sst_im = Image.open(sst_path).convert("RGB")
        sst_im = sst_im.resize((1260, H_CANVAS), Image.Resampling.LANCZOS)
        canvas.paste(sst_im, (0, 0))

    # Right: Live GUI Knapsack B&B Policies Card
    bb_path = os.path.join(CROPS_DIR, "ui_knapsack_bb_card.png")
    if os.path.exists(bb_path):
        bb_im = Image.open(bb_path).convert("RGB")
        bw, bh = 900, 1480
        bb_im = bb_im.resize((bw, bh), Image.Resampling.LANCZOS)
        draw.rounded_rectangle([1290, 45, 1290 + bw + 4, 45 + bh + 4], radius=12, fill=CARD_BG, outline=BORDER_COLOR, width=2)
        canvas.paste(bb_im, (1292, 47))

    out_p = os.path.join(COMPOSITES_DIR, "slide6_composite.png")
    canvas.save(out_p, quality=95)
    print("[+] Created slide6_composite.png")

# -----------------------------------------------------------------------------
# SLIDE 8: Empirical Dashboard + Live Workbench Telemetry & N-Queens Grid
# -----------------------------------------------------------------------------
def make_slide8_composite():
    canvas = create_base_canvas()
    draw = ImageDraw.Draw(canvas)

    # Left: Benchmark Dashboard
    bench_path = os.path.join(ASSETS_DIR, "slide8_empirical_dashboard.png")
    if os.path.exists(bench_path):
        bench_im = Image.open(bench_path).convert("RGB")
        bench_im = bench_im.resize((1180, H_CANVAS), Image.Resampling.LANCZOS)
        canvas.paste(bench_im, (0, 0))

    # Right Top: Live N-Queens Honeypot Grid Card
    nq_path = os.path.join(CROPS_DIR, "ui_nqueens_card.png")
    if os.path.exists(nq_path):
        nq_im = Image.open(nq_path).convert("RGB")
        nw, nh = 970, 850
        nq_im = nq_im.resize((nw, nh), Image.Resampling.LANCZOS)
        draw.rounded_rectangle([1220, 45, 1220 + nw + 4, 45 + nh + 4], radius=12, fill=CARD_BG, outline=BORDER_COLOR, width=2)
        canvas.paste(nq_im, (1222, 47))

    # Right Bottom: Live Telemetry Banner Strip
    tel_path = os.path.join(CROPS_DIR, "ui_telemetry_banner.png")
    if os.path.exists(tel_path):
        tel_im = Image.open(tel_path).convert("RGB")
        tw, th = 970, 580
        tel_im = tel_im.resize((tw, th), Image.Resampling.LANCZOS)
        draw.rounded_rectangle([1220, 930, 1220 + tw + 4, 930 + th + 4], radius=12, fill=CARD_BG, outline=BORDER_COLOR, width=2)
        canvas.paste(tel_im, (1222, 932))

    out_p = os.path.join(COMPOSITES_DIR, "slide8_composite.png")
    canvas.save(out_p, quality=95)
    print("[+] Created slide8_composite.png")

if __name__ == "__main__":
    print("[*] Generating 300 DPI Unified Composite Visual Assets...")
    make_slide1_composite()
    make_slide3_composite()
    make_slide4_composite()
    make_slide5_composite()
    make_slide6_composite()
    make_slide8_composite()
    print("[+] All composite visual cards successfully created!")
