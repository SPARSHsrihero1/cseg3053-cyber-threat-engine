# CSEG3053 DAA PBL: Project 03 — Cybersecurity Log Threat Detection Engine
## Theoretical Complexity: Taxonomies, P vs. NP, & Formal NP-Completeness Reductions

---

### 1. Complexity Class Definitions

* **Class P (Deterministic Polynomial Time):**
  $$\text{P} = \bigcup_{k \ge 1} \text{TIME}(n^k)$$
  The set of decision problems solvable by a deterministic Turing machine in time bounded by a polynomial in the input length $n$.
* **Class NP (Nondeterministic Polynomial Time):**
  The set of decision problems for which a given candidate solution (certificate / witness $y$ of length $|y| = O(n^c)$) can be verified by a deterministic polynomial-time verification algorithm $V(x, y)$ in time $O(|x|^k)$:
  $$L \in \text{NP} \iff \exists V \in \text{P}, \; c, k \in \mathbb{N} : x \in L \iff \exists y \text{ with } |y| \le |x|^c \text{ such that } V(x, y) = 1$$
* **NP-Hard:**
  A language $L'$ is NP-Hard if every language $L \in \text{NP}$ is polynomial-time reducible to $L'$:
  $$\forall L \in \text{NP}, \quad L \le_p L'$$
* **NP-Complete (NPC):**
  A problem $L$ is NP-Complete if:
  1. $L \in \text{NP}$, and
  2. $L$ is NP-Hard ($L \in \text{NP-Hard}$).

---

### 2. Comprehensive Classification of All Engine Algorithms

| Algorithm / Problem Module | Decision / Optimization Form | Complexity Class | Theoretical Rationale & Time Bound |
| :--- | :--- | :--- | :--- |
| **Binary Search** (`unit2`) | Search key in sorted array | **P** | Solvable in $O(\log n)$ deterministic time. |
| **Merge Sort / Quick Sort** (`unit2`) | Total ordering permutation | **P** | Solvable in $O(n \log n)$ deterministic time. |
| **Kadane / Max Subarray** (`unit2`) | Maximum contiguous sum | **P** | Solvable in $O(n)$ time via dynamic programming. |
| **Strassen Matrix Mult** (`unit2`) | Matrix multiplication | **P** | Solvable in $O(n^{2.807})$ deterministic time. |
| **Activity Selection** (`unit3`) | Max non-overlapping intervals | **P** | Matroid greedy choice property; solvable in $O(n \log n)$. |
| **Interval Partitioning** (`unit3`) | Min resources for intervals | **P** | Greedy interval coloring; solvable in $O(n \log n)$. |
| **Fractional Knapsack** (`unit3`) | Continuous linear resource | **P** | Solvable in $O(n \log n)$ via greedy ratio sorting. |
| **Huffman Coding** (`unit3`) | Min redundancy prefix code | **P** | Solvable in $O(n \log n)$ via greedy min-heap tree. |
| **Dijkstra's Algorithm** (`unit3`) | Single-source shortest path | **P** | Non-negative weights; solvable in $O((V + E) \log V)$. |
| **Prim / Kruskal MST** (`unit3`) | Min-weight spanning tree | **P** | Matroid optimization; solvable in $O(E \log V)$. |
| **0/1 Knapsack DP** (`unit4`) | Discrete subset optimization | **NP-Complete (Decision)** / **NP-Hard (Opt)** | Weakly NP-Complete; pseudo-polynomial DP in $O(n W)$. |
| **Matrix Chain Multiplication** (`unit4`) | Optimal parenthesization | **P** | Solvable in $O(n^3)$ via tabular dynamic programming. |
| **Longest Common Subsequence** (`unit4`) | Kill-chain alignment | **P** | Solvable in $O(n \cdot m)$ via tabular DP. |
| **Optimal BST** (`unit4`) | Min expected search tree | **P** | Solvable in $O(n^3)$ via tabular dynamic programming. |
| **Bellman-Ford** (`unit4`) | Paths with negative weights | **P** | Solvable in $O(V \cdot E)$ deterministic time. |
| **Floyd-Warshall** (`unit4`) | All-pairs shortest paths | **P** | Solvable in $O(V^3)$ via dynamic programming. |
| **Forensic Collector TSP** (`unit4`/`unit5`) | Min-latency tour of hosts | **NP-Complete (Decision)** / **NP-Hard (Opt)** | Strongly NP-Complete; exact bitmask DP in $O(n^2 2^n)$. |
| **N-Queens Honeypots** (`unit5`) | Constraint satisfaction | **NP** | General CSP is NP-Complete; solvable via backtracking. |
| **Sum of Subsets** (`unit5`) | Exact target score partition | **NP-Complete (Decision)** | Classic Karp's 21 NP-Complete problem. |
| **Ford-Fulkerson / Edmonds-Karp** (`unit6`)| Max network flow | **P** | Solvable in $O(V E^2)$ deterministic time. |
| **Max Bipartite Matching** (`unit6`) | Maximum cardinality matching| **P** | Solvable in $O(V \cdot E)$ via augmenting paths. |
| **Chinese Remainder Theorem** (`unit6`)| Modular congruence system | **P** | Solvable in $O(k \log(\text{lcm}))$ via Extended Euclidean. |
| **KMP / FA String Matchers** (`unit6`)| Substring pattern search | **P** | Solvable in linear $O(n + m)$ deterministic time. |

