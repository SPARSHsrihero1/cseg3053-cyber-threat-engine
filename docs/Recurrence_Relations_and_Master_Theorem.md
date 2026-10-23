# CSEG3053 DAA PBL: Project 03 — Cybersecurity Log Threat Detection Engine
## Asymptotic Analysis: Recurrence Relations, Derivations, & Master Theorem

This document presents rigorous mathematical solutions for all fundamental recurrence relations implemented across the algorithmic workbench. Each algorithm is evaluated using multiple analytical methodologies: **Iteration (Unrolling)**, **Substitution (Mathematical Induction)**, **Recursion Trees**, and the **Master Theorem (CLRS 4th Edition)**.

---

### 1. Master Theorem Reference Formulation
For a recurrence of the canonical divide-and-conquer form:
$$T(n) = a \, T\left(\frac{n}{b}\right) + f(n), \quad a \ge 1, \; b > 1$$
let $c_{\text{crit}} = \log_b a$. The three standard cases are:

* **Case 1 (Leaf Dominant):** If $f(n) = O(n^{c_{\text{crit}} - \epsilon})$ for some constant $\epsilon > 0$, then:
  $$T(n) = \Theta\left(n^{\log_b a}\right)$$
* **Case 2 (Balanced):** If $f(n) = \Theta\left(n^{c_{\text{crit}}} \log^k n\right)$ for some $k \ge 0$, then:
  $$T(n) = \Theta\left(n^{\log_b a} \log^{k+1} n\right)$$
* **Case 3 (Root Dominant):** If $f(n) = \Omega(n^{c_{\text{crit}} + \epsilon})$ for some constant $\epsilon > 0$, and if $a f(n/b) \le c f(n)$ for some constant $c < 1$ for all sufficiently large $n$ (regularity condition), then:
  $$T(n) = \Theta(f(n))$$

---

### 2. Binary Search (`binary_search_recursive`)

#### 2.1 Recurrence Formulation
At each step, a single comparison against $logs[mid]$ halves the candidate search interval:
$$T(n) = T\left(\frac{n}{2}\right) + c, \quad T(1) = d$$

#### 2.2 Derivation by Iteration (Unrolling)
$$\begin{aligned}
T(n) &= T\left(\frac{n}{2}\right) + c \\
&= \left[T\left(\frac{n}{4}\right) + c\right] + c = T\left(\frac{n}{2^2}\right) + 2c \\
&= T\left(\frac{n}{2^k}\right) + k \cdot c
\end{aligned}$$
The recursion terminates when $\frac{n}{2^k} = 1 \implies k = \log_2 n$:
$$T(n) = T(1) + c \log_2 n = d + c \log_2 n = \Theta(\log n)$$

#### 2.3 Master Theorem Application
* Parameters: $a = 1$, $b = 2$, $f(n) = c = \Theta(n^0)$.
* Critical exponent: $c_{\text{crit}} = \log_2 1 = 0$.
* Comparison: $f(n) = \Theta(n^0) = \Theta(n^{\log_b a} \log^0 n)$.
* **Result (Case 2 with $k=0$):**
  $$T(n) = \Theta\left(n^0 \log^{0+1} n\right) = \Theta(\log n)$$

---

### 3. Merge Sort (`merge_sort`)

#### 3.1 Recurrence Formulation
The event log array is split into two equal halves, each sorted recursively, followed by a linear $O(n)$ two-pointer merge:
$$T(n) = 2 \, T\left(\frac{n}{2}\right) + c \cdot n, \quad T(1) = d$$

#### 3.2 Recursion Tree Derivation
* **Level 0 (Root):** 1 problem of size $n$, work $= cn$.
* **Level 1:** 2 subproblems of size $n/2$, work $= 2 \cdot c(n/2) = cn$.
* **Level $i$:** $2^i$ subproblems of size $n/2^i$, work $= 2^i \cdot c(n/2^i) = cn$.
* **Tree Depth:** The tree terminates at leaf level $h = \log_2 n$.
* **Total Leaves:** $2^{\log_2 n} = n$ leaves, work $= n \cdot d = \Theta(n)$.
* **Sum of All Levels:**
  $$T(n) = \sum_{i=0}^{\log_2 n - 1} cn + \Theta(n) = cn \log_2 n + \Theta(n) = \Theta(n \log n)$$

