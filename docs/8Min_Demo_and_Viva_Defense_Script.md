# CSEG3053 Project-Based Learning: 8-Minute Demo & 4-Minute Viva Defense Script
## Course Code: CSEG3053_4 | Evaluation Date: Saturday, 21 November 2026
### Project 03: Cybersecurity Log Threat Detection Engine (Pure C17)

---

## 1. EVALUATION FORMAT & TIMING BUDGET (TOTAL 12 MINUTES)

* **Part 1: Project Demonstration (Strictly 8 Minutes)**
  - 0:00 – 1:00 (1 min): Slide 1 — Problem Formulation, Objectives, and Pure C17 Constraints
  - 1:00 – 2:00 (1 min): Slide 2 — Architecture, Domain Models, and Decoupled Layout
  - 2:00 – 3:30 (1.5 min): Slide 3 — Syllabus Algorithm Selection Across 5 Paradigms
  - 3:30 – 5:00 (1.5 min): Slide 4 & Live Terminal — Comparative Analysis & Adversarial Benchmarks
  - 5:00 – 6:30 (1.5 min): Slide 6 & Web Studio — Live Demonstration of 3 Scenarios
  - 6:30 – 7:30 (1 min): Slide 5 — Mathematical Recurrence Proofs & Formal NP-Reduction
  - 7:30 – 8:00 (0.5 min): Slide 7 — Test Suite (33/33 Passed) & Conclusion
* **Part 2: Technical Viva Defense (Strictly 4 Minutes)**
  - Answering examiner questions on complexity, correctness, edge cases, and code walk-throughs.

---

## 2. SECOND-BY-SECOND VERBAL SCRIPT FOR 8-MINUTE DEMONSTRATION

### Minute 0:00 – 1:00 | Introduction & Problem Formulation (Slide 1)
**What to say:**
> "Good morning, respected evaluators. My name is [Your Name], and I am presenting Project 03: the Cybersecurity Log Threat Detection Engine for CSEG3053.
> 
> In modern Security Operations Centers, analysts are overwhelmed by tens of thousands of telemetry logs per second. Adversaries exploit algorithmic weaknesses by flooding SOCs with pathological inputs to induce quadratic $O(N^2)$ denial-of-service stalls. Furthermore, during active ransomware attacks, administrators face strict SLA downtime budgets to contain threats before critical infrastructure fails.
> 
> To solve this, I built a high-throughput threat detection engine strictly under the **C17 standard (`-std=c17 -Wall -Wextra -O2`)**. Adhering to the syllabus implementation standard, there are **strictly zero standard library shortcuts**: no `qsort`, no `bsearch`, and no `strstr`. All 25+ syllabus algorithms—from divide-and-conquer to network flow and dynamic programming—are engineered completely from scratch in pure C."

---

### Minute 1:00 – 2:00 | System Architecture & Typed Domain Models (Slide 2)
**What to say:**
> "The engine models enterprise security architecture through strictly typed C structures in `include/domain.h`:
> - `EventLog` represents discrete telemetry records with timestamps, IPs, ports, and payload text.
> - `HostNode` and `AttackGraph` model enterprise subnets as directed weighted graphs, where edge weights represent exploit resistance or privilege escalation benefits.
> - `FlowNetwork` manages residual capacities to halt data exfiltration.
> - `ContainmentPlaybook` models automated response actions with disruption costs and mitigated risk scores.
> 
> The system is fully decoupled into five layers: domain models, an operational `MetricsTracker` measuring exact comparisons, memory writes, recursive calls, and heap bytes, modular algorithmic libraries for Units II through VI, an automated 33-test assertion suite, and both a menu-driven CLI and an interactive browser-based Algorithmic Studio."

---

### Minute 2:00 – 3:30 | Algorithm Selection Across 5 Paradigms (Slide 3)
**What to say:**
> "Every algorithm in the engine maps directly to an assessed syllabus unit:
> 1. **Divide and Conquer:** I implemented MergeSort for stable chronological triage, Randomized QuickSort to defeat adversarial log floods, Binary Search for logarithmic timestamp lookups, and Kadane’s algorithm alongside Divide-and-Conquer to isolate the exact start and end timestamps of a volumetric DDoS burst. I also implemented Celebrity detection to isolate hidden C2 sinkholes in $O(N)$ comparisons.
> 2. **Greedy Methods:** Activity Selection schedules non-overlapping vulnerability scans, Interval Partitioning sizes isolated malware-detonation VMs, Fractional Knapsack allocates DPI bandwidth, and Huffman coding compresses syslog archives by ~50% with lossless recovery.
> 3. **Dynamic Programming:** 0/1 Knapsack selects discrete containment playbooks under SLA downtime crunches; Longest Common Subsequence (LCS) aligns audit logs with known APT kill-chains; and Held-Karp bitmask DP computes minimum-latency forensic collector memory dump tours.
> 4. **Backtracking & Branch-and-Bound:** $N$-Queens validates deception honeypot placements across routing slices, and Least-Cost Branch-and-Bound solves the Travelling Salesperson Problem using strictly admissible lower bounds.
> 5. **Network Flow & Strings:** Ford-Fulkerson computes maximum exfiltration capacity and extracts the exact Minimum $s$-$t$ Cut firewall links to sever, while Knuth-Morris-Pratt guarantees linear $\Theta(n)$ payload string inspection."

