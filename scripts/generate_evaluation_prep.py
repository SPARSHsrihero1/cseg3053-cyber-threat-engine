#!/usr/bin/env python3
"""
Generate Concise 7-Slide Evaluation Presentation & 8-Minute Demo Script
Strictly tailored to CSEG3053 Evaluation Guidelines (8-Min Demo + 4-Min Viva).
Outputs:
  - presentation/CSEG3053_8Min_Evaluation_Deck.pptx (7 Slides, 16:9 Widescreen)
  - docs/8Min_Demo_and_Viva_Defense_Script.md (Complete timing script & cheat sheet)
"""

import os
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRES_DIR = os.path.join(BASE_DIR, "presentation")
DOCS_DIR = os.path.join(BASE_DIR, "docs")
CONCISE_PPTX = os.path.join(PRES_DIR, "CSEG3053_8Min_Evaluation_Deck.pptx")
SCRIPT_MD = os.path.join(DOCS_DIR, "8Min_Demo_and_Viva_Defense_Script.md")

# Modern SOC Dark Palette
BG_DARK = RGBColor(11, 17, 32)       # #0B1120
CARD_BG = RGBColor(21, 32, 51)      # #152033
CARD_BORDER = RGBColor(34, 52, 80)  # #223450
CYAN = RGBColor(0, 240, 255)        # #00F0FF
MAGENTA = RGBColor(255, 0, 85)      # #FF0055
AMBER = RGBColor(245, 158, 11)      # #F59E0B
GREEN = RGBColor(16, 185, 129)      # #10B981
WHITE = RGBColor(255, 255, 255)
MUTED = RGBColor(148, 163, 184)     # #94A3B8

def add_header(slide, title, category="CSEG3053 DAA EVALUATION (8-MIN DEMO + 4-MIN VIVA)"):
    cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.5), Inches(0.35))
    tf_c = cat_box.text_frame
    p_c = tf_c.paragraphs[0]
    p_c.text = category.upper()
    p_c.font.size = Pt(10)
    p_c.font.bold = True
    p_c.font.color.rgb = CYAN
    p_c.font.name = 'Consolas'

    t_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(11.7), Inches(0.8))
    tf_t = t_box.text_frame
    p_t = tf_t.paragraphs[0]
    p_t.text = title
    p_t.font.size = Pt(21)
    p_t.font.bold = True
    p_t.font.color.rgb = WHITE
    p_t.font.name = 'Segoe UI'

def create_card(slide, left, top, width, height, title, subtitle=None, border_color=CARD_BORDER):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = CARD_BG
    shape.line.color.rgb = border_color
    shape.line.width = Pt(1.2)

    tb = slide.shapes.add_textbox(left + Inches(0.15), top + Inches(0.12), width - Inches(0.3), height - Inches(0.24))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(12)
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

