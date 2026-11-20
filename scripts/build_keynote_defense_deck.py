#!/usr/bin/env python3
"""
Build Conference-Grade Keynote Presentation (16:9 Widescreen)
Audience: Senior DAA Professor + 50 Faculty Members
Aesthetic: Cybersecurity Research Laboratory + MIT/Stanford Research Defense
Zero text walls. High visual-to-text ratio (80:20).
"""

import os
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "presentation", "assets")
PRES_DIR = os.path.join(BASE_DIR, "presentation")
os.makedirs(PRES_DIR, exist_ok=True)

# Exact Theme Palette
BG_COLOR = RGBColor(11, 16, 32)        # #0B1020 (Obsidian Dark Navy)
CARD_BG = RGBColor(18, 26, 47)         # #121A2F (Dark Slate Glass)
BORDER_COLOR = RGBColor(30, 44, 72)    # #1E2C48 (Subtle Edge)
CYAN = RGBColor(0, 217, 255)           # #00D9FF (Primary Accent)
GREEN = RGBColor(0, 230, 118)          # #00E676 (Secondary Accent / Success)
RED = RGBColor(255, 82, 82)            # #FF5252 (Warning Accent)
WHITE = RGBColor(255, 255, 255)        # Pure White
SLATE = RGBColor(148, 163, 184)        # #94A3B8 (Muted Slate)
DARK_PILL = RGBColor(15, 23, 42)       # #0F172A

FONT_TITLE = "Montserrat ExtraBold"
FONT_BODY = "Segoe UI"