#### 3.3 Master Theorem Application
* Parameters: $a = 2$, $b = 2$, $f(n) = cn = \Theta(n^1)$.
* Critical exponent: $c_{\text{crit}} = \log_2 2 = 1$.
* Comparison: $f(n) = \Theta(n^1) = \Theta(n^{c_{\text{crit}}} \log^0 n)$.
* **Result (Case 2 with $k=0$):**
  $$T(n) = \Theta(n \log n)$$

---

### 4. Quick Sort (`quick_sort`)

#### 4.1 Best-Case Recurrence (Balanced Partitioning)
Occurs when the partition subroutine splits the array into two exact equal halves:
$$T_{\text{best}}(n) = 2 \, T\left(\frac{n}{2}\right) + \Theta(n)$$
By Master Theorem Case 2 ($a=2, b=2, f(n)=\Theta(n)$):
$$T_{\text{best}}(n) = \Theta(n \log n)$$

#### 4.2 Worst-Case Recurrence (Adversarial Degeneracy)
Occurs when the pivot is always the extreme minimum or maximum element (e.g., deterministic last-element pivot on already-sorted or reverse-sorted event logs):
$$T_{\text{worst}}(n) = T(n - 1) + T(0) + c \cdot n = T(n - 1) + c \cdot n$$

#### 4.3 Why the Master Theorem Fails on Worst-Case Quick Sort
> **Critical Analysis:** The Master Theorem requires subproblems of size $n/b$ where $b > 1$ is a strictly positive constant dividing the problem size.
> In worst-case Quick Sort, the subproblem is of size $n - 1$ (subtractive reduction rather than multiplicative division).
> Because the problem shrinks by a constant difference rather than a constant factor, **the Master Theorem does not apply**.

#### 4.4 Solution by Iteration (Unrolling)
$$\begin{aligned}
T(n) &= T(n - 1) + cn \\
&= [T(n - 2) + c(n - 1)] + cn \\
&= T(1) + c \sum_{i=2}^n i \\
&= d + c\left(\frac{n(n + 1)}{2} - 1\right) = \Theta(n^2)
\end{aligned}$$
* **Engineering Remediation:** `quick_sort_randomized` randomly samples a pivot from the active window, bounding the expected depth to $O(\log n)$ with probability $1 - o(1)$.

---

### 5. Maximum Subarray: Divide-and-Conquer (`max_subarray_dc`)

#### 5.1 Recurrence Formulation
To detect anomaly bursts, the log array is split into two halves, each solved recursively, plus a linear scan crossing the midpoint:
$$T(n) = 2 \, T\left(\frac{n}{2}\right) + \Theta(n)$$
* Parameters: $a = 2$, $b = 2$, $f(n) = \Theta(n)$.
* Critical exponent: $\log_2 2 = 1$.
* By Master Theorem (Case 2):
  $$T(n) = \Theta(n \log n)$$
* **Contrast with Kadane's Algorithm:** Kadane's dynamic programming scan achieves $\Theta(n)$ time with $O(1)$ auxiliary space by maintaining running prefix maximums.

---

### 6. Fast Modular Exponentiation (`fast_power_mod`)

#### 6.1 Recurrence Formulation
For computing $b^e \bmod m$:
$$T(e) = T\left(\left\lfloor \frac{e}{2} \right\rfloor\right) + O(1), \quad T(0) = O(1)$$
* Parameters: $a = 1$, $b = 2$, $f(e) = \Theta(1)$.
* Critical exponent: $\log_2 1 = 0$.
* By Master Theorem (Case 2):
  $$T(e) = \Theta(\log e)$$

---

### 7. Strassen's Matrix Multiplication (`matrix_mult_strassen`)

