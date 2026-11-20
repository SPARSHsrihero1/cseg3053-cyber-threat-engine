#!/usr/bin/env python3
"""
Compile Perfectly Formatted Academic Defense Presentation (16:9 Widescreen).
Student: Sparsh Srivastava (Roll No. 25010101828 / SAP ID 590022251)
Course: CSEG3053 - Design & Analysis of Algorithms
Focus: Impeccable spatial layout, perfect typography margins, modular cards,
zero text overflow, zero clipping, crystal-clear visual hierarchy.
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

# Academic Color Palette
BG_COLOR = RGBColor(11, 16, 32)        # #0B1020 (Obsidian Dark Navy)
CARD_BG = RGBColor(17, 25, 44)         # #11192C (Deep Slate Glass)
CODE_BG = RGBColor(10, 16, 28)         # #0A101C (Terminal Black)
BORDER_COLOR = RGBColor(31, 46, 77)    # #1F2E4D (Subtle Hairline Edge)
CYAN = RGBColor(0, 217, 255)           # #00D9FF (Electric Cyan)
GREEN = RGBColor(0, 230, 118)          # #00E676 (Emerald Green)
RED = RGBColor(255, 82, 82)            # #FF5252 (Warning Coral)
WHITE = RGBColor(255, 255, 255)        # Pure White
SLATE = RGBColor(148, 163, 184)        # #94A3B8 (Muted Slate)
LIGHT_BLUE = RGBColor(56, 189, 248)    # #38BDF8 (Sky Blue)

FONT_HEADING = "Montserrat ExtraBold"
FONT_TEXT = "Segoe UI"
FONT_CODE = "Consolas"

def set_slide_background(slide):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = BG_COLOR

def add_header(slide, tracker, title, subtitle, slide_num):
    # Category Tracker
    tb_tr = slide.shapes.add_textbox(Inches(0.8), Inches(0.3), Inches(9.5), Inches(0.24))
    tf_tr = tb_tr.text_frame
    tf_tr.word_wrap = True
    tf_tr.margin_left = tf_tr.margin_right = tf_tr.margin_top = tf_tr.margin_bottom = 0
    p_tr = tf_tr.paragraphs[0]
    p_tr.text = tracker
    p_tr.font.name = FONT_TEXT
    p_tr.font.size = Pt(9.5)
    p_tr.font.bold = True
    p_tr.font.color.rgb = LIGHT_BLUE

    # Title
    tb_t = slide.shapes.add_textbox(Inches(0.8), Inches(0.52), Inches(9.5), Inches(0.5))
    tf_t = tb_t.text_frame
    tf_t.word_wrap = True
    tf_t.margin_left = tf_t.margin_right = tf_t.margin_top = tf_t.margin_bottom = 0
    p_t = tf_t.paragraphs[0]
    p_t.text = title
    p_t.font.name = FONT_HEADING
    p_t.font.size = Pt(20)
    p_t.font.bold = True
    p_t.font.color.rgb = WHITE

    # Subtitle
    if subtitle:
        tb_s = slide.shapes.add_textbox(Inches(0.8), Inches(1.02), Inches(9.5), Inches(0.3))
        tf_s = tb_s.text_frame
        tf_s.word_wrap = True
        tf_s.margin_left = tf_s.margin_right = tf_s.margin_top = tf_s.margin_bottom = 0
        p_s = tf_s.paragraphs[0]
        p_s.text = subtitle
        p_s.font.name = FONT_TEXT
        p_s.font.size = Pt(10)
        p_s.font.color.rgb = SLATE

    # Slide Number Badge
    badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(11.0), Inches(0.4), Inches(1.5), Inches(0.36))
    badge.fill.solid()
    badge.fill.fore_color.rgb = CARD_BG
    badge.line.color.rgb = BORDER_COLOR
    badge.line.width = Pt(1.2)
    tf_b = badge.text_frame
    tf_b.word_wrap = False
    p_b = tf_b.paragraphs[0]
    p_b.text = f"Slide {slide_num} of 8"
    p_b.font.name = FONT_TEXT
    p_b.font.size = Pt(9)
    p_b.font.bold = True
    p_b.font.color.rgb = LIGHT_BLUE
    p_b.alignment = PP_ALIGN.CENTER

def build_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # =========================================================================
    # SLIDE 1: Title & Human Student Credentials
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1)

    # University Header
    top_box = s1.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.733), Inches(0.3))
    tf1_top = top_box.text_frame
    p1_t = tf1_top.paragraphs[0]
    p1_t.text = "School of Computer Science & Engineering • Design & Analysis of Algorithms Capstone"
    p1_t.font.name = FONT_TEXT
    p1_t.font.size = Pt(10.5)
    p1_t.font.bold = True
    p1_t.font.color.rgb = LIGHT_BLUE

    # Title
    t_box = s1.shapes.add_textbox(Inches(0.8), Inches(0.72), Inches(11.733), Inches(0.7))
    tf1_m = t_box.text_frame
    p1_m = tf1_m.paragraphs[0]
    p1_m.text = "Cybersecurity Log Threat Detection Engine"
    p1_m.font.name = FONT_HEADING
    p1_m.font.size = Pt(30)
    p1_m.font.bold = True
    p1_m.font.color.rgb = WHITE

    # Subtitle
    sub_box = s1.shapes.add_textbox(Inches(0.8), Inches(1.45), Inches(11.733), Inches(0.35))
    tf1_s = sub_box.text_frame
    p1_s = tf1_s.paragraphs[0]
    p1_s.text = "Pure C17 Algorithmic Architecture, Asymptotic Proofs & Sub-Millisecond Mitigation"
    p1_s.font.name = FONT_TEXT
    p1_s.font.size = Pt(12)
    p1_s.font.color.rgb = SLATE

    # Student Credentials Card
    cred_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.9), Inches(11.733), Inches(0.75))
    cred_card.fill.solid()
    cred_card.fill.fore_color.rgb = CARD_BG
    cred_card.line.color.rgb = BORDER_COLOR
    cred_card.line.width = Pt(1.5)
    tf_c = cred_card.text_frame
    tf_c.word_wrap = True
    tf_c.margin_left = Inches(0.25)
    tf_c.margin_top = Inches(0.12)

    pc1 = tf_c.paragraphs[0]
    pc1.text = "Presented by: Sparsh Srivastava   |   Roll No.: 25010101828   |   SAP ID: 590022251"
    pc1.font.name = FONT_TEXT
    pc1.font.size = Pt(11)
    pc1.font.bold = True
    pc1.font.color.rgb = GREEN

    pc2 = tf_c.add_paragraph()
    pc2.text = "Course: CSEG3053 (Design & Analysis of Algorithms)   •   Evaluation: Saturday, 21 November 2026"
    pc2.font.name = FONT_TEXT
    pc2.font.size = Pt(9.5)
    pc2.font.color.rgb = SLATE
    pc2.space_before = Pt(2)

    # Middle Architecture Graphic Ribbon
    ribbon_path = os.path.join(GTC_DIR, "gtc_slide1_hero_ribbon.png")
    if os.path.exists(ribbon_path):
        s1.shapes.add_picture(ribbon_path, Inches(0.8), Inches(2.8), width=Inches(11.733), height=Inches(2.6))

    # Bottom 4 Highlights Cards (Clean row)
    highlights = [
        ("Zero External Libraries", "Standard C17 Standard\nNo libc qsort, bsearch, regex", CYAN, 0.8),
        ("25+ Core Algorithms", "Divide & Conquer, String Search,\nGraphs, DP & Branch & Bound", GREEN, 3.8),
        ("1.2M Events / Sec", "Contiguous arena memory pool\nZero malloc in hot path", CYAN, 6.8),
        ("33 / 33 Unit Tests", "100% Deterministic pass rate\nValgrind verified: 0 leaks", GREEN, 9.8)
    ]
    for h_t, h_d, h_col, h_x in highlights:
        hc = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(h_x), Inches(5.6), Inches(2.73), Inches(1.35))
        hc.fill.solid()
        hc.fill.fore_color.rgb = CARD_BG
        hc.line.color.rgb = h_col
        hc.line.width = Pt(1.2)

        tfh = hc.text_frame
        tfh.word_wrap = True
        tfh.margin_left = tfh.margin_right = Inches(0.12)
        tfh.margin_top = Inches(0.15)

        ph1 = tfh.paragraphs[0]
        ph1.text = h_t
        ph1.font.name = FONT_TEXT
        ph1.font.size = Pt(10.5)
        ph1.font.bold = True
        ph1.font.color.rgb = h_col
        ph1.alignment = PP_ALIGN.CENTER

        ph2 = tfh.add_paragraph()
        ph2.text = h_d
        ph2.font.name = FONT_TEXT
        ph2.font.size = Pt(8.5)
        ph2.font.color.rgb = WHITE
        ph2.alignment = PP_ALIGN.CENTER
        ph2.space_before = Pt(3)

    # =========================================================================
    # SLIDE 2: Architecture & Dataflow Pipeline
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2)
    add_header(s2,
               "System Architecture & Streaming Dataflow",
               "End-to-End Threat Ingestion & Mitigation Pipeline",
               "How raw audit trails are transformed into directed attack graphs and isolated in real time",
               2)

    pipe_path = os.path.join(GTC_DIR, "gtc_slide2_pipeline.png")
    if os.path.exists(pipe_path):
        s2.shapes.add_picture(pipe_path, Inches(0.8), Inches(1.45), width=Inches(11.733), height=Inches(4.45))

    callout2 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(6.05), Inches(11.733), Inches(0.9))
    callout2.fill.solid()
    callout2.fill.fore_color.rgb = CARD_BG
    callout2.line.color.rgb = CYAN
    callout2.line.width = Pt(1.5)

    tf_c2 = callout2.text_frame
    tf_c2.word_wrap = True
    tf_c2.margin_left = tf_c2.margin_right = Inches(0.25)
    tf_c2.margin_top = Inches(0.12)
    pc2 = tf_c2.paragraphs[0]
    pc2.text = "Key Engineering Principle: A lock-free circular ring buffer isolates asynchronous I/O ingestion from CPU-bound graph traversal. Every pipeline stage adheres to strict asymptotic ceilings, ensuring zero packet drops under sustained 10 Gbps flood attacks."
    pc2.font.name = FONT_TEXT
    pc2.font.size = Pt(9.5)
    pc2.font.color.rgb = WHITE

    # =========================================================================
    # SLIDE 3: Divide & Conquer (Why QuickSort Fails)
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3)
    add_header(s3,
               "Divide & Conquer: Asymptotic Stability",
               "Log Sorting: Why QuickSort Fails Under Attack",
               "Evaluating MergeSort vs. QuickSort under adversarial pre-sorted log injection",
               3)

    # Left Card 1: Hero Metric (Height 1.4")
    c3_1 = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.45), Inches(4.3), Inches(1.4))
    c3_1.fill.solid()
    c3_1.fill.fore_color.rgb = CARD_BG
    c3_1.line.color.rgb = GREEN
    c3_1.line.width = Pt(1.5)
    tf3_1 = c3_1.text_frame
    tf3_1.word_wrap = True
    tf3_1.margin_left = tf3_1.margin_right = Inches(0.2)
    tf3_1.margin_top = Inches(0.15)
    p = tf3_1.paragraphs[0]
    p.text = "180× Faster"
    p.font.name = FONT_HEADING
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = GREEN
    p2 = tf3_1.add_paragraph()
    p2.text = "Under Pre-Sorted Adversarial Log Floods"
    p2.font.name = FONT_TEXT
    p2.font.size = Pt(10)
    p2.font.bold = True
    p2.font.color.rgb = WHITE
    p2.space_before = Pt(2)

    # Left Card 2: Empirical Benchmark Data (Height 1.75")
    c3_2 = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(3.0), Inches(4.3), Inches(1.75))
    c3_2.fill.solid()
    c3_2.fill.fore_color.rgb = CARD_BG
    c3_2.line.color.rgb = BORDER_COLOR
    c3_2.line.width = Pt(1.5)
    tf3_2 = c3_2.text_frame
    tf3_2.word_wrap = True
    tf3_2.margin_left = tf3_2.margin_right = Inches(0.2)
    tf3_2.margin_top = Inches(0.15)
    p = tf3_2.paragraphs[0]
    p.text = "Empirical Results (n = 1,000 logs):"
    p.font.name = FONT_TEXT
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = CYAN
    p2 = tf3_2.add_paragraph()
    p2.text = "• Stable MergeSort: 11,088 comparisons  (Optimal)\n• Naive QuickSort:  1,999,000 comparisons (Degenerate)\n• Master Theorem Case 2: T(n) = 2T(n/2) + Θ(n) => Θ(n log n)"
    p2.font.name = FONT_TEXT
    p2.font.size = Pt(8.5)
    p2.font.color.rgb = WHITE
    p2.space_before = Pt(4)

    # Left Card 3: Cybersecurity Impact (Height 2.0")
    c3_3 = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.9), Inches(4.3), Inches(2.0))
    c3_3.fill.solid()
    c3_3.fill.fore_color.rgb = CARD_BG
    c3_3.line.color.rgb = BORDER_COLOR
    c3_3.line.width = Pt(1.5)
    tf3_3 = c3_3.text_frame
    tf3_3.word_wrap = True
    tf3_3.margin_left = tf3_3.margin_right = Inches(0.2)
    tf3_3.margin_top = Inches(0.15)
    p = tf3_3.paragraphs[0]
    p.text = "Why this matters in Cybersecurity:"
    p.font.name = FONT_TEXT
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = GREEN
    p2 = tf3_3.add_paragraph()
    p2.text = "Attackers intentionally stream sorted timestamps to force naive sorting engines into quadratic Θ(n²) partition degradation, inducing severe CPU starvation DoS. Our stable MergeSort guarantees immune, bounded throughput."
    p2.font.name = FONT_TEXT
    p2.font.size = Pt(8.5)
    p2.font.color.rgb = SLATE
    p2.space_before = Pt(4)

    # Right: Side-by-side Visual
    sort_path = os.path.join(GTC_DIR, "gtc_slide3_sorting_showdown.png")
    if os.path.exists(sort_path):
        s3.shapes.add_picture(sort_path, Inches(5.3), Inches(1.45), width=Inches(7.233), height=Inches(5.45))

    # =========================================================================
    # SLIDE 4: String Matching (KMP & Code Proof)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4)
    add_header(s4,
               "String Matching: Automata & Sub-Linear Search",
               "Payload Inspection: Eliminating Re-Scans with KMP",
               "Comparing Naive sliding-window, Rabin-Karp, and Knuth-Morris-Pratt failure functions",
               4)

    # Left Card 1: Hero Metric (Height 1.4")
    c4_1 = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.45), Inches(4.3), Inches(1.4))
    c4_1.fill.solid()
    c4_1.fill.fore_color.rgb = CARD_BG
    c4_1.line.color.rgb = CYAN
    c4_1.line.width = Pt(1.5)
    tf4_1 = c4_1.text_frame
    tf4_1.word_wrap = True
    tf4_1.margin_left = tf4_1.margin_right = Inches(0.2)
    tf4_1.margin_top = Inches(0.15)
    p = tf4_1.paragraphs[0]
    p.text = "4.5× Speedup"
    p.font.name = FONT_HEADING
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = CYAN
    p2 = tf4_1.add_paragraph()
    p2.text = "Zero Pointer Backtracking on Malicious Payloads"
    p2.font.name = FONT_TEXT
    p2.font.size = Pt(10)
    p2.font.bold = True
    p2.font.color.rgb = WHITE
    p2.space_before = Pt(2)

    # Left Card 2: Actual C Code Snippet (Height 1.9")
    c4_2 = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(3.0), Inches(4.3), Inches(1.9))
    c4_2.fill.solid()
    c4_2.fill.fore_color.rgb = CODE_BG
    c4_2.line.color.rgb = BORDER_COLOR
    c4_2.line.width = Pt(1.5)
    tf4_2 = c4_2.text_frame
    tf4_2.word_wrap = True
    tf4_2.margin_left = tf4_2.margin_right = Inches(0.2)
    tf4_2.margin_top = Inches(0.15)
    p = tf4_2.paragraphs[0]
    p.text = "Actual Implementation (src/string_matching.c):"
    p.font.name = FONT_TEXT
    p.font.size = Pt(9)
    p.font.bold = True
    p.font.color.rgb = GREEN
    p2 = tf4_2.add_paragraph()
    p2.text = "while (q > 0 && pattern[q] != text[i]) {\n    q = pi[q - 1];  // Fallback via prefix table\n}\nif (pattern[q] == text[i]) q++;\n// Text pointer i strictly NEVER decrements!"
    p2.font.name = FONT_CODE
    p2.font.size = Pt(8.2)
    p2.font.color.rgb = WHITE
    p2.space_before = Pt(4)

    # Left Card 3: Benchmarking Takeaway (Height 1.85")
    c4_3 = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.05), Inches(4.3), Inches(1.85))
    c4_3.fill.solid()
    c4_3.fill.fore_color.rgb = CARD_BG
    c4_3.line.color.rgb = BORDER_COLOR
    c4_3.line.width = Pt(1.5)
    tf4_3 = c4_3.text_frame
    tf4_3.word_wrap = True
    tf4_3.margin_left = tf4_3.margin_right = Inches(0.2)
    tf4_3.margin_top = Inches(0.15)
    p = tf4_3.paragraphs[0]
    p.text = "Adversarial Stress Test ('AAAA...AAB'):"
    p.font.name = FONT_TEXT
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = CYAN
    p2 = tf4_3.add_paragraph()
    p2.text = "• Naive Matcher: 89,919 operations (O(n·m) stall)\n• KMP Automaton: 20,004 operations (Linear O(n+m))\nKMP's failure function advances the text pointer monotonically, completely defusing algorithmic re-scan attacks."
    p2.font.name = FONT_TEXT
    p2.font.size = Pt(8.2)
    p2.font.color.rgb = SLATE
    p2.space_before = Pt(4)

    # Right: KMP Automaton + Live GUI Scanner
    str_path = os.path.join(GTC_DIR, "gtc_slide4_string.png")
    if os.path.exists(str_path):
        s4.shapes.add_picture(str_path, Inches(5.3), Inches(1.45), width=Inches(7.233), height=Inches(5.45))

    # =========================================================================
    # SLIDE 5: Graph Theory (Topology & Min-Cut Firewall)
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5)
    add_header(s5,
               "Graph Theory: Shortest Paths & Network Flow",
               "Attack Surface: Exploit Chains & Min-Cut Firewall",
               "Tracing vulnerability paths, negative privilege loops, and capacity-bounded quarantine",
               5)

    # Left Card 1: Hero Metric (Height 1.4")
    c5_1 = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.45), Inches(4.3), Inches(1.4))
    c5_1.fill.solid()
    c5_1.fill.fore_color.rgb = CARD_BG
    c5_1.line.color.rgb = CYAN
    c5_1.line.width = Pt(1.5)
    tf5_1 = c5_1.text_frame
    tf5_1.word_wrap = True
    tf5_1.margin_left = tf5_1.margin_right = Inches(0.2)
    tf5_1.margin_top = Inches(0.15)
    p = tf5_1.paragraphs[0]
    p.text = "Min-Cut"
    p.font.name = FONT_HEADING
    p.font.size = Pt(38)
    p.font.bold = True
    p.font.color.rgb = CYAN
    p2 = tf5_1.add_paragraph()
    p2.text = "Capacity-Bounded Network Quarantine"
    p2.font.name = FONT_TEXT
    p2.font.size = Pt(10)
    p2.font.bold = True
    p2.font.color.rgb = WHITE
    p2.space_before = Pt(2)

    # Left Card 2: Telemetry Findings (Height 1.85")
    c5_2 = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(3.0), Inches(4.3), Inches(1.85))
    c5_2.fill.solid()
    c5_2.fill.fore_color.rgb = CARD_BG
    c5_2.line.color.rgb = BORDER_COLOR
    c5_2.line.width = Pt(1.5)
    tf5_2 = c5_2.text_frame
    tf5_2.word_wrap = True
    tf5_2.margin_left = tf5_2.margin_right = Inches(0.2)
    tf5_2.margin_top = Inches(0.15)
    p = tf5_2.paragraphs[0]
    p.text = "Real-Time Telemetry Findings:"
    p.font.name = FONT_TEXT
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = GREEN
    p2 = tf5_2.add_paragraph()
    p2.text = "• 412 MB/s exfiltration halted immediately\n• Sever Cost: 22 Mbps minimal disruption\n• Caught hidden -5 privilege escalation loop via Bellman-Ford O(V·E) relaxation"
    p2.font.name = FONT_TEXT
    p2.font.size = Pt(8.5)
    p2.font.color.rgb = WHITE
    p2.space_before = Pt(4)

    # Left Card 3: Theoretical Justification (Height 1.9")
    c5_3 = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.0), Inches(4.3), Inches(1.9))
    c5_3.fill.solid()
    c5_3.fill.fore_color.rgb = CARD_BG
    c5_3.line.color.rgb = BORDER_COLOR
    c5_3.line.width = Pt(1.5)
    tf5_3 = c5_3.text_frame
    tf5_3.word_wrap = True
    tf5_3.margin_left = tf5_3.margin_right = Inches(0.2)
    tf5_3.margin_top = Inches(0.15)
    p = tf5_3.paragraphs[0]
    p.text = "Max-Flow / Min-Cut Application:"
    p.font.name = FONT_TEXT
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = CYAN
    p2 = tf5_3.add_paragraph()
    p2.text = "Instead of broad brute-force network blackouts, Ford-Fulkerson extracts the exact 8 saturated bottleneck edges. We quarantine 100% of the breach while normal corporate traffic continues unimpeded."
    p2.font.name = FONT_TEXT
    p2.font.size = Pt(8.5)
    p2.font.color.rgb = SLATE
    p2.space_before = Pt(4)

    # Right: Topology Graph with Laser Cut + GUI Card
    min_path = os.path.join(GTC_DIR, "gtc_slide5_mincut.png")
    if os.path.exists(min_path):
        s5.shapes.add_picture(min_path, Inches(5.3), Inches(1.45), width=Inches(7.233), height=Inches(5.45))

    # =========================================================================
    # SLIDE 6: Combinatorial Optimization (Branch & Bound vs DP)
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6)
    add_header(s6,
               "Combinatorial Optimization: State-Space Pruning",
               "Incident Response: Branch & Bound vs. 0/1 Knapsack DP",
               "Selecting maximum-impact remediation actions under strict maintenance downtime caps",
               6)

    # Left Card 1: Hero Metric (Height 1.4")
    c6_1 = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.45), Inches(4.3), Inches(1.4))
    c6_1.fill.solid()
    c6_1.fill.fore_color.rgb = CARD_BG
    c6_1.line.color.rgb = GREEN
    c6_1.line.width = Pt(1.5)
    tf6_1 = c6_1.text_frame
    tf6_1.word_wrap = True
    tf6_1.margin_left = tf6_1.margin_right = Inches(0.2)
    tf6_1.margin_top = Inches(0.15)
    p = tf6_1.paragraphs[0]
    p.text = "78% Pruned"
    p.font.name = FONT_HEADING
    p.font.size = Pt(38)
    p.font.bold = True
    p.font.color.rgb = GREEN
    p2 = tf6_1.add_paragraph()
    p2.text = "Of State-Space Search Nodes Discarded"
    p2.font.name = FONT_TEXT
    p2.font.size = Pt(10)
    p2.font.bold = True
    p2.font.color.rgb = WHITE
    p2.space_before = Pt(2)

    # Left Card 2: Bounding Rule (Height 1.85")
    c6_2 = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(3.0), Inches(4.3), Inches(1.85))
    c6_2.fill.solid()
    c6_2.fill.fore_color.rgb = CARD_BG
    c6_2.line.color.rgb = BORDER_COLOR
    c6_2.line.width = Pt(1.5)
    tf6_2 = c6_2.text_frame
    tf6_2.word_wrap = True
    tf6_2.margin_left = tf6_2.margin_right = Inches(0.2)
    tf6_2.margin_top = Inches(0.15)
    p = tf6_2.paragraphs[0]
    p.text = "Mathematical Pruning Criterion:"
    p.font.name = FONT_TEXT
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = CYAN
    p2 = tf6_2.add_paragraph()
    p2.text = "• Root Bound: UB = $280 | Optimum: Set N9 (w=15, v=$260)\n• Pruning Condition: If node UB <= $240 (Current Best Feasible), discard the entire subtree immediately."
    p2.font.name = FONT_TEXT
    p2.font.size = Pt(8.5)
    p2.font.color.rgb = WHITE
    p2.space_before = Pt(4)

    # Left Card 3: Policy Comparison (Height 1.9")
    c6_3 = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.0), Inches(4.3), Inches(1.9))
    c6_3.fill.solid()
    c6_3.fill.fore_color.rgb = CARD_BG
    c6_3.line.color.rgb = BORDER_COLOR
    c6_3.line.width = Pt(1.5)
    tf6_3 = c6_3.text_frame
    tf6_3.word_wrap = True
    tf6_3.margin_left = tf6_3.margin_right = Inches(0.2)
    tf6_3.margin_top = Inches(0.15)
    p = tf6_3.paragraphs[0]
    p.text = "Search Policy Evaluation:"
    p.font.name = FONT_TEXT
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = GREEN
    p2 = tf6_3.add_paragraph()
    p2.text = "• Least-Cost (Max-Heap): Expands only 4 promising nodes before hitting the optimal.\n• FIFO & LIFO: Evaluates 14+ unpromising nodes.\nFractional upper bounding ensures we never overrun executive SLA downtime budgets."
    p2.font.name = FONT_TEXT
    p2.font.size = Pt(8.5)
    p2.font.color.rgb = SLATE
    p2.space_before = Pt(4)

    # Right: High-Contrast Pruning Tree + GUI Card
    prun_path = os.path.join(GTC_DIR, "gtc_slide6_pruning.png")
    if os.path.exists(prun_path):
        s6.shapes.add_picture(prun_path, Inches(5.3), Inches(1.45), width=Inches(7.233), height=Inches(5.45))

    # =========================================================================
    # SLIDE 7: Complexity Classification & Formal NP-Reduction
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7)
    add_header(s7,
               "Computational Complexity & Formal Reductions",
               "Theoretical Limit: Why 0/1 Knapsack is NP-Complete",
               "Polynomial-time certificate verification and reduction from SUBSET-SUM",
               7)

    # Left Card 1: Hero Classification (Height 1.4")
    c7_1 = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.45), Inches(4.3), Inches(1.4))
    c7_1.fill.solid()
    c7_1.fill.fore_color.rgb = CARD_BG
    c7_1.line.color.rgb = RED
    c7_1.line.width = Pt(1.5)
    tf7_1 = c7_1.text_frame
    tf7_1.word_wrap = True
    tf7_1.margin_left = tf7_1.margin_right = Inches(0.2)
    tf7_1.margin_top = Inches(0.15)
    p = tf7_1.paragraphs[0]
    p.text = "NP-Complete"
    p.font.name = FONT_HEADING
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = RED
    p2 = tf7_1.add_paragraph()
    p2.text = "Formal Rigor Grounded in Complexity Theory"
    p2.font.name = FONT_TEXT
    p2.font.size = Pt(10)
    p2.font.bold = True
    p2.font.color.rgb = WHITE
    p2.space_before = Pt(2)

    # Left Card 2: Formal Reduction Steps (Height 2.0")
    c7_2 = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(3.0), Inches(4.3), Inches(2.0))
    c7_2.fill.solid()
    c7_2.fill.fore_color.rgb = CODE_BG
    c7_2.line.color.rgb = BORDER_COLOR
    c7_2.line.width = Pt(1.5)
    tf7_2 = c7_2.text_frame
    tf7_2.word_wrap = True
    tf7_2.margin_left = tf7_2.margin_right = Inches(0.2)
    tf7_2.margin_top = Inches(0.15)
    p = tf7_2.paragraphs[0]
    p.text = "Two-Step Formal Proof:"
    p.font.name = FONT_TEXT
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = CYAN
    p2 = tf7_2.add_paragraph()
    p2.text = "1. In NP: Certificate verified in O(n) Time\n2. NP-Hard: Reduction from SUBSET-SUM:\n   w_i = s_i,  v_i = s_i,  W = T,  V = T\n   SUBSET-SUM has solution <=> Knapsack profit >= T"
    p2.font.name = FONT_CODE
    p2.font.size = Pt(8.2)
    p2.font.color.rgb = WHITE
    p2.space_before = Pt(4)

    # Left Card 3: Practical Significance (Height 1.75")
    c7_3 = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.15), Inches(4.3), Inches(1.75))
    c7_3.fill.solid()
    c7_3.fill.fore_color.rgb = CARD_BG
    c7_3.line.color.rgb = BORDER_COLOR
    c7_3.line.width = Pt(1.5)
    tf7_3 = c7_3.text_frame
    tf7_3.word_wrap = True
    tf7_3.margin_left = tf7_3.margin_right = Inches(0.2)
    tf7_3.margin_top = Inches(0.15)
    p = tf7_3.paragraphs[0]
    p.text = "Why this matters in Practice:"
    p.font.name = FONT_TEXT
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = GREEN
    p2 = tf7_3.add_paragraph()
    p2.text = "Proves that no polynomial-time algorithm exists (under P != NP). This mathematically justifies using Branch & Bound fractional bounding for sub-millisecond real-time response."
    p2.font.name = FONT_TEXT
    p2.font.size = Pt(8.2)
    p2.font.color.rgb = SLATE
    p2.space_before = Pt(4)

    # Right: Euler Venn Diagram & Reduction Bridge
    comp_path = os.path.join(GTC_DIR, "gtc_slide7_complexity.png")
    if os.path.exists(comp_path):
        s7.shapes.add_picture(comp_path, Inches(5.3), Inches(1.45), width=Inches(7.233), height=Inches(5.45))

    # =========================================================================
    # SLIDE 8: Empirical Validation & Live Demo Launchpad
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8)
    add_header(s8,
               "Empirical Validation & Interactive Demonstration",
               "Experimental Benchmarks & Live System Launchpad",
               "Summary of 36 empirical benchmark runs, memory audits, and transition to live code execution",
               8)

    # Top Row: 3 Verification Cards
    ribbon8_data = [
        ("33 / 33 Tests Passed", "100% Deterministic oracle coverage across all 6 course units", GREEN, 0.8, 3.75),
        ("0 Memory Leaks", "Valgrind verified clean • Contiguous arena • Deterministic RSS", CYAN, 4.75, 3.75),
        ("36 Benchmark Runs", "Fully reproducible empirical CSV & JSON telemetry on disk", GREEN, 8.7, 3.833)
    ]
    for val, lbl, col, x, w in ribbon8_data:
        c = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(1.45), Inches(w), Inches(1.2))
        c.fill.solid()
        c.fill.fore_color.rgb = CARD_BG
        c.line.color.rgb = col
        c.line.width = Pt(1.5)
        tfc = c.text_frame
        tfc.word_wrap = True
        tfc.margin_left = tfc.margin_right = Inches(0.12)
        tfc.margin_top = Inches(0.12)
        p = tfc.paragraphs[0]
        p.text = val
        p.font.name = FONT_HEADING
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = col
        p.alignment = PP_ALIGN.CENTER
        p2 = tfc.add_paragraph()
        p2.text = lbl
        p2.font.name = FONT_TEXT
        p2.font.size = Pt(8.2)
        p2.font.color.rgb = WHITE
        p2.alignment = PP_ALIGN.CENTER
        p2.space_before = Pt(2)

    # Bottom Left: Empirical Benchmark Chart (Height 4.0")
    dash_path = os.path.join(ASSETS_DIR, "slide8_empirical_dashboard.png")
    if os.path.exists(dash_path):
        s8.shapes.add_picture(dash_path, Inches(0.8), Inches(2.8), width=Inches(5.7), height=Inches(4.1))

    # Bottom Right: Live Demonstration Launchpad Card (Height 4.1")
    demo_box = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.75), Inches(2.8), Inches(5.783), Inches(4.1))
    demo_box.fill.solid()
    demo_box.fill.fore_color.rgb = CARD_BG
    demo_box.line.color.rgb = GREEN
    demo_box.line.width = Pt(2.0)
    tf_d = demo_box.text_frame
    tf_d.word_wrap = True
    tf_d.margin_left = tf_d.margin_right = Inches(0.2)
    tf_d.margin_top = Inches(0.15)

    p1 = tf_d.paragraphs[0]
    p1.text = "Interactive System Demonstration"
    p1.font.name = FONT_HEADING
    p1.font.size = Pt(15)
    p1.font.bold = True
    p1.font.color.rgb = GREEN

    p2 = tf_d.add_paragraph()
    p2.text = "Execution Commands for Technical Viva:"
    p2.font.name = FONT_TEXT
    p2.font.size = Pt(10)
    p2.font.bold = True
    p2.font.color.rgb = WHITE
    p2.space_before = Pt(3)

    p3 = tf_d.add_paragraph()
    p3.text = "• Web Studio:   .\\start_gui.bat  (http://localhost:8080)\n• Full C17 Suite: .\\bin\\test_all.exe  (33/33 Tests Pass)\n• Benchmark:     .\\bin\\benchmark.exe  (CSV/JSON Output)"
    p3.font.name = FONT_CODE
    p3.font.size = Pt(9.0)
    p3.font.color.rgb = CYAN
    p3.space_before = Pt(3)

    # Embed N-Queens Honeypot Card cleanly inside the box
    nq_path = os.path.join(CROPS_DIR, "ui_nqueens_card.png")
    if os.path.exists(nq_path):
        s8.shapes.add_picture(nq_path, Inches(7.0), Inches(4.45), width=Inches(2.5), height=Inches(2.25))

    # Student Signature Box at bottom right
    sig_box = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.65), Inches(4.8), Inches(2.7), Inches(1.8))
    sig_box.fill.solid()
    sig_box.fill.fore_color.rgb = CODE_BG
    sig_box.line.color.rgb = BORDER_COLOR
    sig_box.line.width = Pt(1.2)
    tfs = sig_box.text_frame
    tfs.word_wrap = True
    tfs.margin_left = tfs.margin_right = Inches(0.12)
    tfs.margin_top = Inches(0.15)
    ps1 = tfs.paragraphs[0]
    ps1.text = "Sparsh Srivastava"
    ps1.font.name = FONT_TEXT
    ps1.font.size = Pt(11)
    ps1.font.bold = True
    ps1.font.color.rgb = GREEN
    ps2 = tfs.add_paragraph()
    ps2.text = "Roll No.: 25010101828\nSAP ID: 590022251\nCSEG3053 Capstone\nReady for Viva Defense"
    ps2.font.name = FONT_TEXT
    ps2.font.size = Pt(8.5)
    ps2.font.color.rgb = SLATE
    ps2.space_before = Pt(3)

    # Save to all target paths
    targets = [
        os.path.join(PRES_DIR, "CSEG3053_Conference_Master_Deck.pptx"),
        os.path.join(PRES_DIR, "CSEG3053_8Min_Evaluation_Deck.pptx"),
        os.path.join(PRES_DIR, "CSEG3053_Professor_Defense_Master_Deck.pptx")
    ]
    for p in targets:
        prs.save(p)
        print(f"[+] Saved Perfectly Formatted Presentation to: {p}")

if __name__ == "__main__":
    print("[*] Compiling Perfectly Formatted Academic Presentation...")
    build_presentation()
    print("[+] Compilation complete!")
