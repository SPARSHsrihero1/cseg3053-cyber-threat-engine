#!/usr/bin/env python3
"""
Generate 1920x1080 Preview PNGs of all 8 slides for visual verification.
Saved to presentation/previews/
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "presentation", "assets")
PREVIEW_DIR = os.path.join(BASE_DIR, "presentation", "previews")
os.makedirs(PREVIEW_DIR, exist_ok=True)

from build_keynote_defense_deck import SLIDES_DATA

BG_DARK = "#0B1020"
CARD_BG = "#121A2F"
BORDER = "#1E2C48"
CYAN = "#00D9FF"
GREEN = "#00E676"
RED = "#FF5252"
WHITE = "#FFFFFF"
SLATE = "#94A3B8"

plt.rcParams['font.sans-serif'] = 'Segoe UI'
plt.rcParams['font.family'] = 'sans-serif'

def render_previews():
    for idx, d in enumerate(SLIDES_DATA):
        # 16:9 aspect ratio figure (13.333 x 7.5 inches at 150 DPI = 2000 x 1125 px)
        fig = plt.figure(figsize=(13.333, 7.5), dpi=150, facecolor=BG_DARK)
        ax = fig.add_axes([0, 0, 1, 1])
        ax.set_facecolor(BG_DARK)
        ax.set_xlim(0, 13.333)
        ax.set_ylim(0, 7.5)
        ax.axis('off')

        # Eyebrow
        ax.text(0.8, 7.0, d["eyebrow"], color=CYAN, weight='bold', fontsize=9.5)

        # Main Title
        ax.text(0.8, 6.45, d["title"], color=WHITE, weight='bold', fontsize=20)

        # Subtitle
        ax.text(0.8, 6.05, d["subtitle"], color=SLATE, fontsize=11)

        # Top Right Phase Badge
        badge = patches.FancyBboxPatch((10.8, 6.55), 1.8, 0.45, boxstyle="round,pad=0.08,rounding_size=0.1",
                                       facecolor=CARD_BG, edgecolor=BORDER, linewidth=1.5)
        ax.add_patch(badge)
        ax.text(11.7, 6.77, d["phase"], ha='center', va='center', color=CYAN, weight='bold', fontsize=9.5)

        # Left Column Glassmorphism Card
        left_card = patches.FancyBboxPatch((0.8, 0.5), 4.0, 5.42, boxstyle="square,pad=0",
                                          facecolor=CARD_BG, edgecolor=BORDER, linewidth=1.5)
        ax.add_patch(left_card)

        # KPI 1
        k_col1 = GREEN if tuple(d["kpi1_color"]) == (0, 230, 118) else CYAN
        ax.text(1.05, 5.3, d["kpi1_val"], color=k_col1, weight='bold', fontsize=32)
        ax.text(1.05, 4.85, d["kpi1_lbl"], color=SLATE, weight='bold', fontsize=7.5)

        # Divider 1
        ax.plot([1.05, 4.55], [4.65, 4.65], color=BORDER, lw=1.2)

        # KPI 2
        tup2 = tuple(d["kpi2_color"])
        k_col2 = GREEN if tup2 == (0, 230, 118) else (RED if tup2 == (255, 82, 82) else CYAN)
        ax.text(1.05, 4.0, d["kpi2_val"], color=k_col2, weight='bold', fontsize=20)
        ax.text(1.05, 3.65, d["kpi2_lbl"], color=SLATE, weight='bold', fontsize=7.5)

        # Divider 2
        ax.plot([1.05, 4.55], [3.45, 3.45], color=BORDER, lw=1.2)

        # Research Takeaway
        ax.text(1.05, 3.15, "RESEARCH TAKEAWAY", color=CYAN, weight='bold', fontsize=8.5)
        
        # Wrap takeaway into multi-line
        words = d["takeaway"].split()
        lines = []
        cur = []
        for w in words:
            cur.append(w)
            if len(" ".join(cur)) > 34:
                lines.append(" ".join(cur))
                cur = []
        if cur:
            lines.append(" ".join(cur))
        
        ax.text(1.05, 2.85, "\n".join(lines), color=WHITE, fontsize=9.5, va='top', linespacing=1.4)

        # Pills
        ax.text(1.05, 0.75, "  ".join(d["pills"]), color=GREEN, weight='bold', fontsize=7.5)

        # Right Column Container
        right_card = patches.FancyBboxPatch((5.0, 0.5), 7.533, 5.42, boxstyle="square,pad=0",
                                           facecolor=CARD_BG, edgecolor=BORDER, linewidth=1.5)
        ax.add_patch(right_card)

        # Diagram Image
        img_path = os.path.join(ASSETS_DIR, d["diagram"])
        if os.path.exists(img_path):
            img = Image.open(img_path)
            ax.imshow(img, extent=[5.08, 12.45, 0.58, 5.84], zorder=3)

        out_name = f"slide_preview_{idx+1}.png"
        out_file = os.path.join(PREVIEW_DIR, out_name)
        plt.savefig(out_file, dpi=150, facecolor=BG_DARK)
        plt.close()
        print(f"[+] Rendered preview: {out_file}")

if __name__ == "__main__":
    print("[*] Rendering slide preview PNGs...")
    render_previews()
    print("[+] All 8 slide previews rendered!")
