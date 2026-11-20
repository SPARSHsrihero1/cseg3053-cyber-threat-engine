#!/usr/bin/env python3
"""
Render 1920x1080 PNG previews of the NVIDIA GTC / BlackHat Presentation Deck.
Outputs saved to presentation/previews/
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "presentation", "assets")
GTC_DIR = os.path.join(ASSETS_DIR, "gtc")
CROPS_DIR = os.path.join(ASSETS_DIR, "gui_crops")
PREVIEW_DIR = os.path.join(BASE_DIR, "presentation", "previews")
os.makedirs(PREVIEW_DIR, exist_ok=True)

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

def create_base_slide(eyebrow, title, subtitle, phase):
    fig = plt.figure(figsize=(13.333, 7.5), dpi=150, facecolor=BG_DARK)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor(BG_DARK)
    ax.set_xlim(0, 13.333)
    ax.set_ylim(0, 7.5)
    ax.axis('off')

    # Eyebrow
    ax.text(0.8, 7.05, eyebrow, color=CYAN, weight='bold', fontsize=9.5)
    # Title
    ax.text(0.8, 6.55, title, color=WHITE, weight='bold', fontsize=20)
    # Subtitle
    if subtitle:
        ax.text(0.8, 6.15, subtitle, color=SLATE, fontsize=10.5)

    # Phase badge
    badge = patches.FancyBboxPatch((10.8, 6.6), 1.8, 0.45, boxstyle="round,pad=0.08,rounding_size=0.1",
                                   facecolor=CARD_BG, edgecolor=BORDER, linewidth=1.5)
    ax.add_patch(badge)
    ax.text(11.7, 6.82, phase, ha='center', va='center', color=CYAN, weight='bold', fontsize=9.5)

    return fig, ax

def render_all():
    # --- SLIDE 1 ---
    fig, ax = create_base_slide(
        "// CSEG3053 ALGORITHMIC RESEARCH DEFENSE // IEEE S&P 2026 ARCHITECTURE",
        "AUTONOMOUS CYBER-THREAT ENGINE",
        "Pure C17 Deterministic Algorithmic Architecture for Sub-Millisecond Attack Graph Neutralization",
        "PHASE 01 / 08"
    )
    r_path = os.path.join(GTC_DIR, "gtc_slide1_hero_ribbon.png")
    if os.path.exists(r_path):
        rim = Image.open(r_path)
        ax.imshow(rim, extent=[0.8, 12.533, 2.3, 6.0], zorder=2)

    hud_data = [
        ("0 LIBS", "Pure C17 Standard\nZero External Libs", CYAN, 0.8),
        ("25+ ALGOS", "All Syllabus Algos\nBuilt From Scratch", GREEN, 3.8),
        ("1.2M / s", "Peak Event Throughput\nZero malloc in Hot Path", CYAN, 6.8),
        ("33 / 33", "Deterministic Oracles\n100% Pass Rate", GREEN, 9.8)
    ]
    for val, lbl, col, x in hud_data:
        c = patches.FancyBboxPatch((x, 0.5), 2.73, 1.65, boxstyle="round,pad=0.08,rounding_size=0.1",
                                   facecolor=CARD_BG, edgecolor=col, linewidth=1.5)
        ax.add_patch(c)
        ax.text(x + 1.365, 1.55, val, ha='center', color=col, weight='bold', fontsize=26)
        ax.text(x + 1.365, 0.95, lbl, ha='center', color=WHITE, fontsize=8.5, linespacing=1.2)

    plt.savefig(os.path.join(PREVIEW_DIR, "slide_preview_1.png"), dpi=150, facecolor=BG_DARK)
    plt.close()
    print("[+] Rendered slide_preview_1.png")

    # --- SLIDE 2 ---
    fig, ax = create_base_slide(
        "// SYSTEM ARCHITECTURE // FORMAL FOUR-STAGE PIPELINE",
        "FOUR-STAGE STREAMING THREAT PIPELINE",
        "Deterministic dataflow converting unbounded audit streams into capacity-bounded containment",
        "PHASE 02 / 08"
    )
    p_path = os.path.join(GTC_DIR, "gtc_slide2_pipeline.png")
    if os.path.exists(p_path):
        pim = Image.open(p_path)
        ax.imshow(pim, extent=[0.8, 12.533, 1.5, 6.0], zorder=2)

    in_box = patches.FancyBboxPatch((0.8, 0.4), 11.733, 0.95, boxstyle="round,pad=0.08,rounding_size=0.1",
                                    facecolor=CARD_BG, edgecolor=CYAN, linewidth=1.5)
    ax.add_patch(in_box)
    ax.text(1.1, 0.88, "ARCHITECTURAL GUARANTEE: Lock-free circular ring buffer decouples I/O ingestion from CPU-bound graph traversal, ensuring zero dropped syslog packets even under sustained 10 Gbps flood conditions. All stages execute in strictly bounded asymptotic time.",
            color=WHITE, fontsize=9.2, va='center')

    plt.savefig(os.path.join(PREVIEW_DIR, "slide_preview_2.png"), dpi=150, facecolor=BG_DARK)
    plt.close()
    print("[+] Rendered slide_preview_2.png")

    # --- SLIDE 3 ---
    fig, ax = create_base_slide(
        "// DIVIDE & CONQUER // ADVERSARIAL STRESS PROOF",
        "TEMPORAL LOG ORDERING UNDER ADVERSARIAL FLOOD",
        "Master Theorem Equivalence vs Adversarial QuickSort Collapse",
        "PHASE 03 / 08"
    )
    left_c = patches.FancyBboxPatch((0.8, 0.45), 4.5, 5.5, boxstyle="square,pad=0",
                                    facecolor=CARD_BG, edgecolor=BORDER, linewidth=1.5)
    ax.add_patch(left_c)
    ax.text(1.1, 5.3, "180×", color=GREEN, weight='bold', fontsize=56)
    ax.text(1.1, 4.5, "FASTER UNDER PRE-SORTED ADVERSARIAL LOG INFLUX", color=WHITE, weight='bold', fontsize=10.5)
    ax.plot([1.1, 5.0], [4.3, 4.3], color=BORDER, lw=1.2)
    ax.text(1.1, 3.8, "Master Theorem Case 2 Guarantee:\nT(n) = 2T(n/2) + Θ(n) => Strictly Θ(n log n)", color=CYAN, weight='bold', fontsize=9.5)
    ax.text(1.1, 2.5, "Adversaries intentionally flood pre-sorted timestamps\nto induce worst-case Θ(n²) QuickSort collapse\n(1,999,000 ops). Stable MergeSort guarantees uninterrupted\nΘ(n log n) throughput (11,088 ops), defusing attacks.", color=SLATE, fontsize=8.8, linespacing=1.3)
    ax.text(1.1, 1.1, "[ QUICK: 1,999,000 OPS (STALL) ]\n[ MERGE: 11,088 OPS (OPTIMAL) ]", color=GREEN, weight='bold', fontsize=8.5)

    s_path = os.path.join(GTC_DIR, "gtc_slide3_sorting_showdown.png")
    if os.path.exists(s_path):
        sim = Image.open(s_path)
        ax.imshow(sim, extent=[5.5, 12.6, 0.45, 5.95], zorder=2)

    plt.savefig(os.path.join(PREVIEW_DIR, "slide_preview_3.png"), dpi=150, facecolor=BG_DARK)
    plt.close()
    print("[+] Rendered slide_preview_3.png")

    # --- SLIDE 4 ---
    fig, ax = create_base_slide(
        "// STRING MATCHING // AUTOMATA & SUB-LINEAR SEARCH",
        "EXPLOIT SIGNATURE PATTERN MATCHING",
        "KMP Failure Automaton π[q] vs Boyer-Moore & Naive Backtracking",
        "PHASE 04 / 08"
    )
    left_c = patches.FancyBboxPatch((0.8, 0.45), 4.5, 5.5, boxstyle="square,pad=0",
                                    facecolor=CARD_BG, edgecolor=BORDER, linewidth=1.5)
    ax.add_patch(left_c)
    ax.text(1.1, 5.3, "4.5×", color=CYAN, weight='bold', fontsize=56)
    ax.text(1.1, 4.5, "THROUGHPUT GAIN UNDER REPEATING PAYLOAD STRESS", color=WHITE, weight='bold', fontsize=10.5)
    ax.plot([1.1, 5.0], [4.3, 4.3], color=BORDER, lw=1.2)
    ax.text(1.1, 3.8, "Deterministic Linear Bound:\nTime: O(n + m)  |  Backtracking: 0 Ops", color=GREEN, weight='bold', fontsize=9.5)
    ax.text(1.1, 2.5, "Text pointer i strictly NEVER moves backward.\nThe precomputed failure table π[q] encodes longest\nproper prefix matching, eliminating quadratic pointer\nrollback over adversarial repeating buffers.", color=SLATE, fontsize=8.8, linespacing=1.3)
    ax.text(1.1, 1.1, "[ NAIVE: 89,919 OPS (STALL) ]\n[ KMP: 20,004 OPS (MONOTONIC) ]", color=CYAN, weight='bold', fontsize=8.5)

    str_p = os.path.join(GTC_DIR, "gtc_slide4_string.png")
    if os.path.exists(str_p):
        st_im = Image.open(str_p)
        ax.imshow(st_im, extent=[5.5, 12.6, 0.45, 5.95], zorder=2)

    plt.savefig(os.path.join(PREVIEW_DIR, "slide_preview_4.png"), dpi=150, facecolor=BG_DARK)
    plt.close()
    print("[+] Rendered slide_preview_4.png")

    # --- SLIDE 5 ---
    fig, ax = create_base_slide(
        "// GRAPH THEORY // ATTACK SURFACE & DYNAMIC MIN-CUT",
        "ATTACK TOPOLOGY & MIN-CUT FIREWALL ISOLATION",
        "Exploit Paths, Negative Cycle Detection & Capacity-Bounded Quarantine",
        "PHASE 05 / 08"
    )
    left_c = patches.FancyBboxPatch((0.8, 0.45), 4.5, 5.5, boxstyle="square,pad=0",
                                    facecolor=CARD_BG, edgecolor=BORDER, linewidth=1.5)
    ax.add_patch(left_c)
    ax.text(1.1, 5.4, "MIN-CUT", color=CYAN, weight='bold', fontsize=48)
    ax.text(1.1, 4.6, "CAPACITY-BOUNDED NETWORK QUARANTINE VIA EDMONDS-KARP", color=WHITE, weight='bold', fontsize=9.5)
    ax.plot([1.1, 5.0], [4.4, 4.4], color=BORDER, lw=1.2)
    ax.text(1.1, 3.9, "Exfiltration Halted: 412 MB/s\nSever Cost: 22 Mbps (Minimal Interruption)", color=GREEN, weight='bold', fontsize=9.5)
    ax.text(1.1, 3.2, "Negative Privilege Loop: -5 Caught via Bellman-Ford", color=RED, weight='bold', fontsize=9.0)
    ax.text(1.1, 2.1, "Dijkstra traces critical attack vectors in O((V+E) log V).\nBellman-Ford catches negative-weight exploit loops.\nEdmonds-Karp isolates breached subnets with minimal\ncollateral bandwidth cost.", color=SLATE, fontsize=8.8, linespacing=1.3)
    ax.text(1.1, 1.0, "[ BINARY MIN-HEAP ] [ BELLMAN-FORD ] [ MIN-CUT ]", color=CYAN, weight='bold', fontsize=8.0)

    m_path = os.path.join(GTC_DIR, "gtc_slide5_mincut.png")
    if os.path.exists(m_path):
        mim = Image.open(m_path)
        ax.imshow(mim, extent=[5.5, 12.6, 0.45, 5.95], zorder=2)

    plt.savefig(os.path.join(PREVIEW_DIR, "slide_preview_5.png"), dpi=150, facecolor=BG_DARK)
    plt.close()
    print("[+] Rendered slide_preview_5.png")

    # --- SLIDE 6 ---
    fig, ax = create_base_slide(
        "// COMBINATORIAL OPTIMIZATION // STATE-SPACE SEARCH",
        "RESOURCE-BOUNDED PATCH ALLOCATION",
        "0/1 Knapsack Dynamic Programming vs Best-First Branch & Bound",
        "PHASE 06 / 08"
    )
    left_c = patches.FancyBboxPatch((0.8, 0.45), 4.5, 5.5, boxstyle="square,pad=0",
                                    facecolor=CARD_BG, edgecolor=BORDER, linewidth=1.5)
    ax.add_patch(left_c)
    ax.text(1.1, 5.3, "78%", color=GREEN, weight='bold', fontsize=56)
    ax.text(1.1, 4.5, "OF STATE-SPACE SEARCH NODES PRUNED WITHOUT EXPLORATION", color=WHITE, weight='bold', fontsize=9.8)
    ax.plot([1.1, 5.0], [4.3, 4.3], color=BORDER, lw=1.2)
    ax.text(1.1, 3.8, "Mathematical Pruning Criterion:\nIf Upper Bound UB(node) <= Current Best => PRUNE", color=CYAN, weight='bold', fontsize=9.2)
    ax.text(1.1, 2.4, "Root bound UB=$280. LCBB Best-First with Max-Heap\ngreedily guides search toward optimum N9 (w=15, v=$260).\nSubtrees with UB <= $240 are pruned immediately without\nexpansion, eliminating four-fifths of the state space.", color=SLATE, fontsize=8.8, linespacing=1.3)
    ax.text(1.1, 1.1, "[ GREEDY FRACTIONAL RELAXATION ]\n[ LEAST-COST MAX-HEAP QUEUE ]", color=GREEN, weight='bold', fontsize=8.5)

    p_path6 = os.path.join(GTC_DIR, "gtc_slide6_pruning.png")
    if os.path.exists(p_path6):
        pim6 = Image.open(p_path6)
        ax.imshow(pim6, extent=[5.5, 12.6, 0.45, 5.95], zorder=2)

    plt.savefig(os.path.join(PREVIEW_DIR, "slide_preview_6.png"), dpi=150, facecolor=BG_DARK)
    plt.close()
    print("[+] Rendered slide_preview_6.png")

    # --- SLIDE 7 ---
    fig, ax = create_base_slide(
        "// COMPUTATIONAL COMPLEXITY // FORMAL REDUCTION PROOFS",
        "COMPLEXITY CLASSIFICATION & REDUCTION PROOF",
        "Polynomial-Time Verification & Formal Mapping: SUBSET-SUM ≤p 0/1 KNAPSACK",
        "PHASE 07 / 08"
    )
    left_c = patches.FancyBboxPatch((0.8, 0.45), 4.5, 5.5, boxstyle="square,pad=0",
                                    facecolor=CARD_BG, edgecolor=BORDER, linewidth=1.5)
    ax.add_patch(left_c)
    ax.text(1.1, 5.4, "NP-COMPLETE", color=RED, weight='bold', fontsize=40)
    ax.text(1.1, 4.65, "DECISION 0/1 KNAPSACK IS PROVABLY NP-COMPLETE", color=WHITE, weight='bold', fontsize=10.2)
    ax.plot([1.1, 5.0], [4.4, 4.4], color=BORDER, lw=1.2)
    ax.text(1.1, 3.85, "Two-Step Formal Reduction Proof:\n1. In NP: Certificate verified in O(n) Time\n2. NP-Hard: SUBSET-SUM <=p 0/1 KNAPSACK", color=CYAN, weight='bold', fontsize=9.2)
    ax.text(1.1, 2.7, "Instance Transformation:\nw_i = s_i,  v_i = s_i,  Capacity W = T,  Profit V = T\nComputable in O(n) logarithmic space.\nSubset-Sum has solution iff Knapsack profit >= T.", color=WHITE, fontsize=8.5, linespacing=1.2)
    ax.text(1.1, 1.3, "Formal Justification:\nProves exact poly-time algorithms are impossible under\nP != NP, validating our Branch & Bound pruning heuristic.", color=SLATE, fontsize=8.2, linespacing=1.2)

    c_path7 = os.path.join(GTC_DIR, "gtc_slide7_complexity.png")
    if os.path.exists(c_path7):
        cim7 = Image.open(c_path7)
        ax.imshow(cim7, extent=[5.5, 12.6, 0.45, 5.95], zorder=2)

    plt.savefig(os.path.join(PREVIEW_DIR, "slide_preview_7.png"), dpi=150, facecolor=BG_DARK)
    plt.close()
    print("[+] Rendered slide_preview_7.png")

    # --- SLIDE 8 ---
    fig, ax = create_base_slide(
        "// EMPIRICAL VERIFICATION // DEFENSE CONCLUSION",
        "EMPIRICAL BENCHMARKS & LIVE WORKBENCH LAUNCHPAD",
        "36 Empirical Traces & 33/33 Deterministic Test Oracles Passed",
        "PHASE 08 / 08"
    )
    ribbon8_data = [
        ("33 / 33 PASS", "100% Deterministic Test Oracles Passing across all 6 Units", GREEN, 0.8, 3.8),
        ("0 LEAKS", "Valgrind Memory Clean | Fixed Arena RSS | Zero Heap Leaks", CYAN, 4.8, 3.8),
        ("36 TRACES", "Fully Reproducible CSV & JSON Benchmark Metrics Generated", GREEN, 8.8, 3.8)
    ]
    for val, lbl, col, x, w in ribbon8_data:
        c = patches.FancyBboxPatch((x, 4.5), w, 1.4, boxstyle="round,pad=0.08,rounding_size=0.1",
                                   facecolor=CARD_BG, edgecolor=col, linewidth=1.5)
        ax.add_patch(c)
        ax.text(x + w/2, 5.4, val, ha='center', color=col, weight='bold', fontsize=22)
        ax.text(x + w/2, 4.8, lbl, ha='center', color=WHITE, fontsize=8.0, linespacing=1.2)

    d_path = os.path.join(ASSETS_DIR, "slide8_empirical_dashboard.png")
    if os.path.exists(d_path):
        dim = Image.open(d_path)
        ax.imshow(dim, extent=[0.8, 6.6, 0.45, 4.35], zorder=2)

    demo_c = patches.FancyBboxPatch((6.8, 0.45), 5.733, 3.9, boxstyle="round,pad=0.08,rounding_size=0.12",
                                    facecolor=CARD_BG, edgecolor=GREEN, linewidth=2.0)
    ax.add_patch(demo_c)
    ax.text(7.1, 3.9, "LIVE INTERACTIVE WORKBENCH READY", color=GREEN, weight='bold', fontsize=14)
    ax.text(7.1, 2.9, "Execute Live Engine Console & Interactive Testbed:\n• Interactive Studio: .\\start_gui.bat  (http://localhost:8080)\n• Full C17 Test Suite: .\\bin\\test_all.exe  (33/33 Tests Pass)\n• Empirical Benchmark: .\\bin\\benchmark.exe  (CSV/JSON Output)",
            color=WHITE, fontsize=9.2, linespacing=1.35)

    nq_p = os.path.join(CROPS_DIR, "ui_nqueens_card.png")
    if os.path.exists(nq_p):
        nq_im = Image.open(nq_p)
        ax.imshow(nq_im, extent=[7.1, 9.6, 0.6, 2.6], zorder=3)

    ax.text(12.2, 0.8, "[ READY FOR PROFESSOR TECHNICAL VIVA & CODE REVIEW ]",
            ha='right', color=CYAN, weight='bold', fontsize=9.5)

    plt.savefig(os.path.join(PREVIEW_DIR, "slide_preview_8.png"), dpi=150, facecolor=BG_DARK)
    plt.close()
    print("[+] Rendered slide_preview_8.png")

if __name__ == "__main__":
    print("[*] Rendering GTC presentation preview PNGs...")
    render_all()
    print("[+] All 8 GTC preview PNGs rendered successfully!")