#### 7.1 Classical Matrix Multiplication Recurrence
Dividing two $n \times n$ matrices into eight submatrices of size $(n/2) \times (n/2)$ requires 8 recursive multiplications and 4 matrix additions ($O(n^2)$):
$$T_{\text{classical}}(n) = 8 \, T\left(\frac{n}{2}\right) + \Theta(n^2)$$
* $a = 8$, $b = 2$, $c_{\text{crit}} = \log_2 8 = 3$.
* $f(n) = \Theta(n^2) = O(n^{3 - \epsilon})$ for $\epsilon = 1$.
* By Master Theorem (Case 1):
  $$T_{\text{classical}}(n) = \Theta(n^{\log_2 8}) = \Theta(n^3)$$

#### 7.2 Strassen's Breakthrough Recurrence
Volker Strassen (1969) demonstrated that through 14 linear additions and subtractions, the number of submatrix multiplications can be reduced from 8 to 7:
$$T_{\text{strassen}}(n) = 7 \, T\left(\frac{n}{2}\right) + \Theta(n^2)$$

#### 7.3 Master Theorem Application on Strassen
* Parameters: $a = 7$, $b = 2$, $f(n) = \Theta(n^2)$.
* Critical exponent:
  $$c_{\text{crit}} = \log_2 7 \approx 2.807354922$$
* Comparison: Since $2 < 2.80735$, we have:
  $$f(n) = O(n^{\log_2 7 - \epsilon}) \quad \text{for } \epsilon \approx 0.807$$
* **Result (Case 1 — Leaf Dominant):**
  $$T_{\text{strassen}}(n) = \Theta\left(n^{\log_2 7}\right) \approx \Theta(n^{2.807})$$

#### 7.4 Proof by Mathematical Induction (Substitution Method)
We prove that $T(n) \le c n^{\log_2 7} - d n^2$ for constants $c, d > 0$:
$$\begin{aligned}
T(n) &\le 7 \left(c \left(\frac{n}{2}\right)^{\log_2 7} - d \left(\frac{n}{2}\right)^2\right) + k n^2 \\
&= 7 c \frac{n^{\log_2 7}}{7} - \frac{7}{4} d n^2 + k n^2 \\
&= c n^{\log_2 7} - \left(\frac{7}{4} d - k\right) n^2
\end{aligned}$$
For the inequality to hold, we require:
$$\frac{7}{4} d - k \ge d \iff \frac{3}{4} d \ge k \iff d \ge \frac{4}{3} k$$
Choosing $d = \frac{4}{3} k$ and $c$ sufficiently large to satisfy base conditions validates the induction.

---

### 8. Comprehensive Recurrence Summary Table

| Algorithm | Recurrence Relation | Method Applied | Case | Asymptotic Complexity |
| :--- | :--- | :--- | :--- | :--- |
| **Binary Search** | $T(n) = T(n/2) + \Theta(1)$ | Master Theorem | Case 2 ($k=0$) | $\Theta(\log n)$ |
| **Merge Sort** | $T(n) = 2T(n/2) + \Theta(n)$ | Master Theorem / Tree | Case 2 ($k=0$) | $\Theta(n \log n)$ |
| **Quick Sort (Best)** | $T(n) = 2T(n/2) + \Theta(n)$ | Master Theorem | Case 2 ($k=0$) | $\Theta(n \log n)$ |
| **Quick Sort (Worst)** | $T(n) = T(n-1) + \Theta(n)$ | Unrolling (Master fails) | Subtractive | $\Theta(n^2)$ |
| **Max Subarray (D&C)** | $T(n) = 2T(n/2) + \Theta(n)$ | Master Theorem | Case 2 ($k=0$) | $\Theta(n \log n)$ |
| **Fast Exponentiation** | $T(e) = T(e/2) + \Theta(1)$ | Master Theorem | Case 2 ($k=0$) | $\Theta(\log e)$ |
| **Classical MatMul** | $T(n) = 8T(n/2) + \Theta(n^2)$ | Master Theorem | Case 1 | $\Theta(n^3)$ |
| **Strassen MatMul** | $T(n) = 7T(n/2) + \Theta(n^2)$ | Master Theorem / Ind. | Case 1 | $\Theta(n^{\log_2 7}) \approx \Theta(n^{2.807})$ |