---

### 3. Formal Reduction 1: $\text{SUBSET-SUM} \le_p \text{0/1-CONTAINMENT-KNAPSACK}$

We prove that the decision version of the **0/1 Containment Knapsack Problem** is **NP-Complete** by polynomial-time reduction from the known NP-Complete problem **SUBSET-SUM**.

#### 3.1 Problem Definitions
* **SUBSET-SUM (Known NP-Complete):**
  * **Instance:** A finite set of positive integers $S = \{s_1, s_2, \dots, s_n\}$ and a target integer $T \in \mathbb{N}$.
  * **Question:** Does there exist a subset $S' \subseteq S$ such that:
    $$\sum_{s_i \in S'} s_i = T$$
* **0/1-CONTAINMENT-KNAPSACK (Decision Version):**
  * **Instance:** A set of $n$ containment playbooks, each with disruption cost $w_i \in \mathbb{N}$, risk mitigated $v_i \in \mathbb{N}$, a downtime budget $W \in \mathbb{N}$, and a target risk mitigation threshold $V \in \mathbb{N}$.
  * **Question:** Does there exist a subset $I \subseteq \{1, 2, \dots, n\}$ such that:
    $$\sum_{i \in I} w_i \le W \quad \text{and} \quad \sum_{i \in I} v_i \ge V$$

#### 3.2 Membership in NP
* **Certificate:** A binary vector $x = (x_1, x_2, \dots, x_n) \in \{0, 1\}^n$ specifying whether playbook $i$ is selected.
* **Verifier:** In $O(n)$ time, compute:
  $$\text{Total Cost} = \sum_{i=1}^n x_i w_i, \quad \text{Total Value} = \sum_{i=1}^n x_i v_i$$
  Check if $\text{Total Cost} \le W$ and $\text{Total Value} \ge V$. If both hold, output $1$; otherwise output $0$.
  Since verification runs in linear time $O(n)$, $\text{0/1-CONTAINMENT-KNAPSACK} \in \text{NP}$.

#### 3.3 Polynomial-Time Reduction Construction
Given an arbitrary instance of $\text{SUBSET-SUM}$ $(S, T)$ with $S = \{s_1, \dots, s_n\}$:
1. Construct $n$ containment playbooks such that for each $i \in \{1, \dots, n\}$:
   $$w_i = s_i \quad \text{and} \quad v_i = s_i$$
2. Set the downtime budget $W = T$.
3. Set the required risk mitigation threshold $V = T$.

This transformation requires creating $n$ playbook structs and setting two scalar thresholds. The transformation runs in $O(n)$ time and $O(n)$ space, which is strictly polynomial in input size.

#### 3.4 Correctness Proof ($\iff$)
* **($\implies$) Direction:**
  Suppose $(S, T) \in \text{SUBSET-SUM}$. Then there exists $S' \subseteq S$ such that $\sum_{s_i \in S'} s_i = T$.
  Let $I = \{i \mid s_i \in S'\}$. For this playbook subset:
  $$\sum_{i \in I} w_i = \sum_{s_i \in S'} s_i = T \le W$$
  $$\sum_{i \in I} v_i = \sum_{s_i \in S'} s_i = T \ge V$$
  Thus, $I$ is a valid certificate for $\text{0/1-CONTAINMENT-KNAPSACK}$, so the instance is a YES-instance.

* **($\impliedby$) Direction:**
  Suppose the constructed knapsack instance is a YES-instance. Then there exists $I \subseteq \{1, \dots, n\}$ such that:
  $$\sum_{i \in I} w_i \le T \quad \text{and} \quad \sum_{i \in I} v_i \ge T$$
  Since $w_i = v_i = s_i$ for all $i$:
  $$\sum_{i \in I} s_i \le T \quad \text{and} \quad \sum_{i \in I} s_i \ge T \implies \sum_{i \in I} s_i = T$$
  Selecting $S' = \{s_i \mid i \in I\}$ yields a subset whose elements sum exactly to $T$. Hence, $(S, T)$ is a YES-instance of $\text{SUBSET-SUM}$.

**Conclusion:** $\text{SUBSET-SUM} \le_p \text{0/1-CONTAINMENT-KNAPSACK}$, proving that $\text{0/1-CONTAINMENT-KNAPSACK}$ is NP-Complete.

---

### 4. Formal Reduction 2: $\text{HAMILTONIAN-CYCLE} \le_p \text{FORENSIC-TSP-DECISION}$

We prove that the decision version of the **Forensic Collector Travelling Salesperson Problem (TSP)** is **NP-Complete** by polynomial-time reduction from the known NP-Complete problem **HAMILTONIAN-CYCLE**.

#### 4.1 Problem Definitions
* **HAMILTONIAN-CYCLE (Known NP-Complete):**
  * **Instance:** An undirected graph $G = (V, E)$ with $|V| = n$ vertices.
  * **Question:** Does $G$ contain a simple cycle of length $n$ that visits every vertex $v \in V$ exactly once and returns to the starting vertex?
* **FORENSIC-TSP-DECISION (Decision Version):**
  * **Instance:** A complete weighted directed graph $G' = (V', E')$ with metric/non-metric edge weights $c(u, v) \in \mathbb{N}$ and an integer cost threshold $K \in \mathbb{N}$.
  * **Question:** Does there exist a tour visiting every vertex in $V'$ exactly once and returning to the origin with total edge cost $\le K$?

#### 4.2 Membership in NP
* **Certificate:** An ordered permutation of vertices $\sigma = (v_1, v_2, \dots, v_n, v_1)$.
* **Verifier:** In $O(n)$ time:
  1. Check that all $v_i \in V'$ are distinct for $1 \le i \le n$.
  2. Compute total tour cost $C = \sum_{i=1}^{n-1} c(v_i, v_{i+1}) + c(v_n, v_1)$.
  3. Verify that $C \le K$.
  Since verification takes linear time $O(n)$, $\text{FORENSIC-TSP-DECISION} \in \text{NP}$.

#### 4.3 Polynomial-Time Reduction Construction
Given an arbitrary graph $G = (V, E)$ with $V = \{1, 2, \dots, n\}$:
1. Construct complete graph $G' = (V', E')$ where $V' = V$.
2. For every pair of distinct vertices $(u, v) \in V' \times V'$:
   $$c(u, v) = \begin{cases} 1 & \text{if } (u, v) \in E \\ 2 & \text{if } (u, v) \notin E \end{cases}$$
3. Set the target tour threshold $K = n$.

Constructing $G'$ requires setting edge costs for $\binom{n}{2} = O(n^2)$ pairs. The reduction algorithm executes in deterministic $O(n^2)$ polynomial time.

#### 4.4 Correctness Proof ($\iff$)
* **($\implies$) Direction:**
  Suppose $G$ has a Hamiltonian cycle $(v_1, v_2, \dots, v_n, v_1)$.
  Every edge $(v_i, v_{i+1}) \in E$ and $(v_n, v_1) \in E$.
  By our construction, $c(v_i, v_{i+1}) = 1$ for all $1 \le i < n$, and $c(v_n, v_1) = 1$.
  The total cost of this tour in $G'$ is:
  $$\text{Cost} = \sum_{i=1}^{n-1} 1 + 1 = n \le K$$
  Thus, $G'$ contains a tour of cost $\le K$, so $G'$ is a YES-instance of $\text{FORENSIC-TSP-DECISION}$.

* **($\impliedby$) Direction:**
  Suppose $G'$ contains a travelling salesperson tour $(v_1, v_2, \dots, v_n, v_1)$ with total cost $\le n$.
  The tour consists of exactly $n$ edges, each with cost $c(u, v) \in \{1, 2\}$.
  If any edge in the tour had cost $2$, the total cost would satisfy:
  $$\text{Cost} \ge (n - 1) \cdot 1 + 1 \cdot 2 = n + 1 > n$$
  which contradicts the premise that the tour cost is $\le n$.
  Therefore, every edge in the tour must have cost $1$.
  By definition of our construction, $c(u, v) = 1 \iff (u, v) \in E$.
  Thus, every edge in the tour is an actual edge in $G$, forming a valid simple cycle visiting every vertex in $V$ exactly once. Hence, $G$ contains a Hamiltonian cycle.

**Conclusion:** $\text{HAMILTONIAN-CYCLE} \le_p \text{FORENSIC-TSP-DECISION}$, proving that $\text{FORENSIC-TSP-DECISION}$ is NP-Complete.

---

### 5. Algorithmic Coping Strategies for NP-Hard Problems in the Workbench

Because Containment 0/1 Knapsack and Forensic TSP are NP-Hard, no algorithm can guarantee both polynomial time and optimal solutions unless $\text{P} = \text{NP}$. The engine implements complementary coping paradigms:

```text
+--------------------------------------------------------------------------------+
|                             COPING STRATEGIES                                  |
+--------------------------------------------------------------------------------+
| 1. Exact Dynamic Programming (Held-Karp DP, Knapsack 01 DP):                  |
|    - Optimal for bounded enterprise instances (N <= 16 for TSP, W <= 1000).   |
|    - Guarantees true minimum exploit and tour costs.                          |
+--------------------------------------------------------------------------------+
| 2. Branch & Bound with Admissible Lower Bounding (tsp_bb_lc, knapsack_bb_lc):  |
|    - Prunes exponentially large subtrees using tight lower bounds.             |
|    - Evaluates FIFO, LIFO, and Least-Cost exploration policies.                |
+--------------------------------------------------------------------------------+
| 3. Greedy Heuristics (Fractional Knapsack DPI Heuristic):                     |
|    - O(N log N) greedy threat-to-volume ratio sorting.                         |
|    - Provides rapid near-optimal approximations during active SLA crunch.      |
+--------------------------------------------------------------------------------+
```