def generate_concise_deck():
    print("[*] Generating 7-Slide Evaluation Deck: presentation/CSEG3053_8Min_Evaluation_Deck.pptx ...")
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # -------------------------------------------------------------------------
    # SLIDE 1: TITLE & PROBLEM FORMULATION (1 MIN)
    # -------------------------------------------------------------------------
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = BG_DARK
    bg1.line.fill.background()

    t_box = s1.shapes.add_textbox(Inches(0.8), Inches(1.1), Inches(11.7), Inches(2.2))
    tf1 = t_box.text_frame
    tf1.word_wrap = True
    p0 = tf1.paragraphs[0]
    p0.text = "CSEG3053: DESIGN AND ANALYSIS OF ALGORITHMS — PROJECT 03"
    p0.font.size = Pt(12)
    p0.font.bold = True
    p0.font.color.rgb = CYAN
    p0.font.name = 'Consolas'

    p1 = tf1.add_paragraph()
    p1.text = "Cybersecurity Log Threat Detection Engine"
    p1.font.size = Pt(32)
    p1.font.bold = True
    p1.font.color.rgb = WHITE

    p2 = tf1.add_paragraph()
    p2.text = "High-Throughput Algorithmic Workbench & SOC Analytics Engine in Pure C17"
    p2.font.size = Pt(15)
    p2.font.color.rgb = MUTED

    tf_c1 = create_card(s1, Inches(0.8), Inches(3.6), Inches(5.7), Inches(3.3), "Core Cybersecurity Problems", "Operational Motivations")
    pts1 = [
        "Telemetry Explosion: Ingesting 50,000+ logs/sec with zero buffer bloat.",
        "Algorithmic Denial-of-Service: Adversaries intentionally send pre-sorted streams to trigger O(N^2) sorting crashes in naive engines.",
        "Ransomware SLA Crunch: Minimizing business downtime while maximizing risk reduction under active attacks.",
        "Data Exfiltration: Isolating the exact bottleneck firewall links to sever without disrupting legitimate enterprise traffic."
    ]
    for pt in pts1:
        p = tf_c1.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(9.5)
        p.font.color.rgb = WHITE

    tf_c2 = create_card(s1, Inches(6.8), Inches(3.6), Inches(5.7), Inches(3.3), "Engineering Standards & Constraints", "Pure C17 Standard, Zero Shortcuts")
    pts2 = [
        "Strict Pure C17 (-std=c17 -Wall -Wextra -O2): Zero C++ features, zero compiler warnings.",
        "Zero Library Shortcuts: No qsort, bsearch, or strstr. All 25+ syllabus algorithms built entirely from scratch in C.",
        "Full Asymptotic Profiling: Operation counters for comparisons, writes, recursive calls, relaxations, and heap memory.",
        "100% Verification: 33 / 33 assertion unit test oracles passing; live Web GUI Studio."
    ]
    for pt in pts2:
        p = tf_c2.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(9.5)
        p.font.color.rgb = WHITE

    # -------------------------------------------------------------------------
    # SLIDE 2: DOMAIN MODEL & ARCHITECTURE (1 MIN)
    # -------------------------------------------------------------------------
    s2 = prs.slides.add_slide(blank_layout)
    bg2 = s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg2.fill.solid()
    bg2.fill.fore_color.rgb = BG_DARK
    bg2.line.fill.background()
    add_header(s2, "System Architecture & Typed Domain Models")

    tf_d1 = create_card(s2, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.2), "Typed C17 Domain Entities (include/domain.h)", "Mathematical Problem Representations")
    d_pts = [
        "EventLog: Typed struct with monotonic uint64_t ID, timestamp, source/dest IPv4, port, severity, and payload text.",
        "HostNode & AttackGraph: Directed weighted graphs where edge weights represent lateral movement exploit resistance or privilege escalation benefits.",
        "FlowNetwork: Capacitated residual flow network (capacity[][] & flow[][]) for data exfiltration containment.",
        "ContainmentPlaybook: Automated response tasks with downtime disruption cost (weight) and mitigated risk score (value).",
        "MetricsTracker: Telemetry harness tracking atomic comparisons, writes, recursive depth, and heap bytes."
    ]
    for pt in d_pts:
        p = tf_d1.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(10)
        p.font.color.rgb = WHITE

    tf_d2 = create_card(s2, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2), "Decoupled Architecture & Data Flow", "Clean Separation of Concerns")
    f_pts = [
        "1. Ingestion Layer: Deterministic PRNG generator creating normal, burst, and adversarial log datasets.",
        "2. Algorithmic Workbench: Modular C libraries for Units II to VI (D&C, Greedy, DP, Backtracking, B&B, Flow, Strings).",
        "3. Verification Harness: 33 assertion tests in tests/test_all.c; small-instance oracles for mathematical correctness.",
        "4. Persistence & Export: RFC-compliant CSV and JSON exporters generating benchmark_results.csv.",
        "5. Dual Interface: Headless CLI (main.c) and interactive browser-based Algorithmic Studio (gui/index.html)."
    ]
    for pt in f_pts:
        p = tf_d2.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(10)
        p.font.color.rgb = WHITE

    # -------------------------------------------------------------------------
    # SLIDE 3: ALGORITHM SELECTION & PARADIGMS (1.5 MIN)
    # -------------------------------------------------------------------------
    s3 = prs.slides.add_slide(blank_layout)
    bg3 = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg3.fill.solid()
    bg3.fill.fore_color.rgb = BG_DARK
    bg3.line.fill.background()
    add_header(s3, "Algorithm Selection: 5 Paradigms Mapped to Security")

    p_cards = [
        ("Divide & Conquer (Unit II)", "• MergeSort: Stable Theta(N log N) timeline triage.\n• QuickSort: Randomized pivot defeats DoS floods.\n• Binary Search: O(log N) forensic event pinpointing.\n• Kadane & D&C: Isolates exact DDoS surge window.\n• Celebrity: Identifies C2 sinkhole in O(N).", CYAN),
        ("Greedy Methods (Unit III)", "• Activity Selection: Max non-overlapping scan schedule.\n• Interval Partitioning: Min malware sandbox VMs.\n• Fractional Knapsack: DPI bandwidth allocation.\n• Huffman Coding: Cuts syslog storage by ~50%.\n• Dijkstra & Prim/Kruskal: Shortest exploit & MST.", AMBER),
        ("Dynamic Programming (Unit IV)", "• 0/1 Knapsack DP: Playbooks under SLA crunch.\n• LCS Alignment: APT kill-chain sequence discovery.\n• Matrix Chain Order: Optimal telemetry join parenthesization.\n• Bellman-Ford: Exploit paths with negative root privileges.\n• Held-Karp TSP DP: Min-latency forensic patrol.", GREEN),
        ("B&B, Flow & Strings (Unit V-VI)", "• N-Queens: Deception honeypot routing slices (92 sol).\n• Knapsack B&B: Least-Cost priority queue bounding.\n• Ford-Fulkerson: Halts exfiltration via Min-Cut edges.\n• Bipartite Matching: Dispatches incidents to analysts.\n• 4 String Matchers: KMP linear search defeats attacks.", MAGENTA)
    ]
    for idx, (t, desc, col) in enumerate(p_cards):
        x = Inches(0.8 + (idx % 2) * 5.95)
        y = Inches(1.6 + (idx // 2) * 2.65)
        tf_p = create_card(s3, x, y, Inches(5.75), Inches(2.45), t, border_color=col)
        for line in desc.split("\n"):
            p = tf_p.add_paragraph()
            p.text = line
            p.font.size = Pt(9.5)
            p.font.color.rgb = WHITE

    # -------------------------------------------------------------------------
    # SLIDE 4: COMPARATIVE ANALYSIS & ASYMPTOTICS (1.5 MIN)
    # -------------------------------------------------------------------------
    s4 = prs.slides.add_slide(blank_layout)
    bg4 = s4.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg4.fill.solid()
    bg4.fill.fore_color.rgb = BG_DARK
    bg4.line.fill.background()
    add_header(s4, "Comparative Algorithmic Analysis: Theory vs. Empirical Reality")

    tf_tbl = create_card(s4, Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.2), "Empirical Benchmark Showdown (data/benchmark_results.csv)", "Proving Asymptotic Behavior on Small, Large, and Adversarial Datasets")
    table_lines = [
        "Algorithm                      Paradigm              N    Comparisons    Swaps/Writes    Relaxations   Pruned   Time (ms)",
        "-----------------------------------------------------------------------------------------------------------------------------",
        "Merge Sort (Logs)             Divide & Conquer    1000          5,044          19,953              0        0     0.0000",
        "Quick Sort (Rand Pivot)       Divide & Conquer    1000         11,330          12,704              0        0     0.0000",
        "Quick Sort Det (Adversarial)  Adversarial O(N^2)  2000      1,999,000       4,001,998              0        0    33.0000  <-- O(N^2) Stalls",
        "Merge Sort (Adversarial)      Stable O(N log N)   2000         11,088          43,905              0        0     1.0000  <-- 180x Speedup!",
        "Naive Match (Adversarial)     String Matching    10000         89,919               1              0        0     0.0000",
        "KMP Matcher (Adversarial)     String Matching    10000         20,004              10              0        0     0.0000  <-- 4.5x Speedup!",
        "0/1 Knapsack DP               Dynamic Prog.         12            697             509              0        0     0.0000  <-- Optimal (230)",
        "0/1 Knapsack LC-BB            Branch & Bound        12            159              57              0        9     0.0000  <-- Fewest Nodes",
        "TSP Held-Karp DP              Dynamic Prog.         12         56,342          41,618              0        0     2.0000  <-- Optimal (281)",
        "TSP Least-Cost BB             Branch & Bound        12        795,090               1              0   22,474    20.0000  <-- Admissible Bound"
    ]
    for row in table_lines:
        p = tf_tbl.add_paragraph()
        p.text = row
        p.font.size = Pt(8.5)
        p.font.color.rgb = WHITE
        p.font.name = 'Consolas'

    # -------------------------------------------------------------------------
    # SLIDE 5: RECURRENCES & NP-REDUCTIONS (1 MIN)
    # -------------------------------------------------------------------------
    s5 = prs.slides.add_slide(blank_layout)
    bg5 = s5.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg5.fill.solid()
    bg5.fill.fore_color.rgb = BG_DARK
    bg5.line.fill.background()
    add_header(s5, "Mathematical Recurrence Derivations & NP-Reductions")

    tf_r1 = create_card(s5, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.2), "Recurrences & Master Theorem", "Mathematical Proofs")
    r_pts = [
        "MergeSort Recurrence: T(n) = 2T(n/2) + Theta(n)",
        "  - a=2, b=2, f(n)=cn -> n^(log_2 2) = n",
        "  - Master Theorem Case 2 applies: T(n) = Theta(n log n).",
        "Strassen Matrix Recurrence: T(N) = 7T(N/2) + Theta(N^2)",
        "  - a=7, b=2 -> N^(log_2 7) approx N^2.807",
        "  - Master Theorem Case 1 applies: T(N) = Theta(N^2.807).",
        "Why Master Theorem Fails on QuickSort Worst-Case:",
        "  - T(n) = T(n-1) + cn (Subtractive subproblem, not dividing).",
        "  - Unrolling proof: T(n) = T(0) + c * sum(i=1..n) i = Theta(n^2)."
    ]
    for pt in r_pts:
        p = tf_r1.add_paragraph()
        p.text = pt
        p.font.size = Pt(9.5)
        p.font.color.rgb = WHITE
        p.font.name = 'Consolas' if 'T(' in pt else 'Segoe UI'

    tf_r2 = create_card(s5, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2), "Complexity Classes & Reductions", "P, NP-Complete & NP-Hard")
    red_pts = [
        "Classification:",
        "  - Class P: Sorting, Dijkstra, Bellman-Ford, Edmonds-Karp, Matching.",
        "  - Class NP-Complete: 0/1 Knapsack, Subset-Sum, N-Queens.",
        "  - Class NP-Hard: Travelling Salesperson (TSP) Optimization.",
        "Polynomial-Time Reduction: SUBSET-SUM <=_p 0/1 KNAPSACK",
        "  - Given S = {s1,...,sn} and target T:",
        "  - Construct Knapsack with wi = si, vi = si, capacity W = T, value V = T.",
        "  - Reduction runs in O(n) polynomial time.",
        "  - Subset-Sum has solution iff Knapsack achieves value T under weight T."
    ]
    for pt in red_pts:
        p = tf_r2.add_paragraph()
        p.text = pt
        p.font.size = Pt(9.5)
        p.font.color.rgb = WHITE
        p.font.name = 'Consolas' if '<=' in pt else 'Segoe UI'

    # -------------------------------------------------------------------------
    # SLIDE 6: THREE OPERATIONAL SCENARIOS (1.5 MIN)
    # -------------------------------------------------------------------------
    s6 = prs.slides.add_slide(blank_layout)
    bg6 = s6.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg6.fill.solid()
    bg6.fill.fore_color.rgb = BG_DARK
    bg6.line.fill.background()
    add_header(s6, "Demonstration of 3 Minimum Cybersecurity Scenarios")

    sc_cards = [
        ("Scenario 1: Normal SOC Triage", "• Ingests 1,000 logs sorted via MergeSort vs QuickSort.\n• Binary Search locates target timestamp in 9 comparisons.\n• KMP scans payload text for 'UNION SELECT' without backtracking.\n• LCS aligns 4-stage APT kill-chain ('ADGX') hidden in noise.\n• Bipartite Matching dispatches 8 of 12 tickets to certified analysts.", CYAN),
        ("Scenario 2: Ransomware SLA Shock", "• 60% Downtime Budget Crunch: SLA cut from 100 min -> 40 min.\n• Containment Optimization: 0/1 Knapsack DP & B&B achieve optimal 230 risk points under crunch.\n• Negative Edge Exploit Path: Bellman-Ford processes privilege escalation.\n• Halting Exfiltration: Ford-Fulkerson calculates 412 MB/s and severs 8 Min-Cut firewall links.", AMBER),
        ("Scenario 3: Adversarial Stress Defense", "• Pre-Sorted DDoS Attack: Exposes deterministic QuickSort O(N^2) stall (1.99M comps) vs MergeSort (11K comps, 180x speedup).\n• Pathological Payload: Naive takes 89K comps vs KMP 20K comps.\n• Multi-Hop Reachability: Classical O(N^3) vs Strassen sub-cubic tested.\n• Forensic Routing: TSP on 12 hosts converges on cost 281 in DP & LC-BB.", MAGENTA)
    ]
    for idx, (t, desc, col) in enumerate(sc_cards):
        x = Inches(0.8 + idx * 3.95)
        tf_sc = create_card(s6, x, Inches(1.6), Inches(3.8), Inches(5.2), t, border_color=col)
        for line in desc.split("\n"):
            p = tf_sc.add_paragraph()
            p.text = line
            p.font.size = Pt(9.5)
            p.font.color.rgb = WHITE

    # -------------------------------------------------------------------------
    # SLIDE 7: VERIFICATION & VIVA READINESS (0.5 MIN)
    # -------------------------------------------------------------------------
    s7 = prs.slides.add_slide(blank_layout)
    bg7 = s7.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg7.fill.solid()
    bg7.fill.fore_color.rgb = BG_DARK
    bg7.line.fill.background()
    add_header(s7, "Software Quality, Verification & Viva Defense Readiness")

    tf_v1 = create_card(s7, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.2), "Assertion Oracle Test Suite (tests/test_all.c)", "33 / 33 Passing Unit Tests (100% Pass Rate)")
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

    tf_v2 = create_card(s7, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2), "Evaluation Deliverables & Demonstration", "Ready for 12-Minute Solo Defense")
    del_pts = [
        "GitHub Repository: SPARSHsrihero1/cseg3053-cyber-threat-engine",
        "Official Release Tag: v1.1.0 live on GitHub.",
        "Interactive Web Studio: Run .\\start_gui.bat -> http://127.0.0.1:8080",
        "Headless Automated Test: .\\build.ps1 test -> 33 / 33 Passed.",
        "Academic Project Report: docs/Final_Project_Report_CSEG3053.docx",
        "Defense Presentation: presentation/CSEG3053_8Min_Evaluation_Deck.pptx",
        "Core Philosophy: 'A working project demonstrates what you built; technical explanation demonstrates what you learned.'"
    ]
    for pt in del_pts:
        p = tf_v2.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(9.5)
        p.font.color.rgb = WHITE

    prs.save(CONCISE_PPTX)
    print(f"[+] 7-Slide Evaluation Presentation saved to: {CONCISE_PPTX}")

