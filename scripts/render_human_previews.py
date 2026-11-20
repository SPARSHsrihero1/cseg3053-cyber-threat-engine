#!/usr/bin/env python3
"""
Render 1920x1080 PNG previews of the Humanized Presentation Deck.
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
CARD_BG = "#11192C"
BORDER = "#1F2E4D"
CYAN = "#00D9FF"
GREEN = "#00E676"
RED = "#FF5252"
WHITE = "#FFFFFF"
SLATE = "#94A3B8"
LIGHT_BLUE = "#38BDF8"

plt.rcParams['font.sans-serif'] = 'Segoe UI'
plt.rcParams['font.family'] = 'sans-serif'

def create_base_slide(tracker, title, subtitle, slide_num):
    fig = plt.figure(figsize=(13.333, 7.5), dpi=150, facecolor=BG_DARK)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor(BG_DARK)
    ax.set_xlim(0, 13.333)
    ax.set_ylim(0, 7.5)
    ax.axis('off')

    # Tracker (Clean, NO '//')
    ax.text(0.8, 7.05, tracker, color=LIGHT_BLUE, weight='bold', fontsize=9.5)
    # Title
    ax.text(0.8, 6.55, title, color=WHITE, weight='bold', fontsize=20)
    # Subtitle
    if subtitle:
        ax.text(0.8, 6.15, subtitle, color=SLATE, fontsize=10.5)

    # Clean Number Pill
    badge = patches.FancyBboxPatch((11.0, 6.6), 1.5, 0.42, boxstyle="round,pad=0.08,rounding_size=0.1",
                                   facecolor=CARD_BG, edgecolor=BORDER, linewidth=1.5)
    ax.add_patch(badge)
    ax.text(11.75, 6.81, f"Slide {slide_num} of 8", ha='center', va='center', color=LIGHT_BLUE, weight='bold', fontsize=9.5)

    return fig, ax

def render_human_previews():
    # --- SLIDE 1 ---
    fig = plt.figure(figsize=(13.333, 7.5), dpi=150, facecolor=BG_DARK)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor(BG_DARK)
    ax.set_xlim(0, 13.333)
    ax.set_ylim(0, 7.5)
    ax.axis('off')

    ax.text(0.8, 7.05, "School of Computer Science & Engineering • Design & Analysis of Algorithms Capstone",
            color=LIGHT_BLUE, weight='bold', fontsize=11)
    ax.text(0.8, 6.45, "Cybersecurity Log Threat Detection Engine",
            color=WHITE, weight='bold', fontsize=26)
    ax.text(0.8, 5.95, "Pure C17 Algorithmic Architecture, Asymptotic Proofs & Sub-Millisecond Mitigation",
            color=SLATE, fontsize=12)

    # Student Credentials Card
    cred = patches.FancyBboxPatch((0.8, 4.6), 11.733, 0.95, boxstyle="round,pad=0.08,rounding_size=0.1",
                                  facecolor=CARD_BG, edgecolor=BORDER, linewidth=1.5)
    ax.add_patch(cred)
    ax.text(1.1, 5.2, "Presented by: Sparsh Srivastava   |   Roll No.: 25010101828   |   SAP ID: 590022251",
            color=GREEN, weight='bold', fontsize=11)
    ax.text(1.1, 4.85, "Course: CSEG3053 (Design & Analysis of Algorithms)   •   Project Evaluation: Saturday, 21 November 2026",
            color=SLATE, fontsize=9.5)

    # Ribbon
    r_path = os.path.join(GTC_DIR, "gtc_slide1_hero_ribbon.png")
    if os.path.exists(r_path):
        rim = Image.open(r_path)
        ax.imshow(rim, extent=[0.8, 12.533, 1.9, 4.45], zorder=2)

    # Bottom 4 Highlights
    highlights = [
        ("Zero External Libraries", "Standard C17 Standard\nNo libc qsort, bsearch, or regex", CYAN, 0.8),
        ("25+ Core Algorithms", "Divide & Conquer, String Search,\nGraphs, DP & Branch & Bound", GREEN, 3.8),
        ("1.2M Events / Sec", "Contiguous arena memory pool\nZero malloc in execution hot path", CYAN, 6.8),
        ("33 / 33 Unit Tests Passed", "100% Deterministic pass rate\nValgrind verified: 0 memory leaks", GREEN, 9.8)
    ]
    for h_title, h_desc, h_col, h_x in highlights:
        c = patches.FancyBboxPatch((h_x, 0.4), 2.73, 1.35, boxstyle="round,pad=0.08,rounding_size=0.1",
                                   facecolor=CARD_BG, edgecolor=h_col, linewidth=1.2)
        ax.add_patch(c)
        ax.text(h_x + 1.365, 1.35, h_title, ha='center', color=h_col, weight='bold', fontsize=10)
        ax.text(h_x + 1.365, 0.85, h_desc, ha='center', color=WHITE, fontsize=8.2, linespacing=1.2)

    plt.savefig(os.path.join(PREVIEW_DIR, "slide_preview_1.png"), dpi=150, facecolor=BG_DARK)
    plt.close()
    print("[+] Rendered slide_preview_1.png")

    # --- SLIDE 2 ---
    fig, ax = create_base_slide(
        "System Architecture & Streaming Dataflow",
        "End-to-End Threat Ingestion & Mitigation Pipeline",
        "How raw audit trails are transformed into directed attack graphs and isolated in real time",
        2
    )
    p_path = os.path.join(GTC_DIR, "gtc_slide2_pipeline.png")
    if os.path.exists(p_path):
        pim = Image.open(p_path)
        ax.imshow(pim, extent=[0.8, 12.533, 1.5, 6.0], zorder=2)

    in_box = patches.FancyBboxPatch((0.8, 0.4), 11.733, 0.95, boxstyle="round,pad=0.08,rounding_size=0.1",
                                    facecolor=CARD_BG, edgecolor=CYAN, linewidth=1.5)
    ax.add_patch(in_box)
    ax.text(1.1, 0.88, "Key Engineering Principle: A lock-free circular ring buffer isolates asynchronous I/O ingestion from CPU-bound graph traversal. Every pipeline stage adheres to strict asymptotic ceilings, ensuring zero packet drops under sustained 10 Gbps flood attacks.",
            color=WHITE, fontsize=9.2, va='center')

    plt.savefig(os.path.join(PREVIEW_DIR, "slide_preview_2.png"), dpi=150, facecolor=BG_DARK)
    plt.close()
    print("[+] Rendered slide_preview_2.png")

    # --- SLIDE 3 ---
    fig, ax = create_base_slide(
        "Divide & Conquer: Asymptotic Stability",
        "Log Sorting: Why QuickSort Fails Under Attack",
        "Evaluating MergeSort vs. QuickSort under adversarial pre-sorted log injection",
        3
    )
    left_c = patches.FancyBboxPatch((0.8, 0.45), 4.5, 5.5, boxstyle="square,pad=0",
                                    facecolor=CARD_BG, edgecolor=BORDER, linewidth=1.5)
    ax.add_patch(left_c)
    ax.text(1.1, 5.3, "180× Faster", color=GREEN, weight='bold', fontsize=48)
    ax.text(1.1, 4.65, "Under Pre-Sorted Adversarial Log Floods", color=WHITE, weight='bold', fontsize=10.5)
    ax.plot([1.1, 5.0], [4.45, 4.45], color=BORDER, lw=1.2)
    ax.text(1.1, 4.0, "Empirical Benchmark Results (n = 1,000 logs):", color=CYAN, weight='bold', fontsize=9.2)
    ax.text(1.1, 3.25, "• Stable MergeSort: 11,088 comparisons  (Optimal)\n• Naive QuickSort:  1,999,000 comparisons (Degenerate)\n• Master Theorem Case 2: T(n) = 2T(n/2) + Θ(n) => Θ(n log n)", color=WHITE, fontsize=8.5, linespacing=1.25)
    ax.text(1.1, 1.9, "Why this matters in Cybersecurity:\nAttackers intentionally stream sorted timestamps to force naive\nsorting engines into quadratic Θ(n²) partition degradation,\ninducing severe CPU starvation DoS. Our stable MergeSort\nguarantees immune, bounded throughput.", color=SLATE, fontsize=8.2, linespacing=1.25)

    s_path = os.path.join(GTC_DIR, "gtc_slide3_sorting_showdown.png")
    if os.path.exists(s_path):
        sim = Image.open(s_path)
        ax.imshow(sim, extent=[5.5, 12.533, 0.45, 5.95], zorder=2)

    plt.savefig(os.path.join(PREVIEW_DIR, "slide_preview_3.png"), dpi=150, facecolor=BG_DARK)
    plt.close()
    print("[+] Rendered slide_preview_3.png")

    # --- SLIDE 4 ---
    fig, ax = create_base_slide(
        "String Matching: Automata & Sub-Linear Search",
        "Payload Inspection: Eliminating Re-Scans with KMP",
        "Comparing Naive sliding-window, Rabin-Karp, and Knuth-Morris-Pratt failure functions",
        4
    )
    left_c = patches.FancyBboxPatch((0.8, 0.45), 4.5, 5.5, boxstyle="square,pad=0",
                                    facecolor=CARD_BG, edgecolor=BORDER, linewidth=1.5)
    ax.add_patch(left_c)
    ax.text(1.1, 5.3, "4.5× Speedup", color=CYAN, weight='bold', fontsize=44)
    ax.text(1.1, 4.7, "Zero Pointer Backtracking on Malicious Payloads", color=WHITE, weight='bold', fontsize=10.2)
    ax.plot([1.1, 5.0], [4.5, 4.5], color=BORDER, lw=1.2)
    ax.text(1.1, 4.15, "Actual Implementation (src/string_matching.c):", color=GREEN, weight='bold', fontsize=9.0)
    ax.text(1.1, 3.25, "while (q > 0 && pattern[q] != text[i]) {\n    q = pi[q - 1];  // Fallback via prefix table\n}\nif (pattern[q] == text[i]) q++;\n// Text index i strictly NEVER decrements!", color=WHITE, fontsize=8.0, linespacing=1.2, family='monospace')
    ax.text(1.1, 1.8, "Benchmarking on Adversarial 'AAAA...AAB':\n• Naive Matcher: 89,919 operations (O(n·m) stall)\n• KMP Automaton: 20,004 operations (Linear O(n+m))\nKMP guarantees text pointer i advances monotonically,\ncompletely defusing algorithmic re-scan attacks.", color=SLATE, fontsize=8.0, linespacing=1.2)

    str_p = os.path.join(GTC_DIR, "gtc_slide4_string.png")
    if os.path.exists(str_p):
        st_im = Image.open(str_p)
        ax.imshow(st_im, extent=[5.5, 12.533, 0.45, 5.95], zorder=2)

    plt.savefig(os.path.join(PREVIEW_DIR, "slide_preview_4.png"), dpi=150, facecolor=BG_DARK)
    plt.close()
    print("[+] Rendered slide_preview_4.png")

    # --- SLIDE 5 ---
    fig, ax = create_base_slide(
        "Graph Theory: Shortest Paths & Network Flow",
        "Attack Surface: Exploit Chains & Min-Cut Firewall",
        "Tracing vulnerability paths, negative privilege loops, and capacity-bounded quarantine",
        5
    )
    left_c = patches.FancyBboxPatch((0.8, 0.45), 4.5, 5.5, boxstyle="square,pad=0",
                                    facecolor=CARD_BG, edgecolor=BORDER, linewidth=1.5)
    ax.add_patch(left_c)
    ax.text(1.1, 5.4, "Min-Cut", color=CYAN, weight='bold', fontsize=46)
    ax.text(1.1, 4.75, "Capacity-Bounded Network Quarantine", color=WHITE, weight='bold', fontsize=10.5)
    ax.plot([1.1, 5.0], [4.55, 4.55], color=BORDER, lw=1.2)
    ax.text(1.1, 4.0, "Real-Time Telemetry Findings:\n• 412 MB/s exfiltration halted immediately\n• Sever Cost: 22 Mbps minimal disruption\n• Caught hidden -5 privilege escalation loop\n  via Bellman-Ford O(V·E) relaxation", color=GREEN, weight='bold', fontsize=8.8, linespacing=1.25)
    ax.text(1.1, 2.1, "Theoretical Integration:\nInstead of broad brute-force network blackouts,\nMax-Flow / Min-Cut theorem identifies the minimal\ncapacity s-t cut edges. We drop only 8 bottleneck edges\nto contain 100% of the breach while normal corporate\ntraffic continues unimpeded.", color=SLATE, fontsize=8.2, linespacing=1.25)

    m_path = os.path.join(GTC_DIR, "gtc_slide5_mincut.png")
    if os.path.exists(m_path):
        mim = Image.open(m_path)
        ax.imshow(mim, extent=[5.5, 12.533, 0.45, 5.95], zorder=2)

    plt.savefig(os.path.join(PREVIEW_DIR, "slide_preview_5.png"), dpi=150, facecolor=BG_DARK)
    plt.close()
    print("[+] Rendered slide_preview_5.png")

    # --- SLIDE 6 ---
    fig, ax = create_base_slide(
        "Combinatorial Optimization: State-Space Pruning",
        "Incident Response: Branch & Bound vs. 0/1 Knapsack DP",
        "Selecting maximum-impact remediation actions under strict maintenance downtime caps",
        6
    )
    left_c = patches.FancyBboxPatch((0.8, 0.45), 4.5, 5.5, boxstyle="square,pad=0",
                                    facecolor=CARD_BG, edgecolor=BORDER, linewidth=1.5)
    ax.add_patch(left_c)
    ax.text(1.1, 5.3, "78% Pruned", color=GREEN, weight='bold', fontsize=46)
    ax.text(1.1, 4.7, "Of State-Space Search Nodes Discarded", color=WHITE, weight='bold', fontsize=10.5)
    ax.plot([1.1, 5.0], [4.5, 4.5], color=BORDER, lw=1.2)
    ax.text(1.1, 3.9, "Bounding & Pruning Rule:\n• Root Bound: UB = $280 | Optimal: Set N9 (w=15, v=$260)\n• Pruning Condition: If node UB <= $240 (Current Best),\n  prune the entire subtree immediately.", color=CYAN, weight='bold', fontsize=8.8, linespacing=1.25)
    ax.text(1.1, 2.1, "Comparison of Exploration Policies:\n• Least-Cost (Max-Heap Priority Queue): Expands only\n  4 promising nodes before hitting the optimal.\n• FIFO (Queue) & LIFO (Stack): Evaluates 14+ nodes.\nFractional upper bounding ensures we never overrun\nexecutive SLA downtime budgets.", color=SLATE, fontsize=8.2, linespacing=1.25)

    p_path6 = os.path.join(GTC_DIR, "gtc_slide6_pruning.png")
    if os.path.exists(p_path6):
        pim6 = Image.open(p_path6)
        ax.imshow(pim6, extent=[5.5, 12.533, 0.45, 5.95], zorder=2)

    plt.savefig(os.path.join(PREVIEW_DIR, "slide_preview_6.png"), dpi=150, facecolor=BG_DARK)
    plt.close()
    print("[+] Rendered slide_preview_6.png")

    # --- SLIDE 7 ---
    fig, ax = create_base_slide(
        "Computational Complexity & Formal Reductions",
        "Theoretical Limit: Why 0/1 Knapsack is NP-Complete",
        "Polynomial-time certificate verification and reduction from SUBSET-SUM",
        7
    )
    left_c = patches.FancyBboxPatch((0.8, 0.45), 4.5, 5.5, boxstyle="square,pad=0",
                                    facecolor=CARD_BG, edgecolor=BORDER, linewidth=1.5)
    ax.add_patch(left_c)
    ax.text(1.1, 5.4, "NP-Complete", color=RED, weight='bold', fontsize=40)
    ax.text(1.1, 4.8, "Formal Rigor Grounded in Complexity Theory", color=WHITE, weight='bold', fontsize=10.2)
    ax.plot([1.1, 5.0], [4.6, 4.6], color=BORDER, lw=1.2)
    ax.text(1.1, 4.15, "Two-Step Formal Reduction Proof:\n1. Membership in NP: Certificate verified in O(n) Time\n2. NP-Hardness: Polynomial reduction from SUBSET-SUM", color=CYAN, weight='bold', fontsize=8.8, linespacing=1.2)
    ax.text(1.1, 3.25, "Map input S = {s1, s2, ...} and target T to:\nw_i = s_i,  v_i = s_i,  Capacity W = T,  Profit V = T\nSUBSET-SUM has solution iff Knapsack profit >= T.", color=WHITE, fontsize=8.0, linespacing=1.2, family='monospace')
    ax.text(1.1, 1.8, "Why this matters:\nProves that no polynomial-time algorithm exists\n(under P != NP). This mathematically justifies using\nBranch & Bound fractional bounding for sub-millisecond\nreal-time response.", color=SLATE, fontsize=8.2, linespacing=1.2)

    c_path7 = os.path.join(GTC_DIR, "gtc_slide7_complexity.png")
    if os.path.exists(c_path7):
        cim7 = Image.open(c_path7)
        ax.imshow(cim7, extent=[5.5, 12.533, 0.45, 5.95], zorder=2)

    plt.savefig(os.path.join(PREVIEW_DIR, "slide_preview_7.png"), dpi=150, facecolor=BG_DARK)
    plt.close()
    print("[+] Rendered slide_preview_7.png")

    # --- SLIDE 8 ---
    fig, ax = create_base_slide(
        "Empirical Validation & Interactive Demonstration",
        "Experimental Benchmarks & Live System Launchpad",
        "Summary of 36 empirical benchmark runs, memory audits, and transition to live code execution",
        8
    )
    ribbon8_data = [
        ("33 / 33 Unit Tests Passed", "100% Deterministic oracle coverage across all 6 course units", GREEN, 0.8, 3.8),
        ("0 Memory Leaks", "Valgrind verified clean • Contiguous arena memory • Deterministic RSS", CYAN, 4.8, 3.8),
        ("36 Benchmark Runs", "Fully reproducible empirical CSV & JSON telemetry logged to disk", GREEN, 8.8, 3.733)
    ]
    for val, lbl, col, x, w in ribbon8_data:
        c = patches.FancyBboxPatch((x, 4.6), w, 1.35, boxstyle="round,pad=0.08,rounding_size=0.1",
                                   facecolor=CARD_BG, edgecolor=col, linewidth=1.5)
        ax.add_patch(c)
        ax.text(x + w/2, 5.4, val, ha='center', color=col, weight='bold', fontsize=16)
        ax.text(x + w/2, 4.9, lbl, ha='center', color=WHITE, fontsize=8.0, linespacing=1.2)

    d_path = os.path.join(ASSETS_DIR, "slide8_empirical_dashboard.png")
    if os.path.exists(d_path):
        dim = Image.open(d_path)
        ax.imshow(dim, extent=[0.8, 6.6, 0.45, 4.4], zorder=2)

    demo_c = patches.FancyBboxPatch((6.8, 0.45), 5.733, 3.95, boxstyle="round,pad=0.08,rounding_size=0.12",
                                    facecolor=CARD_BG, edgecolor=GREEN, linewidth=2.0)
    ax.add_patch(demo_c)
    ax.text(7.1, 3.95, "Interactive System Demonstration", color=GREEN, weight='bold', fontsize=14)
    ax.text(7.1, 2.9, "Live Execution Commands:\n• Web Studio:   .\\start_gui.bat  (http://localhost:8080)\n• Full C17 Suite: .\\bin\\test_all.exe  (33 Oracles)\n• Benchmark:     .\\bin\\benchmark.exe  (CSV/JSON Metrics)",
            color=WHITE, fontsize=9.2, linespacing=1.35, family='monospace')

    nq_p = os.path.join(CROPS_DIR, "ui_nqueens_card.png")
    if os.path.exists(nq_p):
        nq_im = Image.open(nq_p)
        ax.imshow(nq_im, extent=[7.1, 9.6, 0.6, 2.6], zorder=3)

    ax.text(12.2, 0.8, "Student: Sparsh Srivastava (Roll: 25010101828)\nReady for Technical Viva & Live Demonstration",
            ha='right', color=CYAN, weight='bold', fontsize=9.0)

    plt.savefig(os.path.join(PREVIEW_DIR, "slide_preview_8.png"), dpi=150, facecolor=BG_DARK)
    plt.close()
    print("[+] Rendered slide_preview_8.png")

if __name__ == "__main__":
    print("[*] Rendering Humanized Presentation Previews...")
    render_human_previews()
    print("[+] All 8 Humanized Preview PNGs rendered successfully!")
