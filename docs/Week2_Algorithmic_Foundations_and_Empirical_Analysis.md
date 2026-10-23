# CSEG3053 DAA PBL: Project 03 — Cybersecurity Log Threat Detection Engine
## Week 2: Algorithmic Foundations, Asymptotic Analysis, & Empirical Benchmarking

---

### 1. Executive Summary & Week 2 Scope
During Week 2 of the CSEG3053 Project-Based Learning curriculum, the focus shifts from architectural requirements (Week 1) to the mathematical and empirical evaluation of **Algorithm Foundations, Asymptotics, Recurrence Relations, and Divide-and-Conquer Paradigms**.

This deliverable covers:
1. **Mathematical Derivations & Recurrences:** Full solutions using Iteration (Unrolling), Substitution (Induction), Recursion Trees, and the Master Theorem (CLRS 4th Ed.).
2. **Analysis of Master Theorem Failure:** Mathematical demonstration of why the Master Theorem fails on worst-case Quick Sort and subtractive recurrences.
3. **Empirical Benchmarks:** Quantitative comparison of operation counters (`comparisons`, `swaps_or_writes`, `recursive_calls`, `elapsed_ms`) across Small ($N=100$), Medium ($N=2,500$), Large ($N=10,000$), and Adversarial datasets.
4. **Verification of Divide-and-Conquer Algorithms:** Merge Sort, Randomized vs. Deterministic Quick Sort, Binary Search, Maximum Subarray (Kadane vs. D&C), Fast Modular Exponentiation, $O(N)$ Celebrity C2 Sinkhole Detection, and Strassen's Matrix Multiplication.

---

### 2. Recurrence Relations & Asymptotic Solutions

#### 2.1 Summary of Evaluated Recurrences

| Algorithm | Paradigm | Recurrence Relation | Solving Method | Asymptotic Bound |
| :--- | :--- | :--- | :--- | :--- |
| **Binary Search** | Divide & Conquer | $T(n) = T(n/2) + \Theta(1)$ | Master Theorem (Case 2, $k=0$) | $\Theta(\log n)$ |
| **Merge Sort** | Divide & Conquer | $T(n) = 2T(n/2) + \Theta(n)$ | Master Theorem / Recursion Tree | $\Theta(n \log n)$ |
| **Quick Sort (Best)** | Divide & Conquer | $T(n) = 2T(n/2) + \Theta(n)$ | Master Theorem (Case 2, $k=0$) | $\Theta(n \log n)$ |
| **Quick Sort (Worst)**| Divide & Conquer | $T(n) = T(n-1) + \Theta(n)$ | Unrolling (Master Theorem fails) | $\Theta(n^2)$ |
| **Max Subarray (D&C)**| Divide & Conquer | $T(n) = 2T(n/2) + \Theta(n)$ | Master Theorem (Case 2, $k=0$) | $\Theta(n \log n)$ |
| **Fast Exponentiation**| Divide & Conquer | $T(e) = T(e/2) + \Theta(1)$ | Master Theorem (Case 2, $k=0$) | $\Theta(\log e)$ |
| **Classical MatMul** | Iterative/Recursive | $T(n) = 8T(n/2) + \Theta(n^2)$ | Master Theorem (Case 1) | $\Theta(n^3)$ |
| **Strassen MatMul** | Divide & Conquer | $T(n) = 7T(n/2) + \Theta(n^2)$ | Master Theorem / Substitution | $\Theta(n^{\log_2 7}) \approx \Theta(n^{2.807})$ |

---

### 3. Deep Dive: Why the Master Theorem Fails on Worst-Case Quick Sort

The standard Master Theorem requires recurrences of the form:
$$T(n) = a \, T\left(\frac{n}{b}\right) + f(n), \quad a \ge 1, \; b > 1$$
where the subproblem size decreases **multiplicatively** by a constant factor $b$.

In worst-case Quick Sort (e.g., deterministic last-element pivot on already-sorted or reverse-sorted event logs):
$$T(n) = T(n - 1) + T(0) + c \cdot n = T(n - 1) + c \cdot n$$
Here, the subproblem shrinks **subtractively** by a constant difference ($n - 1$). Since no constant $b > 1$ exists such that $n - 1 = n/b$ for all $n$, **the Master Theorem cannot be applied**.

#### Solution via Iterative Unrolling:
$$\begin{aligned}
T(n) &= T(n - 1) + cn \\
&= [T(n - 2) + c(n - 1)] + cn \\
&= T(1) + c \sum_{i=2}^n i \\
&= d + c\left(\frac{n(n + 1)}{2} - 1\right) = \Theta(n^2)
\end{aligned}$$

#### Engineering Defense:
To protect the SOC analytics engine from malicious Denial-of-Service (DoS) input streams deliberately engineered to trigger this quadratic collapse, the engine implements `quick_sort_randomized`, which uniformly samples a random pivot in the active subarray. This bounds the expected recursion depth to $O(\log n)$ with high probability ($1 - o(1)$).

---

### 4. Empirical Benchmark Data & Comparative Analysis