def generate_script_markdown():
    print("[*] Generating 8-Minute Demo Script: docs/8Min_Demo_and_Viva_Defense_Script.md ...")
    content = """# CSEG3053 Project-Based Learning: 8-Minute Demo & 4-Minute Viva Defense Script
## Course Code: CSEG3053_4 | Evaluation Date: Saturday, 21 November 2026
### Project 03: Cybersecurity Log Threat Detection Engine (Pure C17)

---

## 1. EVALUATION FORMAT & TIMING BUDGET (TOTAL 12 MINUTES)

* **Part 1: Project Demonstration (Strictly 8 Minutes)**
  - 0:00 – 1:00 (1 min): Slide 1 — Problem Formulation, Objectives, and Pure C17 Constraints
  - 1:00 – 2:00 (1 min): Slide 2 — Architecture, Domain Models, and Decoupled Layout
  - 2:00 – 3:30 (1.5 min): Slide 3 — Syllabus Algorithm Selection Across 5 Paradigms
  - 3:30 – 5:00 (1.5 min): Slide 4 & Live Terminal — Comparative Analysis & Adversarial Benchmarks
  - 5:00 – 6:30 (1.5 min): Slide 6 & Web Studio — Live Demonstration of 3 Scenarios
  - 6:30 – 7:30 (1 min): Slide 5 — Mathematical Recurrence Proofs & Formal NP-Reduction
  - 7:30 – 8:00 (0.5 min): Slide 7 — Test Suite (33/33 Passed) & Conclusion
* **Part 2: Technical Viva Defense (Strictly 4 Minutes)**
  - Answering examiner questions on complexity, correctness, edge cases, and code walk-throughs.

---

## 2. SECOND-BY-SECOND VERBAL SCRIPT FOR 8-MINUTE DEMONSTRATION

### Minute 0:00 – 1:00 | Introduction & Problem Formulation (Slide 1)
**What to say:**
> "Good morning, respected evaluators. My name is [Your Name], and I am presenting Project 03: the Cybersecurity Log Threat Detection Engine for CSEG3053.
> 
> In modern Security Operations Centers, analysts are overwhelmed by tens of thousands of telemetry logs per second. Adversaries exploit algorithmic weaknesses by flooding SOCs with pathological inputs to induce quadratic $O(N^2)$ denial-of-service stalls. Furthermore, during active ransomware attacks, administrators face strict SLA downtime budgets to contain threats before critical infrastructure fails.
> 
> To solve this, I built a high-throughput threat detection engine strictly under the **C17 standard (`-std=c17 -Wall -Wextra -O2`)**. Adhering to the syllabus implementation standard, there are **strictly zero standard library shortcuts**: no `qsort`, no `bsearch`, and no `strstr`. All 25+ syllabus algorithms—from divide-and-conquer to network flow and dynamic programming—are engineered completely from scratch in pure C."

---

### Minute 1:00 – 2:00 | System Architecture & Typed Domain Models (Slide 2)
**What to say:**
> "The engine models enterprise security architecture through strictly typed C structures in `include/domain.h`:
> - `EventLog` represents discrete telemetry records with timestamps, IPs, ports, and payload text.
> - `HostNode` and `AttackGraph` model enterprise subnets as directed weighted graphs, where edge weights represent exploit resistance or privilege escalation benefits.
> - `FlowNetwork` manages residual capacities to halt data exfiltration.
> - `ContainmentPlaybook` models automated response actions with disruption costs and mitigated risk scores.
> 
> The system is fully decoupled into five layers: domain models, an operational `MetricsTracker` measuring exact comparisons, memory writes, recursive calls, and heap bytes, modular algorithmic libraries for Units II through VI, an automated 33-test assertion suite, and both a menu-driven CLI and an interactive browser-based Algorithmic Studio."

---

### Minute 2:00 – 3:30 | Algorithm Selection Across 5 Paradigms (Slide 3)
**What to say:**
> "Every algorithm in the engine maps directly to an assessed syllabus unit:
> 1. **Divide and Conquer:** I implemented MergeSort for stable chronological triage, Randomized QuickSort to defeat adversarial log floods, Binary Search for logarithmic timestamp lookups, and Kadane’s algorithm alongside Divide-and-Conquer to isolate the exact start and end timestamps of a volumetric DDoS burst. I also implemented Celebrity detection to isolate hidden C2 sinkholes in $O(N)$ comparisons.
> 2. **Greedy Methods:** Activity Selection schedules non-overlapping vulnerability scans, Interval Partitioning sizes isolated malware-detonation VMs, Fractional Knapsack allocates DPI bandwidth, and Huffman coding compresses syslog archives by ~50% with lossless recovery.
> 3. **Dynamic Programming:** 0/1 Knapsack selects discrete containment playbooks under SLA downtime crunches; Longest Common Subsequence (LCS) aligns audit logs with known APT kill-chains; and Held-Karp bitmask DP computes minimum-latency forensic collector memory dump tours.
> 4. **Backtracking & Branch-and-Bound:** $N$-Queens validates deception honeypot placements across routing slices, and Least-Cost Branch-and-Bound solves the Travelling Salesperson Problem using strictly admissible lower bounds.
> 5. **Network Flow & Strings:** Ford-Fulkerson computes maximum exfiltration capacity and extracts the exact Minimum $s$-$t$ Cut firewall links to sever, while Knuth-Morris-Pratt guarantees linear $\Theta(n)$ payload string inspection."

---

### Minute 3:30 – 5:00 | Comparative Analysis & Adversarial Showdown (Slide 4)
**What to say (Point to Benchmark Table):**
> "A core focus of DAA is understanding when theoretical worst-cases manifest in real execution:
> - **Adversarial Sorting Attack:** On an already-sorted stream of 2,000 logs, deterministic last-element QuickSort suffered worst-case $O(N^2)$ degradation, requiring **1,999,000 comparisons** and taking 33 milliseconds. In contrast, my stable MergeSort completed the same triage in just **11,088 comparisons**—a **180x speedup**!
> - **Pathological Payload Search:** When scanning repetitive malicious padding (`'AAAA...AAAB'`), naive sliding-window string matching performed **89,919 comparisons**, whereas my KMP implementation finished in only **20,004 comparisons**—a **4.5x speedup**—proving its linear $\Theta(n)$ worst-case guarantee.
> - **Knapsack Convergence:** Under a 40-minute SLA budget, 0/1 Knapsack DP, Backtracking, and all three Branch-and-Bound variants converged on the exact same optimal risk value of **230 points**. Least-Cost Branch-and-Bound evaluated the fewest state-space nodes (**9 pruned**), outperforming FIFO and LIFO.
> - **TSP Convergence:** For 12 hosts, Held-Karp Bitmask DP and Least-Cost Branch-and-Bound both arrived at the exact optimal tour cost of **281**."

---

### Minute 5:00 – 6:30 | Live Demonstration of 3 Scenarios (Slide 6 & Live Studio)
**What to do / run:**
Switch to PowerShell or the Web Studio at `http://127.0.0.1:8080` (or execute `.\bin\soc_engine.exe --run-all-demos`).

**What to say:**
> "I have implemented the three required operational scenarios:
> 1. **Scenario 1 (Normal Operations):** 1,000 logs are sorted and indexed; Binary Search pinpoints the target log in 9 comparisons; KMP scans payloads for SQL injection; LCS identifies a 4-stage APT progression; and Maximum Bipartite Matching assigns 8 incident tickets to certified specialists.
> 2. **Scenario 2 (Ransomware SLA Shock):** Management slashes allowable downtime from 100 minutes to 40 minutes. 0/1 Knapsack DP and Branch-and-Bound select optimal playbooks yielding 230 risk points. Bellman-Ford processes negative edge weights representing stolen credentials. Ford-Fulkerson calculates 412 MB/s exfiltration flow and identifies the exact **8 Min-Cut firewall links to sever**, immediately halting data leakage.
> 3. **Scenario 3 (Adversarial Stress):** Progresses scale from $N=100$ to $10,000$ logs, demonstrating that randomized QuickSort and KMP maintain stability under hostile traffic."

---

### Minute 6:30 – 7:30 | Recurrence Proofs & Formal NP-Reduction (Slide 5)
**What to say:**
> "Mathematically, I solved all recursive modules:
> - **MergeSort:** $T(n) = 2T(n/2) + \Theta(n)$. Since $f(n) = \Theta(n^{\log_2 2}) = \Theta(n)$, Master Theorem Case 2 applies, giving $T(n) = \Theta(n \log n)$.
> - **Strassen:** $T(N) = 7T(N/2) + \Theta(N^2)$. Critical exponent is $N^{\log_2 7} \approx N^{2.807}$. Since $f(N) = O(N^{2.807 - \epsilon})$, Master Theorem Case 1 applies, yielding $\Theta(N^{2.807})$.
> - **Why Master Theorem Fails on QuickSort:** The worst-case recurrence is $T(n) = T(n-1) + cn$. The Master Theorem cannot solve subtractive decrements ($n - 1$). Using iterative unrolling, $T(n) = T(0) + c \sum i = \Theta(n^2)$.
> - **Formal NP-Reduction:** I proved that 0/1 Knapsack is NP-Complete by reducing **Subset-Sum to Knapsack** in polynomial time $O(n)$ by setting $w_i = s_i, v_i = s_i, W = T, V = T$."

---

### Minute 7:30 – 8:00 | Test Suite & Conclusion (Slide 7)
**What to run / show:**
Run `.\bin\test_all.exe` in terminal. Show `TEST SUMMARY: 33 / 33 PASSED (100%)`.

**What to say:**
> "Finally, the entire repository is verified using an assertion oracle test suite covering all 6 units. All **33 out of 33 tests pass deterministically**. All code, benchmarks, CSV/JSON datasets, and documentation are committed and tagged under release **`v1.1.0`** on GitHub.
> 
> As stated in the evaluation guidelines: *A working project demonstrates what you built; your technical explanation demonstrates what you learned.* I am now ready for your technical viva questions."

---

## 3. TECHNICAL VIVA CHEAT SHEET (TOP EXAMINER QUESTIONS & WINNING ANSWERS)

### Q1: "Can you show me the code for your Least-Cost Branch-and-Bound lower bound? How do you guarantee it never prunes the optimal tour?"
**Answer:**
> "In `src/unit5_backtracking_bb.c`, the lower bounding function calculates the minimum possible cost to complete a tour. It computes the sum of the minimum outgoing edge from the current vertex plus the minimum outgoing edge from every unvisited vertex to either another unvisited vertex or the origin (Host 0).
> Because every valid Hamiltonian tour must leave each vertex exactly once, and our edge weights are non-negative, this lower bound is strictly **admissible** (it is a true mathematical under-estimate of the remaining cost). Because it never overestimates, it is impossible for the solver to prune a subtree containing the optimal tour. That is why Least-Cost Branch-and-Bound converged on the exact same optimal cost (**281**) as Held-Karp Bitmask DP."

### Q2: "Why can't you use Dijkstra's algorithm when modeling privilege escalation with negative weights?"
**Answer:**
> "Dijkstra is a greedy algorithm based on the premise that once a vertex is extracted from the min-heap, its shortest distance from the source is finalized. However, when negative edges exist—such as when compromising an Active Directory root controller lowers subsequent exploit difficulty—a path passing through that negative edge can produce a lower cumulative cost after a vertex has already been finalized. Dijkstra cannot re-relax already-visited vertices and fails.
> Therefore, in Unit IV I implemented **Bellman-Ford ($\Theta(V \cdot E)$)**, which relaxes all $|E|$ edges $|V|-1$ times and includes a $|V|$-th pass to detect negative-weight cycles (which in cybersecurity represents an infinite privilege escalation loop)."

### Q3: "Explain how your Ford-Fulkerson implementation finds the Minimum s-t Cut."
**Answer:**
> "I implemented the Edmonds-Karp variant using BFS to find augmenting paths in the residual graph until no path with positive residual capacity exists between the compromised store $s$ and external C2 sink $t$.
> At this point, by the **Max-Flow Min-Cut Theorem**, the maximum flow equals the capacity of the minimum cut. To extract the exact cut edges, I run a BFS from $s$ in the residual graph to find all reachable vertices $S$. Any edge in the original network that originates in $S$ and terminates in $V \setminus S$ and whose capacity is fully saturated belongs to the Minimum Cut. In Scenario 2, this isolates the exact 8 firewall rules needed to sever exfiltration."

### Q4: "What is the difference between Kadane's algorithm and Divide-and-Conquer for the Maximum Subarray problem?"
**Answer:**
> "Kadane's algorithm uses dynamic programming with optimal substructure: the maximum subarray ending at index $i$ is $\max(A[i], \text{curr\_max} + A[i])$. It runs in strictly linear time $\Theta(n)$ and $O(1)$ auxiliary space.
> The Divide-and-Conquer approach splits the array into two halves of size $n/2$, recursively finds the max subarray in the left, right, and crossing the midpoint. The crossing sum takes $\Theta(n)$, giving recurrence $T(n) = 2T(n/2) + \Theta(n) = \Theta(n \log n)$ and $O(\log n)$ stack space.
> Both algorithms yield the exact same peak burst anomaly score (sum = 15), but Kadane executes with fewer comparisons."

### Q5: "If the evaluator asks you to change the input data live during the demo, what do you do?"
**Action:**
> - In CLI: Pass custom command-line flags or edit `data_generator.c` / use the interactive menu `.\bin\soc_engine.exe`.
> - In Web GUI: Open `http://127.0.0.1:8080`, change the values directly in the card's input boxes (e.g., change the Downtime Budget slider from 40 to 60 mins on the Knapsack card, or enter a new target ID in Binary Search), and click the action button. The output updates live!
"""
    with open(SCRIPT_MD, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[+] 8-Minute Demo Script saved to: {SCRIPT_MD}")

if __name__ == "__main__":
    generate_concise_deck()
    generate_script_markdown()
    print("[+] Evaluation deliverables successfully generated!")
