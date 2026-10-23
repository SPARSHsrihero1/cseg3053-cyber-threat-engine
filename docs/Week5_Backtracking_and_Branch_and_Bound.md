# CSEG3053 DAA PBL: Project 03 — Cybersecurity Log Threat Detection Engine
## Week 5 Deliverable: State-Space Exploration, Backtracking, & Branch-and-Bound

---

### 1. Executive Summary & Week 5 Scope
Week 5 investigates exact search strategies for **NP-Hard combinatorial optimization and constraint-satisfaction problems** where polynomial-time algorithms are unavailable. The engine evaluates:
1. **N-Queens Backtracking (`n_queens_honeypots`):** Placing deception honeypot sensors across network routing grids without interference.
2. **Sum of Subsets (`sum_of_subsets_alerts`):** Bounding pruning to find all combinations of micro-alert risk scores summing to critical incident escalation thresholds.
3. **0/1 Knapsack Backtracking (`knapsack_01_backtrack`):** Depth-first search with fractional knapsack upper-bound pruning.
4. **0/1 Knapsack Branch & Bound Variants (`knapsack_bb_fifo`, `knapsack_bb_lifo`, `knapsack_bb_lc`):** Systematic comparison of Queue (FIFO), Stack (LIFO), and Max-Heap (Least-Cost/Best-First) search policies.
5. **TSP Least-Cost Branch & Bound (`tsp_bb_lc`):** Best-First Search on the complete attack graph using admissible outgoing edge lower bounds, converging on the exact optimum (Tour Cost = 281).

---

### 2. Search Paradigm Comparison: DFS Backtracking vs. Branch & Bound

```text
+---------------------+-------------------------------+-----------------------------------------+
| Feature             | Backtracking (DFS)            | Branch & Bound (FIFO / LIFO / LC)       |
+---------------------+-------------------------------+-----------------------------------------+
| Traversal Order     | Strict Depth-First Search     | Breadth-First, Depth-First, or Priority |
| Memory Requirement  | O(depth) stack space          | O(active live nodes) heap/queue space   |
| Pruning Mechanism   | Feasibility & simple bounds   | Rigorous Lower/Upper bounding functions |
| Problem Focus       | Constraint Satisfaction / All | Optimization problems (Min / Max)       |
+---------------------+-------------------------------+-----------------------------------------+
```

#### 2.1 Branch & Bound Search Policies Evaluated

* **FIFO (First-In, First-Out):** Nodes are explored using a standard FIFO queue (Breadth-First Search). All nodes at level $k$ are expanded before level $k+1$.
* **LIFO (Last-In, First-Out):** Nodes are explored using a stack (Depth-First Search), rapidly reaching leaves to establish strong initial incumbent solutions.
* **Least-Cost / Best-First (LC-BB):** Nodes are stored in a priority queue (Max-Heap for Knapsack upper bounds, Min-Heap for TSP lower bounds). The algorithm always expands the most promising live node first.

#### 2.2 Admissible Lower Bounding for Forensic TSP
In [`src/unit5_backtracking_bb.c`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/src/unit5_backtracking_bb.c), the lower bound for partial tour $(v_0, v_1, \dots, v_k)$ is computed as:
$$\text{LowerBound} = \text{cost}(v_0 \dots v_k) + \min_{u \notin visited} w(v_k, u) + \sum_{u \notin visited} \min_{v \in (\text{unvisited} \cup \{0\}) \setminus \{u\}} w(u, v)$$
Because every valid completion must leave $v_k$ and leave every unvisited node $u$, this bound is **strictly admissible** (never overestimates the true completion cost), guaranteeing exact convergence on the global optimum without false prunes.

---

### 3. Empirical Comparative Results

#### 3.1 0/1 Containment Knapsack ($N=12$ playbooks, SLA Budget = 40 min)

| Paradigm / Strategy | Explored Nodes | Pruned States | Final Objective Value | Optimality Gap |
| :--- | :--- | :--- | :--- | :--- |
| **0/1 Knapsack DP (Gold Standard)** | Tabular | 0 | **230 pts** | 0.0% (Exact) |
| **Backtracking (DFS + Fractional Bound)**| 47 calls | 35 | **230 pts** | 0.0% (Exact) |
| **FIFO Branch & Bound (Queue)** | 57 generated | 11 | **230 pts** | 0.0% (Exact) |
| **LIFO Branch & Bound (Stack)** | 57 generated | 11 | **230 pts** | 0.0% (Exact) |
| **Least-Cost Branch & Bound (PQ)** | 57 generated | 9 | **230 pts** | 0.0% (Exact) |

#### 3.2 Travelling Salesperson Problem ($N=12$ compromised hosts)

| Solver Paradigm | Theoretical Complexity | Empirical Tour Cost | Execution Time | States Evaluated |
| :--- | :--- | :--- | :--- | :--- |
| **Held-Karp Bitmask DP** | $\Theta(n^2 2^n)$ | **281** | 3.0 ms | 41,618 memo writes |
| **Least-Cost Branch & Bound** | $O(n!)$ worst-case | **281** | 24.0 ms | 22,474 nodes pruned |

---

### 4. Implementation Details & Source Code Cross-Reference

* Source File: [`src/unit5_backtracking_bb.c`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/src/unit5_backtracking_bb.c)
* Header File: [`include/unit5_backtracking_bb.h`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/include/unit5_backtracking_bb.h)
* Unit Tests: Verified in [`tests/test_all.c`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/tests/test_all.c) lines 174–216 (100% passing).
