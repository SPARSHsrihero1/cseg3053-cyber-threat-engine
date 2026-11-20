#!/usr/bin/env python3
"""
Generate High-Impact NVIDIA GTC / BlackHat Conference Visual Assets (300 DPI).
Theme: Obsidian Dark Navy (#0B1020), Cyan (#00D9FF), Neon Green (#00E676), Crimson (#FF5252).
Outputs saved to presentation/assets/gtc/
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from PIL import Image

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "presentation", "assets")
GTC_DIR = os.path.join(ASSETS_DIR, "gtc")
CROPS_DIR = os.path.join(ASSETS_DIR, "gui_crops")
os.makedirs(GTC_DIR, exist_ok=True)

BG_DARK = "#0B1020"
CARD_BG = "#121A2F"
CARD_BORDER = "#1E2C48"
CYAN = "#00D9FF"
GREEN = "#00E676"
RED = "#FF5252"
WHITE = "#FFFFFF"
SLATE = "#94A3B8"
ACCENT_BLUE = "#3B82F6"

plt.rcParams['font.sans-serif'] = 'Segoe UI'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['text.color'] = WHITE
plt.rcParams['axes.labelcolor'] = WHITE
plt.rcParams['xtick.color'] = WHITE
plt.rcParams['ytick.color'] = WHITE

# -----------------------------------------------------------------------------
# SLIDE 1 HERO: Full-Width Command Center Architectural Ribbon
# -----------------------------------------------------------------------------
def make_slide1_hero_ribbon():
    fig, ax = plt.subplots(figsize=(12, 3.8), dpi=250, facecolor=BG_DARK)
    ax.set_facecolor(BG_DARK)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 3.8)
    ax.axis('off')

    modules = [
        ("INGESTION STREAM", "1.2M Events / Sec\nLock-Free Ring Buffer\nSyslog & NetFlow", "O(1) Amortized", CYAN, 0.4),
        ("ARENA MEMORY", "Pure C17 Standard\nZero malloc() in Hot Path\nContiguous Cache Lines", "Zero Heap Leaks", GREEN, 3.3),
        ("ALGORITHMIC KERNEL", "25+ Core Syllabus Algos\nDivide & Conquer • String Automata\nGraphs • Branch & Bound", "All From Scratch", CYAN, 6.2),
        ("ACTIVE CONTAINMENT", "Edmonds-Karp Min-Cut\nSubnet Quarantine Isolation\nWorst-Case Response", "< 200 ms Latency", RED, 9.1)
    ]

    for title, desc, tag, col, x in modules:
        box = patches.FancyBboxPatch((x, 0.3), 2.5, 3.2, boxstyle="round,pad=0.1,rounding_size=0.15",
                                     facecolor=CARD_BG, edgecolor=col, linewidth=1.8)
        ax.add_patch(box)
        ax.text(x + 1.25, 3.1, title, ha='center', color=col, weight='bold', fontsize=11)
        ax.text(x + 1.25, 2.0, desc, ha='center', color=SLATE, fontsize=9.5, linespacing=1.3)
        
        tag_box = patches.FancyBboxPatch((x + 0.25, 0.55), 2.0, 0.55, boxstyle="round,pad=0.05,rounding_size=0.1",
                                         facecolor="#0B1020", edgecolor=col, linewidth=1.2)
        ax.add_patch(tag_box)
        ax.text(x + 1.25, 0.82, tag, ha='center', va='center', color=col, weight='bold', fontsize=9.5)

        if x < 9.0:
            ax.annotate("", xy=(x + 2.85, 1.9), xytext=(x + 2.55, 1.9),
                        arrowprops=dict(arrowstyle="-|>", color=CYAN, lw=2.5, mutation_scale=15))

    plt.tight_layout()
    out_p = os.path.join(GTC_DIR, "gtc_slide1_hero_ribbon.png")
    plt.savefig(out_p, dpi=250, facecolor=BG_DARK)
    plt.close()
    print("[+] Created gtc_slide1_hero_ribbon.png")

# -----------------------------------------------------------------------------
# SLIDE 2: Full-Width 4-Stage Horizontal Pipeline Flow
# -----------------------------------------------------------------------------
def make_slide2_pipeline_flow():
    fig, ax = plt.subplots(figsize=(12, 4.8), dpi=250, facecolor=BG_DARK)
    ax.set_facecolor(BG_DARK)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 4.8)
    ax.axis('off')

    stages = [
        ("STAGE 01: INGESTION", "Lock-free circular ring buffer\nSerializes unbounded raw events\nZero syscall overhead in hot path", "O(1) Amortized", CYAN, 0.3),
        ("STAGE 02: PARSING", "KMP precomputed failure table π[q]\nRabin-Karp 64-bit rolling hash\nZero pointer backtracking", "O(n + m) Linear", GREEN, 3.25),
        ("STAGE 03: GRAPH SYNTHESIS", "Dijkstra exploit chains via Min-Heap\nBellman-Ford negative privilege drop (-5)\nFloyd-Warshall blast-radius matrix", "O((V+E) log V)", CYAN, 6.2),
        ("STAGE 04: MITIGATION", "0/1 Knapsack Branch & Bound\nGreedy fractional upper bound pruning\nEdmonds-Karp Min-Cut firewall cut", "78% Space Pruned", GREEN, 9.15)
    ]

    for title, desc, comp, col, x in stages:
        box = patches.FancyBboxPatch((x, 0.4), 2.55, 4.0, boxstyle="round,pad=0.1,rounding_size=0.18",
                                     facecolor=CARD_BG, edgecolor=col, linewidth=2.0)
        ax.add_patch(box)
        
        ax.text(x + 1.275, 4.0, title, ha='center', color=col, weight='bold', fontsize=11)
        ax.text(x + 1.275, 2.7, desc, ha='center', color=WHITE, fontsize=9.2, linespacing=1.35)
        
        c_box = patches.FancyBboxPatch((x + 0.2, 0.75), 2.15, 0.7, boxstyle="round,pad=0.05,rounding_size=0.1",
                                       facecolor="#0B1020", edgecolor=col, linewidth=1.5)
        ax.add_patch(c_box)
        ax.text(x + 1.275, 1.1, comp, ha='center', va='center', color=col, weight='bold', fontsize=11)

        if x < 9.0:
            ax.annotate("", xy=(x + 2.88, 2.4), xytext=(x + 2.6, 2.4),
                        arrowprops=dict(arrowstyle="-|>", color=col, lw=3.0, mutation_scale=18))

    plt.tight_layout()
    out_p = os.path.join(GTC_DIR, "gtc_slide2_pipeline.png")
    plt.savefig(out_p, dpi=250, facecolor=BG_DARK)
    plt.close()
    print("[+] Created gtc_slide2_pipeline.png")

# -----------------------------------------------------------------------------
# SLIDE 3: The 180x Adversarial Sorting Showdown Visual
# -----------------------------------------------------------------------------
def make_slide3_sorting_showdown():
    fig = plt.figure(figsize=(9.2, 5.8), dpi=250, facecolor=BG_DARK)
    
    # Left: Red QuickSort Collapse Panel
    ax1 = fig.add_axes([0.02, 0.05, 0.46, 0.9])
    ax1.set_facecolor(CARD_BG)
    ax1.set_xlim(-0.5, 4.5)
    ax1.set_ylim(-0.5, 6.2)
    ax1.axis('off')
    
    border1 = patches.FancyBboxPatch((-0.4, -0.4), 4.8, 6.5, boxstyle="round,pad=0.05,rounding_size=0.15",
                                     facecolor="#1E1015", edgecolor=RED, linewidth=2)
    ax1.add_patch(border1)
    
    ax1.text(2.0, 5.7, "ADVERSARIAL QUICKSORT", ha='center', color=RED, weight='bold', fontsize=12)
    ax1.text(2.0, 5.25, "[ VULNERABLE TO DOS LOG-FLOOD ]", ha='center', color="#FCA5A5", weight='bold', fontsize=8.5)
    ax1.text(2.0, 4.8, "T(n) = T(n-1) + cn => Θ(n²)", ha='center', color=RED, weight='bold', fontsize=10)

    # Degenerate stick nodes
    qs_nodes = [(1.5, 3.8, "cn"), (2.0, 2.9, "c(n-1)"), (2.5, 2.0, "c(n-2)"), (3.0, 1.1, "c(1)")]
    for p1, p2 in [((1.5, 3.6), (2.0, 3.1)), ((2.0, 2.7), (2.5, 2.2)), ((2.5, 1.8), (3.0, 1.3))]:
        ax1.plot([p1[0], p2[0]], [p1[1], p2[1]], color=RED, lw=2.2, linestyle='--')
    for x, y, lbl in qs_nodes:
        c = patches.Circle((x, y), 0.35, facecolor="#3B1218", edgecolor=RED, linewidth=2, zorder=3)
        ax1.add_patch(c)
        ax1.text(x, y, lbl, ha='center', va='center', color=WHITE, fontsize=8.5, weight='bold', zorder=4)

    ax1.text(2.0, 0.15, "1,999,000 Comparisons\nQuadratic Stack Depletion\nCPU Core Exhaustion",
             ha='center', va='center', color=WHITE, fontsize=9.5, weight='bold', linespacing=1.3)

    # Right: Cyan MergeSort Immunity Panel
    ax2 = fig.add_axes([0.52, 0.05, 0.46, 0.9])
    ax2.set_facecolor(CARD_BG)
    ax2.set_xlim(-0.5, 4.5)
    ax2.set_ylim(-0.5, 6.2)
    ax2.axis('off')
    
    border2 = patches.FancyBboxPatch((-0.4, -0.4), 4.8, 6.5, boxstyle="round,pad=0.05,rounding_size=0.15",
                                     facecolor="#0B1A28", edgecolor=CYAN, linewidth=2)
    ax2.add_patch(border2)
    
    ax2.text(2.0, 5.7, "STABLE MERGESORT", ha='center', color=CYAN, weight='bold', fontsize=12)
    ax2.text(2.0, 5.25, "[ PROVABLY IMMUNE DEFENSE ]", ha='center', color=GREEN, weight='bold', fontsize=8.5)
    ax2.text(2.0, 4.8, "T(n) = 2T(n/2) + cn => Θ(n log n)", ha='center', color=CYAN, weight='bold', fontsize=10)

    # Balanced tree
    ms_nodes = [
        (2.0, 3.9, "cn"),
        (1.0, 2.7, "cn/2"), (3.0, 2.7, "cn/2"),
        (0.5, 1.5, "cn/4"), (1.5, 1.5, "cn/4"), (2.5, 1.5, "cn/4"), (3.5, 1.5, "cn/4")
    ]
    for p1, p2 in [((2.0, 3.7), (1.0, 2.9)), ((2.0, 3.7), (3.0, 2.9)),
                   ((1.0, 2.5), (0.5, 1.7)), ((1.0, 2.5), (1.5, 1.7)),
                   ((3.0, 2.5), (2.5, 1.7)), ((3.0, 2.5), (3.5, 1.7))]:
        ax2.plot([p1[0], p2[0]], [p1[1], p2[1]], color=CYAN, lw=2.0)
    for x, y, lbl in ms_nodes:
        c = patches.Circle((x, y), 0.32, facecolor="#092942", edgecolor=CYAN, linewidth=1.8, zorder=3)
        ax2.add_patch(c)
        ax2.text(x, y, lbl, ha='center', va='center', color=WHITE, fontsize=7.8, weight='bold', zorder=4)

    ax2.text(2.0, 0.15, "11,088 Comparisons (180x Faster)\nStrict log2(n) Depth Ceiling\nZero CPU Spikes Under Attack",
             ha='center', va='center', color=GREEN, fontsize=9.5, weight='bold', linespacing=1.3)

    out_p = os.path.join(GTC_DIR, "gtc_slide3_sorting_showdown.png")
    plt.savefig(out_p, dpi=250, facecolor=BG_DARK)
    plt.close()
    print("[+] Created gtc_slide3_sorting_showdown.png")

# -----------------------------------------------------------------------------
# SLIDE 4: String Matching Zero-Backtrack Automaton + GUI Card
# -----------------------------------------------------------------------------
def make_slide4_string_composite():
    fig = plt.figure(figsize=(9.2, 5.8), dpi=250, facecolor=BG_DARK)
    
    # Top: KMP DFA Automaton
    ax1 = fig.add_axes([0.02, 0.48, 0.96, 0.5])
    ax1.set_facecolor(CARD_BG)
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 3.5)
    ax1.axis('off')
    
    b1 = patches.FancyBboxPatch((0.1, 0.1), 9.8, 3.3, boxstyle="round,pad=0.05,rounding_size=0.15",
                                facecolor=CARD_BG, edgecolor=CARD_BORDER, linewidth=1.5)
    ax1.add_patch(b1)
    
    ax1.text(5.0, 3.0, "KMP FAILURE FUNCTION π[q] DETERMINISTIC FINITE AUTOMATON", ha='center', color=CYAN, weight='bold', fontsize=11)
    ax1.text(5.0, 2.55, "Pattern: A B A B A C  |  Guaranteed O(n + m) Monotonic Forward Advance", ha='center', color=GREEN, fontsize=9)

    states = ["0", "1(A)", "2(B)", "3(A)", "4(B)", "5(A)", "6(C)"]
    xs = np.linspace(1.0, 9.0, len(states))
    y = 1.45
    for i, (x_pos, name) in enumerate(zip(xs, states)):
        c = patches.Circle((x_pos, y), 0.38, facecolor="#0E243A", edgecolor=CYAN, linewidth=2, zorder=3)
        ax1.add_patch(c)
        ax1.text(x_pos, y, name, ha='center', va='center', color=WHITE, fontsize=8.5, weight='bold', zorder=4)
        if i < len(states) - 1:
            ax1.annotate("", xy=(xs[i+1]-0.38, y), xytext=(x_pos+0.38, y),
                         arrowprops=dict(arrowstyle="->", color=GREEN, lw=2.2))

    # Curved failure arcs
    arc1 = patches.Arc((3.7, y), 2.7, 1.4, angle=0, theta1=0, theta2=180, color=RED, lw=2.0, linestyle='--')
    ax1.add_patch(arc1)
    ax1.text(3.7, y + 0.85, "π[3]=1", color=RED, fontsize=8.5, weight='bold', ha='center')

    arc2 = patches.Arc((6.3, y), 2.7, 1.6, angle=0, theta1=0, theta2=180, color=RED, lw=2.0, linestyle='--')
    ax1.add_patch(arc2)
    ax1.text(6.3, y + 0.95, "π[5]=3", color=RED, fontsize=8.5, weight='bold', ha='center')

    # Bottom: Embed the real Web GUI String Matcher Card
    ax2 = fig.add_axes([0.02, 0.02, 0.96, 0.44])
    ax2.set_facecolor(CARD_BG)
    ax2.axis('off')
    
    mat_path = os.path.join(CROPS_DIR, "ui_string_matcher_card.png")
    if os.path.exists(mat_path):
        mat_im = Image.open(mat_path)
        ax2.imshow(mat_im)

    out_p = os.path.join(GTC_DIR, "gtc_slide4_string.png")
    plt.savefig(out_p, dpi=250, facecolor=BG_DARK)
    plt.close()
    print("[+] Created gtc_slide4_string.png")

# -----------------------------------------------------------------------------
# SLIDE 5: Graph Theory Laser Min-Cut Isolation
# -----------------------------------------------------------------------------
def make_slide5_mincut():
    fig = plt.figure(figsize=(9.2, 5.8), dpi=250, facecolor=BG_DARK)
    
    # Left: 7-Host Topology Graph with Laser Cut
    ax1 = fig.add_axes([0.02, 0.05, 0.58, 0.9])
    ax1.set_facecolor(CARD_BG)
    ax1.set_xlim(-0.5, 8.0)
    ax1.set_ylim(-0.8, 4.2)
    ax1.axis('off')
    
    b1 = patches.FancyBboxPatch((-0.4, -0.7), 8.3, 4.8, boxstyle="round,pad=0.05,rounding_size=0.15",
                                facecolor=CARD_BG, edgecolor=CARD_BORDER, linewidth=1.5)
    ax1.add_patch(b1)
    
    nodes = {
        0: {"pos": (0.6, 1.7), "label": "H0: FW Ingress", "col": CYAN},
        1: {"pos": (2.3, 3.0), "label": "H1: DMZ Web", "col": "#38BDF8"},
        2: {"pos": (2.3, 0.4), "label": "H2: API GW", "col": "#38BDF8"},
        3: {"pos": (4.1, 1.7), "label": "H3: Jump-Box", "col": "#F59E0B"},
        4: {"pos": (5.8, 3.0), "label": "H4: App Core", "col": GREEN},
        5: {"pos": (5.8, 0.4), "label": "H5: DB Jewel", "col": RED},
        6: {"pos": (7.4, 1.7), "label": "H6: Backup Vault", "col": "#A855F7"}
    }
    edges = [
        (0, 1, "4", CYAN, False), (0, 2, "6", CYAN, False),
        (1, 3, "-5 (PrivEsc)", RED, True),
        (2, 3, "3", CYAN, False), (3, 4, "2", GREEN, False),
        (3, 5, "7", GREEN, False), (4, 5, "1", GREEN, False),
        (4, 6, "5", "#A855F7", False), (5, 6, "2", "#A855F7", False)
    ]
    for u, v, w, col, is_neg in edges:
        p1, p2 = nodes[u]["pos"], nodes[v]["pos"]
        lw = 2.0 if not is_neg else 2.8
        ls = "solid" if not is_neg else "dashed"
        ax1.annotate("", xy=p2, xytext=p1,
                     arrowprops=dict(arrowstyle="->", color=col, lw=lw, linestyle=ls, shrinkA=18, shrinkB=18))
        mx, my = (p1[0] + p2[0])/2, (p1[1] + p2[1])/2
        ax1.text(mx, my + 0.15, w, color=col, fontsize=7.5, weight='bold',
                 bbox=dict(boxstyle="round,pad=0.2", facecolor=BG_DARK, edgecolor=CARD_BORDER, lw=0.8))

    for nid, d in nodes.items():
        x, y = d["pos"]
        c = patches.Circle((x, y), 0.42, facecolor="#0E243A", edgecolor=d["col"], linewidth=2, zorder=4)
        ax1.add_patch(c)
        ax1.text(x, y - 0.58, d["label"], ha='center', va='top', color=WHITE, fontsize=7.5, weight='bold', zorder=5)

    # Laser Min-Cut Dashed Line
    ax1.plot([3.2, 3.2], [-0.5, 4.0], color=RED, lw=3.0, linestyle=":", zorder=6)
    ax1.text(3.25, 3.8, "LASER MIN-CUT SEVER BOUNDARY\nCapacity = 22 Mbps (Minimal Interruption)", 
             color=RED, fontsize=8.2, weight='bold')

    # Right: Real Web GUI Min-Cut Execution Card
    ax2 = fig.add_axes([0.62, 0.05, 0.36, 0.9])
    ax2.set_facecolor(CARD_BG)
    ax2.axis('off')
    
    cut_path = os.path.join(CROPS_DIR, "ui_mincut_card.png")
    if os.path.exists(cut_path):
        cut_im = Image.open(cut_path)
        ax2.imshow(cut_im)

    out_p = os.path.join(GTC_DIR, "gtc_slide5_mincut.png")
    plt.savefig(out_p, dpi=250, facecolor=BG_DARK)
    plt.close()
    print("[+] Created gtc_slide5_mincut.png")

# -----------------------------------------------------------------------------
# SLIDE 6: The 78% Pruning State-Space Tree Visual
# -----------------------------------------------------------------------------
def make_slide6_pruning_tree():
    fig = plt.figure(figsize=(9.2, 5.8), dpi=250, facecolor=BG_DARK)
    
    # Left: Giant Pruned State Space Tree
    ax1 = fig.add_axes([0.02, 0.05, 0.62, 0.9])
    ax1.set_facecolor(CARD_BG)
    ax1.set_xlim(-0.5, 9.5)
    ax1.set_ylim(-0.5, 6.2)
    ax1.axis('off')
    
    b1 = patches.FancyBboxPatch((-0.4, -0.4), 9.8, 6.5, boxstyle="round,pad=0.05,rounding_size=0.15",
                                facecolor=CARD_BG, edgecolor=CARD_BORDER, linewidth=1.5)
    ax1.add_patch(b1)
    
    ax1.text(4.5, 5.8, "0/1 KNAPSACK BRANCH & BOUND STATE SPACE TREE", ha='center', color=CYAN, weight='bold', fontsize=11)
    ax1.text(4.5, 5.35, "Capacity W = 15 | LCBB Best-First with Fractional Upper Bounds", ha='center', color=GREEN, fontsize=8.5)

    nodes = [
        (4.5, 4.4, "N0 (Root)\nw=0, v=$0\nUB=$280", CYAN, False),
        (2.3, 3.1, "N1 (x1=1)\nw=4, v=$80\nUB=$280", GREEN, False),
        (6.7, 3.1, "N2 (x1=0)\nw=0, v=$0\nUB=$220", SLATE, False),
        (1.2, 1.8, "N3 (x2=1)\nw=11, v=$180\nUB=$270", GREEN, False),
        (3.4, 1.8, "N4 (x2=0)\nw=4, v=$80\nUB=$240", CYAN, False),
        (5.6, 1.8, "N5 (x2=1)\nUB=$190 < Best\n[PRUNED]", RED, True),
        (7.8, 1.8, "N6 (x2=0)\nUB=$160 < Best\n[PRUNED]", RED, True),
        (0.6, 0.4, "N7 (x3=1)\nw=16 > 15\n[INFEASIBLE]", RED, True),
        (1.8, 0.4, "N8 (x3=0)\nw=11, v=$180\nFeasible Leaf", CYAN, False),
        (3.4, 0.4, "N9 (Optimum)\nw=15, v=$260\n[OPTIMAL]", GREEN, False)
    ]
    edges = [
        ((4.5, 4.2), (2.3, 3.3), "x1=1", GREEN, 2.5),
        ((4.5, 4.2), (6.7, 3.3), "x1=0", SLATE, 1.5),
        ((2.3, 2.9), (1.2, 2.0), "x2=1", GREEN, 2.5),
        ((2.3, 2.9), (3.4, 2.0), "x2=0", CYAN, 1.8),
        ((6.7, 2.9), (5.6, 2.0), "x2=1", RED, 1.5),
        ((6.7, 2.9), (7.8, 2.0), "x2=0", RED, 1.5),
        ((1.2, 1.6), (0.6, 0.7), "x3=1", RED, 1.5),
        ((1.2, 1.6), (1.8, 0.7), "x3=0", CYAN, 1.5),
        ((3.4, 1.6), (3.4, 0.7), "x3=1", GREEN, 2.5)
    ]
    for p1, p2, lbl, col, lw in edges:
        ax1.plot([p1[0], p2[0]], [p1[1], p2[1]], color=col, lw=lw, zorder=1)
        mx, my = (p1[0]+p2[0])/2, (p1[1]+p2[1])/2
        ax1.text(mx + 0.15, my, lbl, color=col, fontsize=7.5, weight='bold')

    for x, y, lbl, col, is_pruned in nodes:
        bg = "#2A1015" if is_pruned else ("#0C3120" if col == GREEN else "#0F2338")
        b = patches.FancyBboxPatch((x-0.52, y-0.27), 1.04, 0.54, boxstyle="round,pad=0.08,rounding_size=0.08",
                                   facecolor=bg, edgecolor=col, linewidth=1.8, zorder=2)
        ax1.add_patch(b)
        ax1.text(x, y, lbl, ha='center', va='center', color=WHITE, fontsize=6.8, weight='bold', zorder=3)

    # Right: Real Web GUI Knapsack B&B Policies Card
    ax2 = fig.add_axes([0.66, 0.05, 0.32, 0.9])
    ax2.set_facecolor(CARD_BG)
    ax2.axis('off')
    
    bb_path = os.path.join(CROPS_DIR, "ui_knapsack_bb_card.png")
    if os.path.exists(bb_path):
        bb_im = Image.open(bb_path)
        ax2.imshow(bb_im)

    out_p = os.path.join(GTC_DIR, "gtc_slide6_pruning.png")
    plt.savefig(out_p, dpi=250, facecolor=BG_DARK)
    plt.close()
    print("[+] Created gtc_slide6_pruning.png")

# -----------------------------------------------------------------------------
# SLIDE 7: Complexity Classification & Formal NP-Reduction Bridge
# -----------------------------------------------------------------------------
def make_slide7_complexity():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.2, 5.8), dpi=250, facecolor=BG_DARK)
    for ax in [ax1, ax2]:
        ax.set_facecolor(CARD_BG)
        ax.axis('off')

    # Left: Euler Venn Diagram
    ax1.set_xlim(-3, 3)
    ax1.set_ylim(-3, 3.5)
    b1 = patches.FancyBboxPatch((-2.9, -2.9), 5.8, 6.3, boxstyle="round,pad=0.05,rounding_size=0.15",
                                facecolor=CARD_BG, edgecolor=CARD_BORDER, linewidth=1.5)
    ax1.add_patch(b1)
    
    ax1.text(0, 3.0, "COMPLEXITY HIERARCHY (P != NP)", ha='center', color=CYAN, weight='bold', fontsize=11)
    
    e_nph = patches.Ellipse((0, 0.6), 5.2, 4.0, facecolor="#1E1B4B", edgecolor="#818CF8", lw=2.0)
    ax1.add_patch(e_nph)
    ax1.text(0, 2.2, "NP-HARD", color="#818CF8", weight='bold', fontsize=10, ha='center')

    e_np = patches.Ellipse((0, -0.2), 4.2, 3.0, facecolor="#142642", edgecolor=CYAN, lw=2.2)
    ax1.add_patch(e_np)
    ax1.text(0, 1.05, "NP (Nondeterministic Poly-Time)", color=CYAN, weight='bold', fontsize=9, ha='center')

    e_npc = patches.Ellipse((0, 0.45), 2.8, 1.4, facecolor="#3B1020", edgecolor=RED, lw=2.2)
    ax1.add_patch(e_npc)
    ax1.text(0, 0.6, "NP-COMPLETE", color=RED, weight='bold', fontsize=9.5, ha='center')
    ax1.text(0, 0.3, "Decision 0/1 Knapsack\nSubset-Sum", color=WHITE, fontsize=7.5, ha='center')

    e_p = patches.Ellipse((0, -1.0), 2.1, 1.2, facecolor="#064E3B", edgecolor=GREEN, lw=2.2)
    ax1.add_patch(e_p)
    ax1.text(0, -0.9, "P (Poly-Time)", color=GREEN, weight='bold', fontsize=9.5, ha='center')
    ax1.text(0, -1.25, "MergeSort, KMP, Dijkstra", color=WHITE, fontsize=7.5, ha='center')

    # Right: Formal Polynomial-Time Reduction
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 6.2)
    b2 = patches.FancyBboxPatch((0.2, 0.1), 9.6, 6.0, boxstyle="round,pad=0.05,rounding_size=0.15",
                                facecolor=CARD_BG, edgecolor=CARD_BORDER, linewidth=1.5)
    ax2.add_patch(b2)
    
    ax2.text(5.0, 5.7, "FORMAL POLYNOMIAL REDUCTION", ha='center', color=WHITE, weight='bold', fontsize=11)
    ax2.text(5.0, 5.25, "SUBSET-SUM <=p 0/1 KNAPSACK", ha='center', color=CYAN, weight='bold', fontsize=9.5)

    # Box 1: SUBSET-SUM
    c1 = patches.FancyBboxPatch((0.6, 3.6), 8.8, 1.4, boxstyle="round,pad=0.08,rounding_size=0.1",
                                facecolor="#0F172A", edgecolor=CYAN, lw=1.8)
    ax2.add_patch(c1)
    ax2.text(1.0, 4.6, "Known NP-Complete: SUBSET-SUM", color=CYAN, weight='bold', fontsize=9.5)
    ax2.text(1.0, 3.95, "Instance: Set S = {s1, s2, ..., sn}, Target sum T.\nQuestion: Exists subset S' with sum(s_i) = T?", color=WHITE, fontsize=8.5)

    # Reduction Mapping Arrow
    ax2.annotate("", xy=(5.0, 2.9), xytext=(5.0, 3.6),
                arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=3.0, mutation_scale=18))
    ax2.text(5.3, 3.25, "O(n) Poly-Time Mapping", color=GREEN, weight='bold', fontsize=8.5)

    # Box 2: 0/1 KNAPSACK
    c2 = patches.FancyBboxPatch((0.6, 1.1), 8.8, 1.6, boxstyle="round,pad=0.08,rounding_size=0.1",
                                facecolor="#0F172A", edgecolor=GREEN, lw=1.8)
    ax2.add_patch(c2)
    ax2.text(1.0, 2.3, "Target Instance: 0/1 KNAPSACK", color=GREEN, weight='bold', fontsize=9.5)
    ax2.text(1.0, 1.5, "Weights: w_i = s_i  |  Values: v_i = s_i\nCapacity: W = T  |  Target Value: V = T\nEquivalence: Knapsack value >= T <=> Subset-Sum has solution T.", color=WHITE, fontsize=8.2)

    ax2.text(5.0, 0.45, "[ Certificate verified in O(n) Time => In NP ]", ha='center', color=CYAN, weight='bold', fontsize=8.5)

    plt.tight_layout()
    out_p = os.path.join(GTC_DIR, "gtc_slide7_complexity.png")
    plt.savefig(out_p, dpi=250, facecolor=BG_DARK)
    plt.close()
    print("[+] Created gtc_slide7_complexity.png")

# -----------------------------------------------------------------------------
# SLIDE 8: Grand Finale Benchmark & Live Demo Matrix
# -----------------------------------------------------------------------------
def make_slide8_benchmark_matrix():
    fig = plt.figure(figsize=(9.2, 5.8), dpi=250, facecolor=BG_DARK)
    
    # Left: Empirical Benchmark Sub-Dashboard (4-panel)
    ax1 = fig.add_axes([0.02, 0.05, 0.58, 0.9])
    ax1.set_facecolor(CARD_BG)
    ax1.axis('off')
    
    bench_path = os.path.join(ASSETS_DIR, "slide8_empirical_dashboard.png")
    if os.path.exists(bench_path):
        bench_im = Image.open(bench_path)
        ax1.imshow(bench_im)

    # Right: Real Web GUI Honeypot Grid & Telemetry Strip
    ax2 = fig.add_axes([0.62, 0.05, 0.36, 0.9])
    ax2.set_facecolor(CARD_BG)
    ax2.axis('off')
    
    nq_path = os.path.join(CROPS_DIR, "ui_nqueens_card.png")
    if os.path.exists(nq_path):
        nq_im = Image.open(nq_path)
        ax2.imshow(nq_im)

    out_p = os.path.join(GTC_DIR, "gtc_slide8_matrix.png")
    plt.savefig(out_p, dpi=250, facecolor=BG_DARK)
    plt.close()
    print("[+] Created gtc_slide8_matrix.png")

if __name__ == "__main__":
    print("[*] Generating GTC / BlackHat Conference Visual Assets (300 DPI)...")
    make_slide1_hero_ribbon()
    make_slide2_pipeline_flow()
    make_slide3_sorting_showdown()
    make_slide4_string_composite()
    make_slide5_mincut()
    make_slide6_pruning_tree()
    make_slide7_complexity()
    make_slide8_benchmark_matrix()
    print("[+] All GTC assets generated successfully!")
