# CSEG3053 DAA PBL: Project 03 — Cybersecurity Log Threat Detection Engine
## Week 4 Deliverable: Dynamic Programming & State Optimization

---

### 1. Executive Summary & Week 4 Scope
Week 4 focuses on **Dynamic Programming (DP)** formulations where problems exhibit **overlapping subproblems** and **optimal substructure**. In this cybersecurity engine, DP algorithms solve discrete containment trade-offs, multi-stage telemetry matrix ordering, signature indexing, behavioral kill-chain tracking, and graph-wide lateral movement exposure.

Key deliverables implemented:
1. **0/1 Knapsack DP (`knapsack_01_dp`):** Exact selection and backtracking reconstruction of containment playbooks under strict downtime budgets.
2. **Matrix Chain Multiplication (`matrix_chain_order_dp`):** Minimizing scalar operations for multi-stage correlation queries across Firewall, DNS, IAM, and EDR dimensions.
3. **Longest Common Subsequence (`lcs_attack_correlation`):** Behavioral pattern correlation aligning audit event codes with known APT kill-chain sequences.
4. **Optimal Binary Search Tree (`obst_signature_index`):** Constructing static search trees minimizing expected signature lookup cost based on historical trigger frequencies.
5. **Bellman-Ford Algorithm (`bellman_ford_escalation`):** Shortest exploit paths with negative edge weights and negative cycle detection.
6. **Floyd-Warshall Algorithm (`floyd_warshall_exposure`):** Enterprise all-pairs shortest paths and next-hop exposure matrix.
7. **Forensic Collector TSP (`tsp_held_karp_dp`):** Exact Held-Karp bitmask DP ($O(n^2 2^n)$) for visiting all compromised hosts.

---

### 2. Recurrence Formulations & State Space

#### 2.1 0/1 Containment Knapsack
Let $dp[i][w]$ be the maximum risk mitigated using a subset of the first $i$ playbooks under downtime budget $w$:
$$dp[i][w] = \begin{cases}
dp[i-1][w] & \text{if } w_i > w \\
\max\left(dp[i-1][w], \; dp[i-1][w - w_i] + v_i\right) & \text{if } w_i \le w
\end{cases}$$
* Space Complexity: $O(n W)$ via dynamic allocation with tracked memory.
* Time Complexity: $\Theta(n W)$ pseudo-polynomial time.

#### 2.2 Matrix Chain Parenthesization
Let $m[i][j]$ be the minimum scalar multiplications needed to compute $A_{i..j}$:
$$m[i][j] = \begin{cases}
0 & \text{if } i = j \\
\min_{i \le k < j} \left(m[i][k] + m[k+1][j] + p_{i-1} p_k p_j\right) & \text{if } i < j
\end{cases}$$
* Time Complexity: $\Theta(n^3)$ via bottom-up chain-length tabulation.

#### 2.3 Longest Common Subsequence (Kill-Chain Alignment)
Let $L[i][j]$ be the length of the LCS between observed events $X[1..i]$ and APT pattern $Y[1..j]$:
$$L[i][j] = \begin{cases}
0 & \text{if } i = 0 \text{ or } j = 0 \\
L[i-1][j-1] + 1 & \text{if } X[i] = Y[j] \\
\max(L[i-1][j], L[i][j-1]) & \text{if } X[i] \ne Y[j]
\end{cases}$$

#### 2.4 Held-Karp Bitmask DP for Forensic Collector TSP
Let $dp[mask][u]$ represent the minimum cost of visiting the subset of hosts in $mask$ (where bit $i$ is set if host $i$ has been visited), ending at host $u$:
$$dp[mask][v] = \min_{u \in mask, u \ne v} \left(dp[mask \setminus \{v\}][u] + \text{weight}(u, v)\right)$$
* Base Case: $dp[1][0] = 0$ (starting at jump-box host 0).
* Final Tour Cost: $\min_{u=1..n-1} (dp[(1 \ll n) - 1][u] + \text{weight}(u, 0))$.
* Complexity: $\Theta(n^2 2^n)$ time and $\Theta(n 2^n)$ space.

---

### 3. Empirical Metrics & Performance

| Algorithm | Paradigm | Input Size ($N$) | Comparisons | Writes / Swaps | Graph Relaxations | Memory (bytes) | Time (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **0/1 Knapsack DP** | DP | 12 items ($W=40$) | 697 | 509 | 0 | 2,132 | < 1.0 |
| **Matrix Chain Order** | DP | 5 dimensions | 20 | 10 | 0 | 0 | < 1.0 |
| **LCS Kill-Chain** | DP | $30 \times 9$ events | 297 | 297 | 0 | 0 | < 1.0 |
| **Optimal BST** | DP | 8 signatures | 120 | 59 | 0 | 0 | < 1.0 |
| **Bellman-Ford** | DP | 10 hosts | 306 | 10 | 10 | 0 | < 1.0 |
| **Floyd-Warshall** | DP | 10 hosts | 1,000 | 18 | 18 | 0 | < 1.0 |
| **TSP Held-Karp** | Bitmask DP | 12 hosts | 56,342 | 41,618 | 0 | 393,216 | 3.0 |

---

### 4. Implementation Details & Source Code Cross-Reference

* Source File: [`src/unit4_dp.c`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/src/unit4_dp.c)
* Header File: [`include/unit4_dp.h`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/include/unit4_dp.h)
* Unit Tests: Verified in [`tests/test_all.c`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/tests/test_all.c) lines 114–172 (100% passing).