---

### Minute 3:30 – 5:00 | Comparative Analysis & Adversarial Showdown (Slide 4)
**What to say (Point to Benchmark Table):**
> "A core focus of DAA is understanding when theoretical worst-cases manifest in real execution:
> - **Adversarial Sorting Attack:** On an already-sorted stream of 2,000 logs, deterministic last-element QuickSort suffered worst-case $O(N^2)$ degradation, requiring **1,999,000 comparisons** and taking 33 milliseconds. In contrast, my stable MergeSort completed the same triage in just **11,088 comparisons**—a **180x speedup**!
> - **Pathological Payload Search:** When scanning repetitive malicious padding (`'AAAA...AAAB'`), naive sliding-window string matching performed **89,919 comparisons**, whereas my KMP implementation finished in only **20,004 comparisons**—a **4.5x speedup**—proving its linear $\Theta(n)$ worst-case guarantee.
> - **Knapsack Convergence:** Under a 40-minute SLA budget, 0/1 Knapsack DP, Backtracking, and all three Branch-and-Bound variants converged on the exact same optimal risk value of **230 points**. Least-Cost Branch-and-Bound evaluated the fewest state-space nodes (**9 pruned**), outperforming FIFO and LIFO.
> - **TSP Convergence:** For 12 hosts, Held-Karp Bitmask DP and Least-Cost Branch-and-Bound both arrived at the exact optimal tour cost of **281**."

---

### Minute 5:00 – 6:30 | Live Demonstration of 3 Scenarios (Slide 6 & Live Studio)
**What to do / run:**
Switch to PowerShell or the Web Studio at `http://127.0.0.1:8080` (or execute `.in\soc_engine.exe --run-all-demos`).

**What to say:**
> "I have implemented the three required operational scenarios:
> 1. **Scenario 1 (Normal Operations):** 1,000 logs are sorted and indexed; Binary Search pinpoints the target log in 9 comparisons; KMP scans payloads for SQL injection; LCS identifies a 4-stage APT progression; and Maximum Bipartite Matching assigns 8 incident tickets to certified specialists.
> 2. **Scenario 2 (Ransomware SLA Shock):** Management slashes allowable downtime from 100 minutes to 40 minutes. 0/1 Knapsack DP and Branch-and-Bound select optimal playbooks yielding 230 risk points. Bellman-Ford processes negative edge weights representing stolen credentials. Ford-Fulkerson calculates 412 MB/s exfiltration flow and identifies the exact **8 Min-Cut firewall links to sever**, immediately halting data leakage.
> 3. **Scenario 3 (Adversarial Stress):** Progresses scale from $N=100$ to $10,000$ logs, demonstrating that randomized QuickSort and KMP maintain stability under hostile traffic."

---

### Minute 6:30 – 7:30 | Recurrence Proofs & Formal NP-Reduction (Slide 5)
**What to say:**
> "Mathematically, I solved all recursive modules:
> - **MergeSort:** $T(n) = 2T(n/2) + \Theta(n)$. Since $f(n) = \Theta(n^{\log_2 2}) = \Theta(n)$, Master Theorem Case 2 applies, giving $T(n) = \Theta(n \log n)$.
> - **Strassen:** $T(N) = 7T(N/2) + \Theta(N^2)$. Critical exponent is $N^{\log_2 7} pprox N^{2.807}$. Since $f(N) = O(N^{2.807 - \epsilon})$, Master Theorem Case 1 applies, yielding $\Theta(N^{2.807})$.
> - **Why Master Theorem Fails on QuickSort:** The worst-case recurrence is $T(n) = T(n-1) + cn$. The Master Theorem cannot solve subtractive decrements ($n - 1$). Using iterative unrolling, $T(n) = T(0) + c \sum i = \Theta(n^2)$.
> - **Formal NP-Reduction:** I proved that 0/1 Knapsack is NP-Complete by reducing **Subset-Sum to Knapsack** in polynomial time $O(n)$ by setting $w_i = s_i, v_i = s_i, W = T, V = T$."

