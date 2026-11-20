#!/usr/bin/env python3
"""
Generate Extraordinary, Impactful Evaluation Presentation (7 Slides)
Designed strictly according to the "How to Create a Project Presentation" Guide
and the CSEG3053 Project-Based Evaluation Rules (8-Min Demo + 4-Min Viva).

Output:
  - presentation/CSEG3053_8Min_Evaluation_Deck.pptx (16:9 Widescreen)
"""

import os
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRES_DIR = os.path.join(BASE_DIR, "presentation")
PPTX_PATH = os.path.join(PRES_DIR, "CSEG3053_8Min_Evaluation_Deck.pptx")

# Executive Modern SOC Dark Palette
BG_DARK = RGBColor(11, 17, 32)       # Slate 950 #0B1120
CARD_BG = RGBColor(21, 32, 51)      # Dark Navy #152033
CARD_BORDER = RGBColor(34, 52, 80)  # Border #223450
CYAN = RGBColor(0, 240, 255)        # Electric Cyan #00F0FF
MAGENTA = RGBColor(255, 0, 85)      # Neon Magenta #FF0055
AMBER = RGBColor(245, 158, 11)      # Amber #F59E0B
GREEN = RGBColor(16, 185, 129)      # Emerald #10B981
WHITE = RGBColor(255, 255, 255)
MUTED = RGBColor(148, 163, 184)     # Slate 400 #94A3B8
HEADER_BG = RGBColor(15, 23, 42)    # Slate 900 #0F172A

def set_slide_background(slide):
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = BG_DARK
    bg.line.fill.background()
    return bg

def add_header(slide, title, category="CSEG3053 DESIGN AND ANALYSIS OF ALGORITHMS | EVALUATION DECK"):
    cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.35), Inches(11.7), Inches(0.35))
    tf_c = cat_box.text_frame
    tf_c.word_wrap = True
    p_c = tf_c.paragraphs[0]
    p_c.text = category.upper()
    p_c.font.size = Pt(9.5)
    p_c.font.bold = True
    p_c.font.color.rgb = CYAN
    p_c.font.name = 'Consolas'

    t_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.68), Inches(11.7), Inches(0.8))
    tf_t = t_box.text_frame
    tf_t.word_wrap = True
    p_t = tf_t.paragraphs[0]
    p_t.text = title
    p_t.font.size = Pt(21)
    p_t.font.bold = True
    p_t.font.color.rgb = WHITE
    p_t.font.name = 'Segoe UI'

def create_card(slide, left, top, width, height, title, subtitle=None, border_color=CARD_BORDER, bg_color=CARD_BG):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = bg_color
    shape.line.color.rgb = border_color
    shape.line.width = Pt(1.3)

    tb = slide.shapes.add_textbox(left + Inches(0.18), top + Inches(0.12), width - Inches(0.36), height - Inches(0.24))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(12.5)
    p.font.bold = True
    p.font.color.rgb = CYAN
    p.font.name = 'Segoe UI'

    if subtitle:
        p2 = tf.add_paragraph()
        p2.text = subtitle
        p2.font.size = Pt(9)
        p2.font.color.rgb = MUTED
        p2.font.name = 'Consolas'

    return tf

def create_kpi_badge(slide, left, top, width, height, title, value, border_color=CYAN):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = CARD_BG
    shape.line.color.rgb = border_color
    shape.line.width = Pt(1.5)

    tb = slide.shapes.add_textbox(left + Inches(0.1), top + Inches(0.08), width - Inches(0.2), height - Inches(0.16))
    tf = tb.text_frame
    tf.word_wrap = True

    p1 = tf.paragraphs[0]
    p1.text = title.upper()
    p1.font.size = Pt(8.5)
    p1.font.bold = True
    p1.font.color.rgb = border_color
    p1.font.name = 'Consolas'

    p2 = tf.add_paragraph()
    p2.text = value
    p2.font.size = Pt(12)
    p2.font.bold = True
    p2.font.color.rgb = WHITE
    p2.font.name = 'Segoe UI'

