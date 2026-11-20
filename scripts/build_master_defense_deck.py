#!/usr/bin/env python3
"""
Generate Master Professor-Defense Presentation (8 Slides) with Embedded High-Res Diagrams.
Tailored for presenting before high-level DAA Professors and Faculty Evaluation Panels.
Outputs:
  - presentation/CSEG3053_Professor_Defense_Master_Deck.pptx
  - presentation/CSEG3053_8Min_Evaluation_Deck.pptx (Updated)
"""

import os
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRES_DIR = os.path.join(BASE_DIR, "presentation")
ASSETS_DIR = os.path.join(PRES_DIR, "assets")
PPTX_MASTER = os.path.join(PRES_DIR, "CSEG3053_Professor_Defense_Master_Deck.pptx")
PPTX_EVAL = os.path.join(PRES_DIR, "CSEG3053_8Min_Evaluation_Deck.pptx")

# Dark SOC Palette
BG_DARK = RGBColor(11, 17, 32)       # #0B1120
CARD_BG = RGBColor(21, 32, 51)      # #152033
CARD_BORDER = RGBColor(34, 52, 80)  # #223450
CYAN = RGBColor(0, 240, 255)        # #00F0FF
MAGENTA = RGBColor(255, 0, 85)      # #FF0055
AMBER = RGBColor(245, 158, 11)      # #F59E0B
GREEN = RGBColor(16, 185, 129)      # #10B981
WHITE = RGBColor(255, 255, 255)
MUTED = RGBColor(148, 163, 184)     # #94A3B8

def set_slide_background(slide):
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = BG_DARK
    bg.line.fill.background()
    return bg

def add_header(slide, title, category="CSEG3053 DAA CAPSTONE DEFENSE | PROFESSOR EVALUATION PANEL"):
    cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.32), Inches(11.7), Inches(0.35))
    tf_c = cat_box.text_frame
    p_c = tf_c.paragraphs[0]
    p_c.text = category.upper()
    p_c.font.size = Pt(9.5)
    p_c.font.bold = True
    p_c.font.color.rgb = CYAN
    p_c.font.name = 'Consolas'

    t_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.65), Inches(11.7), Inches(0.8))
    tf_t = t_box.text_frame
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
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = CYAN
    p.font.name = 'Segoe UI'

    if subtitle:
        p2 = tf.add_paragraph()
        p2.text = subtitle
        p2.font.size = Pt(8.5)
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
    p2.font.size = Pt(11.5)
    p2.font.bold = True
    p2.font.color.rgb = WHITE
    p2.font.name = 'Segoe UI'