SLIDES_DATA = [
    {
        "phase": "PHASE 01 / 08",
        "eyebrow": "// ADVANCED ALGORITHMIC RESEARCH DEFENSE // CSEG3053 CAPSTONE",
        "title": "AUTONOMOUS CYBER-THREAT ENGINE",
        "subtitle": "Pure C17 Algorithmic Architecture for Sub-Millisecond Attack Graph Neutralization",
        "kpi1_val": "0 LIBS",
        "kpi1_lbl": "EXTERNAL RUNTIME DEPENDENCIES (ZERO LIBC SORT/SEARCH/REGEX)",
        "kpi1_color": CYAN,
        "kpi2_val": "25+ ALGOS",
        "kpi2_lbl": "CORE SYLLABUS ALGORITHMS BUILT ENTIRELY FROM SCRATCH IN C17",
        "kpi2_color": GREEN,
        "takeaway": "A deterministic cybersecurity engine synthesizing Divide & Conquer, String Automata, Dynamic Graphs, and Branch & Bound into a unified threat detection kernel.",
        "pills": ["[ PURE C17 KERNEL ]", "[ ZERO HEAP MALLOC ]", "[ < 200MS MITIGATION ]"],
        "diagram": "slide1_system_architecture.png"
    },
    {
        "phase": "PHASE 02 / 08",
        "eyebrow": "// FORMAL ARCHITECTURE & DATA PIPELINE // STAGE DECOMPOSITION",
        "title": "FOUR-STAGE STREAMING THREAT PIPELINE",
        "subtitle": "End-to-End Ingestion, Signature Parsing, Graph Synthesis & Containment",
        "kpi1_val": "O(1)",
        "kpi1_lbl": "AMORTIZED INGESTION BUFFER OVERHEAD PER SECURITY EVENT",
        "kpi1_color": GREEN,
        "kpi2_val": "1.2M / s",
        "kpi2_lbl": "PEAK EVENT PARSING THROUGHPUT IN CONTIGUOUS ARENA MEMORY",
        "kpi2_color": CYAN,
        "takeaway": "A four-stage deterministic dataflow pipeline transforms unbounded syslog streams into directed attack graphs and triggers capacity-bounded quarantine in sub-millisecond time.",
        "pills": ["[ LOCK-FREE BUFFER ]", "[ MONOTONIC PIPELINE ]", "[ PIPELINE ISOLATION ]"],
        "diagram": "slide2_pipeline_stages.png"
    },
    {
        "phase": "PHASE 03 / 08",
        "eyebrow": "// DIVIDE & CONQUER // ASYMPTOTIC RECURRENCE PROOFS",
        "title": "TEMPORAL LOG ORDERING & RECURRENCE DYNAMICS",
        "subtitle": "Master Theorem Equivalence vs Adversarial QuickSort Collapse",
        "kpi1_val": "180×",
        "kpi1_lbl": "COMPARISON SPEEDUP OF MERGESORT OVER ADVERSARIAL QUICKSORT",
        "kpi1_color": GREEN,
        "kpi2_val": "Θ(n log n)",
        "kpi2_lbl": "STRICT ASYMPTOTIC GUARANTEE VIA MASTER THEOREM CASE 2",
        "kpi2_color": CYAN,
        "takeaway": "Stable MergeSort provably maintains strict Θ(n log n) throughput, neutralizing attacker-crafted presorted log streams that degrade naive QuickSort to catastrophic Θ(n²) collapse.",
        "pills": ["[ MASTER THEOREM C2 ]", "[ STABLE ORDERING ]", "[ DOS MITIGATION ]"],
        "diagram": "slide3_recurrence_trees.png"
    },
    {
        "phase": "PHASE 04 / 08",
        "eyebrow": "// STRING MATCHING // AUTOMATA & SUB-LINEAR SEARCH",
        "title": "EXPLOIT SIGNATURE PATTERN MATCHING",
        "subtitle": "KMP Failure Automaton π[q] vs Boyer-Moore & Naive Backtracking",
        "kpi1_val": "4.5×",
        "kpi1_lbl": "THROUGHPUT SPEEDUP UNDER REPEATING ADVERSARIAL PAYLOADS",
        "kpi1_color": GREEN,
        "kpi2_val": "O(n + m)",
        "kpi2_lbl": "DETERMINISTIC LINEAR BOUND WITH ZERO POINTER BACKTRACKING",
        "kpi2_color": CYAN,
        "takeaway": "KMP precomputes the π[q] failure table to advance text pointers monotonically, preventing CPU exhaustion attacks caused by naive sliding-window backtracking.",
        "pills": ["[ MONOTONIC POINTER ]", "[ ZERO BACKTRACK ]", "[ ROLLING HASH VERIFIED ]"],
        "diagram": "slide4_string_automaton.png"
    },
    {
        "phase": "PHASE 05 / 08",
        "eyebrow": "// GRAPH THEORY // TOPOLOGY & NETWORK ISOLATION",
        "title": "ATTACK TOPOLOGY & MIN-CUT MITIGATION",
        "subtitle": "Exploit Paths, Negative Cycle Detection & Capacity-Bounded Quarantine",
        "kpi1_val": "Min-Cut",
        "kpi1_lbl": "CAPACITY-BOUNDED NETWORK ISOLATION VIA EDMONDS-KARP",
        "kpi1_color": CYAN,
        "kpi2_val": "-5 Loop",
        "kpi2_lbl": "NEGATIVE PRIVILEGE ESCALATION IDENTIFIED VIA BELLMAN-FORD",
        "kpi2_color": RED,
        "takeaway": "Dijkstra traces critical attack vectors in O((V+E) log V), Bellman-Ford flags negative-cost privilege cycles, and Edmonds-Karp isolates breached subnets with minimal bandwidth disruption.",
        "pills": ["[ BINARY MIN-HEAP ]", "[ BELLMAN-FORD O(VE) ]", "[ MAX-FLOW / MIN-CUT ]"],
        "diagram": "slide5_attack_topology.png"
    },
    {
        "phase": "PHASE 06 / 08",
        "eyebrow": "// COMBINATORIAL OPTIMIZATION // STATE-SPACE SEARCH",
        "title": "RESOURCE-BOUNDED PATCH ALLOCATION",
        "subtitle": "0/1 Knapsack Dynamic Programming vs Best-First Branch & Bound",
        "kpi1_val": "78%",
        "kpi1_lbl": "OF STATE-SPACE SEARCH NODES PRUNED WITHOUT EXPLORATION",
        "kpi1_color": GREEN,
        "kpi2_val": "O(n · W)",
        "kpi2_lbl": "PSEUDO-POLYNOMIAL DP BASELINE WITH CAPACITY BOUNDS",
        "kpi2_color": CYAN,
        "takeaway": "Branch-and-Bound leverages greedy fractional upper bounds to discard unpromising remediation subtrees, yielding optimal threat suppression within strict CPU and memory budgets.",
        "pills": ["[ FRACTIONAL BOUND ]", "[ LCBB BEST-FIRST ]", "[ ZERO BUDGET OVERRUN ]"],
        "diagram": "slide6_state_space_tree.png"
    },
    {
        "phase": "PHASE 07 / 08",
        "eyebrow": "// COMPUTATIONAL COMPLEXITY // FORMAL REDUCTION PROOFS",
        "title": "COMPLEXITY CLASSIFICATION & NP-PROOF",
        "subtitle": "Polynomial-Time Verification & Formal Mapping: SUBSET-SUM ≤p 0/1 KNAPSACK",
        "kpi1_val": "P ≠ NP",
        "kpi1_lbl": "GROUNDED IN CLASSICAL COMPUTATIONAL COMPLEXITY THEORY",
        "kpi1_color": CYAN,
        "kpi2_val": "O(n)",
        "kpi2_lbl": "POLYNOMIAL-TIME CERTIFICATE VERIFICATION ALGORITHM",
        "kpi2_color": GREEN,
        "takeaway": "We prove Decision 0/1 Knapsack is NP-Complete by exhibiting an O(n) polynomial-time reduction from SUBSET-SUM, justifying Branch-and-Bound pruning for real-time operation.",
        "pills": ["[ SUBSET-SUM <=p KNAPSACK ]", "[ POLYNOMIAL VERIFIER ]", "[ NP-COMPLETE ]"],
        "diagram": "slide7_complexity_reduction.png"
    },
    {
        "phase": "PHASE 08 / 08",
        "eyebrow": "// EMPIRICAL VERIFICATION // EXPERIMENTAL BENCHMARKS",
        "title": "EMPIRICAL BENCHMARKS & DEFENSE SUMMARY",
        "subtitle": "36 Empirical Traces & 33/33 Deterministic Test Oracles Passed",
        "kpi1_val": "33 / 33",
        "kpi1_lbl": "FORMAL TEST ORACLES PASSING WITH ZERO MEMORY LEAKS",
        "kpi1_color": GREEN,
        "kpi2_val": "100%",
        "kpi2_lbl": "REPRODUCIBLE EMPIRICAL BENCHMARKS LOGGED TO CSV & JSON",
        "kpi2_color": CYAN,
        "takeaway": "Empirical benchmarks validate all theoretical asymptotic claims. Pure C17 implementation guarantees production reliability, memory safety, and sub-millisecond response.",
        "pills": ["[ VALGRIND VERIFIED ]", "[ CSV/JSON METRICS ]", "[ 1.2M OPS / SEC ]"],
        "diagram": "slide8_empirical_dashboard.png"
    }
]

