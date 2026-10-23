# CSEG3053 DAA PBL: Project 03 — Cybersecurity Log Threat Detection Engine
## Week 6 Deliverable: Network Flow, String Matching, Number Theory, & NP Reductions

---

### 1. Executive Summary & Week 6 Scope
Week 6 culminates the core algorithmic modules by implementing advanced network flow formulations, algebraic sensor telemetry, four distinct string-matching engines, and formal complexity class reductions.

Key deliverables implemented:
1. **Ford-Fulkerson / Edmonds-Karp (`ford_fulkerson_max_flow`):** BFS augmenting paths computing maximum data exfiltration flow and extracting the exact Minimum $s$-$t$ Cut firewall edges.
2. **Maximum Bipartite Matching (`max_bipartite_matching_soc`):** Incident-to-analyst assignment via augmenting paths.
3. **Chinese Remainder Theorem (`crt_reconstruct_telemetry`):** Extended Euclidean algorithm and modular inverse reconstructing global packet counters from distributed low-memory sensors.
4. **4 String-Matching Engines:**
   * Naive sliding window (`strmatch_naive`)
   * Rabin-Karp modular rolling hash with spurious hit tracking (`strmatch_rabin_karp`)
   * Finite Automaton state transition table (`strmatch_finite_automaton`)
   * Knuth-Morris-Pratt with $\pi$ LPS array (`strmatch_kmp`)
5. **Formal NP-Completeness Proofs:**
   * $\text{SUBSET-SUM} \le_p \text{0/1-CONTAINMENT-KNAPSACK}$
   * $\text{HAMILTONIAN-CYCLE} \le_p \text{FORENSIC-TSP-DECISION}$

---

### 2. Theoretical Formulations

#### 2.1 Max-Flow Min-Cut Theorem in Data Exfiltration
Let $G = (V, E)$ be a capacitated network where source $s$ is the compromised internal database and sink $t$ is the attacker's external C2 server:
$$\max |f| = \min_{(S, T)} c(S, T)$$
By finding the reachable set $S$ in the residual graph $G_f$ using BFS from $s$, the edges $(u, v)$ with $u \in S, v \notin S$ define the **Minimum $s$-$t$ Cut** — the exact minimum-capacity firewall rules to sever to completely shut down exfiltration.

#### 2.2 String-Matching Worst-Case Asymptotics

| Algorithm | Preprocessing Time | Matching Time | Space | Spurious Collision Resilient |
| :--- | :--- | :--- | :--- | :--- |
| **Naive** | None ($0$) | $O((n - m + 1) m)$ | $O(1)$ | No ($O(n \cdot m)$ on `"AAAA...B"`) |
| **Rabin-Karp** | $\Theta(m)$ | $O(n + m)$ avg, $O(n m)$ worst | $O(1)$ | Tracks collisions explicitly |
| **Finite Automaton**| $O(m \cdot |\Sigma|)$ | $\Theta(n)$ | $O(m \cdot |\Sigma|)$ | Yes (deterministic single-pass) |
| **KMP** | $\Theta(m)$ | $\Theta(n)$ | $\Theta(m)$ | Yes (strict linear guarantee) |

#### 2.3 Adversarial Payload Benchmark: Repetitive `"AAAA...AAAB"` ($N=10,000$)
* **Naive Matching:** Required **89,919 comparisons**.
* **KMP Matching:** Required only **20,004 comparisons** (a $4.5\times$ speedup).

---

### 3. Empirical Operation Counts & Benchmark Metrics

| Algorithm | Paradigm | Input Size ($N$) | Comparisons | Writes / Swaps | Graph Relaxations | Time (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Ford-Fulkerson Max Flow** | Network Flow | 10 hosts | 155 | 62 | 31 | < 1.0 |
| **Bipartite Analyst Matching**| Augmenting Paths | 12 incidents | 42 | 20 | 0 | < 1.0 |
| **CRT Telemetry Solver** | Algebraic / Euclid | 3 sensors | 3 | 3 | 0 | < 1.0 |
| **Naive String Matcher** | String Search | 1,371 chars | 1,371 | 1 | 0 | < 1.0 |
| **Rabin-Karp Rolling Hash** | Rolling Hash | 1,371 chars | 1,372 | 1,360 | 0 | < 1.0 |
| **Finite Automaton Matcher** | State Transition | 1,371 chars | 1,371 | 4,699 | 0 | < 1.0 |
| **KMP Matcher** | Prefix Function | 1,371 chars | 2,741 | 13 | 0 | < 1.0 |

---

### 4. Implementation Details & Source Code Cross-Reference

* Source File: [`src/unit6_flow_string_crt.c`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/src/unit6_flow_string_crt.c)
* Header File: [`include/unit6_flow_string_crt.h`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/include/unit6_flow_string_crt.h)
* Proofs File: [`docs/Complexity_Classes_and_NP_Reductions.md`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/docs/Complexity_Classes_and_NP_Reductions.md)
* Unit Tests: Verified in [`tests/test_all.c`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/tests/test_all.c) lines 218–268 (100% passing).
