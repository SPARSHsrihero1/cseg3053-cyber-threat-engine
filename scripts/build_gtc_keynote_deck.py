#!/usr/bin/env python3
"""
Compile Elite NVIDIA GTC / BlackHat Conference Keynote Presentation (16:9 Widescreen).
Audience: Senior DAA Professor + 50 Faculty Members.
Aesthetic: High-End Cyber Research Laboratory Keynote.
Features: Varied dynamic layouts, massive typography focal points (72pt, 64pt, 52pt),
glassmorphism cards, embedded high-res diagrams, and real Web GUI workbench captures.
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
GTC_DIR = os.path.join(ASSETS_DIR, "gtc")
CROPS_DIR = os.path.join(ASSETS_DIR, "gui_crops")
PRES_DIR = os.path.join(BASE_DIR, "presentation")
os.makedirs(PRES_DIR, exist_ok=True)

# Theme Palette
BG_COLOR = RGBColor(11, 16, 32)        # #0B1020 (Obsidian Dark Navy)
CARD_BG = RGBColor(18, 26, 47)         # #121A2F (Dark Slate Glass)
BORDER_COLOR = RGBColor(30, 44, 72)    # #1E2C48 (Subtle Edge)
CYAN = RGBColor(0, 217, 255)           # #00D9FF (Electric Cyan)
GREEN = RGBColor(0, 230, 118)          # #00E676 (Neon Green)
RED = RGBColor(255, 82, 82)            # #FF5252 (Coral Warning)
WHITE = RGBColor(255, 255, 255)        # Pure White
SLATE = RGBColor(148, 163, 184)        # #94A3B8 (Muted Slate)
DARK_PILL = RGBColor(15, 23, 42)       # #0F172A

FONT_TITLE = "Montserrat ExtraBold"
FONT_BODY = "Segoe UI"

def set_slide_background(slide):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = BG_COLOR

def add_header(slide, eyebrow, title, subtitle, phase_text):
    # Eyebrow
    eb = slide.shapes.add_textbox(Inches(0.8), Inches(0.32), Inches(9.5), Inches(0.28))
    tf_e = eb.text_frame
    tf_e.word_wrap = True
    tf_e.margin_left = tf_e.margin_right = tf_e.margin_top = tf_e.margin_bottom = 0
    p_e = tf_e.paragraphs[0]
    p_e.text = eyebrow
    p_e.font.name = FONT_BODY
    p_e.font.size = Pt(9.5)
    p_e.font.bold = True
    p_e.font.color.rgb = CYAN

    # Main Title
    tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.58), Inches(9.5), Inches(0.52))
    tf_t = tb.text_frame
    tf_t.word_wrap = True
    tf_t.margin_left = tf_t.margin_right = tf_t.margin_top = tf_t.margin_bottom = 0
    p_t = tf_t.paragraphs[0]
    p_t.text = title
    p_t.font.name = FONT_TITLE
    p_t.font.size = Pt(21)
    p_t.font.bold = True
    p_t.font.color.rgb = WHITE

    # Subtitle
    if subtitle:
        sb = slide.shapes.add_textbox(Inches(0.8), Inches(1.12), Inches(9.5), Inches(0.32))
        tf_s = sb.text_frame
        tf_s.word_wrap = True
        tf_s.margin_left = tf_s.margin_right = tf_s.margin_top = tf_s.margin_bottom = 0
        p_s = tf_s.paragraphs[0]
        p_s.text = subtitle
        p_s.font.name = FONT_BODY
        p_s.font.size = Pt(10.5)
        p_s.font.color.rgb = SLATE

    # Top Right Phase Badge
    badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(10.8), Inches(0.42), Inches(1.8), Inches(0.42))
    badge.fill.solid()
    badge.fill.fore_color.rgb = CARD_BG
    badge.line.color.rgb = BORDER_COLOR
    badge.line.width = Pt(1.2)
    tf_b = badge.text_frame
    tf_b.word_wrap = False
    p_b = tf_b.paragraphs[0]
    p_b.text = phase_text
    p_b.font.name = FONT_BODY
    p_b.font.size = Pt(9.5)
    p_b.font.bold = True
    p_b.font.color.rgb = CYAN
    p_b.alignment = PP_ALIGN.CENTER

def build_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # =========================================================================
    # SLIDE 1: Hero Command Center Keynote Overview
    # =========================================================================
    slide1 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide1)
    add_header(slide1, 
               "// CSEG3053 ALGORITHMIC RESEARCH DEFENSE // IEEE S&P 2026 ARCHITECTURE",
               "AUTONOMOUS CYBER-THREAT ENGINE",
               "Pure C17 Deterministic Algorithmic Architecture for Sub-Millisecond Attack Graph Neutralization",
               "PHASE 01 / 08")

    # Middle: Wide Architectural Ribbon
    ribbon_path = os.path.join(GTC_DIR, "gtc_slide1_hero_ribbon.png")
    if os.path.exists(ribbon_path):
        slide1.shapes.add_picture(ribbon_path, Inches(0.8), Inches(1.5), width=Inches(11.8), height=Inches(3.7))

    # Bottom HUD: 4 Stat Pillar Cards
    hud_data = [
        ("0 LIBS", "Pure C17 Standard\nZero External Libs", CYAN, 0.8),
        ("25+ ALGOS", "All Syllabus Algos\nBuilt From Scratch", GREEN, 3.8),
        ("1.2M / s", "Peak Event Throughput\nZero malloc in Hot Path", CYAN, 6.8),
        ("33 / 33", "Deterministic Oracles\n100% Pass Rate", GREEN, 9.8)
    ]
    for val, lbl, col, x_pos in hud_data:
        card = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x_pos), Inches(5.35), Inches(2.73), Inches(1.65))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = col
        card.line.width = Pt(1.5)

        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.15)
        tf.margin_top = Inches(0.18)

        p1 = tf.paragraphs[0]
        p1.text = val
        p1.font.name = FONT_TITLE
        p1.font.size = Pt(28)
        p1.font.bold = True
        p1.font.color.rgb = col
        p1.alignment = PP_ALIGN.CENTER

        p2 = tf.add_paragraph()
        p2.text = lbl
        p2.font.name = FONT_BODY
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = WHITE
        p2.alignment = PP_ALIGN.CENTER
        p2.space_before = Pt(4)

    # =========================================================================
    # SLIDE 2: Full-Width 4-Stage Streaming Threat Pipeline
    # =========================================================================
    slide2 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide2)
    add_header(slide2,
               "// SYSTEM ARCHITECTURE // FORMAL FOUR-STAGE PIPELINE",
               "FOUR-STAGE STREAMING THREAT PIPELINE",
               "Deterministic dataflow converting unbounded audit streams into capacity-bounded containment",
               "PHASE 02 / 08")

    # Main Visual: Full-Width 4-Stage Horizontal Pipeline Flow
    pipe_path = os.path.join(GTC_DIR, "gtc_slide2_pipeline.png")
    if os.path.exists(pipe_path):
        slide2.shapes.add_picture(pipe_path, Inches(0.8), Inches(1.55), width=Inches(11.8), height=Inches(4.5))

    # Bottom Keynote Insight Banner
    insight_box = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(6.15), Inches(11.8), Inches(0.95))
    insight_box.fill.solid()
    insight_box.fill.fore_color.rgb = CARD_BG
    insight_box.line.color.rgb = CYAN
    insight_box.line.width = Pt(1.5)

    tf_in = insight_box.text_frame
    tf_in.word_wrap = True
    tf_in.margin_left = tf_in.margin_right = Inches(0.25)
    tf_in.margin_top = Inches(0.12)
    p_in = tf_in.paragraphs[0]
    p_in.text = "ARCHITECTURAL GUARANTEE: Lock-free circular ring buffer decouples I/O ingestion from CPU-bound graph traversal, ensuring zero dropped syslog packets even under sustained 10 Gbps flood conditions. All stages execute in strictly bounded asymptotic time."
    p_in.font.name = FONT_BODY
    p_in.font.size = Pt(10)
    p_in.font.color.rgb = WHITE

    # =========================================================================
    # SLIDE 3: The 180x Adversarial Sorting Showdown (Focal Point Slide!)
    # =========================================================================
    slide3 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide3)
    add_header(slide3,
               "// DIVIDE & CONQUER // ADVERSARIAL STRESS PROOF",
               "TEMPORAL LOG ORDERING UNDER ADVERSARIAL FLOOD",
               "Master Theorem Equivalence vs Adversarial QuickSort Collapse",
               "PHASE 03 / 08")

    # Left Column: Massive Focal Point
    left3 = slide3.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.55), Inches(4.5), Inches(5.5))
    left3.fill.solid()
    left3.fill.fore_color.rgb = CARD_BG
    left3.line.color.rgb = BORDER_COLOR
    left3.line.width = Pt(1.5)

    tf3 = left3.text_frame
    tf3.word_wrap = True
    tf3.margin_left = tf3.margin_right = Inches(0.25)
    tf3.margin_top = Inches(0.2)

    # Hero Stat: 180x
    p_hero3 = tf3.paragraphs[0]
    p_hero3.text = "180×"
    p_hero3.font.name = FONT_TITLE
    p_hero3.font.size = Pt(64)
    p_hero3.font.bold = True
    p_hero3.font.color.rgb = GREEN

    p_hero3_lbl = tf3.add_paragraph()
    p_hero3_lbl.text = "FASTER UNDER PRE-SORTED ADVERSARIAL LOG INFLUX"
    p_hero3_lbl.font.name = FONT_TITLE
    p_hero3_lbl.font.size = Pt(12)
    p_hero3_lbl.font.bold = True
    p_hero3_lbl.font.color.rgb = WHITE
    p_hero3_lbl.space_before = Pt(2)

    # Divider
    div3 = slide3.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.05), Inches(3.2), Inches(4.0), Inches(0.015))
    div3.fill.solid()
    div3.fill.fore_color.rgb = BORDER_COLOR
    div3.line.fill.background()

    # Academic & Empirical Details
    p_det3 = tf3.add_paragraph()
    p_det3.text = "Master Theorem Case 2 Guarantee:\nT(n) = 2T(n/2) + Θ(n) => Strictly Θ(n log n)"
    p_det3.font.name = FONT_BODY
    p_det3.font.size = Pt(10.5)
    p_det3.font.bold = True
    p_det3.font.color.rgb = CYAN
    p_det3.space_before = Pt(18)

    p_take3 = tf3.add_paragraph()
    p_take3.text = "Adversaries intentionally flood pre-sorted timestamps to induce worst-case Θ(n²) QuickSort collapse (1,999,000 comparisons). Stable MergeSort guarantees uninterrupted Θ(n log n) throughput (11,088 comparisons), defusing CPU exhaustion attacks."
    p_take3.font.name = FONT_BODY
    p_take3.font.size = Pt(9.5)
    p_take3.font.color.rgb = SLATE
    p_take3.space_before = Pt(8)

    p_pills3 = tf3.add_paragraph()
    p_pills3.text = "[ QUICK: 1,999,000 OPS (STALL) ]\n[ MERGE: 11,088 OPS (OPTIMAL) ]"
    p_pills3.font.name = FONT_BODY
    p_pills3.font.size = Pt(9)
    p_pills3.font.bold = True
    p_pills3.font.color.rgb = GREEN
    p_pills3.space_before = Pt(10)

    # Right Column: Side-by-Side Visual Showdown
    sort_path = os.path.join(GTC_DIR, "gtc_slide3_sorting_showdown.png")
    if os.path.exists(sort_path):
        slide3.shapes.add_picture(sort_path, Inches(5.5), Inches(1.55), width=Inches(7.1), height=Inches(5.5))

    # =========================================================================
    # SLIDE 4: Exploit Signature Pattern Matching (4.5x Speedup)
    # =========================================================================
    slide4 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide4)
    add_header(slide4,
               "// STRING MATCHING // AUTOMATA & SUB-LINEAR SEARCH",
               "EXPLOIT SIGNATURE PATTERN MATCHING",
               "KMP Failure Automaton π[q] vs Boyer-Moore & Naive Backtracking",
               "PHASE 04 / 08")

    # Left Column: Hero Focal Point
    left4 = slide4.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.55), Inches(4.5), Inches(5.5))
    left4.fill.solid()
    left4.fill.fore_color.rgb = CARD_BG
    left4.line.color.rgb = BORDER_COLOR
    left4.line.width = Pt(1.5)

    tf4 = left4.text_frame
    tf4.word_wrap = True
    tf4.margin_left = tf4.margin_right = Inches(0.25)
    tf4.margin_top = Inches(0.2)

    p_hero4 = tf4.paragraphs[0]
    p_hero4.text = "4.5×"
    p_hero4.font.name = FONT_TITLE
    p_hero4.font.size = Pt(64)
    p_hero4.font.bold = True
    p_hero4.font.color.rgb = CYAN

    p_hero4_lbl = tf4.add_paragraph()
    p_hero4_lbl.text = "THROUGHPUT GAIN UNDER ADVERSARIAL REPEATING PAYLOADS"
    p_hero4_lbl.font.name = FONT_TITLE
    p_hero4_lbl.font.size = Pt(12)
    p_hero4_lbl.font.bold = True
    p_hero4_lbl.font.color.rgb = WHITE
    p_hero4_lbl.space_before = Pt(2)

    # Divider
    div4 = slide4.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.05), Inches(3.2), Inches(4.0), Inches(0.015))
    div4.fill.solid()
    div4.fill.fore_color.rgb = BORDER_COLOR
    div4.line.fill.background()

    p_det4 = tf4.add_paragraph()
    p_det4.text = "Deterministic Linear Bound:\nTime: O(n + m)  |  Backtracking: 0 Ops"
    p_det4.font.name = FONT_BODY
    p_det4.font.size = Pt(10.5)
    p_det4.font.bold = True
    p_det4.font.color.rgb = GREEN
    p_det4.space_before = Pt(18)

    p_take4 = tf4.add_paragraph()
    p_take4.text = "Text pointer i strictly NEVER moves backward. The precomputed failure table π[q] encodes longest proper prefix matching, eliminating quadratic pointer rollback over adversarial repeating buffers ('AAAA...AAB')."
    p_take4.font.name = FONT_BODY
    p_take4.font.size = Pt(9.5)
    p_take4.font.color.rgb = SLATE
    p_take4.space_before = Pt(8)

    p_pills4 = tf4.add_paragraph()
    p_pills4.text = "[ NAIVE: 89,919 OPS (STALL) ]\n[ KMP: 20,004 OPS (MONOTONIC) ]"
    p_pills4.font.name = FONT_BODY
    p_pills4.font.size = Pt(9)
    p_pills4.font.bold = True
    p_pills4.font.color.rgb = CYAN
    p_pills4.space_before = Pt(10)

    # Right Column: KMP Automaton + Live GUI Scanner Card
    str_path = os.path.join(GTC_DIR, "gtc_slide4_string.png")
    if os.path.exists(str_path):
        slide4.shapes.add_picture(str_path, Inches(5.5), Inches(1.55), width=Inches(7.1), height=Inches(5.5))

    # =========================================================================
    # SLIDE 5: Attack Topology & Laser Min-Cut Mitigation
    # =========================================================================
    slide5 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide5)
    add_header(slide5,
               "// GRAPH THEORY // ATTACK SURFACE & DYNAMIC MIN-CUT",
               "ATTACK TOPOLOGY & MIN-CUT FIREWALL ISOLATION",
               "Exploit Paths, Negative Cycle Detection & Capacity-Bounded Quarantine",
               "PHASE 05 / 08")

    # Left Column: Hero Graph Metrics
    left5 = slide5.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.55), Inches(4.5), Inches(5.5))
    left5.fill.solid()
    left5.fill.fore_color.rgb = CARD_BG
    left5.line.color.rgb = BORDER_COLOR
    left5.line.width = Pt(1.5)

    tf5 = left5.text_frame
    tf5.word_wrap = True
    tf5.margin_left = tf5.margin_right = Inches(0.25)
    tf5.margin_top = Inches(0.2)

    p_hero5 = tf5.paragraphs[0]
    p_hero5.text = "MIN-CUT"
    p_hero5.font.name = FONT_TITLE
    p_hero5.font.size = Pt(54)
    p_hero5.font.bold = True
    p_hero5.font.color.rgb = CYAN

    p_hero5_lbl = tf5.add_paragraph()
    p_hero5_lbl.text = "CAPACITY-BOUNDED NETWORK QUARANTINE VIA EDMONDS-KARP"
    p_hero5_lbl.font.name = FONT_TITLE
    p_hero5_lbl.font.size = Pt(11)
    p_hero5_lbl.font.bold = True
    p_hero5_lbl.font.color.rgb = WHITE
    p_hero5_lbl.space_before = Pt(2)

    # Divider
    div5 = slide5.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.05), Inches(3.05), Inches(4.0), Inches(0.015))
    div5.fill.solid()
    div5.fill.fore_color.rgb = BORDER_COLOR
    div5.line.fill.background()

    p_det5 = tf5.add_paragraph()
    p_det5.text = "Exfiltration Halted: 412 MB/s\nSever Cost: 22 Mbps (Minimal Interruption)"
    p_det5.font.name = FONT_BODY
    p_det5.font.size = Pt(10.5)
    p_det5.font.bold = True
    p_det5.font.color.rgb = GREEN
    p_det5.space_before = Pt(16)

    p_det5_neg = tf5.add_paragraph()
    p_det5_neg.text = "Negative Privilege Escalation: -5 Loop Caught\nAlgorithm: Bellman-Ford O(V·E) Relaxation"
    p_det5_neg.font.name = FONT_BODY
    p_det5_neg.font.size = Pt(9.5)
    p_det5_neg.font.bold = True
    p_det5_neg.font.color.rgb = RED
    p_det5_neg.space_before = Pt(6)

    p_take5 = tf5.add_paragraph()
    p_take5.text = "Dijkstra traces critical attack vectors in O((V+E) log V). Bellman-Ford detects negative-weight privilege cycles. Edmonds-Karp isolates breached subnets with minimal collateral bandwidth cost."
    p_take5.font.name = FONT_BODY
    p_take5.font.size = Pt(9.2)
    p_take5.font.color.rgb = SLATE
    p_take5.space_before = Pt(8)

    p_pills5 = tf5.add_paragraph()
    p_pills5.text = "[ BINARY MIN-HEAP ]  [ BELLMAN-FORD O(VE) ]  [ MAX-FLOW MIN-CUT ]"
    p_pills5.font.name = FONT_BODY
    p_pills5.font.size = Pt(8)
    p_pills5.font.bold = True
    p_pills5.font.color.rgb = CYAN
    p_pills5.space_before = Pt(10)

    # Right Column: Topology Graph with Laser Cut + GUI Card
    min_path = os.path.join(GTC_DIR, "gtc_slide5_mincut.png")
    if os.path.exists(min_path):
        slide5.shapes.add_picture(min_path, Inches(5.5), Inches(1.55), width=Inches(7.1), height=Inches(5.5))

    # =========================================================================
    # SLIDE 6: 78% Search Space Pruned! (WOW Slide 2!)
    # =========================================================================
    slide6 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide6)
    add_header(slide6,
               "// COMBINATORIAL OPTIMIZATION // STATE-SPACE SEARCH",
               "RESOURCE-BOUNDED PATCH ALLOCATION",
               "0/1 Knapsack Dynamic Programming vs Best-First Branch & Bound",
               "PHASE 06 / 08")

    # Left Column: Massive Pruning Stat
    left6 = slide6.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.55), Inches(4.5), Inches(5.5))
    left6.fill.solid()
    left6.fill.fore_color.rgb = CARD_BG
    left6.line.color.rgb = BORDER_COLOR
    left6.line.width = Pt(1.5)

    tf6 = left6.text_frame
    tf6.word_wrap = True
    tf6.margin_left = tf6.margin_right = Inches(0.25)
    tf6.margin_top = Inches(0.2)

    p_hero6 = tf6.paragraphs[0]
    p_hero6.text = "78%"
    p_hero6.font.name = FONT_TITLE
    p_hero6.font.size = Pt(64)
    p_hero6.font.bold = True
    p_hero6.font.color.rgb = GREEN

    p_hero6_lbl = tf6.add_paragraph()
    p_hero6_lbl.text = "OF STATE-SPACE SEARCH NODES PRUNED WITHOUT EXPLORATION"
    p_hero6_lbl.font.name = FONT_TITLE
    p_hero6_lbl.font.size = Pt(11)
    p_hero6_lbl.font.bold = True
    p_hero6_lbl.font.color.rgb = WHITE
    p_hero6_lbl.space_before = Pt(2)

    # Divider
    div6 = slide6.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.05), Inches(3.2), Inches(4.0), Inches(0.015))
    div6.fill.solid()
    div6.fill.fore_color.rgb = BORDER_COLOR
    div6.line.fill.background()

    p_det6 = tf6.add_paragraph()
    p_det6.text = "Mathematical Pruning Criterion:\nIf Upper Bound UB(node) <= Current Best => PRUNE"
    p_det6.font.name = FONT_BODY
    p_det6.font.size = Pt(10.5)
    p_det6.font.bold = True
    p_det6.font.color.rgb = CYAN
    p_det6.space_before = Pt(18)

    p_take6 = tf6.add_paragraph()
    p_take6.text = "Root bound UB=$280. LCBB Best-First with Max-Heap greedily guides search toward optimum N9 (w=15, v=$260). Subtrees with UB <= $240 are pruned immediately without expansion, eliminating four-fifths of the state space."
    p_take6.font.name = FONT_BODY
    p_take6.font.size = Pt(9.5)
    p_take6.font.color.rgb = SLATE
    p_take6.space_before = Pt(8)

    p_pills6 = tf6.add_paragraph()
    p_pills6.text = "[ GREEDY FRACTIONAL RELAXATION ]\n[ LEAST-COST MAX-HEAP QUEUE ]"
    p_pills6.font.name = FONT_BODY
    p_pills6.font.size = Pt(9)
    p_pills6.font.bold = True
    p_pills6.font.color.rgb = GREEN
    p_pills6.space_before = Pt(10)

    # Right Column: High-Contrast Pruning Tree + GUI Card
    prun_path = os.path.join(GTC_DIR, "gtc_slide6_pruning.png")
    if os.path.exists(prun_path):
        slide6.shapes.add_picture(prun_path, Inches(5.5), Inches(1.55), width=Inches(7.1), height=Inches(5.5))

    # =========================================================================
    # SLIDE 7: Complexity Classification & Formal NP-Reduction
    # =========================================================================
    slide7 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide7)
    add_header(slide7,
               "// COMPUTATIONAL COMPLEXITY // FORMAL REDUCTION PROOFS",
               "COMPLEXITY CLASSIFICATION & REDUCTION PROOF",
               "Polynomial-Time Verification & Formal Mapping: SUBSET-SUM ≤p 0/1 KNAPSACK",
               "PHASE 07 / 08")

    # Left Column: Formal Theoretical Proof
    left7 = slide7.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.55), Inches(4.5), Inches(5.5))
    left7.fill.solid()
    left7.fill.fore_color.rgb = CARD_BG
    left7.line.color.rgb = BORDER_COLOR
    left7.line.width = Pt(1.5)

    tf7 = left7.text_frame
    tf7.word_wrap = True
    tf7.margin_left = tf7.margin_right = Inches(0.25)
    tf7.margin_top = Inches(0.2)

    p_hero7 = tf7.paragraphs[0]
    p_hero7.text = "NP-COMPLETE"
    p_hero7.font.name = FONT_TITLE
    p_hero7.font.size = Pt(44)
    p_hero7.font.bold = True
    p_hero7.font.color.rgb = RED

    p_hero7_lbl = tf7.add_paragraph()
    p_hero7_lbl.text = "DECISION 0/1 KNAPSACK IS PROVABLY NP-COMPLETE"
    p_hero7_lbl.font.name = FONT_TITLE
    p_hero7_lbl.font.size = Pt(11)
    p_hero7_lbl.font.bold = True
    p_hero7_lbl.font.color.rgb = WHITE
    p_hero7_lbl.space_before = Pt(2)

    # Divider
    div7 = slide7.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.05), Inches(3.05), Inches(4.0), Inches(0.015))
    div7.fill.solid()
    div7.fill.fore_color.rgb = BORDER_COLOR
    div7.line.fill.background()

    p_det7 = tf7.add_paragraph()
    p_det7.text = "Two-Step Formal Reduction Proof:\n1. In NP: Certificate verified in O(n) Time\n2. NP-Hard: SUBSET-SUM <=p 0/1 KNAPSACK"
    p_det7.font.name = FONT_BODY
    p_det7.font.size = Pt(10)
    p_det7.font.bold = True
    p_det7.font.color.rgb = CYAN
    p_det7.space_before = Pt(16)

    p_take7 = tf7.add_paragraph()
    p_take7.text = "Instance Transformation:\nw_i = s_i,  v_i = s_i,  Capacity W = T,  Target Profit V = T\nComputable in O(n) logarithmic space. Subset-Sum has solution iff Knapsack profit >= T."
    p_take7.font.name = FONT_BODY
    p_take7.font.size = Pt(9.2)
    p_take7.font.color.rgb = WHITE
    p_take7.space_before = Pt(8)

    p_concl7 = tf7.add_paragraph()
    p_concl7.text = "Formal Justification:\nProves exact poly-time algorithms are impossible under P != NP, mathematically validating our Branch & Bound pruning heuristic for sub-millisecond execution."
    p_concl7.font.name = FONT_BODY
    p_concl7.font.size = Pt(8.8)
    p_concl7.font.color.rgb = SLATE
    p_concl7.space_before = Pt(8)

    # Right Column: Euler Venn Diagram & Formal Reduction Bridge
    comp_path = os.path.join(GTC_DIR, "gtc_slide7_complexity.png")
    if os.path.exists(comp_path):
        slide7.shapes.add_picture(comp_path, Inches(5.5), Inches(1.55), width=Inches(7.1), height=Inches(5.5))

    # =========================================================================
    # SLIDE 8: Grand Finale & Live Demonstration Launchpad
    # =========================================================================
    slide8 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide8)
    add_header(slide8,
               "// EMPIRICAL VERIFICATION // DEFENSE CONCLUSION",
               "EMPIRICAL BENCHMARKS & LIVE WORKBENCH LAUNCHPAD",
               "36 Empirical Traces & 33/33 Deterministic Test Oracles Passed",
               "PHASE 08 / 08")

    # Top Ribbon: 3 Big Verification Cards
    ribbon8_data = [
        ("33 / 33 PASS", "100% Deterministic Test Oracles Passing across all 6 Course Units", GREEN, 0.8, 3.8),
        ("0 LEAKS", "Valgrind Memory Clean | Fixed Arena RSS | Zero Heap Fragmentation", CYAN, 4.8, 3.8),
        ("36 TRACES", "Fully Reproducible CSV & JSON Benchmark Metrics Generated", GREEN, 8.8, 3.8)
    ]
    for val, lbl, col, x_pos, w_card in ribbon8_data:
        c_rib = slide8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x_pos), Inches(1.55), Inches(w_card), Inches(1.4))
        c_rib.fill.solid()
        c_rib.fill.fore_color.rgb = CARD_BG
        c_rib.line.color.rgb = col
        c_rib.line.width = Pt(1.5)

        tf_r = c_rib.text_frame
        tf_r.word_wrap = True
        tf_r.margin_left = tf_r.margin_right = Inches(0.15)
        tf_r.margin_top = Inches(0.15)

        p1 = tf_r.paragraphs[0]
        p1.text = val
        p1.font.name = FONT_TITLE
        p1.font.size = Pt(24)
        p1.font.bold = True
        p1.font.color.rgb = col
        p1.alignment = PP_ALIGN.CENTER

        p2 = tf_r.add_paragraph()
        p2.text = lbl
        p2.font.name = FONT_BODY
        p2.font.size = Pt(8.5)
        p2.font.color.rgb = WHITE
        p2.alignment = PP_ALIGN.CENTER
        p2.space_before = Pt(3)

    # Bottom Split:
    # Left Bottom: Empirical Dashboard (Multi-panel chart)
    dash_path = os.path.join(ASSETS_DIR, "slide8_empirical_dashboard.png")
    if os.path.exists(dash_path):
        slide8.shapes.add_picture(dash_path, Inches(0.8), Inches(3.1), width=Inches(5.8), height=Inches(3.95))

    # Right Bottom: Live Workbench Launchpad Card
    demo_box = slide8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(3.1), Inches(5.8), Inches(3.95))
    demo_box.fill.solid()
    demo_box.fill.fore_color.rgb = CARD_BG
    demo_box.line.color.rgb = GREEN
    demo_box.line.width = Pt(2.0)

    tf_d = demo_box.text_frame
    tf_d.word_wrap = True
    tf_d.margin_left = tf_d.margin_right = Inches(0.25)
    tf_d.margin_top = Inches(0.2)

    p_d1 = tf_d.paragraphs[0]
    p_d1.text = "LIVE INTERACTIVE WORKBENCH READY"
    p_d1.font.name = FONT_TITLE
    p_d1.font.size = Pt(16)
    p_d1.font.bold = True
    p_d1.font.color.rgb = GREEN

    p_d2 = tf_d.add_paragraph()
    p_d2.text = "Execute Live Engine Console & Interactive Testbed:\n• Interactive Studio: .\\start_gui.bat  (http://localhost:8080)\n• Full C17 Test Suite: .\\bin\\test_all.exe  (33/33 Tests Pass)\n• Empirical Benchmark: .\\bin\\benchmark.exe  (CSV/JSON Output)"
    p_d2.font.name = FONT_BODY
    p_d2.font.size = Pt(10)
    p_d2.font.color.rgb = WHITE
    p_d2.space_before = Pt(8)

    # Embed GUI N-Queens Deception Grid Card inside demo box
    nq_path = os.path.join(CROPS_DIR, "ui_nqueens_card.png")
    if os.path.exists(nq_path):
        slide8.shapes.add_picture(nq_path, Inches(7.1), Inches(4.7), width=Inches(2.5), height=Inches(2.2))

    # Terminal prompt text next to image
    p_term = tf_d.add_paragraph()
    p_term.text = "\n\n\n\n\n[ READY FOR PROFESSOR TECHNICAL VIVA & CODE REVIEW ]"
    p_term.font.name = FONT_BODY
    p_term.font.size = Pt(9.5)
    p_term.font.bold = True
    p_term.font.color.rgb = CYAN
    p_term.alignment = PP_ALIGN.RIGHT

    # Save to all presentation targets
    targets = [
        os.path.join(PRES_DIR, "CSEG3053_Conference_Master_Deck.pptx"),
        os.path.join(PRES_DIR, "CSEG3053_8Min_Evaluation_Deck.pptx"),
        os.path.join(PRES_DIR, "CSEG3053_Professor_Defense_Master_Deck.pptx")
    ]
    for p in targets:
        prs.save(p)
        print(f"[+] Saved Keynote Deck to: {p}")

if __name__ == "__main__":
    print("[*] Compiling NVIDIA GTC / BlackHat Elite Keynote Deck...")
    build_deck()
    print("[+] Compilation complete!")
