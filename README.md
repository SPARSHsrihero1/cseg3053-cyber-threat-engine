# CSEG3053 DAA PBL — Project 03: Cybersecurity Log Threat Detection Engine

[![Language](https://img.shields.io/badge/Language-Pure%20C%20(C17)-blue.svg)](#)
[![CI Build & Test](https://github.com/SPARSHsrihero1/cseg3053-cyber-threat-engine/actions/workflows/ci.yml/badge.svg)](https://github.com/SPARSHsrihero1/cseg3053-cyber-threat-engine/actions/workflows/ci.yml)
[![Standard](https://img.shields.io/badge/Standard--std%3Dc17-informational.svg)](#)
[![Compiler](https://img.shields.io/badge/GCC--Wall--Wextra--O2-brightgreen.svg)](#)
[![Tests](https://img.shields.io/badge/Unit%20Tests-33%2F33%20Passing%20(100%25)-success.svg)](#)
[![Course](https://img.shields.io/badge/Course-CSEG3053%20DAA-orange.svg)](#)

A high-performance Security Operations Center (SOC) telemetry and analytics engine implemented in **Strict Pure C (C17 Standard)** for the **Design and Analysis of Algorithms (Course Code: CSEG3053)** Project-Based Learning (PBL) curriculum.

The engine parses event logs, models enterprise network infrastructure through weighted/capacitated graphs, identifies anomalous attack bursts, correlates APT kill-chain sequences, optimizes containment response under SLA downtime crunch, halts data exfiltration links, and benchmarks fundamental algorithmic paradigms with zero library shortcuts.

---

## 1. Syllabus-to-Domain Mapping

| Syllabus Unit | Assessable Algorithm | Domain Function in SOC Engine | Implementation File |
| :--- | :--- | :--- | :--- |
| **Unit I** | Empirical Metrics Tracker | Track comparisons, writes, recursive calls, relaxations, pruned states, and heap allocations | [`src/core/metrics.c`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/src/core/metrics.c) |
| **Unit II** | Iterative & Recursive Binary Search | Search sorted event logs by timestamp; BST signature lookup | [`src/unit2_divide_conquer.c`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/src/unit2_divide_conquer.c) |
| **Unit II** | Merge Sort | Stable $O(n \log n)$ sorting of incoming log streams | [`src/unit2_divide_conquer.c`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/src/unit2_divide_conquer.c) |
| **Unit II** | Quick Sort (Det & Rand) | In-place log sorting; deterministic vs. randomized pivot | [`src/unit2_divide_conquer.c`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/src/unit2_divide_conquer.c) |
| **Unit II** | Maximum Subarray (D&C vs. Kadane) | Identify DDoS and brute-force surge time windows | [`src/unit2_divide_conquer.c`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/src/unit2_divide_conquer.c) |
| **Unit II** | Fast Modular Exponentiation | Rolling hash modulus and cryptographic decay scoring | [`src/unit2_divide_conquer.c`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/src/unit2_divide_conquer.c) |
| **Unit II** | Celebrity Problem | $O(N)$ identification of hidden Command-and-Control (C2) sinkhole | [`src/unit2_divide_conquer.c`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/src/unit2_divide_conquer.c) |
| **Unit II** | Classical vs. Strassen Matrix Mult | Multi-hop lateral movement reachability on transition matrices | [`src/unit2_divide_conquer.c`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/src/unit2_divide_conquer.c) |
| **Unit III** | Activity Selection | Maximize non-overlapping vulnerability scans on an engine | [`src/unit3_greedy.c`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/src/unit3_greedy.c) |
| **Unit III** | Interval Partitioning | Min isolated malware sandbox VMs for alert windows | [`src/unit3_greedy.c`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/src/unit3_greedy.c) |
| **Unit III** | Fractional Knapsack | Deep Packet Inspection (DPI) bandwidth allocation | [`src/unit3_greedy.c`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/src/unit3_greedy.c) |
| **Unit III** | Huffman Coding | Lossless forensic syslog compression and decompression | [`src/unit3_greedy.c`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/src/unit3_greedy.c) |
| **Unit III** | Dijkstra's Algorithm | Least-resistance lateral movement attack path | [`src/unit3_greedy.c`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/src/unit3_greedy.c) |
| **Unit III** | Prim & Kruskal MST | Minimum-cost resilient out-of-band quarantine spanning tree | [`src/unit3_greedy.c`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/src/unit3_greedy.c) |
| **Unit IV** | 0/1 Knapsack DP | Automated containment playbooks under SLA downtime budget | [`src/unit4_dp.c`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/src/unit4_dp.c) |
| **Unit IV** | Matrix Chain Multiplication DP | Multi-stage telemetry correlation matrix chain ordering | [`src/unit4_dp.c`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/src/unit4_dp.c) |
| **Unit IV** | Longest Common Subsequence (LCS) | Correlate audit event sequences with APT kill-chains | [`src/unit4_dp.c`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/src/unit4_dp.c) |
| **Unit IV** | Optimal Binary Search Tree (OBST) | Static frequency-optimized threat signature lookup index | [`src/unit4_dp.c`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/src/unit4_dp.c) |
| **Unit IV** | Bellman-Ford Shortest Path | Exploit pathing with negative weights and cycle detection | [`src/unit4_dp.c`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/src/unit4_dp.c) |
| **Unit IV** | Floyd-Warshall All-Pairs | Enterprise-wide lateral movement exposure matrix | [`src/unit4_dp.c`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/src/unit4_dp.c) |
| **Unit IV** | Bounded TSP Held-Karp Bitmask DP | Minimum-latency tour for automated forensic collector | [`src/unit4_dp.c`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/src/unit4_dp.c) |
| **Unit V** | N-Queens Backtracking | Deception honeypot sensor placement across network grid | [`src/unit5_backtracking_bb.c`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/src/unit5_backtracking_bb.c) |
| **Unit V** | Sum of Subsets Backtracking | Micro-alert risk score combinations reaching critical threshold | [`src/unit5_backtracking_bb.c`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/src/unit5_backtracking_bb.c) |
| **Unit V** | 0/1 Knapsack Backtracking | DFS state-space tree with fractional bound pruning | [`src/unit5_backtracking_bb.c`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/src/unit5_backtracking_bb.c) |
| **Unit V** | 0/1 Knapsack Branch & Bound | FIFO (Queue), LIFO (Stack), and LC (Priority Queue) solvers | [`src/unit5_backtracking_bb.c`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/src/unit5_backtracking_bb.c) |
| **Unit V** | TSP Least-Cost Branch & Bound | LC-BB solver using admissible outgoing edge lower bounds | [`src/unit5_backtracking_bb.c`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/src/unit5_backtracking_bb.c) |
| **Unit VI** | Ford-Fulkerson / Edmonds-Karp | Max exfiltration flow & Min $s$-$t$ Cut firewall severing | [`src/unit6_flow_string_crt.c`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/src/unit6_flow_string_crt.c) |
| **Unit VI** | Maximum Bipartite Matching | Assign security incidents to qualified SOC analysts | [`src/unit6_flow_string_crt.c`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/src/unit6_flow_string_crt.c) |
| **Unit VI** | Chinese Remainder Theorem (CRT) | Reconstruct global packet counters from distributed edge sensors | [`src/unit6_flow_string_crt.c`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/src/unit6_flow_string_crt.c) |
| **Unit VI** | 4 String Matchers (Naive, RK, FA, KMP) | Payload threat string scanning and collision tracking | [`src/unit6_flow_string_crt.c`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/src/unit6_flow_string_crt.c) |

---

## 2. Directory Layout

```text
cseg3053-cyber-threat-engine/
├── Makefile                               # Standard GNU Makefile
├── CMakeLists.txt                         # CMake 3.16+ configuration
├── build.bat                              # Windows batch build script
├── build.ps1                              # Windows PowerShell build script
├── README.md                              # Main project documentation
├── docs/
│   ├── Week1_Requirements_and_Architecture.md
│   ├── Recurrence_Relations_and_Master_Theorem.md
│   └── Complexity_Classes_and_NP_Reductions.md
├── data/
│   ├── benchmark_results.csv              # Empirical exported metrics table
│   └── benchmark_results.json             # Structured JSON benchmark results
├── include/
│   ├── domain.h                           # Core SOC structs (EventLog, AttackGraph, etc.)
│   ├── metrics.h                          # MetricsTracker & telemetry hooks
│   ├── data_generator.h                   # Synthetic & adversarial log generators
│   ├── unit2_divide_conquer.h
│   ├── unit3_greedy.h
│   ├── unit4_dp.h
│   ├── unit5_backtracking_bb.h
│   └── unit6_flow_string_crt.h
├── src/
│   ├── core/
│   │   ├── metrics.c                      # Operation counters & file exporters
│   │   └── data_generator.c               # Deterministic PRNG & attack topologies
│   ├── unit2_divide_conquer.c
│   ├── unit3_greedy.c
│   ├── unit4_dp.c
│   ├── unit5_backtracking_bb.c
│   ├── unit6_flow_string_crt.c
│   └── main.c                             # CLI console & demonstration scenarios
└── tests/
    └── test_all.c                         # Assertion-based oracle test suite (33 tests)
```

---

## 3. Build & Compilation Instructions

### Option A: Direct GCC Compilation (Zero Configuration)
Compile with strict C17 standards, all warnings enabled, and level 2 optimizations:

```bash
# Windows / Linux / macOS
gcc -std=c17 -Wall -Wextra -O2 -Iinclude \
    src/core/metrics.c src/core/data_generator.c \
    src/unit2_divide_conquer.c src/unit3_greedy.c \
    src/unit4_dp.c src/unit5_backtracking_bb.c \
    src/unit6_flow_string_crt.c src/main.c \
    -o bin/soc_engine

# Compile test suite
gcc -std=c17 -Wall -Wextra -O2 -Iinclude \
    src/core/metrics.c src/core/data_generator.c \
    src/unit2_divide_conquer.c src/unit3_greedy.c \
    src/unit4_dp.c src/unit5_backtracking_bb.c \
    src/unit6_flow_string_crt.c tests/test_all.c \
    -o bin/test_all
```

### Option B: Using Make
```bash
make all      # Builds bin/soc_engine and bin/test_all
make test     # Runs the test suite
make run      # Runs all demonstration scenarios and exports benchmarks
make clean    # Cleans build artifacts and exported data
```

### Option C: Using CMake
```bash
cmake -B build
cmake --build build --config Release
ctest --test-dir build --output-on-failure
```

---

## 4. Interactive SOC Web GUI Dashboard

In addition to the headless CLI, an interactive SOC analyst Web Dashboard is provided in `gui/`:

* **Live Attack Graph Canvas:** Visualizes network hosts, firewall boundaries, and shortest exploit paths (Dijkstra vs. Bellman-Ford).
* **Interactive Honeypot Grid:** Visualizes $N$-Queens deceptive sensor placement with step-by-step backtracking solutions.
* **Payload Scanner & Log Inspector:** Interactive comparison of Naive, Rabin-Karp, FA, and KMP string search engines.
* **Algorithmic Workbench Console:** Directly trigger and stream live execution outputs for all 6 syllabus units.

To launch the GUI:
```powershell
# Navigate to project repository
cd C:\Users\spars\.gemini\antigravity\scratch\cseg3053-cyber-threat-engine

# Start the GUI server
.\start_gui.bat
```

Alternative launch commands:
```powershell
# PowerShell script
.\start_gui.ps1

# Direct Python
python gui/server.py
```
Open your browser to `http://127.0.0.1:8080`.

---

## 5. Execution & CLI Usage

### Running Unit Tests
```bash
./bin/test_all
```
Expected output:
```text
===============================================================
TEST SUMMARY: 33 / 33 PASSED (100%)
===============================================================
```

### Running Demonstration Scenarios
```bash
# Non-interactive execution of all 3 mandatory scenarios + CSV/JSON export
./bin/soc_engine --run-all-demos

# Lab viva workbench evaluations for individual units
./bin/soc_engine --unit2
./bin/soc_engine --unit3
./bin/soc_engine --unit4
./bin/soc_engine --unit5
./bin/soc_engine --unit6

# Launch interactive SOC console
./bin/soc_engine
```

---

## 6. Demonstration Scenarios Summary

### Scenario 1: Normal SOC Operation (Baseline Triage & Signature Scanning)
* Sorts incoming event log streams using Merge Sort vs. Randomized Quick Sort.
* Evaluates Iterative vs. Recursive Binary Search and BST signature lookup.
* Scans payload text using Naive, Rabin-Karp, Finite Automaton, and KMP.
* Correlates multi-stage kill-chain sequences via LCS and assigns incidents to SOC analysts using Maximum Bipartite Matching.

### Scenario 2: Capacity / Constraint Shock (Active Ransomware Outbreak & SLA Crunch)
* Under a sudden 60% reduction in allowable downtime budget (100 min $\to$ 40 min), compares Fractional Knapsack (Greedy), 0/1 Knapsack (DP), Backtracking, and FIFO/LIFO/Least-Cost Branch & Bound for containment playbook selection.
* Computes lateral exploit paths using Dijkstra vs. Bellman-Ford (privilege escalation modeling).
* Constructs resilient out-of-band quarantine spanning tree using Prim vs. Kruskal MST.
* Halts data exfiltration by computing Ford-Fulkerson Max Flow and severing the exact Minimum $s$-$t$ Cut firewall links.

### Scenario 3: Large-Data Stress & Adversarial Inputs
* Benchmarks scale progression on $N=100$, $N=2,500$, and $N=10,000$ logs.
* Exposes $O(N^2)$ degradation of deterministic Quick Sort on already-sorted logs ($1,999,000$ comparisons) vs. stable Merge Sort ($11,088$ comparisons).
* Exposes pathological repetitive string matching (`"AAAA...AAAB"`): Naive ($89,919$ comparisons) vs. KMP ($20,004$ comparisons).
* Compares Classical $O(N^3)$ vs. Strassen $O(N^{2.807})$ matrix multiplication on host transition matrices.
* Solves Travelling Salesperson Problem (TSP) on 12 hosts using Held-Karp Bitmask DP vs. Least-Cost Branch & Bound (both reaching identical optimal tour cost: 281).

---

## 7. Weekly Project Roadmap & Submission Milestones (Oct 23 – Dec 1)

This project follows a 7-week academic trajectory culminating in the final PBL viva and practical defense on **December 1, 2026**:

| Milestone | Target Dates | Deliverable Report | Key Assessed Concepts |
| :--- | :--- | :--- | :--- |
| **Week 1** | Oct 16 – Oct 23 | [`docs/Week1_Requirements_and_Architecture.md`](docs/Week1_Requirements_and_Architecture.md) | Problem formulation, I/O schemas, loop invariants, Mermaid architecture |
| **Week 2** | Oct 24 – Oct 30 | [`docs/Week2_Algorithmic_Foundations_and_Empirical_Analysis.md`](docs/Week2_Algorithmic_Foundations_and_Empirical_Analysis.md) | Recurrences, Master Theorem limits, empirical sorting/searching benchmarks |
| **Week 3** | Oct 31 – Nov 06 | [`docs/Week3_Greedy_Method_and_Network_Optimization.md`](docs/Week3_Greedy_Method_and_Network_Optimization.md) | Dijkstra, Prim & Kruskal MST, Huffman compression, Activity Selection |
| **Week 4** | Nov 07 – Nov 13 | [`docs/Week4_Dynamic_Programming_and_State_Optimization.md`](docs/Week4_Dynamic_Programming_and_State_Optimization.md) | 0/1 Knapsack DP, Matrix Chain, LCS kill-chain, OBST, Bellman-Ford, Floyd-Warshall |
| **Week 5** | Nov 14 – Nov 20 | [`docs/Week5_Backtracking_and_Branch_and_Bound.md`](docs/Week5_Backtracking_and_Branch_and_Bound.md) | N-Queens, Sum of Subsets, Knapsack BB (FIFO/LIFO/LC), TSP LC-BB |
| **Week 6** | Nov 21 – Nov 27 | [`docs/Week6_Network_Flow_String_Matching_and_Complexity.md`](docs/Week6_Network_Flow_String_Matching_and_Complexity.md) | Edmonds-Karp Max-Flow/Min-Cut, Matching, CRT, 4 String Matchers, NP Reductions |
| **Week 7** | Nov 28 – Dec 01 | [`docs/Week7_Final_Integration_and_Defense_Dossier.md`](docs/Week7_Final_Integration_and_Defense_Dossier.md) | Full system capstone integration, 33-test oracle matrix, final viva defense FAQ |

### Theoretical Supplements & Mathematical Proofs
* [`docs/Recurrence_Relations_and_Master_Theorem.md`](docs/Recurrence_Relations_and_Master_Theorem.md): Derivations using Unrolling, Substitution, Trees, and Master Theorem.
* [`docs/Complexity_Classes_and_NP_Reductions.md`](docs/Complexity_Classes_and_NP_Reductions.md): Formal polynomial reductions ($\text{SUBSET-SUM} \le_p \text{KNAPSACK}$ and $\text{HAM-CYCLE} \le_p \text{TSP}$).

---

## 8. Ethical, Safety, & Privacy Considerations

The deployment of algorithmic cybersecurity threat detection and automated response systems involves significant ethical, legal, and operational responsibilities:

1. **Telemetry Privacy & Data Minimization:** Raw event logs ingested from corporate endpoints often contain sensitive personal data, unencrypted session cookies, and employee credentials. The engine enforces data minimization by stripping PII before persistence and hashing event identifiers.
2. **Dual-Use Safeguards:** Algorithmic routines developed for defensive gap identification (such as Dijkstra's exploit path or Floyd-Warshall reachability) possess dual-use potential if turned against external targets. The software contains strict architectural boundaries intended solely for authorized internal audit and defensive analysis.
3. **Automated Containment Safety:** Automated severing of network connections (via Max-Flow Min-Cut) or machine quarantine (via Knapsack playbooks) could inadvertently cause Denial of Service to mission-critical infrastructure (e.g., healthcare equipment or banking settlement systems). Production deployments require human-in-the-loop analyst sign-off and staged dry-run simulation modes.
4. **Algorithmic Fairness:** Alert triage must balance greedy short-term prioritization against long-term slow-and-low stealth threats to prevent alert starvation.
