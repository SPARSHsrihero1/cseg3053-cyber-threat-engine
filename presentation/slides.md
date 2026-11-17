# CSEG3053: Cybersecurity Threat Detection Engine
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
* **Celebrity C2 Detection:** Identifies hidden C2 sinkholes in an $N 	imes N$ matrix in $O(N)$ comparisons.
* **Strassen Matrix Mult:** Sub-cubic $\Theta(N^{2.807})$ multi-hop lateral movement reachability.

---

## Slide 6: Mathematical Recurrence Proofs
* **Merge Sort:** $T(n) = 2T(n/2) + \Theta(n) \implies \Theta(n \log n)$ (Master Theorem Case 2).
* **Strassen MatMul:** $T(N) = 7T(N/2) + \Theta(N^2) \implies \Theta(N^{\log_2 7}) pprox \Theta(N^{2.807})$ (Master Theorem Case 1).
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
* **Reduction 1:** $	ext{SUBSET-SUM} \le_p 	ext{KNAPSACK}$ via $w_i = s_i, v_i = s_i, W = T, V = T$.
* **Reduction 2:** $	ext{HAMILTONIAN-CYCLE} \le_p 	ext{TSP}$ via edge weight 1 (in $E$) vs weight 2 (not in $E$).

---

## Slide 12: Scenario 1 — Normal SOC Operation
* **Triage & Chronology:** 1,000 logs sorted via MergeSort vs Randomized QuickSort.
* **Logarithmic Search:** Binary Search pinpoints target timestamp at Index 500 in 9 comparisons.
* **Payload Inspection:** KMP and FA scan payloads for `"UNION SELECT"`.
* **APT Correlation & Dispatch:** LCS aligns kill-chain tokens; Bipartite Matching dispatches 8 of 12 incidents to certified analysts.

---

## Slide 13: Scenario 2 — Ransomware SLA Shock
* **60% Downtime Crunch:** Allowable downtime budget slashed from 100 min $	o$ 40 min.
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
  cd C:\Users\spars\.gemini\antigravity\scratch\cseg3053-cyber-threat-engine
  .\start_gui.bat
  ```