---

### Minute 7:30 – 8:00 | Test Suite & Conclusion (Slide 7)
**What to run / show:**
Run `.in	est_all.exe` in terminal. Show `TEST SUMMARY: 33 / 33 PASSED (100%)`.

**What to say:**
> "Finally, the entire repository is verified using an assertion oracle test suite covering all 6 units. All **33 out of 33 tests pass deterministically**. All code, benchmarks, CSV/JSON datasets, and documentation are committed and tagged under release **`v1.1.0`** on GitHub.
> 
> As stated in the evaluation guidelines: *A working project demonstrates what you built; your technical explanation demonstrates what you learned.* I am now ready for your technical viva questions."

---

## 3. TECHNICAL VIVA CHEAT SHEET (TOP EXAMINER QUESTIONS & WINNING ANSWERS)

### Q1: "Can you show me the code for your Least-Cost Branch-and-Bound lower bound? How do you guarantee it never prunes the optimal tour?"
**Answer:**
> "In `src/unit5_backtracking_bb.c`, the lower bounding function calculates the minimum possible cost to complete a tour. It computes the sum of the minimum outgoing edge from the current vertex plus the minimum outgoing edge from every unvisited vertex to either another unvisited vertex or the origin (Host 0).
> Because every valid Hamiltonian tour must leave each vertex exactly once, and our edge weights are non-negative, this lower bound is strictly **admissible** (it is a true mathematical under-estimate of the remaining cost). Because it never overestimates, it is impossible for the solver to prune a subtree containing the optimal tour. That is why Least-Cost Branch-and-Bound converged on the exact same optimal cost (**281**) as Held-Karp Bitmask DP."

### Q2: "Why can't you use Dijkstra's algorithm when modeling privilege escalation with negative weights?"
**Answer:**
> "Dijkstra is a greedy algorithm based on the premise that once a vertex is extracted from the min-heap, its shortest distance from the source is finalized. However, when negative edges exist—such as when compromising an Active Directory root controller lowers subsequent exploit difficulty—a path passing through that negative edge can produce a lower cumulative cost after a vertex has already been finalized. Dijkstra cannot re-relax already-visited vertices and fails.
> Therefore, in Unit IV I implemented **Bellman-Ford ($\Theta(V \cdot E)$)**, which relaxes all $|E|$ edges $|V|-1$ times and includes a $|V|$-th pass to detect negative-weight cycles (which in cybersecurity represents an infinite privilege escalation loop)."

### Q3: "Explain how your Ford-Fulkerson implementation finds the Minimum s-t Cut."
**Answer:**
> "I implemented the Edmonds-Karp variant using BFS to find augmenting paths in the residual graph until no path with positive residual capacity exists between the compromised store $s$ and external C2 sink $t$.
> At this point, by the **Max-Flow Min-Cut Theorem**, the maximum flow equals the capacity of the minimum cut. To extract the exact cut edges, I run a BFS from $s$ in the residual graph to find all reachable vertices $S$. Any edge in the original network that originates in $S$ and terminates in $V \setminus S$ and whose capacity is fully saturated belongs to the Minimum Cut. In Scenario 2, this isolates the exact 8 firewall rules needed to sever exfiltration."

### Q4: "What is the difference between Kadane's algorithm and Divide-and-Conquer for the Maximum Subarray problem?"
**Answer:**
> "Kadane's algorithm uses dynamic programming with optimal substructure: the maximum subarray ending at index $i$ is $\max(A[i], 	ext{curr\_max} + A[i])$. It runs in strictly linear time $\Theta(n)$ and $O(1)$ auxiliary space.
> The Divide-and-Conquer approach splits the array into two halves of size $n/2$, recursively finds the max subarray in the left, right, and crossing the midpoint. The crossing sum takes $\Theta(n)$, giving recurrence $T(n) = 2T(n/2) + \Theta(n) = \Theta(n \log n)$ and $O(\log n)$ stack space.
> Both algorithms yield the exact same peak burst anomaly score (sum = 15), but Kadane executes with fewer comparisons."

### Q5: "If the evaluator asks you to change the input data live during the demo, what do you do?"
**Action:**
> - In CLI: Pass custom command-line flags or edit `data_generator.c` / use the interactive menu `.in\soc_engine.exe`.
> - In Web GUI: Open `http://127.0.0.1:8080`, change the values directly in the card's input boxes (e.g., change the Downtime Budget slider from 40 to 60 mins on the Knapsack card, or enter a new target ID in Binary Search), and click the action button. The output updates live!
