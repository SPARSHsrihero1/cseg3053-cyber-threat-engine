#!/usr/bin/env python3
"""
Generate High-Quality Executive Presentation for CSEG3053 Project 03:
Cybersecurity Log Threat Detection Engine (Pure C17)
Outputs:
  - presentation/CSEG3053_Cyber_Threat_Engine_Presentation.pptx (16:9 Widescreen PPTX)
  - presentation/slides.md (Markdown Slide Deck)
"""

import os
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRES_DIR = os.path.join(BASE_DIR, "presentation")
PPTX_PATH = os.path.join(PRES_DIR, "CSEG3053_Cyber_Threat_Engine_Presentation.pptx")
MD_SLIDES_PATH = os.path.join(PRES_DIR, "slides.md")

# SOC Modern Color Palette
BG_DARK = RGBColor(11, 17, 32)       # Slate 950 #0B1120
CARD_BG = RGBColor(21, 32, 51)      # Dark Navy #152033
CARD_BORDER = RGBColor(34, 52, 80)  # Border #223450
CYAN = RGBColor(0, 240, 255)        # Electric Cyan #00F0FF
MAGENTA = RGBColor(255, 0, 85)      # Neon Magenta #FF0055
AMBER = RGBColor(245, 158, 11)      # Amber #F59E0B
GREEN = RGBColor(16, 185, 129)      # Emerald #10B981
WHITE = RGBColor(255, 255, 255)
MUTED = RGBColor(148, 163, 184)     # Slate 400 #94A3B8

def add_header(slide, title_text, category_text="CSEG3053 DESIGN AND ANALYSIS OF ALGORITHMS"):
    # Category Tracker
    cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11), Inches(0.4))
    tf_cat = cat_box.text_frame
    tf_cat.word_wrap = True
    p_cat = tf_cat.paragraphs[0]
    p_cat.text = category_text.upper()
    p_cat.font.size = Pt(10)
    p_cat.font.bold = True
    p_cat.font.color.rgb = CYAN
    p_cat.font.name = 'Consolas'

    # Title
    t_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(11.5), Inches(0.8))
    tf_t = t_box.text_frame
    tf_t.word_wrap = True
    p_t = tf_t.paragraphs[0]
    p_t.text = title_text
    p_t.font.size = Pt(22)
    p_t.font.bold = True
    p_t.font.color.rgb = WHITE
    p_t.font.name = 'Segoe UI'

def create_card(slide, left, top, width, height, title, subtitle=None, bg_color=CARD_BG, border_color=CARD_BORDER):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = bg_color
    shape.line.color.rgb = border_color
    shape.line.width = Pt(1.2)

    tb = slide.shapes.add_textbox(left + Inches(0.15), top + Inches(0.12), width - Inches(0.3), height - Inches(0.24))
    tf = tb.text_frame
    tf.word_wrap = True
    
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = CYAN
    p.font.name = 'Segoe UI'

    if subtitle:
        p2 = tf.add_paragraph()
        p2.text = subtitle
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = MUTED
        p2.font.name = 'Consolas'
    
    return tf