def build_master_deck():
    print("[*] Generating Master Professor-Defense Presentation (8 Slides)...")
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # =========================================================================
    # SLIDE 1: TITLE, VISION & ENGINEERING STANDARDS
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1)

    t_box = s1.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(11.7), Inches(2.0))
    tf1 = t_box.text_frame
    tf1.word_wrap = True

    p0 = tf1.paragraphs[0]
    p0.text = "CSEG3053: DESIGN AND ANALYSIS OF ALGORITHMS — CAPSTONE PBL DEFENSE"
    p0.font.size = Pt(11)
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
    p2.text = "A High-Throughput Algorithmic Workbench & SOC Analytics Engine in Pure C17 (ISO/IEC 9899:2018)"
    p2.font.size = Pt(14)
    p2.font.color.rgb = MUTED

    # 4 KPI Badges
    create_kpi_badge(s1, Inches(0.8), Inches(2.55), Inches(2.75), Inches(1.0), "Standard", "Strict Pure C17 (-O2)", CYAN)
    create_kpi_badge(s1, Inches(3.78), Inches(2.55), Inches(2.75), Inches(1.0), "Zero Shortcuts", "No qsort/bsearch/strstr", AMBER)
    create_kpi_badge(s1, Inches(6.76), Inches(2.55), Inches(2.75), Inches(1.0), "Verification", "33 / 33 Unit Tests (100%)", GREEN)
    create_kpi_badge(s1, Inches(9.74), Inches(2.55), Inches(2.75), Inches(1.0), "Git Artifacts", "v1.1.0 Tagged Release", MAGENTA)

    # 2 Detailed Cards
    tf_c1 = create_card(s1, Inches(0.8), Inches(3.75), Inches(5.7), Inches(3.3), "1. The Operational Security Problem", "Data Explosion & Algorithmic Denial-of-Service", border_color=MAGENTA)
    pts1 = [
        "High-Velocity Telemetry: Modern SOCs ingest 50,000+ logs/sec across firewalls, EDR, and DNS.",
        "Algorithmic Denial-of-Service: Adversaries intentionally stream pre-sorted logs to trigger O(N^2) worst-case sorting stalls in naive detection systems.",
        "Ransomware SLA Downtime Crunch: Containment actions must be prioritized under strict downtime limits before critical business assets collapse.",
        "Data Exfiltration Velocity: Identifying exact bottleneck links to sever without disrupting legitimate enterprise traffic."
    ]
    for pt in pts1:
        p = tf_c1.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(9.5)
        p.font.color.rgb = WHITE

    tf_c2 = create_card(s1, Inches(6.8), Inches(3.75), Inches(5.7), Inches(3.3), "2. The Pure C17 Algorithmic Engine", "Rigor, Determinism & Zero Black-Box Shortcuts", border_color=CYAN)
    pts2 = [
        "Zero Standard Library Shortcuts: All sorting, searching, DP, graph, tree, flow, string matching, and number-theoretic algorithms written 100% from scratch in C.",
        "Predictable Hardware Footprint: Tracked contiguous heap memory and cache-friendly structs without opaque abstraction overhead.",
        "Empirical Telemetry Harness: MetricsTracker instrumentation capturing exact atomic comparisons, writes, recursive calls, relaxations, and heap bytes.",
        "Dual Interface: Menu-driven headless CLI and real-time browser-based Algorithmic Studio (gui/index.html)."
    ]
    for pt in pts2:
        p = tf_c2.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(9.5)
        p.font.color.rgb = WHITE

    # =========================================================================
    # SLIDE 2: ENTERPRISE TOPOLOGY GRAPH & DATA MODELS (WITH EMBEDDED DIAGRAM)
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2)
    add_header(s2, "Enterprise Threat Topology & Typed Domain Models")

    # Left Card: Text & Model details
    tf_m = create_card(s2, Inches(0.8), Inches(1.5), Inches(4.8), Inches(5.5), "Typed C17 Domain Entities", "include/domain.h Structs", border_color=CYAN)
    m_pts = [
        "EventLog Struct: Monotonic uint64_t ID, timestamp, IPv4 endpoints, port, severity, and payload buffer.",
        "HostNode & AttackGraph: Directed weighted graphs where edge weights represent lateral movement exploit resistance or privilege escalation benefits.",
        "FlowNetwork: Capacitated residual network (capacity[][] & flow[][]) for data exfiltration containment.",
        "ContainmentPlaybook: Automated response tasks with downtime disruption cost (weight) & mitigated risk score (value).",
        "MetricsTracker: Telemetry harness capturing exact atomic comparisons, writes, recursive calls, and heap allocations."
    ]
    for pt in m_pts:
        p = tf_m.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(9.5)
        p.font.color.rgb = WHITE

    # Right Box: Embedded High-Res Attack Topology Graph
    img_topo = os.path.join(ASSETS_DIR, "attack_topology_graph.png")
    if os.path.exists(img_topo):
        s2.shapes.add_picture(img_topo, Inches(5.8), Inches(1.5), Inches(6.73), Inches(5.5))

    # =========================================================================
    # SLIDE 3: COMPLETE SYLLABUS ALGORITHMIC BLUEPRINT
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3)
    add_header(s3, "Complete Syllabus Algorithmic Blueprint (Units II – VI)")

    p_cards = [
        ("Divide & Conquer (Unit II)", "• MergeSort: Stable Theta(N log N) chronological triage.\n• QuickSort: Randomized pivot defeats DoS floods.\n• Binary Search: O(log N) forensic event pinpointing.\n• Kadane & D&C: Isolates exact DDoS surge window.\n• Celebrity Problem: Identifies C2 sinkhole in O(N).\n• Strassen MatMult: Sub-cubic Theta(N^2.807) reachability.", CYAN),
        ("Greedy Methods (Unit III)", "• Activity Selection: Max non-overlapping scan schedule.\n• Interval Partitioning: Min malware sandbox VMs.\n• Fractional Knapsack: DPI bandwidth allocation.\n• Huffman Coding: Cuts syslog storage by ~50%.\n• Dijkstra Exploit Path: Shortest exploit routes.\n• Prim & Kruskal MST: Resilient quarantine cabling tree.", AMBER),
        ("Dynamic Programming (Unit IV)", "• 0/1 Knapsack DP: Playbooks under SLA crunch.\n• Matrix Chain Order: Optimal telemetry join parens.\n• LCS Kill-Chain: Aligns audit logs with APT progressions.\n• Optimal BST Index: Frequency-weighted rule lookup.\n• Bellman-Ford: Exploit routes with negative privileges.\n• Held-Karp TSP DP: Min-latency forensic memory tour.", GREEN),
        ("B&B, Flow & Strings (Unit V-VI)", "• N-Queens: Deception honeypot routing slices (92 sol).\n• Sum of Subsets: Dual-bounding alert escalation.\n• Knapsack B&B: Least-Cost priority queue bounding.\n• Ford-Fulkerson: Halts exfiltration via Min-Cut edges.\n• Bipartite Matching: Dispatches incidents to analysts.\n• 4 String Matchers: KMP linear search defeats attacks.", MAGENTA)
    ]
    for idx, (t, desc, col) in enumerate(p_cards):
        x = Inches(0.8 + (idx % 2) * 5.95)
        y = Inches(1.5 + (idx // 2) * 2.75)
        tf_p = create_card(s3, x, y, Inches(5.75), Inches(2.55), t, border_color=col)
        for line in desc.split("\n"):
            p = tf_p.add_paragraph()
            p.text = line
            p.font.size = Pt(9.5)
            p.font.color.rgb = WHITE

    # =========================================================================
    # SLIDE 4: MATHEMATICAL RECURRENCES (WITH EMBEDDED DIAGRAM)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4)
    add_header(s4, "Mathematical Recurrence Derivations & Master Theorem Proofs")

    # Left Text: Explanations
    tf_rc = create_card(s4, Inches(0.8), Inches(1.5), Inches(4.8), Inches(5.5), "Master Theorem Proofs & Limits", "Theoretical Asymptotic Derivations", border_color=CYAN)
    rc_pts = [
        "MergeSort Recurrence: T(n) = 2T(n/2) + Theta(n)",
        "  - a=2, b=2, f(n)=cn -> n^(log_2 2) = n^1 = n",
        "  - Since f(n) = Theta(n^(log_b a)), Case 2 applies:",
        "  - Result: T(n) = Theta(n log n).",
        "Strassen Matrix Recurrence: T(N) = 7T(N/2) + Theta(N^2)",
        "  - a=7, b=2 -> N^(log_2 7) approx N^2.807",
        "  - Since f(N) = N^2 = O(N^(2.807 - eps)), Case 1 applies:",
        "  - Result: T(N) = Theta(N^2.807).",
        "Why Master Theorem Fails on QuickSort Worst-Case:",
        "  - T(n) = T(n-1) + cn (Subtractive subproblem decrement).",
        "  - Master Theorem requires multiplicative division (n/b).",
        "  - Unrolling proof: T(0) + c * sum(i=1..n) i = Theta(n^2)."
    ]
    for pt in rc_pts:
        p = tf_rc.add_paragraph()
        p.text = pt
        p.font.size = Pt(9)
        p.font.color.rgb = WHITE
        p.font.name = 'Consolas' if 'T(' in pt or 'a=' in pt else 'Segoe UI'

    # Right: Embedded Recursion Trees Image
    img_trees = os.path.join(ASSETS_DIR, "recurrence_trees.png")
    if os.path.exists(img_trees):
        s4.shapes.add_picture(img_trees, Inches(5.8), Inches(1.5), Inches(6.73), Inches(5.5))

    # =========================================================================
    # SLIDE 5: EMPIRICAL BENCHMARK SHOWDOWN (WITH EMBEDDED CHARTS & TABLE)
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5)
    add_header(s5, "Empirical Benchmark Showdown: Theory vs. Execution Reality")

    # Left: Embedded High-Res Comparison Bar Charts
    img_charts = os.path.join(ASSETS_DIR, "benchmark_charts.png")
    if os.path.exists(img_charts):
        s5.shapes.add_picture(img_charts, Inches(0.8), Inches(1.5), Inches(5.8), Inches(5.5))

    # Right: Benchmark Data Matrix Card
    tf_bm = create_card(s5, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.5), "Key Empirical Discoveries", "data/benchmark_results.csv", border_color=GREEN)
    bm_pts = [
        "180x Speedup on Adversarial Log Streams:",
        "  - Deterministic QuickSort stalled at 1,999,000 comparisons (35.0 ms) on pre-sorted logs (O(N^2) crash).",
        "  - Stable MergeSort required only 11,088 comparisons (1.0 ms) on the exact same stream.",
        "4.5x Speedup Against Pathological String Floods:",
        "  - Naive matching took 89,919 comparisons on repetitive attack payloads ('AAAA...B').",
        "  - KMP linear scan completed in 20,004 comparisons with zero backtracking.",
        "Knapsack Solvers Exact Convergence:",
        "  - 0/1 Knapsack DP, Backtracking, and Branch & Bound all converged on 230 risk points under 40 min SLA.",
        "  - Least-Cost B&B evaluated the fewest nodes (9 pruned).",
        "Forensic TSP Optimal Tour Convergence:",
        "  - Held-Karp Bitmask DP and Least-Cost B&B both converged on identical minimum tour cost: 281."
    ]
    for pt in bm_pts:
        p = tf_bm.add_paragraph()
        p.text = pt
        p.font.size = Pt(9.5)
        p.font.color.rgb = WHITE
        p.font.name = 'Consolas' if 'QuickSort' in pt or 'KMP' in pt or '0/1' in pt else 'Segoe UI'

    # =========================================================================
    # SLIDE 6: STATE-SPACE SEARCH & BRANCH-AND-BOUND (WITH EMBEDDED TREE)
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6)
    add_header(s6, "State-Space Search & Branch-and-Bound Pruning")

    # Left Card: State-space strategy comparison
    tf_bb = create_card(s6, Inches(0.8), Inches(1.5), Inches(4.8), Inches(5.5), "Branch & Bound Search Policies", "FIFO vs. LIFO vs. Least-Cost (LC)", border_color=MAGENTA)
    bb_pts = [
        "Queue-Based FIFO (BFS):",
        "  - Evaluates 57 nodes, prunes 11 unpromising branches under budget constraints.",
        "Stack-Based LIFO (DFS):",
        "  - Explores deep states, pruning 11 branches with low memory footprint.",
        "Least-Cost Priority Queue (LC-BB):",
        "  - Evaluates node with highest fractional upper bound first, achieving the tightest exploration (9 pruned).",
        "TSP Least-Cost B&B Admissible Lower Bound:",
        "  - Computes min outgoing edge from current vertex + min outgoing edges from all unvisited vertices.",
        "  - Strictly admissible (never overestimates).",
        "  - Converged on exact Held-Karp cost (281) while pruning 22,474 subtrees!"
    ]
    for pt in bb_pts:
        p = tf_bb.add_paragraph()
        p.text = pt
        p.font.size = Pt(9.5)
        p.font.color.rgb = WHITE

    # Right: Embedded State-Space Tree Diagram
    img_tree = os.path.join(ASSETS_DIR, "state_space_tree.png")
    if os.path.exists(img_tree):
        s6.shapes.add_picture(img_tree, Inches(5.8), Inches(1.5), Inches(6.73), Inches(5.5))

    # =========================================================================
    # SLIDE 7: COMPLEXITY CLASSES & NP-REDUCTIONS (WITH EMBEDDED DIAGRAM)
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7)
    add_header(s7, "Complexity Theory & Formal Polynomial-Time Reductions")

    # Left Card: Reduction logic
    tf_rd = create_card(s7, Inches(0.8), Inches(1.5), Inches(4.8), Inches(5.5), "Formal NP-Completeness Proof", "SUBSET-SUM <=_p 0/1 KNAPSACK", border_color=AMBER)
    rd_pts = [
        "Classification Matrix:",
        "  - Class P: Sorting, Dijkstra, Bellman-Ford, Edmonds-Karp, Bipartite Matching.",
        "  - Class NP-Complete: 0/1 Knapsack Decision, Subset-Sum, N-Queens.",
        "  - Class NP-Hard: Travelling Salesperson (TSP) Optimization.",
        "Polynomial Reduction Construction:",
        "  - Given Subset-Sum instance: S = {s1, ..., sn}, Target T.",
        "  - Construct Knapsack with wi = si, vi = si, capacity W = T, value V = T.",
        "  - Mapping takes strictly O(n) polynomial time.",
        "Equivalence Proof:",
        "  - (=>) If sum(si) = T, selecting same items gives weight T <= W and value T >= V.",
        "  - (<=) Since wi = vi, weight <= T and value >= T forces sum(wi) = sum(vi) = T.",
        "  - Therefore, 0/1 Knapsack decision is NP-Complete."
    ]
    for pt in rd_pts:
        p = tf_rd.add_paragraph()
        p.text = pt
        p.font.size = Pt(9.2)
        p.font.color.rgb = WHITE
        p.font.name = 'Consolas' if '<=' in pt or 'wi' in pt else 'Segoe UI'

    # Right: Embedded Complexity & Reduction Image
    img_cplx = os.path.join(ASSETS_DIR, "complexity_reduction.png")
    if os.path.exists(img_cplx):
        s7.shapes.add_picture(img_cplx, Inches(5.8), Inches(1.5), Inches(6.73), Inches(5.5))

    # =========================================================================
    # SLIDE 8: OPERATIONAL SCENARIOS, 33/33 TESTS & VIVA DEFENSE READINESS
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8)
    add_header(s8, "Demonstration Scenarios, Verification & Viva Defense Readiness")

    tf_sc = create_card(s8, Inches(0.8), Inches(1.5), Inches(5.7), Inches(5.5), "3 Operational Cybersecurity Scenarios", "Real-World Threat Simulations", border_color=CYAN)
    sc_pts = [
        "Scenario 1: Normal SOC Operations:",
        "  - Chronological log sort, logarithmic binary search, KMP SQLi payload scan, LCS APT progression ('ADGX'), bipartite ticket dispatch.",
        "Scenario 2: Ransomware 60% SLA Shock:",
        "  - SLA downtime budget slashed from 100 to 40 mins. Knapsack DP/B&B achieve optimal 230 risk score. Bellman-Ford handles negative privilege edges. Ford-Fulkerson isolates 8 Min-Cut firewall links.",
        "Scenario 3: Adversarial Stress Defense:",
        "  - Pre-sorted DDoS streams, pathological repetitive text, and 12-host TSP collector routing solved via Held-Karp DP and Least-Cost B&B."
    ]
    for pt in sc_pts:
        p = tf_sc.add_paragraph()
        p.text = pt
        p.font.size = Pt(9.5)
        p.font.color.rgb = WHITE

    tf_qa = create_card(s8, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.5), "Verification & Viva Defense Readiness", "33 / 33 Unit Tests (100% Pass Rate)", border_color=GREEN)
    qa_pts = [
        "Automated Test Suite (tests/test_all.c):",
        "  - 33 / 33 Unit Tests passing across all 6 syllabus units with small-instance assertion oracles.",
        "Compiler Verification:",
        "  - Strict -std=c17 -Wall -Wextra -O2 compilation with zero warnings.",
        "Live Interactive Studio:",
        "  - Run .\\start_gui.bat -> http://127.0.0.1:8080 (Interactive sliders, topology canvas, honeypot board).",
        "GitHub Artifacts:",
        "  - SPARSHsrihero1/cseg3053-cyber-threat-engine (Release v1.1.0).",
        "Core Academic Principle:",
        "  - 'A working project demonstrates what you built; your technical explanation demonstrates what you learned.'"
    ]
    for pt in qa_pts:
        p = tf_qa.add_paragraph()
        p.text = pt
        p.font.size = Pt(9.5)
        p.font.color.rgb = WHITE

    # Save both decks
    prs.save(PPTX_MASTER)
    prs.save(PPTX_EVAL)
    print(f"[+] Master Defense Presentation saved to: {PPTX_MASTER}")
    print(f"[+] Evaluation Deck updated at: {PPTX_EVAL}")

if __name__ == "__main__":
    build_master_deck()