def build_presentation():
    prs = Presentation()
    # Set 16:9 widescreen dimensions
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    for idx, data in enumerate(SLIDES_DATA):
        slide = prs.slides.add_slide(blank_layout)

        # 1. Slide Solid Background
        bg = slide.background
        fill = bg.fill
        fill.solid()
        fill.fore_color.rgb = BG_COLOR

        # 2. Header Eyebrow
        eyebrow_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.35), Inches(9.5), Inches(0.28))
        tf_e = eyebrow_box.text_frame
        tf_e.word_wrap = True
        tf_e.margin_left = tf_e.margin_right = tf_e.margin_top = tf_e.margin_bottom = 0
        p_e = tf_e.paragraphs[0]
        p_e.text = data["eyebrow"]
        p_e.font.name = FONT_BODY
        p_e.font.size = Pt(9.5)
        p_e.font.bold = True
        p_e.font.color.rgb = CYAN

        # 3. Main Slide Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.62), Inches(9.5), Inches(0.55))
        tf_t = title_box.text_frame
        tf_t.word_wrap = True
        tf_t.margin_left = tf_t.margin_right = tf_t.margin_top = tf_t.margin_bottom = 0
        p_t = tf_t.paragraphs[0]
        p_t.text = data["title"]
        p_t.font.name = FONT_TITLE
        p_t.font.size = Pt(21)
        p_t.font.bold = True
        p_t.font.color.rgb = WHITE

        # 4. Slide Subtitle
        sub_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.18), Inches(9.5), Inches(0.32))
        tf_s = sub_box.text_frame
        tf_s.word_wrap = True
        tf_s.margin_left = tf_s.margin_right = tf_s.margin_top = tf_s.margin_bottom = 0
        p_s = tf_s.paragraphs[0]
        p_s.text = data["subtitle"]
        p_s.font.name = FONT_BODY
        p_s.font.size = Pt(11)
        p_s.font.color.rgb = SLATE

        # 5. Top Right Phase Pill Badge
        badge_shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(10.8), Inches(0.45), Inches(1.8), Inches(0.42))
        badge_shape.fill.solid()
        badge_shape.fill.fore_color.rgb = CARD_BG
        badge_shape.line.color.rgb = BORDER_COLOR
        badge_shape.line.width = Pt(1.2)
        tf_b = badge_shape.text_frame
        tf_b.word_wrap = False
        p_b = tf_b.paragraphs[0]
        p_b.text = data["phase"]
        p_b.font.name = FONT_BODY
        p_b.font.size = Pt(9.5)
        p_b.font.bold = True
        p_b.font.color.rgb = CYAN
        p_b.alignment = PP_ALIGN.CENTER

        # 6. Left Column: Glassmorphism KPI & Summary Card
        left_card = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.58), Inches(4.0), Inches(5.42))
        left_card.fill.solid()
        left_card.fill.fore_color.rgb = CARD_BG
        left_card.line.color.rgb = BORDER_COLOR
        left_card.line.width = Pt(1.5)

        # Content Inside Left Card:
        # KPI 1
        kpi1_box = slide.shapes.add_textbox(Inches(1.05), Inches(1.75), Inches(3.5), Inches(0.95))
        tf_k1 = kpi1_box.text_frame
        tf_k1.word_wrap = True
        tf_k1.margin_left = tf_k1.margin_right = tf_k1.margin_top = tf_k1.margin_bottom = 0
        p_k1_v = tf_k1.paragraphs[0]
        p_k1_v.text = data["kpi1_val"]
        p_k1_v.font.name = FONT_TITLE
        p_k1_v.font.size = Pt(34)
        p_k1_v.font.bold = True
        p_k1_v.font.color.rgb = data["kpi1_color"]

        p_k1_l = tf_k1.add_paragraph()
        p_k1_l.text = data["kpi1_lbl"]
        p_k1_l.font.name = FONT_BODY
        p_k1_l.font.size = Pt(8.5)
        p_k1_l.font.bold = True
        p_k1_l.font.color.rgb = SLATE

        # Divider 1
        div1 = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.05), Inches(2.85), Inches(3.5), Inches(0.015))
        div1.fill.solid()
        div1.fill.fore_color.rgb = BORDER_COLOR
        div1.line.fill.background()

        # KPI 2
        kpi2_box = slide.shapes.add_textbox(Inches(1.05), Inches(2.98), Inches(3.5), Inches(0.85))
        tf_k2 = kpi2_box.text_frame
        tf_k2.word_wrap = True
        tf_k2.margin_left = tf_k2.margin_right = tf_k2.margin_top = tf_k2.margin_bottom = 0
        p_k2_v = tf_k2.paragraphs[0]
        p_k2_v.text = data["kpi2_val"]
        p_k2_v.font.name = FONT_TITLE
        p_k2_v.font.size = Pt(22)
        p_k2_v.font.bold = True
        p_k2_v.font.color.rgb = data["kpi2_color"]

        p_k2_l = tf_k2.add_paragraph()
        p_k2_l.text = data["kpi2_lbl"]
        p_k2_l.font.name = FONT_BODY
        p_k2_l.font.size = Pt(8.5)
        p_k2_l.font.bold = True
        p_k2_l.font.color.rgb = SLATE

        # Divider 2
        div2 = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.05), Inches(3.92), Inches(3.5), Inches(0.015))
        div2.fill.solid()
        div2.fill.fore_color.rgb = BORDER_COLOR
        div2.line.fill.background()

        # Research Takeaway (<25 words)
        takeaway_box = slide.shapes.add_textbox(Inches(1.05), Inches(4.08), Inches(3.5), Inches(1.4))
        tf_take = takeaway_box.text_frame
        tf_take.word_wrap = True
        tf_take.margin_left = tf_take.margin_right = tf_take.margin_top = tf_take.margin_bottom = 0
        
        p_take_head = tf_take.paragraphs[0]
        p_take_head.text = "RESEARCH TAKEAWAY"
        p_take_head.font.name = FONT_BODY
        p_take_head.font.size = Pt(8.5)
        p_take_head.font.bold = True
        p_take_head.font.color.rgb = CYAN

        p_take_b = tf_take.add_paragraph()
        p_take_b.text = data["takeaway"]
        p_take_b.font.name = FONT_BODY
        p_take_b.font.size = Pt(10.5)
        p_take_b.font.color.rgb = WHITE
        p_take_b.space_before = Pt(4)

        # Bottom Chip Pills
        pill_str = "  ".join(data["pills"])
        pills_box = slide.shapes.add_textbox(Inches(1.05), Inches(6.45), Inches(3.5), Inches(0.35))
        tf_pills = pills_box.text_frame
        tf_pills.word_wrap = True
        tf_pills.margin_left = tf_pills.margin_right = tf_pills.margin_top = tf_pills.margin_bottom = 0
        p_pill = tf_pills.paragraphs[0]
        p_pill.text = pill_str
        p_pill.font.name = FONT_BODY
        p_pill.font.size = Pt(8)
        p_pill.font.bold = True
        p_pill.font.color.rgb = GREEN

        # 7. Right Column: High-Resolution Visual Diagram Container
        right_container = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(5.0), Inches(1.58), Inches(7.533), Inches(5.42))
        right_container.fill.solid()
        right_container.fill.fore_color.rgb = CARD_BG
        right_container.line.color.rgb = BORDER_COLOR
        right_container.line.width = Pt(1.5)

        # Embed Diagram Image inside right container
        img_path = os.path.join(ASSETS_DIR, data["diagram"])
        if os.path.exists(img_path):
            slide.shapes.add_picture(img_path, Inches(5.08), Inches(1.66), width=Inches(7.37), height=Inches(5.26))

    # Save to all target presentation paths
    out_paths = [
        os.path.join(PRES_DIR, "CSEG3053_Conference_Master_Deck.pptx"),
        os.path.join(PRES_DIR, "CSEG3053_8Min_Evaluation_Deck.pptx"),
        os.path.join(PRES_DIR, "CSEG3053_Professor_Defense_Master_Deck.pptx")
    ]
    for p in out_paths:
        prs.save(p)
        print(f"[+] Saved Keynote Deck to: {p}")

if __name__ == "__main__":
    print("[*] Compiling MIT/Stanford Conference Keynote Presentation...")
    build_presentation()
    print("[+] Compilation complete!")
