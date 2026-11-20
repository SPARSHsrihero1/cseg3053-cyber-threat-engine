#!/usr/bin/env python3
"""
Generate High-Resolution Professional Diagrams for CSEG3053 Master Presentation.
Theme: Cyber Dark SOC (Midnight Navy #0B1120, Cyan #00F0FF, Magenta #FF0055, Amber #F59E0B, Green #10B981).
Outputs saved to presentation/assets/
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "presentation", "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)

# Theme Colors
BG_DARK = "#0B1120"
CARD_BG = "#152033"
BORDER = "#223450"
CYAN = "#00F0FF"
MAGENTA = "#FF0055"
AMBER = "#F59E0B"
GREEN = "#10B981"
WHITE = "#FFFFFF"
MUTED = "#94A3B8"

plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['text.color'] = WHITE
plt.rcParams['axes.labelcolor'] = WHITE
plt.rcParams['xtick.color'] = WHITE
plt.rcParams['ytick.color'] = WHITE

# =============================================================================
# DIAGRAM 1: ATTACK TOPOLOGY GRAPH
# =============================================================================
def draw_attack_topology():
    fig, ax = plt.subplots(figsize=(8.5, 4.5), dpi=300, facecolor=BG_DARK)
    ax.set_facecolor(BG_DARK)
    ax.set_xlim(-0.5, 7.5)
    ax.set_ylim(-0.8, 3.8)
    ax.axis('off')

    nodes = {
        0: {"pos": (0.5, 1.5), "label": "H0: Perimeter FW\n(Entry)", "col": CYAN},
        1: {"pos": (2.2, 2.7), "label": "H1: DMZ Web 1\n(Nginx)", "col": "#38BDF8"},
        2: {"pos": (2.2, 0.3), "label": "H2: DMZ Web 2\n(API Gateway)", "col": "#38BDF8"},
        3: {"pos": (3.8, 1.5), "label": "H3: Jump-Box\n(Bastion)", "col": AMBER},
        4: {"pos": (5.4, 2.7), "label": "H4: Internal DB\n(Crown Jewel)", "col": MAGENTA},
        5: {"pos": (5.4, 0.3), "label": "H5: Domain AD\n(Kerberos)", "col": "#A855F7"},
        6: {"pos": (6.8, 1.5), "label": "H6: C2 Sinkhole\n(Attacker)", "col": "#EF4444"}
    }

    edges = [
        (0, 1, "w=10", CYAN, 2.0, False),
        (0, 2, "w=15", MUTED, 1.2, False),
        (1, 3, "w=8", CYAN, 2.5, False),
        (2, 3, "w=12", MUTED, 1.2, False),
        (3, 4, "w=14 (Dijkstra)", CYAN, 2.5, False),
        (3, 5, "w=20", MUTED, 1.2, False),
        (5, 4, "w=-5 (Root Priv)", MAGENTA, 2.5, True), # Negative edge
        (4, 6, "Cap=250 MB/s", "#EF4444", 2.5, False),
        (5, 6, "Cap=162 MB/s", "#EF4444", 2.0, False)
    ]

    for u, v, lbl, col, lw, is_dashed in edges:
        p1 = nodes[u]["pos"]
        p2 = nodes[v]["pos"]
        style = "arc3,rad=0.08" if is_dashed else "arc3,rad=0.0"
        ls = "--" if is_dashed else "-"
        ax.annotate("", xy=p2, xytext=p1,
                    arrowprops=dict(arrowstyle="->", color=col, lw=lw, ls=ls,
                                   connectionstyle=style, shrinkA=18, shrinkB=18))
        mx, my = (p1[0] + p2[0])/2, (p1[1] + p2[1])/2
        ax.text(mx, my + 0.15, lbl, color=col, fontsize=7.5, ha='center',
                bbox=dict(boxstyle="round,pad=0.2", facecolor=CARD_BG, edgecolor=BORDER, lw=0.8))

    # Min-Cut Line
    ax.plot([6.0, 6.0], [-0.5, 3.5], color=MAGENTA, ls=":", lw=2.5)
    ax.text(6.0, 3.6, "MINIMUM s-t CUT (SEVER HERE)", color=MAGENTA, fontsize=8, fontweight='bold', ha='center',
            bbox=dict(boxstyle="round,pad=0.2", facecolor=BG_DARK, edgecolor=MAGENTA, lw=1))

    # Draw Nodes
    for idx, d in nodes.items():
        x, y = d["pos"]
        circle = patches.Circle((x, y), 0.32, facecolor=CARD_BG, edgecolor=d["col"], lw=2.2, zorder=5)
        ax.add_patch(circle)
        ax.text(x, y, f"H{idx}", color=WHITE, fontsize=9.5, fontweight='bold', ha='center', va='center', zorder=6)
        ax.text(x, y - 0.45, d["label"], color=WHITE, fontsize=7, ha='center', va='top')

    plt.title("ENTERPRISE ATTACK TOPOLOGY: EXPLOIT PATHS, NEGATIVE EDGES & MIN-CUT",
              color=CYAN, fontsize=10, fontweight='bold', pad=12)
    plt.tight_layout()
    out_path = os.path.join(ASSETS_DIR, "attack_topology_graph.png")
    plt.savefig(out_path, dpi=300, facecolor=BG_DARK)
    plt.close()
    print(f"[+] Generated: {out_path}")

# =============================================================================
# DIAGRAM 2: RECURRENCE TREES (MERGESORT VS QUICKSORT)
# =============================================================================
def draw_recurrence_trees():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.5, 4.2), dpi=300, facecolor=BG_DARK)
    for ax in [ax1, ax2]:
        ax.set_facecolor(BG_DARK)
        ax.axis('off')

    # Tree 1: Balanced MergeSort Tree
    ax1.set_xlim(-0.5, 4.5)
    ax1.set_ylim(-0.5, 3.5)
    ax1.text(2.0, 3.3, "MergeSort Tree: T(n) = 2T(n/2) + cn", color=CYAN, fontsize=9.5, fontweight='bold', ha='center')

    # Root
    ax1.text(2.0, 2.6, "cn", bbox=dict(boxstyle="circle,pad=0.3", facecolor=CARD_BG, edgecolor=CYAN, lw=1.5), ha='center', fontsize=8.5)
    ax1.text(4.2, 2.6, "Work = cn", color=GREEN, fontsize=8, fontweight='bold', va='center')

    # Level 1
    ax1.plot([2.0, 1.0], [2.4, 1.7], color=BORDER, lw=1.2)
    ax1.plot([2.0, 3.0], [2.4, 1.7], color=BORDER, lw=1.2)
    ax1.text(1.0, 1.6, "cn/2", bbox=dict(boxstyle="circle,pad=0.25", facecolor=CARD_BG, edgecolor=CYAN, lw=1.2), ha='center', fontsize=7.5)
    ax1.text(3.0, 1.6, "cn/2", bbox=dict(boxstyle="circle,pad=0.25", facecolor=CARD_BG, edgecolor=CYAN, lw=1.2), ha='center', fontsize=7.5)
    ax1.text(4.2, 1.6, "Work = cn", color=GREEN, fontsize=8, fontweight='bold', va='center')

    # Level 2
    for parent_x in [1.0, 3.0]:
        for offset in [-0.4, 0.4]:
            ax1.plot([parent_x, parent_x + offset], [1.4, 0.7], color=BORDER, lw=1)
            ax1.text(parent_x + offset, 0.6, "cn/4", bbox=dict(boxstyle="circle,pad=0.2", facecolor=CARD_BG, edgecolor=CYAN, lw=1), ha='center', fontsize=6.5)
    ax1.text(4.2, 0.6, "Work = cn", color=GREEN, fontsize=8, fontweight='bold', va='center')

    # Summary
    ax1.text(2.0, -0.3, "Height = log2(n) | Total Work = cn * (log2 n + 1) = \u0398(n log n)\nMaster Theorem Case 2 Applies",
             color=GREEN, fontsize=8, ha='center', bbox=dict(boxstyle="round,pad=0.3", facecolor=CARD_BG, edgecolor=GREEN, lw=1))

    # Tree 2: Degenerate Adversarial QuickSort Tree
    ax2.set_xlim(-0.5, 4.5)
    ax2.set_ylim(-0.5, 3.5)
    ax2.text(2.0, 3.3, "Adversarial QuickSort: T(n) = T(n-1) + cn", color=MAGENTA, fontsize=9.5, fontweight='bold', ha='center')

    # Skewed chain
    ax2.text(1.2, 2.6, "cn", bbox=dict(boxstyle="circle,pad=0.3", facecolor=CARD_BG, edgecolor=MAGENTA, lw=1.5), ha='center', fontsize=8.5)
    ax2.text(3.8, 2.6, "Work = cn", color=MUTED, fontsize=8, va='center')

    ax2.plot([1.2, 1.6], [2.4, 1.7], color=BORDER, lw=1.2)
    ax2.text(1.6, 1.6, "c(n-1)", bbox=dict(boxstyle="circle,pad=0.25", facecolor=CARD_BG, edgecolor=MAGENTA, lw=1.2), ha='center', fontsize=7.5)
    ax2.text(3.8, 1.6, "Work = c(n-1)", color=MUTED, fontsize=8, va='center')

    ax2.plot([1.6, 2.0], [1.4, 0.7], color=BORDER, lw=1.2)
    ax2.text(2.0, 0.6, "c(n-2)", bbox=dict(boxstyle="circle,pad=0.25", facecolor=CARD_BG, edgecolor=MAGENTA, lw=1.2), ha='center', fontsize=7.5)
    ax2.text(3.8, 0.6, "Work = c(n-2)", color=MUTED, fontsize=8, va='center')

    ax2.text(2.0, -0.3, "Master Theorem Inapplicable (Subtractive, not Dividing)\nUnrolling Sum: c \u03a3 i = c * n(n+1)/2 = \u0398(n\u00b2) CRASH",
             color=MAGENTA, fontsize=8, ha='center', bbox=dict(boxstyle="round,pad=0.3", facecolor=CARD_BG, edgecolor=MAGENTA, lw=1))

    plt.tight_layout()
    out_path = os.path.join(ASSETS_DIR, "recurrence_trees.png")
    plt.savefig(out_path, dpi=300, facecolor=BG_DARK)
    plt.close()
    print(f"[+] Generated: {out_path}")

# =============================================================================
# DIAGRAM 3: BENCHMARK COMPARISON BAR CHARTS (180X & 4.5X SPEEDUPS)
# =============================================================================
def draw_benchmark_charts():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.5, 4.2), dpi=300, facecolor=BG_DARK)
    for ax in [ax1, ax2]:
        ax.set_facecolor(CARD_BG)
        ax.grid(color=BORDER, linestyle='--', linewidth=0.7, alpha=0.6)

    # Chart 1: Adversarial Sorting Comparisons (Logarithmic Scale)
    algos_sort = ['QuickSort (Det)\nAdversarial Last-Pivot', 'MergeSort (Stable)\nGuaranteed O(N log N)']
    comps_sort = [1999000, 11088]
    colors_sort = [MAGENTA, GREEN]

    bars1 = ax1.bar(algos_sort, comps_sort, color=colors_sort, width=0.45, edgecolor=BORDER, lw=1.2)
    ax1.set_yscale('log')
    ax1.set_ylabel('Exact Operation Comparisons (Log Scale)', fontsize=8.5, color=MUTED)
    ax1.set_title('Sorted Log Flood (N = 2,000):\n180x SPEEDUP with MergeSort', fontsize=9.5, fontweight='bold', color=CYAN, pad=10)

    for bar, val in zip(bars1, comps_sort):
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2.0, yval * 1.3, f"{val:,}\ncomps", ha='center', va='bottom', fontsize=8, fontweight='bold', color=WHITE)

    # Chart 2: Adversarial String Matching Comparisons
    algos_str = ['Naive Sliding\nWindow Matcher', 'Knuth-Morris-Pratt\n(KMP \u03c0 Array)']
    comps_str = [89919, 20004]
    colors_str = [AMBER, CYAN]

    bars2 = ax2.bar(algos_str, comps_str, color=colors_str, width=0.45, edgecolor=BORDER, lw=1.2)
    ax2.set_ylabel('Exact Comparisons Done', fontsize=8.5, color=MUTED)
    ax2.set_title('Pathological Attack ("AAAA...B", N = 10,000):\n4.5x SPEEDUP with KMP Linear Scan', fontsize=9.5, fontweight='bold', color=CYAN, pad=10)

    for bar, val in zip(bars2, comps_str):
        yval = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2.0, yval + 1800, f"{val:,}\ncomps", ha='center', va='bottom', fontsize=8, fontweight='bold', color=WHITE)

    plt.tight_layout()
    out_path = os.path.join(ASSETS_DIR, "benchmark_charts.png")
    plt.savefig(out_path, dpi=300, facecolor=BG_DARK)
    plt.close()
    print(f"[+] Generated: {out_path}")

# =============================================================================
# DIAGRAM 4: STATE-SPACE SEARCH & BRANCH-AND-BOUND PRUNING
# =============================================================================
def draw_state_space_tree():
    fig, ax = plt.subplots(figsize=(8.5, 4.5), dpi=300, facecolor=BG_DARK)
    ax.set_facecolor(BG_DARK)
    ax.set_xlim(-0.5, 8.5)
    ax.set_ylim(-0.5, 4.5)
    ax.axis('off')

    # Root Node
    ax.text(4.0, 4.0, "Root: (w=0, v=0)\nUpper Bound UB = 269.6",
            bbox=dict(boxstyle="round,pad=0.3", facecolor=CARD_BG, edgecolor=CYAN, lw=1.5), ha='center', fontsize=8)

    # Level 1: Include / Exclude Item 1 (w1=10, v1=60)
    ax.plot([4.0, 2.0], [3.6, 2.8], color=BORDER, lw=1.2)
    ax.plot([4.0, 6.0], [3.6, 2.8], color=BORDER, lw=1.2)

    ax.text(2.0, 2.7, "Include Playbook 1\nw=10, v=60\nUB = 269.6 [ACTIVE]",
            bbox=dict(boxstyle="round,pad=0.3", facecolor=CARD_BG, edgecolor=GREEN, lw=1.5), ha='center', fontsize=7.5)
    ax.text(6.0, 2.7, "Exclude Playbook 1\nw=0, v=0\nUB = 220.0 [LOW UB]",
            bbox=dict(boxstyle="round,pad=0.3", facecolor=CARD_BG, edgecolor=AMBER, lw=1.2), ha='center', fontsize=7.5)

    # Level 2
    ax.plot([2.0, 1.0], [2.2, 1.3], color=BORDER, lw=1)
    ax.plot([2.0, 3.0], [2.2, 1.3], color=BORDER, lw=1)

    ax.text(1.0, 1.2, "Include Playbook 2\nw=25, v=140\nUB = 250.0 [OPTIMAL PATH]",
            bbox=dict(boxstyle="round,pad=0.25", facecolor=CARD_BG, edgecolor=GREEN, lw=1.5), ha='center', fontsize=7)
    ax.text(3.0, 1.2, "Exclude Playbook 2\nw=10, v=60\nUB = 210.0 [SUB-OPTIMAL]",
            bbox=dict(boxstyle="round,pad=0.25", facecolor=CARD_BG, edgecolor=AMBER, lw=1), ha='center', fontsize=7)

    # Pruned Subtree
    ax.plot([6.0, 5.0], [2.2, 1.3], color=BORDER, lw=1)
    ax.plot([6.0, 7.0], [2.2, 1.3], color=MAGENTA, lw=1.5, ls="--")

    ax.text(5.0, 1.2, "Capacity Exceeded\nw > 40 min SLA\n[PRUNED: INFEASIBLE]",
            bbox=dict(boxstyle="round,pad=0.25", facecolor=CARD_BG, edgecolor=MAGENTA, lw=1.5), ha='center', fontsize=7, color=MAGENTA)
    ax.text(7.0, 1.2, "UB <= Current Best\nUB = 180 <= 230\n[PRUNED: BOUNDING]",
            bbox=dict(boxstyle="round,pad=0.25", facecolor=CARD_BG, edgecolor=MAGENTA, lw=1.5), ha='center', fontsize=7, color=MAGENTA)

    ax.text(4.0, 0.0, "LEAST-COST (LC-BB) ADVANTAGE: Priority Queue explores node with highest Upper Bound first,\npruning branches before generating them (Evaluated only 9 nodes vs 11 in FIFO/LIFO).",
            color=GREEN, fontsize=7.5, ha='center', bbox=dict(boxstyle="round,pad=0.3", facecolor=CARD_BG, edgecolor=GREEN, lw=1))

    plt.title("BRANCH & BOUND STATE-SPACE TREE: FRACTIONAL BOUNDING & PRUNING",
              color=CYAN, fontsize=10, fontweight='bold', pad=12)
    plt.tight_layout()
    out_path = os.path.join(ASSETS_DIR, "state_space_tree.png")
    plt.savefig(out_path, dpi=300, facecolor=BG_DARK)
    plt.close()
    print(f"[+] Generated: {out_path}")

# =============================================================================
# DIAGRAM 5: COMPLEXITY CLASSES & NP-REDUCTION FLOWCHART
# =============================================================================
def draw_complexity_reduction():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.5, 4.2), dpi=300, facecolor=BG_DARK)
    for ax in [ax1, ax2]:
        ax.set_facecolor(BG_DARK)
        ax.axis('off')

    # Euler Diagram of Complexity Classes
    ax1.set_xlim(-2.5, 2.5)
    ax1.set_ylim(-2.5, 2.5)
    ax1.set_title("Euler Map of Complexity Classes", color=CYAN, fontsize=9.5, fontweight='bold', pad=10)

    # NP-Hard (Outer circle)
    c_nph = patches.Circle((0, 0.4), 1.9, facecolor=CARD_BG, edgecolor="#7C3AED", lw=1.5)
    ax1.add_patch(c_nph)
    ax1.text(0, 1.9, "NP-HARD (TSP Optimization)", color="#A855F7", fontsize=8, fontweight='bold', ha='center')

    # NP Circle
    c_np = patches.Circle((0, -0.2), 1.4, facecolor="#0E1A2E", edgecolor=AMBER, lw=1.5)
    ax1.add_patch(c_np)
    ax1.text(0, 0.9, "NP (Verifiable in Polynomial Time)", color=AMBER, fontsize=7.5, fontweight='bold', ha='center')

    # NP-Complete (Intersection)
    c_npc = patches.Ellipse((0, 0.35), 1.7, 0.7, facecolor="#1F1528", edgecolor=MAGENTA, lw=1.8)
    ax1.add_patch(c_npc)
    ax1.text(0, 0.35, "NP-COMPLETE\n(0/1 Knapsack, Subset-Sum, N-Queens)", color=MAGENTA, fontsize=7, fontweight='bold', ha='center', va='center')

    # P Circle
    c_p = patches.Circle((0, -0.8), 0.65, facecolor="#0A2229", edgecolor=GREEN, lw=1.5)
    ax1.add_patch(c_p)
    ax1.text(0, -0.8, "CLASS P\n(MergeSort, Dijkstra,\nMax-Flow)", color=GREEN, fontsize=6.5, fontweight='bold', ha='center', va='center')

    # Polynomial Reduction Diagram
    ax2.set_xlim(0, 6)
    ax2.set_ylim(0, 6)
    ax2.set_title("Polynomial-Time Reduction: SUBSET-SUM \u2264_p 0/1 KNAPSACK", color=CYAN, fontsize=9.5, fontweight='bold', pad=10)

    # Box 1: Subset Sum
    ax2.text(3.0, 5.0, "Subset-Sum Instance (Known NP-Complete)\nSet S = {s1, s2, ..., sn}, Target Threshold T\nQuestion: \u2203 S' \u2286 S such that \u03a3 s_i = T ?",
             bbox=dict(boxstyle="round,pad=0.3", facecolor=CARD_BG, edgecolor=AMBER, lw=1.5), ha='center', fontsize=7.5)

    # Arrow
    ax2.annotate("", xy=(3.0, 3.7), xytext=(3.0, 4.3),
                 arrowprops=dict(arrowstyle="->", color=CYAN, lw=2.2))
    ax2.text(3.1, 4.0, "Polynomial Transformation f(x) in O(n) time\nw_i = s_i,  v_i = s_i,  Capacity W = T,  Target Value V = T",
             color=CYAN, fontsize=7, va='center')

    # Box 2: Knapsack
    ax2.text(3.0, 2.7, "0/1 Knapsack Instance\nItems with weight w_i = s_i and value v_i = s_i\nQuestion: Fit capacity \u2264 T to achieve value \u2265 T ?",
             bbox=dict(boxstyle="round,pad=0.3", facecolor=CARD_BG, edgecolor=MAGENTA, lw=1.5), ha='center', fontsize=7.5)

    # Equivalence box
    ax2.text(3.0, 0.9, "Equivalence Proof:\n(\u21d2) If \u03a3 s_i = T, selecting same items gives weight T \u2264 W and value T \u2265 V. Knapsack answers YES.\n(\u21d0) Since w_i = v_i, weight \u2264 T and value \u2265 T implies \u03a3 w_i = \u03a3 v_i = T. Subset-Sum answers YES.\n\u2234 0/1 Knapsack Decision Problem is NP-Complete.",
             bbox=dict(boxstyle="round,pad=0.3", facecolor=CARD_BG, edgecolor=GREEN, lw=1.2), ha='center', fontsize=6.8, color=WHITE)

    plt.tight_layout()
    out_path = os.path.join(ASSETS_DIR, "complexity_reduction.png")
    plt.savefig(out_path, dpi=300, facecolor=BG_DARK)
    plt.close()
    print(f"[+] Generated: {out_path}")

if __name__ == "__main__":
    draw_attack_topology()
    draw_recurrence_trees()
    draw_benchmark_charts()
    draw_state_space_tree()
    draw_complexity_reduction()
    print("[+] All professional academic diagrams successfully generated!")