def build_presentation():
    print("[*] Generating Impactful 7-Slide Presentation: presentation/CSEG3053_8Min_Evaluation_Deck.pptx ...")
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # =========================================================================
    # SLIDE 1: HERO / VISION & PROBLEM FORMULATION (1 MIN)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1)

    t_box = s1.shapes.add_textbox(Inches(0.8), Inches(0.8), Inches(11.7), Inches(2.2))
    tf1 = t_box.text_frame
    tf1.word_wrap = True

    p0 = tf1.paragraphs[0]
    p0.text = "CSEG3053: DESIGN AND ANALYSIS OF ALGORITHMS — PROJECT 03"
    p0.font.size = Pt(11.5)
    p0.font.bold = True
    p0.font.color.rgb = CYAN
    p0.font.name = 'Consolas'

    p1 = tf1.add_paragraph()
    p1.text = "Cybersecurity Log Threat Detection Engine"
    p1.font.size = Pt(32)
    p1.font.bold = True
    p1.font.color.rgb = WHITE
    p1.font.name = 'Segoe UI'

    p2 = tf1.add_paragraph()
    p2.text = "A High-Throughput Algorithmic Workbench & SOC Analytics Engine in Pure C17"
    p2.font.size = Pt(14)
    p2.font.color.rgb = MUTED
    p2.font.name = 'Segoe UI'

    # 4 High-Impact KPI Badges
    create_kpi_badge(s1, Inches(0.8), Inches(2.75), Inches(2.75), Inches(1.0), "Standard", "Pure C17 (-O2)", CYAN)
    create_kpi_badge(s1, Inches(3.78), Inches(2.75), Inches(2.75), Inches(1.0), "Zero Shortcuts", "No qsort/bsearch", AMBER)
    create_kpi_badge(s1, Inches(6.76), Inches(2.75), Inches(2.75), Inches(1.0), "Verification", "33 / 33 Tests Pass", GREEN)
    create_kpi_badge(s1, Inches(9.74), Inches(2.75), Inches(2.75), Inches(1.0), "Release", "v1.1.0 on GitHub", MAGENTA)

    # 2 Visual Story Cards
    tf_c1 = create_card(s1, Inches(0.8), Inches(3.95), Inches(5.7), Inches(3.1), "The Security Operations Challenge", "Massive Data Velocity & Algorithmic DoS", border_color=MAGENTA)
    pts1 = [
        "Telemetry Avalanche: Ingesting 50,000+ logs/sec across firewalls, EDR, and DNS.",
        "Algorithmic Denial-of-Service: Adversaries intentionally stream pre-sorted logs to trigger O(N^2) worst-case sorting stalls in naive detection systems.",
        "Ransomware SLA Downtime Crunch: Containment actions must be prioritized under strict downtime limits before critical infrastructure fails.",
        "Data Exfiltration Velocity: Identifying exact bottleneck links to sever without disrupting legitimate enterprise traffic."
    ]
    for pt in pts1:
        p = tf_c1.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(9.5)
        p.font.color.rgb = WHITE

    tf_c2 = create_card(s1, Inches(6.8), Inches(3.95), Inches(5.7), Inches(3.1), "The Pure C17 Solution Engine", "Zero Black-Box Abstractions", border_color=CYAN)
    pts2 = [
        "Strict Pure C17 Standard (-std=c17 -Wall -Wextra -O2): Zero C++ dependencies, zero compiler warnings.",
        "Zero Library Shortcuts: All 25+ syllabus algorithms—from divide-and-conquer to flow and DP—engineered entirely from scratch in C.",
        "Empirical Telemetry: MetricsTracker instrumentation capturing atomic comparisons, writes, recursive calls, relaxations, and heap memory.",
        "Live Interactive Studio: Browser-based visualizer for topology maps, honeypot chessboards, and string matchers."
    ]
    for pt in pts2:
        p = tf_c2.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(9.5)
        p.font.color.rgb = WHITE

    # =========================================================================
    # SLIDE 2: ARCHITECTURE & DATA STRUCTURES (1 MIN)
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2)
    add_header(s2, "System Architecture & Typed Domain Models")

    tf_d1 = create_card(s2, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.3), "Typed C17 Domain Entities (include/domain.h)", "Mathematical Problem Representations", border_color=CYAN)
    d_pts = [
        "EventLog: Typed struct with monotonic uint64_t ID, timestamp, IPv4 endpoints, port, severity, and payload string buffer.",
        "HostNode & AttackGraph: Directed weighted graphs where edge weights model lateral movement exploit resistance or privilege escalation benefits.",
        "FlowNetwork: Capacitated residual flow network (capacity[][] & flow[][]) for data exfiltration containment.",
        "ContainmentPlaybook: Automated response tasks with downtime disruption cost (weight) and mitigated risk score (value).",
        "MetricsTracker: Telemetry harness tracking atomic comparisons, writes, recursive depth, and heap memory in real time."
    ]
    for pt in d_pts:
        p = tf_d1.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(10)
        p.font.color.rgb = WHITE

    tf_d2 = create_card(s2, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.3), "Decoupled Multi-Layer Data Flow", "Clean Separation of Concerns", border_color=AMBER)
    f_pts = [
        "Layer 1: Ingestion & Data Generation: Deterministic PRNG generator creating normal, burst, and adversarial log streams.",
        "Layer 2: Algorithmic Workbench: Modular C libraries for Units II to VI (D&C, Greedy, DP, Backtracking, B&B, Flow, Strings).",
        "Layer 3: Verification Harness: 33 assertion unit tests in tests/test_all.c; small-instance oracles for mathematical correctness.",
        "Layer 4: Persistence & Export: RFC-compliant CSV and JSON exporters generating benchmark_results.csv.",
        "Layer 5: Dual Interface: Headless CLI (main.c) and interactive browser-based Algorithmic Studio (gui/index.html)."
    ]
    for pt in f_pts:
        p = tf_d2.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(10)
        p.font.color.rgb = WHITE

    # =========================================================================
    # SLIDE 3: ALGORITHM SELECTION ACROSS 5 PARADIGMS (1.5 MIN)
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3)
    add_header(s3, "Algorithm Selection: 5 Paradigms Mapped to Security")

    p_cards = [
        ("Divide & Conquer (Unit II)", "• MergeSort: Stable Theta(N log N) timeline triage.\n• QuickSort: Randomized pivot defeats DoS floods.\n• Binary Search: O(log N) forensic event pinpointing.\n• Kadane & D&C: Isolates exact DDoS surge window.\n• Celebrity: Identifies C2 sinkhole in O(N).", CYAN),
        ("Greedy Methods (Unit III)", "• Activity Selection: Max non-overlapping scan schedule.\n• Interval Partitioning: Min malware sandbox VMs.\n• Fractional Knapsack: DPI bandwidth allocation.\n• Huffman Coding: Cuts syslog storage by ~50%.\n• Dijkstra & Prim/Kruskal: Shortest exploit & MST.", AMBER),
        ("Dynamic Programming (Unit IV)", "• 0/1 Knapsack DP: Playbooks under SLA crunch.\n• LCS Alignment: APT kill-chain sequence discovery.\n• Matrix Chain Order: Optimal telemetry join parenthesization.\n• Bellman-Ford: Exploit paths with negative root privileges.\n• Held-Karp TSP DP: Min-latency forensic patrol.", GREEN),
        ("B&B, Flow & Strings (Unit V-VI)", "• N-Queens: Deception honeypot routing slices (92 sol).\n• Knapsack B&B: Least-Cost priority queue bounding.\n• Ford-Fulkerson: Halts exfiltration via Min-Cut edges.\n• Bipartite Matching: Dispatches incidents to analysts.\n• 4 String Matchers: KMP linear search defeats attacks.", MAGENTA)
    ]
    for idx, (t, desc, col) in enumerate(p_cards):
        x = Inches(0.8 + (idx % 2) * 5.95)
        y = Inches(1.6 + (idx // 2) * 2.7)
        tf_p = create_card(s3, x, y, Inches(5.75), Inches(2.5), t, border_color=col)
        for line in desc.split("\n"):
            p = tf_p.add_paragraph()
            p.text = line
            p.font.size = Pt(9.5)
            p.font.color.rgb = WHITE

    # =========================================================================
    # SLIDE 4: COMPARATIVE ANALYSIS (HIGH-IMPACT TABLE) (1.5 MIN)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4)
    add_header(s4, "Comparative Algorithmic Analysis: Theory vs. Empirical Reality")

    # Table Shape
    rows, cols = 10, 7
    table_shape = s4.shapes.add_table(rows, cols, Inches(0.8), Inches(1.6), Inches(11.73), Inches(5.3))
    t = table_shape.table

    col_widths = [Inches(2.5), Inches(1.7), Inches(0.9), Inches(1.3), Inches(1.3), Inches(1.1), Inches(2.93)]
    for i, w in enumerate(col_widths):
        t.columns[i].width = w

    headers = ["Algorithm", "Paradigm", "N", "Comparisons", "Swaps/Writes", "Time (ms)", "Empirical Discovery / Defense"]
    for c_idx, h in enumerate(headers):
        cell = t.cell(0, c_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = HEADER_BG
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.size = Pt(9)
        p.font.bold = True
        p.font.color.rgb = CYAN
        p.font.name = 'Consolas'

    bench_data = [
        ("Merge Sort (Logs)", "Divide & Conquer", "1,000", "5,044", "19,953", "0.00 ms", "Guaranteed stable chronological triage"),
        ("Quick Sort (Rand Pivot)", "Divide & Conquer", "1,000", "11,330", "12,704", "1.00 ms", "Random pivot defeats crafted worst cases"),
        ("QuickSort Det (Adversarial)", "Adversarial O(N^2)", "2,000", "1,999,000", "4,001,998", "35.00 ms", "CRITICAL STALL: Naive last pivot fails"),
        ("MergeSort (Adversarial)", "Stable O(N log N)", "2,000", "11,088", "43,905", "1.00 ms", "180x SPEEDUP: Maintains O(N log N) bound"),
        ("Naive String Match", "String Matching", "10,000", "89,919", "1", "0.00 ms", "Quadratic penalty on repetitive text"),
        ("KMP Matcher (Adversarial)", "String Matching", "10,000", "20,004", "10", "0.00 ms", "4.5x SPEEDUP: Linear Theta(N) guarantee"),
        ("0/1 Knapsack DP", "Dynamic Prog.", "12", "697", "509", "0.00 ms", "Optimal 230 risk score under 40 min SLA"),
        ("0/1 Knapsack LC-BB", "Branch & Bound", "12", "159", "57", "0.00 ms", "Tightest exploration: Only 9 nodes pruned"),
        ("TSP Held-Karp / LC-BB", "DP / B&B", "12", "56,342", "41,618", "2.00 ms", "Both converge on exact optimal cost 281")
    ]

    for r_idx, row in enumerate(bench_data):
        for c_idx, val in enumerate(row):
            cell = t.cell(r_idx + 1, c_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = CARD_BG if r_idx % 2 == 0 else RGBColor(16, 25, 41)
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.size = Pt(8.5)
            p.font.name = 'Consolas' if c_idx in [2,3,4,5] else 'Segoe UI'
            if "SPEEDUP" in val or "Optimal" in val:
                p.font.color.rgb = GREEN
                p.font.bold = True
            elif "CRITICAL" in val:
                p.font.color.rgb = MAGENTA
                p.font.bold = True
            else:
                p.font.color.rgb = WHITE

    # =========================================================================
    # SLIDE 5: RECURRENCES & NP-REDUCTIONS (1 MIN)
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5)
    add_header(s5, "Mathematical Recurrence Derivations & NP-Reductions")

    tf_r1 = create_card(s5, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.3), "Recurrences & Master Theorem", "Rigorous Mathematical Proofs", border_color=CYAN)
    r_pts = [
        "MergeSort Recurrence: T(n) = 2T(n/2) + Theta(n)",
        "  - a=2, b=2, f(n)=cn -> n^(log_2 2) = n^1 = n",
        "  - Master Theorem Case 2 applies: T(n) = Theta(n log n).",
        "Strassen Matrix Recurrence: T(N) = 7T(N/2) + Theta(N^2)",
        "  - a=7, b=2 -> Critical exponent N^(log_2 7) approx N^2.807",
        "  - Since f(N) = N^2 = O(N^(2.807 - eps)), Master Theorem Case 1 applies:",
        "  - Result: T(N) = Theta(N^2.807).",
        "Why Master Theorem Fails on QuickSort Worst-Case:",
        "  - Recurrence: T(n) = T(n-1) + cn (Subtractive subproblem division).",
        "  - Master Theorem strictly requires multiplicative division (n/b with b > 1).",
        "  - Unrolling proof: T(n) = T(0) + c * sum(i=1..n) i = Theta(n^2)."
    ]
    for pt in r_pts:
        p = tf_r1.add_paragraph()
        p.text = pt
        p.font.size = Pt(9.5)
        p.font.color.rgb = WHITE
        p.font.name = 'Consolas' if 'T(' in pt or 'a=' in pt else 'Segoe UI'

    tf_r2 = create_card(s5, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.3), "Complexity Classes & Formal Reductions", "P, NP-Complete & NP-Hard", border_color=MAGENTA)
    red_pts = [
        "Classification Matrix:",
        "  - Class P (Polynomial Time): Sorting, Dijkstra, Bellman-Ford, Edmonds-Karp, Bipartite Matching.",
        "  - Class NP-Complete: 0/1 Knapsack Decision, Subset-Sum, N-Queens.",
        "  - Class NP-Hard: Travelling Salesperson (TSP) Optimization.",
        "Polynomial-Time Reduction: SUBSET-SUM <=_p 0/1 KNAPSACK",
        "  - Given S = {s1,...,sn} and target T:",
        "  - Construct Knapsack instance with wi = si, vi = si, capacity W = T, value V = T.",
        "  - Reduction construction executes in O(n) polynomial time.",
        "  - Subset-Sum has solution iff Knapsack achieves value T under weight T.",
        "Reduction 2: HAM-CYCLE <=_p TSP",
        "  - Map edges in G to weight 1, non-edges to weight 2, tour bound K = |V|."
    ]
    for pt in red_pts:
        p = tf_r2.add_paragraph()
        p.text = pt
        p.font.size = Pt(9.5)
        p.font.color.rgb = WHITE
        p.font.name = 'Consolas' if '<=' in pt or 'G=' in pt else 'Segoe UI'

    # =========================================================================
    # SLIDE 6: THREE OPERATIONAL SCENARIOS (1.5 MIN)
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6)
    add_header(s6, "Demonstration of 3 Minimum Cybersecurity Scenarios")

    sc_cards = [
        ("Scenario 1: Normal SOC Triage", "• Ingests 1,000 logs sorted via MergeSort vs QuickSort.\n• Binary Search locates target timestamp in 9 comparisons.\n• KMP scans payload text for 'UNION SELECT' without backtracking.\n• LCS aligns 4-stage APT kill-chain ('ADGX') hidden in noise.\n• Bipartite Matching dispatches 8 of 12 tickets to certified analysts.", CYAN),
        ("Scenario 2: Ransomware SLA Shock", "• 60% Downtime Budget Crunch: SLA cut from 100 min -> 40 min.\n• Containment Optimization: 0/1 Knapsack DP & B&B achieve optimal 230 risk points under crunch.\n• Negative Edge Exploit Path: Bellman-Ford processes privilege escalation.\n• Halting Exfiltration: Ford-Fulkerson calculates 412 MB/s and severs 8 Min-Cut firewall links.", AMBER),
        ("Scenario 3: Adversarial Stress Defense", "• Pre-Sorted DDoS Attack: Exposes deterministic QuickSort O(N^2) stall (1.99M comps) vs MergeSort (11K comps, 180x speedup).\n• Pathological Payload: Naive takes 89K comps vs KMP 20K comps.\n• Multi-Hop Reachability: Classical O(N^3) vs Strassen sub-cubic tested.\n• Forensic Routing: TSP on 12 hosts converges on cost 281 in DP & LC-BB.", MAGENTA)
    ]
    for idx, (t, desc, col) in enumerate(sc_cards):
        x = Inches(0.8 + idx * 3.95)
        tf_sc = create_card(s6, x, Inches(1.6), Inches(3.8), Inches(5.3), t, border_color=col)
        for line in desc.split("\n"):
            p = tf_sc.add_paragraph()
            p.text = line
            p.font.size = Pt(9.5)
            p.font.color.rgb = WHITE

    # =========================================================================
    # SLIDE 7: VERIFICATION & VIVA READINESS (0.5 MIN)
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7)
    add_header(s7, "Software Quality, Verification & Viva Defense Readiness")

    tf_v1 = create_card(s7, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.3), "Assertion Oracle Test Suite (tests/test_all.c)", "33 / 33 Passing Unit Tests (100% Deterministic)", border_color=GREEN)
    v_pts = [
        "Unit II (D&C): Merge/Quick, BS (Iter/Rec), BST, Max Subarray, Fast Exp, Celebrity, Strassen (9/9 PASS)",
        "Unit III (Greedy): Activity Selection, Interval Partitioning, Fractional Knapsack, Huffman, Dijkstra, MST (6/6 PASS)",
        "Unit IV (DP): 0/1 Knapsack, Matrix Chain, LCS, OBST, Bellman-Ford, Floyd-Warshall, TSP DP (7/7 PASS)",
        "Unit V (B&B): N-Queens (4-Q & 8-Q), Sum of Subsets, Knapsack B&B, TSP LC-BB (5/5 PASS)",
        "Unit VI (Flow/Strings): Max Flow, Min-Cut, Matching, CRT, 4 String Matchers (6/6 PASS)",
        "Compiler Verification: Strictly clean -std=c17 -Wall -Wextra -O2 compilation with zero warnings."
    ]
    for pt in v_pts:
        p = tf_v1.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(9.5)
        p.font.color.rgb = WHITE

    tf_v2 = create_card(s7, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.3), "Evaluation Deliverables & Demonstration", "Ready for 12-Minute Solo Defense", border_color=CYAN)
    del_pts = [
        "GitHub Repository: SPARSHsrihero1/cseg3053-cyber-threat-engine",
        "Official Release Tag: v1.1.0 live on GitHub.",
        "Interactive Web Studio: Run .\\start_gui.bat -> http://127.0.0.1:8080",
        "Headless Automated Test: .\\bin\\test_all.exe -> 33 / 33 Passed.",
        "Academic Project Report: docs/Final_Project_Report_CSEG3053.docx",
        "Defense Presentation: presentation/CSEG3053_8Min_Evaluation_Deck.pptx",
        "Faculty Core Principle: 'A working project demonstrates what you built; your technical explanation demonstrates what you learned.'"
    ]
    for pt in del_pts:
        p = tf_v2.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(9.5)
        p.font.color.rgb = WHITE

    prs.save(PPTX_PATH)
    print(f"[+] Impactful 7-Slide Evaluation Deck saved to: {PPTX_PATH}")

if __name__ == "__main__":
    build_presentation()
