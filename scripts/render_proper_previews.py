#!/usr/bin/env python3
"""
Render 1920x1080 PNG previews of the Perfectly Formatted Presentation Deck.
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
CODE_BG = "#0A101C"
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
    ax.text(0.8, 7.08, tracker, color=LIGHT_BLUE, weight='bold', fontsize=9.5)
    # Title
    ax.text(0.8, 6.62, title, color=WHITE, weight='bold', fontsize=19)
    # Subtitle
    if subtitle:
        ax.text(0.8, 6.22, subtitle, color=SLATE, fontsize=10.2)

    # Clean Number Pill
    badge = patches.FancyBboxPatch((11.0, 6.65), 1.5, 0.38, boxstyle="round,pad=0.08,rounding_size=0.1",
                                   facecolor=CARD_BG, edgecolor=BORDER, linewidth=1.5)
    ax.add_patch(badge)
    ax.text(11.75, 6.84, f"Slide {slide_num} of 8", ha='center', va='center', color=LIGHT_BLUE, weight='bold', fontsize=9.0)

    return fig, ax

def render_proper():
    # --- SLIDE 1 ---
    fig = plt.figure(figsize=(13.333, 7.5), dpi=150, facecolor=BG_DARK)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor(BG_DARK)
    ax.set_xlim(0, 13.333)
    ax.set_ylim(0, 7.5)
    ax.axis('off')

    ax.text(0.8, 7.0, "School of Computer Science & Engineering • Design & Analysis of Algorithms Capstone",
            color=LIGHT_BLUE, weight='bold', fontsize=10.5)
    ax.text(0.8, 6.42, "Cybersecurity Log Threat Detection Engine",
            color=WHITE, weight='bold', fontsize=26)
    ax.text(0.8, 5.92, "Pure C17 Algorithmic Architecture, Asymptotic Proofs & Sub-Millisecond Mitigation",
            color=SLATE, fontsize=11.5)

    # Student Credentials Card
    cred = patches.FancyBboxPatch((0.8, 4.85), 11.733, 0.75, boxstyle="round,pad=0.08,rounding_size=0.1",
                                  facecolor=CARD_BG, edgecolor=BORDER, linewidth=1.5)
    ax.add_patch(cred)
    ax.text(1.05, 5.32, "Presented by: Sparsh Srivastava   |   Roll No.: 25010101828   |   SAP ID: 590022251",
            color=GREEN, weight='bold', fontsize=10.5)
    ax.text(1.05, 5.0, "Course: CSEG3053 (Design & Analysis of Algorithms)   •   Evaluation: Saturday, 21 November 2026",
            color=SLATE, fontsize=9.2)

    # Ribbon
    r_path = os.path.join(GTC_DIR, "gtc_slide1_hero_ribbon.png")
    if os.path.exists(r_path):
        rim = Image.open(r_path)
        ax.imshow(rim, extent=[0.8, 12.533, 2.05, 4.65], zorder=2)

    # Bottom Highlights
    highlights = [
        ("Zero External Libraries", "Standard C17 Standard\nNo libc qsort, bsearch, regex", CYAN, 0.8),
        ("25+ Core Algorithms", "Divide & Conquer, String Search,\nGraphs, DP & Branch & Bound", GREEN, 3.8),
        ("1.2M Events / Sec", "Contiguous arena memory pool\nZero malloc in hot path", CYAN, 6.8),
        ("33 / 33 Unit Tests", "100% Deterministic pass rate\nValgrind verified: 0 leaks", GREEN, 9.8)
    ]
    for h_t, h_d, h_col, h_x in highlights:
        c = patches.FancyBboxPatch((h_x, 0.45), 2.73, 1.35, boxstyle="round,pad=0.08,rounding_size=0.1",
                                   facecolor=CARD_BG, edgecolor=h_col, linewidth=1.2)
        ax.add_patch(c)
        ax.text(h_x + 1.365, 1.38, h_t, ha='center', color=h_col, weight='bold', fontsize=9.8)
        ax.text(h_x + 1.365, 0.9, h_d, ha='center', color=WHITE, fontsize=8.2, linespacing=1.2)

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
        ax.imshow(pim, extent=[0.8, 12.533, 1.55, 6.0], zorder=2)

    in_box = patches.FancyBboxPatch((0.8, 0.45), 11.733, 0.9, boxstyle="round,pad=0.08,rounding_size=0.1",
                                    facecolor=CARD_BG, edgecolor=CYAN, linewidth=1.5)
    ax.add_patch(in_box)
    ax.text(1.1, 0.9, "Key Engineering Principle: A lock-free circular ring buffer isolates asynchronous I/O ingestion from CPU-bound graph traversal. Every pipeline stage adheres to strict asymptotic ceilings, ensuring zero packet drops under sustained 10 Gbps flood attacks.",
            color=WHITE, fontsize=9.0, va='center')

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
    # Left Card 1
    c1 = patches.FancyBboxPatch((0.8, 4.65), 4.3, 1.4, boxstyle="round,pad=0.08,rounding_size=0.1",
                                facecolor=CARD_BG, edgecolor=GREEN, linewidth=1.5)
    ax.add_patch(c1)
    ax.text(1.05, 5.5, "180× Faster", color=GREEN, weight='bold', fontsize=36)
    ax.text(1.05, 4.95, "Under Pre-Sorted Adversarial Log Floods", color=WHITE, weight='bold', fontsize=9.8)

    # Left Card 2
    c2 = patches.FancyBboxPatch((0.8, 2.75), 4.3, 1.75, boxstyle="round,pad=0.08,rounding_size=0.1",
                                facecolor=CARD_BG, edgecolor=BORDER, linewidth=1.5)
    ax.add_patch(c2)
    ax.text(1.05, 4.15, "Empirical Results (n = 1,000 logs):", color=CYAN, weight='bold', fontsize=9.2)
    ax.text(1.05, 3.25, "• Stable MergeSort: 11,088 comparisons  (Optimal)\n• Naive QuickSort:  1,999,000 comparisons (Degenerate)\n• Master Theorem Case 2: T(n) = 2T(n/2) + Θ(n) => Θ(n log n)",
            color=WHITE, fontsize=8.2, linespacing=1.3)

    # Left Card 3
    c3 = patches.FancyBboxPatch((0.8, 0.45), 4.3, 2.1, boxstyle="round,pad=0.08,rounding_size=0.1",
                                facecolor=CARD_BG, edgecolor=BORDER, linewidth=1.5)
    ax.add_patch(c3)
    ax.text(1.05, 2.15, "Why this matters in Cybersecurity:", color=GREEN, weight='bold', fontsize=9.2)
    ax.text(1.05, 1.15, "Attackers intentionally stream sorted timestamps to force naive\nsorting engines into quadratic Θ(n²) partition degradation,\ninducing severe CPU starvation DoS. Our stable MergeSort\nguarantees immune, bounded throughput.",
            color=SLATE, fontsize=8.2, linespacing=1.3)

    s_path = os.path.join(GTC_DIR, "gtc_slide3_sorting_showdown.png")
    if os.path.exists(s_path):
        sim = Image.open(s_path)
        ax.imshow(sim, extent=[5.3, 12.533, 0.45, 5.95], zorder=2)

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
    # Left Card 1
    c1 = patches.FancyBboxPatch((0.8, 4.65), 4.3, 1.4, boxstyle="round,pad=0.08,rounding_size=0.1",
                                facecolor=CARD_BG, edgecolor=CYAN, linewidth=1.5)
    ax.add_patch(c1)
    ax.text(1.05, 5.5, "4.5× Speedup", color=CYAN, weight='bold', fontsize=34)
    ax.text(1.05, 4.95, "Zero Pointer Backtracking on Malicious Payloads", color=WHITE, weight='bold', fontsize=9.5)

    # Left Card 2
    c2 = patches.FancyBboxPatch((0.8, 2.6), 4.3, 1.9, boxstyle="round,pad=0.08,rounding_size=0.1",
                                facecolor=CODE_BG, edgecolor=BORDER, linewidth=1.5)
    ax.add_patch(c2)
    ax.text(1.05, 4.15, "Actual Implementation (src/string_matching.c):", color=GREEN, weight='bold', fontsize=8.8)
    ax.text(1.05, 3.15, "while (q > 0 && pattern[q] != text[i]) {\n    q = pi[q - 1];  // Fallback via prefix table\n}\nif (pattern[q] == text[i]) q++;\n// Text pointer i strictly NEVER decrements!",
            color=WHITE, fontsize=7.8, linespacing=1.2, family='monospace')

    # Left Card 3
    c3 = patches.FancyBboxPatch((0.8, 0.45), 4.3, 2.0, boxstyle="round,pad=0.08,rounding_size=0.1",
                                facecolor=CARD_BG, edgecolor=BORDER, linewidth=1.5)
    ax.add_patch(c3)
    ax.text(1.05, 2.05, "Adversarial Stress Test ('AAAA...AAB'):", color=CYAN, weight='bold', fontsize=9.0)
    ax.text(1.05, 1.1, "• Naive Matcher: 89,919 operations (O(n·m) stall)\n• KMP Automaton: 20,004 operations (Linear O(n+m))\nKMP's failure function advances the text pointer monotonically,\ncompletely defusing algorithmic re-scan attacks.",
            color=SLATE, fontsize=8.0, linespacing=1.25)

    str_p = os.path.join(GTC_DIR, "gtc_slide4_string.png")
    if os.path.exists(str_p):
        st_im = Image.open(str_p)
        ax.imshow(st_im, extent=[5.3, 12.533, 0.45, 5.95], zorder=2)

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
    # Left Card 1
    c1 = patches.FancyBboxPatch((0.8, 4.65), 4.3, 1.4, boxstyle="round,pad=0.08,rounding_size=0.1",
                                facecolor=CARD_BG, edgecolor=CYAN, linewidth=1.5)
    ax.add_patch(c1)
    ax.text(1.05, 5.5, "Min-Cut", color=CYAN, weight='bold', fontsize=38)
    ax.text(1.05, 4.95, "Capacity-Bounded Network Quarantine", color=WHITE, weight='bold', fontsize=10.0)

    # Left Card 2
    c2 = patches.FancyBboxPatch((0.8, 2.65), 4.3, 1.85, boxstyle="round,pad=0.08,rounding_size=0.1",
                                facecolor=CARD_BG, edgecolor=BORDER, linewidth=1.5)
    ax.add_patch(c2)
    ax.text(1.05, 4.15, "Real-Time Telemetry Findings:", color=GREEN, weight='bold', fontsize=9.2)
    ax.text(1.05, 3.2, "• 412 MB/s exfiltration halted immediately\n• Sever Cost: 22 Mbps minimal disruption\n• Caught hidden -5 privilege escalation loop\n  via Bellman-Ford O(V·E) relaxation",
            color=WHITE, fontsize=8.2, linespacing=1.25)

    # Left Card 3
    c3 = patches.FancyBboxPatch((0.8, 0.45), 4.3, 2.05, boxstyle="round,pad=0.08,rounding_size=0.1",
                                facecolor=CARD_BG, edgecolor=BORDER, linewidth=1.5)
    ax.add_patch(c3)
    ax.text(1.05, 2.15, "Max-Flow / Min-Cut Application:", color=CYAN, weight='bold', fontsize=9.2)
    ax.text(1.05, 1.15, "Instead of broad brute-force network blackouts,\nFord-Fulkerson extracts the exact 8 saturated bottleneck edges.\nWe quarantine 100% of the breach while normal corporate\ntraffic continues unimpeded.",
            color=SLATE, fontsize=8.2, linespacing=1.25)

    m_path = os.path.join(GTC_DIR, "gtc_slide5_mincut.png")
    if os.path.exists(m_path):
        mim = Image.open(m_path)
        ax.imshow(mim, extent=[5.3, 12.533, 0.45, 5.95], zorder=2)

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
    # Left Card 1
    c1 = patches.FancyBboxPatch((0.8, 4.65), 4.3, 1.4, boxstyle="round,pad=0.08,rounding_size=0.1",
                                facecolor=CARD_BG, edgecolor=GREEN, linewidth=1.5)
    ax.add_patch(c1)
    ax.text(1.05, 5.5, "78% Pruned", color=GREEN, weight='bold', fontsize=38)
    ax.text(1.05, 4.95, "Of State-Space Search Nodes Discarded", color=WHITE, weight='bold', fontsize=10.0)

    # Left Card 2
    c2 = patches.FancyBboxPatch((0.8, 2.65), 4.3, 1.85, boxstyle="round,pad=0.08,rounding_size=0.1",
                                facecolor=CARD_BG, edgecolor=BORDER, linewidth=1.5)
    ax.add_patch(c2)
    ax.text(1.05, 4.15, "Mathematical Pruning Criterion:", color=CYAN, weight='bold', fontsize=9.2)
    ax.text(1.05, 3.2, "• Root Bound: UB = $280 | Optimum: Set N9 (w=15, v=$260)\n• Pruning Condition: If node UB <= $240 (Current Best Feasible),\n  discard the entire subtree immediately.",
            color=WHITE, fontsize=8.2, linespacing=1.25)

    # Left Card 3
    c3 = patches.FancyBboxPatch((0.8, 0.45), 4.3, 2.05, boxstyle="round,pad=0.08,rounding_size=0.1",
                                facecolor=CARD_BG, edgecolor=BORDER, linewidth=1.5)
    ax.add_patch(c3)
    ax.text(1.05, 2.15, "Search Policy Evaluation:", color=GREEN, weight='bold', fontsize=9.2)
    ax.text(1.05, 1.15, "• Least-Cost (Max-Heap): Expands only 4 promising nodes\n  before hitting the optimal.\n• FIFO & LIFO: Evaluates 14+ unpromising nodes.\nFractional upper bounding ensures we never overrun\nexecutive SLA downtime budgets.",
            color=SLATE, fontsize=8.2, linespacing=1.25)

    p_path6 = os.path.join(GTC_DIR, "gtc_slide6_pruning.png")
    if os.path.exists(p_path6):
        pim6 = Image.open(p_path6)
        ax.imshow(pim6, extent=[5.3, 12.533, 0.45, 5.95], zorder=2)

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
    # Left Card 1
    c1 = patches.FancyBboxPatch((0.8, 4.65), 4.3, 1.4, boxstyle="round,pad=0.08,rounding_size=0.1",
                                facecolor=CARD_BG, edgecolor=RED, linewidth=1.5)
    ax.add_patch(c1)
    ax.text(1.05, 5.5, "NP-Complete", color=RED, weight='bold', fontsize=34)
    ax.text(1.05, 4.95, "Formal Rigor Grounded in Complexity Theory", color=WHITE, weight='bold', fontsize=9.8)

    # Left Card 2
    c2 = patches.FancyBboxPatch((0.8, 2.5), 4.3, 2.0, boxstyle="round,pad=0.08,rounding_size=0.1",
                                facecolor=CODE_BG, edgecolor=BORDER, linewidth=1.5)
    ax.add_patch(c2)
    ax.text(1.05, 4.15, "Two-Step Formal Proof:", color=CYAN, weight='bold', fontsize=9.0)
    ax.text(1.05, 3.15, "1. In NP: Certificate verified in O(n) Time\n2. NP-Hard: Reduction from SUBSET-SUM:\n   w_i = s_i,  v_i = s_i,  W = T,  V = T\n   SUBSET-SUM has solution <=> Knapsack profit >= T",
            color=WHITE, fontsize=7.8, linespacing=1.2, family='monospace')

    # Left Card 3
    c3 = patches.FancyBboxPatch((0.8, 0.45), 4.3, 1.9, boxstyle="round,pad=0.08,rounding_size=0.1",
                                facecolor=CARD_BG, edgecolor=BORDER, linewidth=1.5)
    ax.add_patch(c3)
    ax.text(1.05, 2.05, "Why this matters in Practice:", color=GREEN, weight='bold', fontsize=9.2)
    ax.text(1.05, 1.15, "Proves that no polynomial-time algorithm exists\n(under P != NP). This mathematically justifies using\nBranch & Bound fractional bounding for sub-millisecond\nreal-time response.",
            color=SLATE, fontsize=8.2, linespacing=1.25)

    c_path7 = os.path.join(GTC_DIR, "gtc_slide7_complexity.png")
    if os.path.exists(c_path7):
        cim7 = Image.open(c_path7)
        ax.imshow(cim7, extent=[5.3, 12.533, 0.45, 5.95], zorder=2)

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
    # Top Row
    ribbon8_data = [
        ("33 / 33 Tests Passed", "100% Deterministic oracle coverage across all 6 course units", GREEN, 0.8, 3.75),
        ("0 Memory Leaks", "Valgrind clean • Contiguous arena • Deterministic RSS", CYAN, 4.75, 3.75),
        ("36 Benchmark Runs", "Fully reproducible empirical CSV & JSON telemetry on disk", GREEN, 8.7, 3.833)
    ]
    for val, lbl, col, x, w in ribbon8_data:
        c = patches.FancyBboxPatch((x, 4.85), w, 1.2, boxstyle="round,pad=0.08,rounding_size=0.1",
                                   facecolor=CARD_BG, edgecolor=col, linewidth=1.5)
        ax.add_patch(c)
        ax.text(x + w/2, 5.65, val, ha='center', color=col, weight='bold', fontsize=14.5)
        ax.text(x + w/2, 5.15, lbl, ha='center', color=WHITE, fontsize=7.8, linespacing=1.2)

    # Bottom Left Dashboard
    d_path = os.path.join(ASSETS_DIR, "slide8_empirical_dashboard.png")
    if os.path.exists(d_path):
        dim = Image.open(d_path)
        ax.imshow(dim, extent=[0.8, 6.5, 0.45, 4.55], zorder=2)

    # Bottom Right Demo Box
    demo_c = patches.FancyBboxPatch((6.75, 0.45), 5.783, 4.1, boxstyle="round,pad=0.08,rounding_size=0.12",
                                    facecolor=CARD_BG, edgecolor=GREEN, linewidth=2.0)
    ax.add_patch(demo_c)
    ax.text(7.05, 4.25, "Interactive System Demonstration", color=GREEN, weight='bold', fontsize=13.5)
    ax.text(7.05, 3.85, "Execution Commands for Technical Viva:", color=WHITE, weight='bold', fontsize=9.2)
    ax.text(7.05, 3.15, "• Web Studio:   .\\start_gui.bat  (http://localhost:8080)\n• Full C17 Suite: .\\bin\\test_all.exe  (33/33 Tests Pass)\n• Benchmark:     .\\bin\\benchmark.exe  (CSV/JSON Output)",
            color=CYAN, fontsize=8.5, linespacing=1.25, family='monospace')

    # GUI Honeypot Image cleanly embedded
    nq_p = os.path.join(CROPS_DIR, "ui_nqueens_card.png")
    if os.path.exists(nq_p):
        nq_im = Image.open(nq_p)
        ax.imshow(nq_im, extent=[7.05, 9.4, 0.65, 2.5], zorder=3)

    # Signature card on right side of honeypot
    sig_c = patches.FancyBboxPatch((9.6, 0.65), 2.7, 1.85, boxstyle="round,pad=0.08,rounding_size=0.1",
                                  facecolor=CODE_BG, edgecolor=BORDER, linewidth=1.2)
    ax.add_patch(sig_c)
    ax.text(9.8, 2.15, "Sparsh Srivastava", color=GREEN, weight='bold', fontsize=10.5)
    ax.text(9.8, 1.35, "Roll No.: 25010101828\nSAP ID: 590022251\nCSEG3053 Capstone\nReady for Viva Defense",
            color=SLATE, fontsize=8.0, linespacing=1.25)

    plt.savefig(os.path.join(PREVIEW_DIR, "slide_preview_8.png"), dpi=150, facecolor=BG_DARK)
    plt.close()
    print("[+] Rendered slide_preview_8.png")

if __name__ == "__main__":
    print("[*] Rendering Properly Formatted Previews...")
    render_proper()
    print("[+] All 8 Previews rendered successfully!")
