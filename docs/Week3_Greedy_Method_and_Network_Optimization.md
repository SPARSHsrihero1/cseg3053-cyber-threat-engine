# CSEG3053 DAA PBL: Project 03 — Cybersecurity Log Threat Detection Engine
## Week 3 Deliverable: Greedy Paradigm, Network Infrastructure, & Out-of-Band Resilience

---

### 1. Executive Summary & Week 3 Scope
Week 3 transitions from divide-and-conquer triage to **greedy approximation and optimization algorithms** applied to live enterprise cybersecurity defense. The primary engineering goals are:
1. **Activity Selection (`activity_selection_scans`):** Maximizing non-overlapping vulnerability scans on an inspection engine.
2. **Interval Partitioning (`interval_partition_sandboxes`):** Minimizing the allocation of isolated malware-detonation sandbox VMs for overlapping alert windows.
3. **Fractional Knapsack (`fractional_knapsack_dpi`):** Continuous resource allocation of Deep Packet Inspection (DPI) bandwidth based on threat-to-volume ratio ($v_i / w_i$).
4. **Huffman Coding (`huffman_compress_logs`, `huffman_decompress_logs`):** Construction of a custom array-based min-heap and prefix-free variable-length encoding tree to achieve lossless compression on syslog archives.
5. **Dijkstra's Algorithm (`dijkstra_attack_path`):** Single-source shortest path calculation through non-negative exploit cost graphs.
6. **Minimum Spanning Tree (Prim & Kruskal MST):** Resilient out-of-band telemetry cabling across quarantined enterprise switches, using a custom Disjoint Set Union (DSU) with union-by-rank and path compression.

---

### 2. Theoretical Foundations: Greedy-Choice Property & Optimal Substructure

#### 2.1 The Greedy-Choice Property
A global optimum can be arrived at by selecting a locally optimal (greedy) choice at each step without ever reconsidering previous choices.
* **Activity Selection:** Greedily picking the activity with the earliest finish time $f_k$ leaves the maximum possible remaining time for subsequent activities.
* **DPI Fractional Knapsack:** Greedily selecting items with the highest threat-to-bandwidth ratio $r_i = v_i / w_i$ guarantees maximum total risk mitigation under continuous capacity.
* **Huffman Coding:** Greedily merging the two lowest-frequency forest nodes iteratively generates a provably optimal prefix-free binary tree with minimum expected weighted path length.

#### 2.2 Prim's vs. Kruskal's Algorithms for Quarantine Spanning Trees
* **Prim's Algorithm:** Grows a single component from an arbitrary start node using a priority queue, selecting the minimum-weight cut edge $(u, v)$ with $u \in V_{\text{tree}}, v \notin V_{\text{tree}}$. Complexity: $O((V + E) \log V)$.
* **Kruskal's Algorithm:** Treats the graph as an edge collection, sorts all edges by weight, and greedily adds edges that do not form cycles using Disjoint Set Union (DSU). Complexity: $O(E \log E)$.

---

### 3. Empirical Operation Counts & Benchmark Metrics

The table below reflects actual empirical metrics collected by [`src/core/metrics.c`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/src/core/metrics.c):

| Algorithm | Paradigm | Input Size ($N$) | Comparisons | Swaps / Writes | Graph Relaxations | Memory Allocated (bytes) | Time (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Activity Selection** | Greedy | 6 | 15 | 18 | 0 | 0 | < 1.0 |
| **Interval Partitioning** | Greedy | 6 | 15 | 24 | 0 | 0 | < 1.0 |
| **Fractional Knapsack** | Greedy | 12 | 70 | 116 | 0 | 0 | < 1.0 |
| **Huffman Compression** | Greedy | 46 bytes | 312 | 485 | 0 | 1,472 | < 1.0 |
| **Dijkstra Attack Path** | Greedy | 10 hosts | 34 | 10 | 10 | 0 | < 1.0 |
| **Prim Quarantine MST** | Greedy | 8 switches | 54 | 19 | 12 | 0 | < 1.0 |
| **Kruskal Quarantine MST**| Greedy | 8 switches | 240 | 213 | 0 | 0 | 1.0 |

---

### 4. Implementation Details & Source Code Cross-Reference

* Source File: [`src/unit3_greedy.c`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/src/unit3_greedy.c)
* Header File: [`include/unit3_greedy.h`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/include/unit3_greedy.h)
* Unit Tests: Verified in [`tests/test_all.c`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/tests/test_all.c) lines 66–112 (100% passing).