The data below was empirically captured by [`src/core/metrics.c`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/src/core/metrics.c) and exported directly to [`data/benchmark_results.csv`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/data/benchmark_results.csv) during execution of the test harness and demonstration scenarios.

#### 4.1 Scale Progression: Merge Sort vs. Randomized Quick Sort

| Input Size ($N$) | Algorithm | Comparisons | Swaps / Writes | Recursive Calls | Memory Allocated (bytes) | Time (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **$N = 100$** | Merge Sort | 356 | 1,345 | 99 | 32,000 | < 1.0 |
| **$N = 100$** | Quick Sort (Rand) | 620 | 916 | 67 | 0 (In-place) | < 1.0 |
| **$N = 2,500$** | Merge Sort | 14,752 | 56,809 | 2,499 | 800,000 | 2.0 |
| **$N = 2,500$** | Quick Sort (Rand) | 32,668 | 37,774 | 1,664 | 0 (In-place) | < 1.0 |
| **$N = 10,000$** | Merge Sort | 69,008 | 267,233 | 9,999 | 3,200,000 | 7.0 |
| **$N = 10,000$** | Quick Sort (Rand) | 153,002 | 176,850 | 6,657 | 0 (In-place) | 3.0 |

**Observations:**
1. **Time vs. Space Trade-off:** Randomized Quick Sort operates completely in-place ($0$ auxiliary heap allocations) and runs faster due to lower cache miss penalties. Merge Sort requires $O(n)$ auxiliary buffer space ($3.2$ MB for $N=10,000$).
2. **Stability:** Merge Sort maintains strict stability (essential for preserving sub-order of logs with identical timestamps across different severity categories).

#### 4.2 Adversarial Stress Test: Pre-Sorted Event Logs ($N = 2,000$)

| Algorithm | Input Condition | Comparisons | Swaps / Writes | Recursive Calls | Observed Asymptotic Behavior |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Quick Sort (Deterministic)**| Sorted Logs | **1,999,000** | 4,001,998 | 1,999 | **$\Theta(N^2)$ Quadratic Degradation** |
| **Merge Sort** | Sorted Logs | **11,088** | 43,905 | 1,999 | **$\Theta(N \log N)$ Robust & Stable** |

> [!CAUTION]
> Under already-sorted input, Deterministic Quick Sort performed **1,999,000 comparisons** ($\approx \frac{2000 \times 1999}{2}$), whereas Merge Sort required only **11,088 comparisons**, empirically proving a **$180\times$ efficiency gap**.

#### 4.3 Burst Anomaly Detection: Divide-and-Conquer vs. Kadane

| Method | Comparisons | Swaps / Writes | Recursive Calls | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **D&C (`max_subarray_dc`)** | 24 | 0 | 19 | $\Theta(N \log N)$ | $O(\log N)$ stack |
| **Kadane (`max_subarray_kadane`)**| 18 | 0 | 0 | $\Theta(N)$ | $O(1)$ auxiliary |

Both methods independently isolated the exact same peak anomaly burst (Sum = 15 points) across identical test windows, confirming oracle correctness.

#### 4.4 Matrix Multiplication: Classical vs. Strassen on $16 \times 16$ Host Graphs

| Paradigm | Matrix Size | Multiplications / Additions | Recursive Calls | Theoretical Complexity |
| :--- | :--- | :--- | :--- | :--- |
| **Classical** | $16 \times 16$ | 4,096 writes | 0 | $\Theta(N^3) = 16^3 = 4,096$ |
| **Strassen** | $16 \times 16$ | 4,232 writes | 57 | $\Theta(N^{2.807}) \approx 2,401$ mults |

---

### 5. Week 2 Unit Test Verification Matrix

All Unit II algorithms were subjected to rigorous oracle tests in [`tests/test_all.c`](file:///C:/Users/spars/.gemini/antigravity/scratch/cseg3053-cyber-threat-engine/tests/test_all.c):

* `[PASS] Merge Sort produces monotonically sorted timestamps`
* `[PASS] Iterative and Recursive Binary Search locate exact target`
* `[PASS] Binary Search returns -1 on absent timestamp`
* `[PASS] BST Iterative and Recursive search locate threat signature`
* `[PASS] Deterministic and Randomized Quick Sort sort correctly`
* `[PASS] Maximum Subarray: Divide-and-Conquer and Kadane yield identical optimal burst (sum=15)`
* `[PASS] Fast Exponentiation: 7^13 mod 1000 == 407 for both recursive and iterative`
* `[PASS] Celebrity Problem: O(N) detection identifies hidden C2 node 3`
* `[PASS] Matrix Multiplication: Classical and Strassen match expected product`

---

### 6. Submission & Defense Checklist (For Evaluators)
- [x] Mathematical recurrences derived using 4 distinct methods.
- [x] Formal proof of Master Theorem failure condition documented.
- [x] Empirical metrics recorded across $N=100, 2500, 10000$ and adversarial feeds.
- [x] Full source code written in Pure C17 with zero warnings under `-Wall -Wextra -O2`.
- [x] 100% test pass rate across all unit oracle checks.
