#!/usr/bin/env python3
"""
Extract and polish UI card assets from user uploaded screenshots.
Saves extracted cards to presentation/assets/gui_crops/
"""

import os
from PIL import Image

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOAD_DIR = r"C:\Users\spars\.gemini\antigravity\brain\3acffb33-9357-4fc8-873f-0945ed4e3252\.user_uploaded"
CROPS_DIR = os.path.join(BASE_DIR, "presentation", "assets", "gui_crops")
os.makedirs(CROPS_DIR, exist_ok=True)

# 1. Top Telemetry Banner from Image 1 (media_1795189632556_faf89e4f.jpg)
img1_path = os.path.join(UPLOAD_DIR, "media_1795189632556_faf89e4f.jpg")
if os.path.exists(img1_path):
    im1 = Image.open(img1_path)
    # Crop header and telemetry KPI cards (x: 10 to 1014, y: 5 to 142)
    telemetry_crop = im1.crop((10, 5, 1014, 142))
    telemetry_crop.save(os.path.join(CROPS_DIR, "ui_telemetry_banner.png"))
    print("[+] Saved ui_telemetry_banner.png", telemetry_crop.size)

    # Also crop the MergeSort vs QuickSort card (x: 65, y: 150, x: 355, y: 440)
    sorting_crop = im1.crop((65, 150, 355, 435))
    sorting_crop.save(os.path.join(CROPS_DIR, "ui_sorting_workbench.png"))
    print("[+] Saved ui_sorting_workbench.png", sorting_crop.size)

# 2. String Matching Scanner Card from Image 7 (media_1795189718274_bda70f84.png)
img7_path = os.path.join(UPLOAD_DIR, "media_1795189718274_bda70f84.png")
if os.path.exists(img7_path):
    im7 = Image.open(img7_path)
    # Full card crop
    im7_rgb = im7.convert("RGB")
    im7_rgb.save(os.path.join(CROPS_DIR, "ui_string_matcher_card.png"))
    print("[+] Saved ui_string_matcher_card.png", im7_rgb.size)

# 3. Ford-Fulkerson Min-Cut Card from Image 6 (media_1795189710046_cdb7763c.jpg)
img6_path = os.path.join(UPLOAD_DIR, "media_1795189710046_cdb7763c.jpg")
if os.path.exists(img6_path):
    im6 = Image.open(img6_path)
    # Left card: Ford-Fulkerson (x: 15, y: 8, x: 335, y: 468)
    ff_crop = im6.crop((15, 8, 335, 468))
    ff_crop.save(os.path.join(CROPS_DIR, "ui_mincut_card.png"))
    print("[+] Saved ui_mincut_card.png", ff_crop.size)

# 4. Dijkstra vs Bellman-Ford Card from Image 3 (media_1795189662700_a4ee9f9d.jpg)
img3_path = os.path.join(UPLOAD_DIR, "media_1795189662700_a4ee9f9d.jpg")
if os.path.exists(img3_path):
    im3 = Image.open(img3_path)
    # Middle card: Dijkstra vs Bellman-Ford (x: 380, y: 70, x: 605, y: 310)
    dijkstra_crop = im3.crop((380, 70, 605, 310))
    dijkstra_crop.save(os.path.join(CROPS_DIR, "ui_dijkstra_bellman_card.png"))
    print("[+] Saved ui_dijkstra_bellman_card.png", dijkstra_crop.size)

# 5. N-Queens Honeypot & Knapsack B&B from Image 5 (media_1795189699378_59bc1ddc.jpg)
img5_path = os.path.join(UPLOAD_DIR, "media_1795189699378_59bc1ddc.jpg")
if os.path.exists(img5_path):
    im5 = Image.open(img5_path)
    # Left card: N-Queens Deception Grid (x: 15, y: 10, x: 285, y: 365)
    nqueens_crop = im5.crop((15, 10, 285, 365))
    nqueens_crop.save(os.path.join(CROPS_DIR, "ui_nqueens_card.png"))
    print("[+] Saved ui_nqueens_card.png", nqueens_crop.size)

    # Right card: Knapsack B&B Policies (x: 590, y: 10, x: 865, y: 365)
    bb_crop = im5.crop((590, 10, 865, 365))
    bb_crop.save(os.path.join(CROPS_DIR, "ui_knapsack_bb_card.png"))
    print("[+] Saved ui_knapsack_bb_card.png", bb_crop.size)

print("[+] All UI card crops processed successfully!")
