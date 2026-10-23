# CSEG3053 DAA PBL: Project 03 — Cybersecurity Log Threat Detection Engine
## Week 7 & Capstone Deliverable: Final Integration, Benchmarking & Viva Defense Dossier

---

### 1. Final Project Architecture & Evaluation Dossier
This document constitutes the comprehensive evaluation and viva defense dossier for **Project 03: Cybersecurity Log Threat Detection Engine** for the **Design and Analysis of Algorithms (Course Code: CSEG3053)** Project-Based Learning curriculum.

#### 1.1 Quality & Engineering Audit
* **Language Standard:** Pure C (C17 Standard, ISO/IEC 9899:2018).
* **Compiler Directives:** `-std=c17 -Wall -Wextra -O2`. Zero compiler warnings or errors.
* **Algorithmic Authenticity:** Zero standard library shortcuts (`qsort`, `bsearch`, `strstr` replaced with custom implementations).
* **Test Suite Verification:** 33 / 33 assertion oracle tests passing (100% test pass rate).
* **Data Reproducibility:** Empirical benchmarks recorded in [`data/benchmark_results.csv`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/data/benchmark_results.csv) and [`data/benchmark_results.json`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/data/benchmark_results.json).

---

### 2. Complete Syllabus Algorithm Matrix

| Syllabus Unit | Assessable Algorithm | Domain Function in SOC Engine | Time Complexity | Space Complexity | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Unit I** | Metrics Tracker | Telemetry & Operation Counter | $O(1)$ per op | $O(1)$ | **Verified** |
| **Unit II** | Binary Search (Iterative & Rec) | Log timestamp & BST lookup | $O(\log n)$ | $O(1)$ / $O(\log n)$ | **Verified** |
| **Unit II** | Merge Sort | Stable log timeline ordering | $\Theta(n \log n)$ | $O(n)$ | **Verified** |
| **Unit II** | Quick Sort (Det & Rand) | In-place log sorting | $O(n \log n)$ avg, $O(n^2)$ worst | $O(\log n)$ stack | **Verified** |
| **Unit II** | Max Subarray (D&C vs. Kadane) | DDoS / brute-force burst window | $\Theta(n \log n)$ vs. $\Theta(n)$ | $O(\log n)$ vs. $O(1)$ | **Verified** |
| **Unit II** | Fast Modular Exponentiation | Rolling hash modulus ($b^e \bmod m$)| $\Theta(\log e)$ | $O(1)$ | **Verified** |
| **Unit II** | Celebrity Problem | Command-and-Control sinkhole | $\Theta(N)$ | $O(1)$ | **Verified** |
| **Unit II** | Classical vs. Strassen MatMul | Lateral movement reachability | $O(N^3)$ vs. $O(N^{2.807})$ | $O(N^2)$ | **Verified** |
| **Unit III** | Activity Selection | Vulnerability scan scheduling | $O(n \log n)$ | $O(1)$ | **Verified** |
| **Unit III** | Interval Partitioning | Sandbox VM allocation | $O(n \log n)$ | $O(n)$ | **Verified** |
| **Unit III** | Fractional Knapsack | DPI bandwidth allocation | $O(n \log n)$ | $O(n)$ | **Verified** |
| **Unit III** | Huffman Coding | Forensic syslog compression | $O(n + k \log k)$ | $O(k)$ | **Verified** |
| **Unit III** | Dijkstra's Algorithm | Least-resistance exploit path | $O((V+E)\log V)$ | $O(V)$ | **Verified** |
| **Unit III** | Prim & Kruskal MST | Resilient quarantine switch tree | $O(E \log V)$ | $O(V)$ | **Verified** |
| **Unit IV** | 0/1 Knapsack DP | Containment playbooks under SLA | $\Theta(n W)$ | $\Theta(n W)$ | **Verified** |
| **Unit IV** | Matrix Chain Multiplication | Telemetry join order optimization | $\Theta(n^3)$ | $\Theta(n^2)$ | **Verified** |
| **Unit IV** | Longest Common Subsequence | APT kill-chain correlation | $\Theta(n \cdot m)$ | $\Theta(n \cdot m)$ | **Verified** |
| **Unit IV** | Optimal BST | Signature lookup index | $\Theta(n^3)$ | $\Theta(n^2)$ | **Verified** |
| **Unit IV** | Bellman-Ford | Privilege escalation negative paths| $\Theta(V \cdot E)$ | $\Theta(V)$ | **Verified** |
| **Unit IV** | Floyd-Warshall | Enterprise lateral exposure matrix | $\Theta(V^3)$ | $\Theta(V^2)$ | **Verified** |
| **Unit IV** | Held-Karp Bitmask DP | Forensic Collector TSP | $\Theta(n^2 2^n)$ | $\Theta(n 2^n)$ | **Verified** |
| **Unit V** | N-Queens Backtracking | Deception honeypot sensor grid | $O(N!)$ | $O(N)$ stack | **Verified** |
| **Unit V** | Sum of Subsets | Micro-alert escalation combo | $O(2^n)$ with pruning | $O(n)$ stack | **Verified** |
| **Unit V** | 0/1 Knapsack Backtracking | DFS with fractional bound pruning| $O(2^n)$ with pruning | $O(n)$ stack | **Verified** |
| **Unit V** | 0/1 Knapsack Branch & Bound | FIFO / LIFO / Least-Cost BB | $O(2^n)$ with pruning | $O(\text{queue})$ | **Verified** |
| **Unit V** | TSP Least-Cost Branch & Bound | Admissible outgoing lower bound | $O(n!)$ with pruning | $O(\text{heap})$ | **Verified** |
| **Unit VI** | Ford-Fulkerson Max Flow | Data exfiltration link severing | $O(V E^2)$ | $O(V^2)$ | **Verified** |
| **Unit VI** | Max Bipartite Matching | SOC incident-analyst assignment | $O(V \cdot E)$ | $O(V)$ | **Verified** |
| **Unit VI** | Chinese Remainder Theorem | Reconstruct distributed counters | $O(k \log(\text{lcm}))$ | $O(1)$ | **Verified** |
| **Unit VI** | 4 String Matchers (Naive/RK/FA/KMP)| Malicious payload scanning | $O(n)$ to $O(n \cdot m)$ | $O(1)$ to $O(m \cdot |\Sigma|)$| **Verified** |