def build_pptx():
    print("[*] Generating Widescreen 16:9 Presentation: presentation/CSEG3053_Cyber_Threat_Engine_Presentation.pptx ...")
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # =========================================================================
    # SLIDE 1: TITLE SLIDE
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = BG_DARK
    bg1.line.fill.background()

    # Title Card
    t_box = s1.shapes.add_textbox(Inches(1.0), Inches(1.5), Inches(11.3), Inches(3.0))
    tf1 = t_box.text_frame
    tf1.word_wrap = True

    p0 = tf1.paragraphs[0]
    p0.text = "CSEG3053: DESIGN AND ANALYSIS OF ALGORITHMS — CAPSTONE PBL"
    p0.font.size = Pt(13)
    p0.font.bold = True
    p0.font.color.rgb = CYAN
    p0.font.name = 'Consolas'

    p1 = tf1.add_paragraph()
    p1.text = "Cybersecurity Log Threat Detection Engine"
    p1.font.size = Pt(36)
    p1.font.bold = True
    p1.font.color.rgb = WHITE
    p1.font.name = 'Segoe UI'

    p2 = tf1.add_paragraph()
    p2.text = "A Complete Industry-Grade Algorithmic Workbench & SOC Analytics Engine in Pure C17"
    p2.font.size = Pt(16)
    p2.font.color.rgb = MUTED
    p2.font.name = 'Segoe UI'

    # 4 Meta Stat Badges
    badges = [
        ("STANDARD", "Strict Pure C17 (-std=c17 -O2)", CYAN),
        ("ALGORITHMS", "25+ Mandatory Syllabus Implementations", AMBER),
        ("TEST SUITE", "33 / 33 Passing Unit Test Oracles", GREEN),
        ("GIT RELEASE", "v1.0.0 Tagged on GitHub", MAGENTA)
    ]
    for idx, (lbl, val, col) in enumerate(badges):
        x = Inches(1.0 + idx * 2.85)
        shape = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(4.8), Inches(2.7), Inches(1.5))
        shape.fill.solid()
        shape.fill.fore_color.rgb = CARD_BG
        shape.line.color.rgb = col
        shape.line.width = Pt(1.5)

        tf_b = shape.text_frame
        tf_b.word_wrap = True
        pb1 = tf_b.paragraphs[0]
        pb1.text = lbl
        pb1.font.size = Pt(9.5)
        pb1.font.bold = True
        pb1.font.color.rgb = col
        pb1.font.name = 'Consolas'

        pb2 = tf_b.add_paragraph()
        pb2.text = val
        pb2.font.size = Pt(11)
        pb2.font.bold = True
        pb2.font.color.rgb = WHITE
        pb2.font.name = 'Segoe UI'

    # =========================================================================
    # SLIDE 2: PROBLEM STATEMENT & SOC OPERATIONS
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    bg2 = s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg2.fill.solid()
    bg2.fill.fore_color.rgb = BG_DARK
    bg2.line.fill.background()
    add_header(s2, "SOC Operations Challenge: The Telemetry Explosion Problem")

    tf_c1 = create_card(s2, Inches(0.8), Inches(1.7), Inches(5.6), Inches(5.1), "1. The Operational Security Crisis", "Telemetry Overload & Analyst Fatigue")
    pts1 = [
        "Massive Data Velocity: Enterprise networks generate 50,000+ syslog events/sec across firewalls, EDR agents, and DNS.",
        "Algorithmic Denial-of-Service: Adversaries intentionally send pre-sorted or repetitive traffic to induce worst-case O(N^2) stalls in naive detection systems.",
        "SLA Downtime Crunch: In active ransomware outbreaks, administrators face strict downtime limits before critical operations collapse.",
        "Data Exfiltration Velocity: Stolen data routes through complex multi-hop relays; disconnecting whole networks causes unacceptable business interruption."
    ]
    for pt in pts1:
        p = tf_c1.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(11)
        p.font.color.rgb = WHITE

    tf_c2 = create_card(s2, Inches(6.8), Inches(1.7), Inches(5.7), Inches(5.1), "2. The Pure C17 Solution Engine", "Zero Black-Box Abstractions")
    pts2 = [
        "Pure C17 Standard: ISO/IEC 9899:2018 with strictly zero standard library shortcuts (no qsort, bsearch, or strstr).",
        "Deterministic Resource Bounds: Predictable memory allocation through tracked heap wrappers and cache-friendly contiguous arrays.",
        "Full Asymptotic Analysis: Operational instrumentation tracking exact comparisons, writes, recursive calls, and graph relaxations.",
        "Interactive SOC Studio: A modern visual workbench enabling real-time inspection, parameter tuning, and dynamic simulation."
    ]
    for pt in pts2:
        p = tf_c2.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(11)
        p.font.color.rgb = WHITE

    # =========================================================================
    # SLIDE 3: SYSTEM ARCHITECTURE
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    bg3 = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg3.fill.solid()
    bg3.fill.fore_color.rgb = BG_DARK
    bg3.line.fill.background()
    add_header(s3, "System Architecture: Decoupled Multi-Layer Design")

    layers = [
        ("1. Display & Interaction", "CLI Console (main.c) & Web Studio Dashboard (index.html, server.py)", CYAN),
        ("2. Core Domain & Telemetry", "Typed C Entities (domain.h), MetricsTracker (metrics.c), PRNG DataGen", AMBER),
        ("3. Algorithmic Workbench", "Units II to VI modular libraries: D&C, Greedy, DP, Backtracking, B&B, Flow, Strings", GREEN),
        ("4. Verification & Persistence", "33/33 Assertion Unit Tests, RFC CSV/JSON Exporters, CMake & Makefile Build", MAGENTA)
    ]
    for i, (l_title, l_desc, l_col) in enumerate(layers):
        y = Inches(1.7 + i * 1.25)
        tf_lay = create_card(s3, Inches(0.8), y, Inches(11.7), Inches(1.05), l_title, l_desc, border_color=l_col)

    # =========================================================================
    # SLIDE 4: COMPLETE SYLLABUS MAPPING MATRIX
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    bg4 = s4.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg4.fill.solid()
    bg4.fill.fore_color.rgb = BG_DARK
    bg4.line.fill.background()
    add_header(s4, "Complete CSEG3053 Syllabus Mapping Matrix")

    units = [
        ("Unit II: Divide & Conquer", ["Merge & Quick Sort (Deterministic vs Randomized)", "Iterative & Recursive Binary Search & BST Search", "Maximum Subarray (Kadane vs D&C Anomaly)", "Celebrity Problem (O(N) C2 Sinkhole Detection)", "Classical vs Strassen Matrix Multiplication"], CYAN),
        ("Unit III: Greedy Methods", ["Activity Selection (Vulnerability Scan Scheduler)", "Interval Partitioning (Malware Detonation Sandboxes)", "Fractional Knapsack (DPI Bandwidth Allocation)", "Huffman Coding (Syslog Cold-Storage Compression)", "Dijkstra & Prim/Kruskal MST (Quarantine Spanning)"], AMBER),
        ("Unit IV: Dynamic Prog.", ["0/1 Knapsack DP (Containment Playbooks with Recon)", "Matrix Chain Multiplication (Telemetry Join Ordering)", "LCS (APT Kill-Chain Sequence Alignment)", "Optimal BST Index & Bellman-Ford Negative Escalation", "Floyd-Warshall Exposure & Held-Karp TSP DP"], GREEN),
        ("Unit V & VI: B&B, Flow, CRT", ["N-Queens Deception Honeypots & Sum of Subsets", "Knapsack B&B (FIFO, LIFO, Least-Cost Policies)", "Ford-Fulkerson & Min-Cut Firewall Link Severing", "Maximum Bipartite Matching (Analyst Dispatch)", "Chinese Remainder Thm & 4 String Matchers (KMP)"], MAGENTA)
    ]

    for idx, (u_title, alg_list, u_col) in enumerate(units):
        col_x = Inches(0.8 + (idx % 2) * 5.95)
        col_y = Inches(1.7 + (idx // 2) * 2.65)
        tf_u = create_card(s4, col_x, col_y, Inches(5.75), Inches(2.45), u_title, "All Implemented From Scratch in Pure C17", border_color=u_col)
        for a in alg_list:
            p = tf_u.add_paragraph()
            p.text = "• " + a
            p.font.size = Pt(9.5)
            p.font.color.rgb = WHITE

    # =========================================================================
    # SLIDE 5: UNIT II - DIVIDE & CONQUER
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    bg5 = s5.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg5.fill.solid()
    bg5.fill.fore_color.rgb = BG_DARK
    bg5.line.fill.background()
    add_header(s5, "Unit II: Divide and Conquer in Cybersecurity Triage")

    tf_u2_1 = create_card(s5, Inches(0.8), Inches(1.7), Inches(5.7), Inches(5.1), "Merge vs. Quick Sort & Binary Search", "Log Ingestion & Fast Timeline Triage")
    u2_pts1 = [
        "Stable Chronological Sorting: MergeSort guarantees Theta(N log N) sorting without reordering simultaneous arrivals.",
        "Defeating Algorithmic Denial of Service: Deterministic QuickSort degrades to O(N^2) on pre-sorted logs (1,999,000 comparisons). Randomized pivot restores O(N log N) stability.",
        "Logarithmic Timeline Search: Iterative & Recursive Binary Search locate forensic event timestamps in exactly 9 comparisons on 1,000 logs.",
        "BST Signature Index: Dynamic binary tree lookup for active intrusion detection rules."
    ]
    for pt in u2_pts1:
        p = tf_u2_1.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(10.5)
        p.font.color.rgb = WHITE

    tf_u2_2 = create_card(s5, Inches(6.8), Inches(1.7), Inches(5.7), Inches(5.1), "Burst Anomaly, C2 Detection & Strassen", "Advanced Pattern Discovery")
    u2_pts2 = [
        "Maximum Subarray (Kadane vs D&C): Isolates the exact start and end timestamps of a volumetric DDoS or brute-force attack window.",
        "Fast Modular Exponentiation: Computes b^e mod m in Theta(log e) for polynomial rolling hashes without integer overflow.",
        "Celebrity Problem (C2 Sinkhole): Eliminates non-C2 hosts in N-1 comparisons, identifying hidden relays beaconed to by all compromised bots in O(N).",
        "Strassen Matrix Multiplication: Sub-cubic Theta(N^2.807) multiplication on host transition matrices for multi-hop lateral movement reachability."
    ]
    for pt in u2_pts2:
        p = tf_u2_2.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(10.5)
        p.font.color.rgb = WHITE

    # =========================================================================
    # SLIDE 6: MATHEMATICAL RECURRENCE PROOFS
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    bg6 = s6.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg6.fill.solid()
    bg6.fill.fore_color.rgb = BG_DARK
    bg6.line.fill.background()
    add_header(s6, "Mathematical Recurrence Derivations & Master Theorem")

    tf_m1 = create_card(s6, Inches(0.8), Inches(1.7), Inches(5.7), Inches(5.1), "1. Master Theorem Applications", "Merge Sort & Strassen Multiplications")
    m1_pts = [
        "Merge Sort: T(n) = 2T(n/2) + Theta(n)",
        "  - a = 2, b = 2, f(n) = cn -> n^(log_b a) = n^1 = n",
        "  - Since f(n) = Theta(n^(log_b a)), Master Theorem Case 2 applies:",
        "  - Result: T(n) = Theta(n log n)",
        "Strassen Matrix: T(N) = 7T(N/2) + Theta(N^2)",
        "  - a = 7, b = 2 -> N^(log_2 7) approx N^2.807",
        "  - Since f(N) = N^2 = O(N^(2.807 - eps)), Case 1 applies:",
        "  - Result: T(N) = Theta(N^2.807)"
    ]
    for pt in m1_pts:
        p = tf_m1.add_paragraph()
        p.text = pt
        p.font.size = Pt(10)
        p.font.color.rgb = WHITE
        p.font.name = 'Consolas' if 'T(' in pt else 'Segoe UI'

    tf_m2 = create_card(s6, Inches(6.8), Inches(1.7), Inches(5.7), Inches(5.1), "2. Master Theorem Inapplicability", "Quick Sort Adversarial Worst-Case")
    m2_pts = [
        "Adversarial QuickSort Recurrence: T(n) = T(n-1) + T(0) + Theta(n) = T(n-1) + cn",
        "Why Master Theorem Fails: Master Theorem requires subproblem division (n/b with b > 1). It cannot solve subtractive decrements (n - 1).",
        "Solution via Iterative Unrolling:",
        "  T(n) = T(n-1) + cn",
        "  T(n) = T(n-2) + c(n-1) + cn",
        "  T(n) = T(0) + c * sum(i=1 to n) i",
        "  T(n) = Theta(1) + c * [n(n+1)/2] = Theta(n^2)",
        "Conclusion: Proves the necessity of randomized pivot selection in security engines."
    ]
    for pt in m2_pts:
        p = tf_m2.add_paragraph()
        p.text = pt
        p.font.size = Pt(10)
        p.font.color.rgb = WHITE
        p.font.name = 'Consolas' if 'T(' in pt else 'Segoe UI'

    # =========================================================================
    # SLIDE 7: UNIT III - GREEDY METHODS
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    bg7 = s7.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg7.fill.solid()
    bg7.fill.fore_color.rgb = BG_DARK
    bg7.line.fill.background()
    add_header(s7, "Unit III: Greedy Methods for Network Optimization")

    g_cards = [
        ("Activity Selection", "Earliest-finish-time scan scheduling to maximize non-overlapping vulnerability scans.", CYAN),
        ("Interval Partitioning", "Min-heap allocation sizing minimum parallel sandbox VMs for concurrent alert windows.", AMBER),
        ("Fractional Knapsack", "Prioritizes Deep Packet Inspection (DPI) bandwidth fractions by threat-to-volume ratio.", GREEN),
        ("Huffman Compression", "Min-heap prefix-free variable-length binary tree cutting syslog storage costs by ~50%.", MAGENTA),
        ("Dijkstra Exploit Path", "Custom binary min-heap calculating single-source least-resistance exploit routes.", CYAN),
        ("Prim & Kruskal MST", "Minimum-cost resilient out-of-band quarantine cabling tree via custom Union-Find.", GREEN)
    ]
    for idx, (title, desc, col) in enumerate(g_cards):
        x = Inches(0.8 + (idx % 3) * 3.95)
        y = Inches(1.7 + (idx // 3) * 2.65)
        tf_g = create_card(s7, x, y, Inches(3.8), Inches(2.45), title, border_color=col)
        p = tf_g.add_paragraph()
        p.text = desc
        p.font.size = Pt(10)
        p.font.color.rgb = WHITE

    # =========================================================================
    # SLIDE 8: UNIT IV - DYNAMIC PROGRAMMING
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    bg8 = s8.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg8.fill.solid()
    bg8.fill.fore_color.rgb = BG_DARK
    bg8.line.fill.background()
    add_header(s8, "Unit IV: Dynamic Programming & State Optimization")

    dp_cards = [
        ("0/1 Knapsack DP", "Maximizes risk mitigation under tight SLA downtime budgets; reconstructs chosen playbooks via table backtracking.", CYAN),
        ("Matrix Chain Order", "Computes optimal parenthesization for multi-stage telemetry joins across Firewall, DNS, IAM, and EDR dimensions.", AMBER),
        ("LCS Kill-Chain", "Aligns observed audit tokens with known APT kill-chains, isolating stealthy attacks despite camouflage noise.", GREEN),
        ("Optimal BST Index", "Static frequency-optimized signature lookup tree minimizing expected search depth based on attack frequencies.", MAGENTA),
        ("Bellman-Ford", "Shortest exploit pathing with negative edge weights (privilege escalation benefits) and negative cycle detection.", CYAN),
        ("Held-Karp TSP DP", "Exact bitmask dynamic programming (Theta(n^2 2^n)) finding minimum-latency forensic collector memory dump tours.", GREEN)
    ]
    for idx, (title, desc, col) in enumerate(dp_cards):
        x = Inches(0.8 + (idx % 3) * 3.95)
        y = Inches(1.7 + (idx // 3) * 2.65)
        tf_dp = create_card(s8, x, y, Inches(3.8), Inches(2.45), title, border_color=col)
        p = tf_dp.add_paragraph()
        p.text = desc
        p.font.size = Pt(10)
        p.font.color.rgb = WHITE

    # =========================================================================
    # SLIDE 9: UNIT V - BACKTRACKING & BRANCH AND BOUND
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    bg9 = s9.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg9.fill.solid()
    bg9.fill.fore_color.rgb = BG_DARK
    bg9.line.fill.background()
    add_header(s9, "Unit V: Backtracking and Branch & Bound Solvers")

    tf_bb1 = create_card(s9, Inches(0.8), Inches(1.7), Inches(5.7), Inches(5.1), "1. Backtracking Constraint Solvers", "N-Queens & Sum of Subsets")
    bb1_pts = [
        "N-Queens Deception Grid: Validates placement of N honeypot sensors across an NxN routing grid with zero shared rows, columns, or diagonal subnet slices (Verified 92 solutions on N=8).",
        "Sum of Subsets Alert Escalation: Backtracking solver with dual-bounding pruning to find all micro-alert combinations that sum to a critical escalation threshold W.",
        "0/1 Knapsack Backtracking: Explores state-space tree depth-first using continuous fractional bounds to prune subtrees that cannot beat the incumbent."
    ]
    for pt in bb1_pts:
        p = tf_bb1.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(10.5)
        p.font.color.rgb = WHITE

    tf_bb2 = create_card(s9, Inches(6.8), Inches(1.7), Inches(5.7), Inches(5.1), "2. Branch and Bound Strategies", "FIFO vs LIFO vs Least-Cost (LC)")
    bb2_pts = [
        "Queue-Based FIFO (BFS): Evaluates 57 nodes, prunes 11 unpromising branches under budget constraints.",
        "Stack-Based LIFO (DFS): Explores deep states, pruning 11 branches with lower memory footprint.",
        "Least-Cost Priority Queue (LC-BB): Evaluates the most promising upper-bound nodes first, achieving the tightest exploration (9 nodes pruned).",
        "TSP Least-Cost B&B: Utilizes an admissible lower bounding function, converging on the exact same optimal tour cost (281) as Held-Karp DP while pruning 22,474 subtrees."
    ]
    for pt in bb2_pts:
        p = tf_bb2.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(10.5)
        p.font.color.rgb = WHITE

    # =========================================================================
    # SLIDE 10: UNIT VI - FLOW, CRT & STRING MATCHING
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    bg10 = s10.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg10.fill.solid()
    bg10.fill.fore_color.rgb = BG_DARK
    bg10.line.fill.background()
    add_header(s10, "Unit VI: Network Flow, Number Theory & String Matchers")

    tf_fl1 = create_card(s10, Inches(0.8), Inches(1.7), Inches(5.7), Inches(5.1), "1. Flow, Cut & Bipartite Matching", "Capacity & Incident Containment")
    fl1_pts = [
        "Ford-Fulkerson (Edmonds-Karp): Computes maximum exfiltration data flow (412 MB/s) from internal database source to external C2 sink via BFS augmenting paths.",
        "Minimum s-t Cut Link Severing: Extracts the exact 8 saturated bottleneck firewall rules to sever, halting 100% of exfiltration with minimal collateral disruption.",
        "Maximum Bipartite Matching: Dispatches security incidents to certified SOC analysts based on skill matrix compatibility in O(V * E).",
        "Chinese Remainder Theorem: Reconstructs global 32-bit packet counters from low-memory edge sensors using the Extended Euclidean algorithm."
    ]
    for pt in fl1_pts:
        p = tf_fl1.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(10.5)
        p.font.color.rgb = WHITE

    tf_fl2 = create_card(s10, Inches(6.8), Inches(1.7), Inches(5.7), Inches(5.1), "2. The 4 String-Matching Engines", "Defeating Pathological Infiltration")
    fl2_pts = [
        "Naive Sliding Window: Baseline inspection algorithm with O(n * m) worst-case vulnerability.",
        "Rabin-Karp Rolling Hash: Linear average-case inspection tracking modular hash collisions with zero false positives.",
        "Finite Automaton Matcher: Precomputes state transition delta(q, a) table for deterministic single-pass scanning in Theta(n).",
        "Knuth-Morris-Pratt (KMP): Uses precomputed prefix pi table to skip redundant checks, achieving linear Theta(n) time on repetitive payloads ('AAAA...B') where Naive takes 89,919 comparisons."
    ]
    for pt in fl2_pts:
        p = tf_fl2.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(10.5)
        p.font.color.rgb = WHITE

    # =========================================================================
    # SLIDE 11: COMPLEXITY THEORY & REDUCTIONS
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    bg11 = s11.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg11.fill.solid()
    bg11.fill.fore_color.rgb = BG_DARK
    bg11.line.fill.background()
    add_header(s11, "Complexity Classes & Formal NP-Reductions")

    tf_cp1 = create_card(s11, Inches(0.8), Inches(1.7), Inches(5.7), Inches(5.1), "1. Problem Classification Matrix", "P, NP, NP-Complete, and NP-Hard")
    cp1_pts = [
        "Class P (Polynomial Time): Sorting (MergeSort), Shortest Paths (Dijkstra, Bellman-Ford), Max Flow (Edmonds-Karp), Bipartite Matching.",
        "Class NP-Complete: 0/1 Knapsack Decision, Subset-Sum Risk Escalation, Deception N-Queens, Hamiltonian Cycle.",
        "Class NP-Hard: Travelling Salesperson Optimization (Forensic Collector Routing).",
        "Verification: Solutions to NP problems are verified in polynomial time (e.g., checking if subset risk scores sum to threshold W takes O(n))."
    ]
    for pt in cp1_pts:
        p = tf_cp1.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(10.5)
        p.font.color.rgb = WHITE

    tf_cp2 = create_card(s11, Inches(6.8), Inches(1.7), Inches(5.7), Inches(5.1), "2. Formal Polynomial Reductions", "Proving NP-Completeness")
    cp2_pts = [
        "Reduction 1: SUBSET-SUM <=_p 0/1 KNAPSACK",
        "  - Given S = {s1,...,sn} and target T:",
        "  - Construct Knapsack instance with wi = si, vi = si, capacity W = T, value V = T.",
        "  - Total construction time is O(n) (strictly polynomial).",
        "  - S has a subset summing to T iff Knapsack fits capacity T and achieves value T.",
        "Reduction 2: HAM-CYCLE <=_p TSP",
        "  - Transform G=(V,E) into complete graph G' with edge weight 1 if in E, weight 2 otherwise.",
        "  - Set tour cost bound K = |V|.",
        "  - G has a Hamiltonian cycle iff G' has a TSP tour of weight <= |V|."
    ]
    for pt in cp2_pts:
        p = tf_cp2.add_paragraph()
        p.text = pt
        p.font.size = Pt(10)
        p.font.color.rgb = WHITE
        p.font.name = 'Consolas' if '<=' in pt or 'G=' in pt else 'Segoe UI'

    # =========================================================================
    # SLIDE 12: SCENARIO 1 - NORMAL SOC OPERATION
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    bg12 = s12.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg12.fill.solid()
    bg12.fill.fore_color.rgb = BG_DARK
    bg12.line.fill.background()
    add_header(s12, "Scenario 1: Normal SOC Operation (Baseline Triage)")

    tf_sc1 = create_card(s12, Inches(0.8), Inches(1.7), Inches(11.7), Inches(5.1), "Baseline Telemetry Ingestion, Search, and Dispatch Workflow", "Simulating 1,000 Concurrent System Events")
    sc1_pts = [
        "1. Chronological Event Ingestion: 1,000 security logs sorted via MergeSort (5,044 comparisons) and Randomized QuickSort (11,330 comparisons).",
        "2. Timeline Forensic Query: Binary Search pinpoints target timestamp at Index 500 in exactly 9 comparisons.",
        "3. Signature Matching Showdown: Ingested telemetry payload scanned for 'UNION SELECT' by Naive, Rabin-Karp, FA, and KMP engines.",
        "4. Multi-Stage Kill-Chain Correlation: Longest Common Subsequence (LCS) identifies 4-stage APT progression ('ADGX') embedded within noisy audit logs.",
        "5. Specialist Dispatch: Maximum Bipartite Matching dispatches 8 high-priority incidents to available certified SOC specialists in real time."
    ]
    for pt in sc1_pts:
        p = tf_sc1.add_paragraph()
        p.text = pt
        p.font.size = Pt(12)
        p.font.color.rgb = WHITE

    # =========================================================================
    # SLIDE 13: SCENARIO 2 - CONSTRAINT SHOCK
    # =========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    bg13 = s13.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg13.fill.solid()
    bg13.fill.fore_color.rgb = BG_DARK
    bg13.line.fill.background()
    add_header(s13, "Scenario 2: Active Ransomware Outbreak (60% SLA Crunch)")

    tf_sc2 = create_card(s13, Inches(0.8), Inches(1.7), Inches(11.7), Inches(5.1), "Constraint Shock: Downtime Budget Slashed from 100 min -> 40 min", "Immediate Autonomous Incident Containment")
    sc2_pts = [
        "1. Containment Playbook Optimization: Slashed SLA budget forces trade-off. 0/1 Knapsack DP selects discrete mitigations achieving 230 risk points. Branch & Bound prunes unpromising nodes to find optimal response.",
        "2. Lateral Exploit Pathing: Dijkstra and Bellman-Ford evaluate lateral movement to Internal DB. Bellman-Ford correctly processes negative weights modeling credential theft.",
        "3. Quarantine Infrastructure: Prim and Kruskal MST construct an out-of-band cabling tree (weight = 30) across 8 quarantine switches.",
        "4. Halting Active Exfiltration: Ford-Fulkerson calculates 412 MB/s exfiltration flow and identifies 8 critical Min-Cut firewall links to drop, immediately halting data leakage."
    ]
    for pt in sc2_pts:
        p = tf_sc2.add_paragraph()
        p.text = pt
        p.font.size = Pt(12)
        p.font.color.rgb = WHITE

    # =========================================================================
    # SLIDE 14: SCENARIO 3 - ADVERSARIAL STRESS
    # =========================================================================
    s14 = prs.slides.add_slide(blank_layout)
    bg14 = s14.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg14.fill.solid()
    bg14.fill.fore_color.rgb = BG_DARK
    bg14.line.fill.background()
    add_header(s14, "Scenario 3: Large-Data Stress & Adversarial Attacks")

    tf_sc3 = create_card(s14, Inches(0.8), Inches(1.7), Inches(11.7), Inches(5.1), "Scale Progression (N=100, 2500, 10000) & Pathological Inputs", "Exposing Theoretical Asymptotics in Execution")
    sc3_pts = [
        "1. QuickSort Worst-Case Exposure: On pre-sorted adversarial streams (N=2,000), deterministic QuickSort required 1,999,000 comparisons (33 ms). Stable MergeSort executed in 11,088 comparisons (180x speedup).",
        "2. Pathological String Search Defense: Repetitive attack text ('AAAA...B') triggered 89,919 comparisons in Naive matching, while KMP completed in 20,004 comparisons (4.5x faster).",
        "3. Lateral Reachability Scaling: Classical Theta(N^3) vs Strassen Theta(N^2.807) tested on 16x16 transition matrices, revealing recursive overhead trade-offs.",
        "4. Forensic Collector Routing: 12-host Travelling Salesperson solved via Held-Karp Bitmask DP and Least-Cost B&B, both converging on optimal latency 281."
    ]
    for pt in sc3_pts:
        p = tf_sc3.add_paragraph()
        p.text = pt
        p.font.size = Pt(12)
        p.font.color.rgb = WHITE

    # =========================================================================
    # SLIDE 15: EMPIRICAL BENCHMARKS SUMMARY
    # =========================================================================
    s15 = prs.slides.add_slide(blank_layout)
    bg15 = s15.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg15.fill.solid()
    bg15.fill.fore_color.rgb = BG_DARK
    bg15.line.fill.background()
    add_header(s15, "Empirical Benchmarking & Performance Highlights")

    tf_bm = create_card(s15, Inches(0.8), Inches(1.7), Inches(11.7), Inches(5.1), "Reproducible Empirical Performance Metrics (data/benchmark_results.csv)", "Collected via MetricsTracker Instrumentation Harness")
    bm_table = [
        "Algorithm                      N        Comparisons    Swaps/Writes    Relaxations    Pruned    Time (ms)",
        "---------------------------------------------------------------------------------------------------------",
        "Merge Sort (Logs)             1000            5,044          19,953              0         0       0.0000",
        "Quick Sort (Rand Pivot)       1000           11,330          12,704              0         0       0.0000",
        "Quick Sort Det (Adversarial)  2000        1,999,000       4,001,998              0         0      33.0000",
        "Merge Sort (Adversarial)      2000           11,088          43,905              0         0       1.0000",
        "Naive Match (Adversarial)    10000           89,919               1              0         0       0.0000",
        "KMP Match (Adversarial)      10000           20,004              10              0         0       0.0000",
        "0/1 Knapsack DP                 12              697             509              0         0       0.0000",
        "0/1 Knapsack LC-BB              12              159              57              0         9       0.0000",
        "TSP Held-Karp DP                12           56,342          41,618              0         0       2.0000",
        "TSP Least-Cost BB               12          795,090               1              0    22,474      20.0000"
    ]
    for row in bm_table:
        p = tf_bm.add_paragraph()
        p.text = row
        p.font.size = Pt(9.5)
        p.font.color.rgb = WHITE
        p.font.name = 'Consolas'

    # =========================================================================
    # SLIDE 16: INTERACTIVE SOC STUDIO (WEB GUI)
    # =========================================================================
    s16 = prs.slides.add_slide(blank_layout)
    bg16 = s16.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg16.fill.solid()
    bg16.fill.fore_color.rgb = BG_DARK
    bg16.line.fill.background()
    add_header(s16, "Interactive SOC Algorithmic Studio (Web GUI)")

    tf_gui1 = create_card(s16, Inches(0.8), Inches(1.7), Inches(5.7), Inches(5.1), "1. Independent Algorithmic Playgrounds", "Interactive Sliders, Canvases & Boards")
    gui1_pts = [
        "Dedicated Cards for Every Algorithm: Every syllabus algorithm features its own independent card with inputs, sliders, and telemetry visualizers.",
        "Attack Topology Canvas: Interactive HTML5 canvas rendering enterprise hosts, firewalls, and glowing exploit pathways.",
        "N-Queens Deception Grid: Real-time chessboard visualizer cycling through all 92 non-conflicting sensor placements.",
        "Live String Matcher Showdown: Side-by-side comparison cards for Naive, Rabin-Karp, FA, and KMP."
    ]
    for pt in gui1_pts:
        p = tf_gui1.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(10.5)
        p.font.color.rgb = WHITE

    tf_gui2 = create_card(s16, Inches(6.8), Inches(1.7), Inches(5.7), Inches(5.1), "2. Zero-Dependency Native Architecture", "Standard Python Server & Floating Console")
    gui2_pts = [
        "Pure Standard Library: Zero pip dependencies required (runs instantly via python gui/server.py or ./start_gui.bat).",
        "Floating C17 Subprocess Terminal: Collapsible console drawer executing native compiled C17 binaries and streaming output.",
        "Instant Search & Category Filter: Search any algorithm instantly or filter by syllabus unit pills.",
        "Direct Exporter Links: Download empirical benchmark datasets in CSV and JSON formats with a single click."
    ]
    for pt in gui2_pts:
        p = tf_gui2.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(10.5)
        p.font.color.rgb = WHITE

    # =========================================================================
    # SLIDE 17: SOFTWARE QUALITY & 33/33 TEST SUITE
    # =========================================================================
    s17 = prs.slides.add_slide(blank_layout)
    bg17 = s17.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg17.fill.solid()
    bg17.fill.fore_color.rgb = BG_DARK
    bg17.line.fill.background()
    add_header(s17, "Software Engineering Quality & Test Suite")

    tf_tst = create_card(s17, Inches(0.8), Inches(1.7), Inches(11.7), Inches(5.1), "33 / 33 Unit Tests Passing with 100% Deterministic Coverage", "Automated Oracle Verification Harness (tests/test_all.c)")
    tst_pts = [
        "Unit II (D&C): MergeSort, Binary Search (Iter/Rec), BST Search, QuickSort, Max Subarray, Fast Exp, Celebrity, Matrix Mult (9/9 PASS)",
        "Unit III (Greedy): Activity Selection, Interval Partitioning, Fractional Knapsack, Huffman Coding, Dijkstra, Prim/Kruskal (6/6 PASS)",
        "Unit IV (DP): 0/1 Knapsack DP, Matrix Chain DP, LCS Kill-Chain, Optimal BST, Bellman-Ford, Floyd-Warshall, TSP DP (7/7 PASS)",
        "Unit V (B&B): N-Queens Backtracking, Sum of Subsets, Knapsack Backtrack, FIFO/LIFO/LC B&B, TSP LC-BB (5/5 PASS)",
        "Unit VI (Flow/CRT/Strings): Ford-Fulkerson Max Flow, Min-Cut Severing, Bipartite Matching, CRT, 4 String Matchers (6/6 PASS)",
        "Build Directives: Strict -std=c17 -Wall -Wextra -O2 compilation with zero warnings or memory leaks."
    ]
    for pt in tst_pts:
        p = tf_tst.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(11)
        p.font.color.rgb = WHITE

    # =========================================================================
    # SLIDE 18: CONCLUSION & VIVA DEFENSE CHECKLIST
    # =========================================================================
    s18 = prs.slides.add_slide(blank_layout)
    bg18 = s18.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg18.fill.solid()
    bg18.fill.fore_color.rgb = BG_DARK
    bg18.line.fill.background()
    add_header(s18, "Final Submission & Viva Defense Checklist")

    tf_chk1 = create_card(s18, Inches(0.8), Inches(1.7), Inches(5.7), Inches(5.1), "1. Complete PBL Rubric Compliance", "Verified Across All 7 Evaluation Dimensions")
    chk1_pts = [
        "Problem Modelling (10%): Correct typed entities, attack graphs, and SLA constraints.",
        "Algorithm Coverage (30%): Complete syllabus workbench implemented from scratch in pure C17.",
        "Comparative Analysis (15%): Recurrences, empirical CSV/JSON benchmarks, and paradigm comparisons.",
        "Software Quality (15%): Modularity, C17 standard, CMake/Make build, and 33/33 test suite.",
        "Product Integration (15%): Realistic scenarios, CLI console, and interactive Web Studio.",
        "Complexity & Ethics (10%): Formal NP reductions, P/NP matrix, PII scrubbing, and safety boundaries."
    ]
    for pt in chk1_pts:
        p = tf_chk1.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(10.5)
        p.font.color.rgb = WHITE

    tf_chk2 = create_card(s18, Inches(6.8), Inches(1.7), Inches(5.7), Inches(5.1), "2. Project Deliverables & Repository", "Ready for Defense Evaluation")
    chk2_pts = [
        "GitHub Repository: SPARSHsrihero1/cseg3053-cyber-threat-engine (Branch: main)",
        "Official Release Tag: v1.0.0 tagged and published on GitHub.",
        "Documentation Dossiers: Comprehensive academic reports in Markdown and Microsoft Word (docs/).",
        "Quick Launch Command:",
        "  cd C:\\Users\\spars\\.gemini\\antigravity\\scratch\\cseg3053-cyber-threat-engine",
        "  .\\start_gui.bat"
    ]
    for pt in chk2_pts:
        p = tf_chk2.add_paragraph()
        p.text = pt
        p.font.size = Pt(10.5)
        p.font.color.rgb = WHITE
        p.font.name = 'Consolas' if 'cd ' in pt or '.\\' in pt else 'Segoe UI'

    prs.save(PPTX_PATH)
    print(f"[+] PowerPoint presentation saved to: {PPTX_PATH}")

def build_markdown_slides():
    print("[*] Generating Markdown Slide Deck: presentation/slides.md ...")
    content = """# CSEG3053: Cybersecurity Threat Detection Engine
## High-Throughput Algorithmic Workbench in Pure C17
### Project 03 — Design and Analysis of Algorithms (PBL Capstone)

---

## Slide 1: Title & Overview
* **Project Title:** Project 03 — Cybersecurity Log Threat Detection Engine
* **Course:** CSEG3053 Design and Analysis of Algorithms (DAA)
* **Standard:** Strictly Pure C17 (`-std=c17 -Wall -Wextra -O2`), ISO/IEC 9899:2018
* **GitHub Repository:** [SPARSHsrihero1/cseg3053-cyber-threat-engine](https://github.com/SPARSHsrihero1/cseg3053-cyber-threat-engine)
* **Official Release:** `v1.0.0`
* **Test Suite:** 33 / 33 Unit Tests Passing (100% Pass Rate)

---

## Slide 2: The Cybersecurity Operations Crisis
* **Telemetry Avalanche:** Enterprise firewalls, EDR agents, and servers generate 50,000+ logs/second.
* **Algorithmic DoS Vulnerability:** Adversaries send pre-sorted or repetitive traffic to force quadratic $O(N^2)$ stalls.
* **SLA Downtime Crunch:** In active ransomware attacks, allowable containment downtime is severely constrained.
* **Pure C17 Solution:** Zero black-box library shortcuts (`qsort`, `bsearch`, `strstr` replaced with custom implementations).

---

## Slide 3: Decoupled Multi-Layer Architecture
1. **Display & Interaction:** CLI Console (`src/main.c`) & Web Algorithmic Studio (`gui/index.html`).
2. **Core Domain & Telemetry:** Typed entities (`include/domain.h`), MetricsTracker (`src/core/metrics.c`), PRNG data generator.
3. **Algorithmic Workbench:** Modular C implementations covering Units II to VI.
4. **Verification & Persistence:** 33/33 Assertion Unit Tests, RFC CSV/JSON benchmark exporters.

---

## Slide 4: Complete Syllabus Mapping
* **Unit II (Divide & Conquer):** Merge/Quick Sort, Binary Search, BST, Max Subarray, Fast Exp, Celebrity C2, Strassen MatMul.
* **Unit III (Greedy Methods):** Activity Selection, Interval Partitioning, Fractional Knapsack, Huffman Coding, Dijkstra, Prim/Kruskal MST.
* **Unit IV (Dynamic Programming):** 0/1 Knapsack DP, Matrix Chain Order, LCS Kill-Chain, Optimal BST, Bellman-Ford, Floyd-Warshall, TSP DP.
* **Unit V (Backtracking & B&B):** N-Queens Honeypot Grid, Sum of Subsets, Knapsack B&B (FIFO/LIFO/LC), TSP LC-BB.
* **Unit VI (Flow, CRT & Strings):** Ford-Fulkerson Max Flow, Min-Cut Link Severing, Bipartite Matching, CRT, 4 String Matchers (KMP).

---

## Slide 5: Unit II — Divide and Conquer
* **MergeSort vs QuickSort:** Stable $O(N \log N)$ sorting vs in-place partitioning; randomized pivot defeats adversarial pre-sorted streams.
* **Forensic Pinpointing:** Binary Search locates target event timestamps in 9 comparisons on 1,000 logs.
* **DDoS Window Isolation:** Maximum Subarray (Kadane $\Theta(n)$ vs D&C $\Theta(n \log n)$) isolates burst start and end times.
* **Celebrity C2 Detection:** Identifies hidden C2 sinkholes in an $N \times N$ matrix in $O(N)$ comparisons.
* **Strassen Matrix Mult:** Sub-cubic $\Theta(N^{2.807})$ multi-hop lateral movement reachability.

---

## Slide 6: Mathematical Recurrence Proofs
* **Merge Sort:** $T(n) = 2T(n/2) + \Theta(n) \implies \Theta(n \log n)$ (Master Theorem Case 2).
* **Strassen MatMul:** $T(N) = 7T(N/2) + \Theta(N^2) \implies \Theta(N^{\log_2 7}) \approx \Theta(N^{2.807})$ (Master Theorem Case 1).
* **Inapplicability of Master Theorem:** Adversarial QuickSort recurrence $T(n) = T(n-1) + cn$. Master Theorem fails because subproblem shrinks by subtraction, not division. Solved via unrolling to $\Theta(n^2)$.

---

## Slide 7: Unit III — Greedy Optimization
* **Activity Selection:** Schedules maximum non-overlapping vulnerability scans sorted by earliest finish time.
* **Interval Partitioning:** Computes minimum parallel malware-detonation sandbox VMs needed.
* **Fractional Knapsack:** Allocates DPI inspection bandwidth by threat-to-volume ratio.
* **Huffman Coding:** Compresses syslog forensic archives by ~50% with 100% lossless recovery.
* **Dijkstra Exploit Path:** Custom binary min-heap calculating single-source least-resistance routes.
* **Prim & Kruskal MST:** Resilient out-of-band quarantine cabling tree (Weight = 30).

---

## Slide 8: Unit IV — Dynamic Programming
* **0/1 Knapsack DP:** Maximizes risk mitigated under SLA downtime budgets; reconstructs playbooks via table backtracking.
* **Matrix Chain Order:** Optimal parenthesization of correlation matrices across Firewall, DNS, IAM, and EDR dimensions.
* **LCS Kill-Chain:** Aligns audit tokens with known APT kill-chains despite camouflage noise.
* **Optimal BST Index:** Frequency-weighted signature lookup minimizing expected search depth.
* **Bellman-Ford:** Shortest attack paths with negative privilege-escalation weights and cycle detection.
* **Held-Karp TSP DP:** Bitmask dynamic programming finding minimum-latency forensic collector tours.

---

## Slide 9: Unit V — Backtracking and Branch & Bound
* **N-Queens Deception Grid:** Deception sensor placement with zero conflicting rows, columns, or diagonal slices (92 solutions on $N=8$).
* **Sum of Subsets:** Dual-bounding backtracking finding micro-alert combinations reaching critical threshold $W$.
* **Branch & Bound Solvers:** Systematic comparison of FIFO (Queue), LIFO (Stack), and Least-Cost (Priority Queue) search policies.
* **TSP Least-Cost B&B:** Admissible lower bounds converge on optimal tour cost (281) while pruning 22,474 subtrees.

---

## Slide 10: Unit VI — Flow, Strings & CRT
* **Ford-Fulkerson Max Flow:** Computes 412 MB/s exfiltration capacity via Edmonds-Karp augmenting paths.
* **Min-Cut Link Severing:** Extracts exact 8 saturated firewall links to sever, halting exfiltration with minimal collateral impact.
* **Bipartite Matching:** Dispatches incidents to qualified SOC analysts in $O(V \cdot E)$.
* **Chinese Remainder Theorem:** Reconstructs global 32-bit packet counters from distributed edge sensors.
* **4 String Matchers:** Naive, Rabin-Karp, Finite Automaton, and KMP. KMP defeats adversarial repetitive attacks (`"AAAA...B"`).

---

## Slide 11: Complexity Classes & NP-Reductions
* **Problem Classification:**
  - Class P: MergeSort, Binary Search, Dijkstra, Edmonds-Karp, Bipartite Matching.
  - Class NP-Complete: 0/1 Knapsack, Subset-Sum, N-Queens.
  - Class NP-Hard: Travelling Salesperson (TSP) Optimization.
* **Reduction 1:** $\text{SUBSET-SUM} \le_p \text{KNAPSACK}$ via $w_i = s_i, v_i = s_i, W = T, V = T$.
* **Reduction 2:** $\text{HAMILTONIAN-CYCLE} \le_p \text{TSP}$ via edge weight 1 (in $E$) vs weight 2 (not in $E$).

---

## Slide 12: Scenario 1 — Normal SOC Operation
* **Triage & Chronology:** 1,000 logs sorted via MergeSort vs Randomized QuickSort.
* **Logarithmic Search:** Binary Search pinpoints target timestamp at Index 500 in 9 comparisons.
* **Payload Inspection:** KMP and FA scan payloads for `"UNION SELECT"`.
* **APT Correlation & Dispatch:** LCS aligns kill-chain tokens; Bipartite Matching dispatches 8 of 12 incidents to certified analysts.

---

## Slide 13: Scenario 2 — Ransomware SLA Shock
* **60% Downtime Crunch:** Allowable downtime budget slashed from 100 min $\to$ 40 min.
* **Containment Optimization:** 0/1 Knapsack DP and Branch & Bound both find optimal response (230 risk points).
* **Negative Privilege Paths:** Bellman-Ford correctly handles negative edge weights.
* **Exfiltration Severing:** Ford-Fulkerson identifies 8 Min-Cut firewall links to sever.

---

## Slide 14: Scenario 3 — Adversarial Stress
* **Adversarial Sorting Attack:** Pre-sorted stream causes deterministic QuickSort to stall with 1,999,000 comparisons (33 ms). MergeSort finishes in 11,088 comparisons (180x speedup).
* **Adversarial Payload Search:** Pathological repetitive text triggers 89,919 comparisons in Naive vs 20,004 in KMP (4.5x faster).
* **Forensic Collector TSP:** Solved on 12 hosts using Held-Karp Bitmask DP vs Least-Cost B&B (both reach optimal cost 281).

---

## Slide 15: Empirical Benchmarks Summary
* **Full Data Export:** Stored in `data/benchmark_results.csv` and `data/benchmark_results.json`.
* **Tracked Metrics:** Comparisons, Memory Writes, Recursive Calls, Relaxations, States Pruned, Execution Time (ms).
* **Cross-Paradigm Verification:** Knapsack and TSP solvers converge on identical optimal values across paradigms.

---

## Slide 16: Interactive SOC Web Algorithmic Studio
* **Dedicated Cards for Every Algorithm:** Independent sliders, parameters, and live telemetry screens.
* **Topology Canvas:** Real-time visualization of enterprise hosts, firewalls, and glowing exploit paths.
* **N-Queens Visualizer:** Dynamic chessboard cycling through all 92 non-conflicting honeypot placements.
* **Zero Dependencies:** Pure Python standard library server (`python gui/server.py`).

---

## Slide 17: Software Quality & Verification
* **Test Suite:** 33 / 33 Unit Tests Passing (100% Pass Rate).
* **Compiler Directives:** `-std=c17 -Wall -Wextra -O2`. Zero warnings or errors.
* **Build Systems:** Tested under GNU Make, CMake 3.16+, and Windows batch/PowerShell scripts.

---

## Slide 18: Conclusion & Viva Checklist
* **100% Syllabus Compliance:** Complete algorithmic workbench fulfilling all CSEG3053 criteria.
* **GitHub Repository:** [SPARSHsrihero1/cseg3053-cyber-threat-engine](https://github.com/SPARSHsrihero1/cseg3053-cyber-threat-engine).
* **Official Release:** `v1.0.0` with full commit history and release tag.
* **Launch Command:**
  ```powershell
  cd C:\\Users\\spars\\.gemini\\antigravity\\scratch\\cseg3053-cyber-threat-engine
  .\\start_gui.bat
  ```
"""
    with open(MD_SLIDES_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[+] Markdown slide deck saved to: {MD_SLIDES_PATH}")

if __name__ == "__main__":
    build_pptx()
    build_markdown_slides()
    print("[+] Presentation deliverables successfully generated in presentation/!")
