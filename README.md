# CSEG3053 DAA PBL — Project 03: Cybersecurity Log Threat Detection Engine

[![Language](https://img.shields.io/badge/Language-Pure%20C%20(C17)-blue.svg)](#)
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

## 4. Execution & CLI Usage

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

## 5. Demonstration Scenarios Summary

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

## 6. Documentation Deliverables

* [`docs/Week1_Requirements_and_Architecture.md`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/docs/Week1_Requirements_and_Architecture.md): Formal problem statement, I/O specifications, mathematical loop invariants, edge cases, and Mermaid architecture diagrams.
* [`docs/Recurrence_Relations_and_Master_Theorem.md`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/docs/Recurrence_Relations_and_Master_Theorem.md): Step-by-step mathematical solutions of recurrences via Unrolling, Substitution, Recursion Trees, and Master Theorem (including where Master Theorem fails).
* [`docs/Complexity_Classes_and_NP_Reductions.md`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/docs/Complexity_Classes_and_NP_Reductions.md): P, NP, NP-Complete, and NP-Hard classification with formal polynomial-time reductions for Containment Knapsack and Forensic TSP.