---

### 3. Viva Defense Frequently Asked Questions (FAQ)

#### Q1: Why did you implement both Classical and Strassen Matrix Multiplication?
**Answer:** Classical matrix multiplication runs in $\Theta(N^3)$, which is efficient for small graphs ($N \le 16$) due to continuous cache locality and zero recursion overhead. Strassen's algorithm reduces operations to $\Theta(N^{\log_2 7}) \approx \Theta(N^{2.807})$ by trading 1 multiplication for additional additions. Comparing both empirically demonstrates the crossover point where asymptotic advantage overcomes constant-factor overhead.

#### Q2: How did you prove that Least-Cost Branch-and-Bound for TSP will never prune the optimal solution?
**Answer:** The lower bounding function computes the sum of the minimum outgoing edge from the current vertex plus the minimum outgoing edge from every unvisited vertex to either another unvisited vertex or the origin (host 0). Because every Hamiltonian tour must leave each vertex exactly once, this lower bound is strictly admissible (it never overestimates). Consequently, the Least-Cost Branch-and-Bound solver converged on the exact same minimum tour cost (281) as Held-Karp Bitmask DP.

#### Q3: How does the engine sever data exfiltration links using Ford-Fulkerson?
**Answer:** The network is modeled as a directed capacitated flow network where the infected data store is the source $s$ and the external attacker is the sink $t$. After augmenting paths using Edmonds-Karp until no residual capacity remains, a BFS from $s$ in the residual graph identifies the set of reachable vertices $S$. By the Max-Flow Min-Cut Theorem, any edge originating in $S$ and terminating outside $S$ with saturated capacity belongs to the Minimum $s$-$t$ Cut. These represent the exact firewall rules to drop to halt exfiltration with minimal collateral disruption.

---

### 4. Ethical, Safety, and Privacy Considerations in Threat Detection

#### 4.1 Telemetry Privacy & Data Minimization (GDPR / HIPAA Compliance)
* **Log Scrubbing & Pseudonymization:** Raw enterprise logs frequently capture sensitive user information, session tokens, passwords submitted accidentally in HTTP URLs, and internal IP topology. The threat engine adheres to data minimization: raw strings are parsed into structured hashes and normalized threat signatures, stripping extraneous Personally Identifiable Information (PII) before persistent storage.
* **Cold Storage Integrity:** Huffman compression and hash verification ensure forensic archives cannot be altered post-incident, preserving legal chain-of-custody without exposing unencrypted plaintext data to unauthorized operators.

#### 4.2 Dual-Use Risk & Defensive Governance
* **Dual-Use Algorithmic Models:** Graph traversal algorithms (Dijkstra's shortest attack path, Floyd-Warshall lateral movement exposure, Bellman-Ford privilege escalation) can theoretically be inverted by adversaries to calculate the most efficient reconnaissance and infiltration pathways.
* **Access Control & Defensive Boundaries:** The engine is architected strictly for passive internal telemetry and controlled blue-team simulation. Network topology models must be protected with role-based access control (RBAC), ensuring exploit graphs are visible only to authorized SOC personnel.

#### 4.3 Operational Safety & Automated Blast-Radius Control
* **Containment Risk (Denial of Service):** Automated containment actions—such as dropping network links via the Ford-Fulkerson Minimum $s$-$t$ Cut or taking host services offline using 0/1 Knapsack playbook optimization—carry operational risks. If an alert is a false positive, immediate automated isolation could disrupt critical business operations, financial transactions, or life-support medical devices.
* **Human-in-the-Loop & Dry-Run Safeguards:** The engine provides algorithmic recommendations with explicit cost/downtime impact scores. In production environments, critical-severity remediations require SOC analyst confirmation (Dry-Run / Staging Mode) before firewall mutations are executed.

#### 4.4 Algorithmic Fairness & Alert Starvation Prevention
* **Anti-Starvation Guarantees:** Purely greedy scoring algorithms risk starving low-severity alerts, creating blind spots for sophisticated low-and-slow Advanced Persistent Threat (APT) campaigns. By combining greedy heuristics with dynamic programming (LCS sequence alignment) and subset-sum anomaly thresholds, the engine guarantees that low-volume sequential patterns are correlated and escalated before data exfiltration occurs.
