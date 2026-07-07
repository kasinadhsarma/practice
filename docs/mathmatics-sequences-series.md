# 🔁 Mathematics — Sequences & Series

**Location:** [`mathmatics/sequences_series/`](../mathmatics/sequences_series/)

Patterns in ordered lists of numbers, and closed-form shortcuts for summing them without looping. Each file is a standalone, self-contained class (no cross-file imports) with a runnable demo.

---

## Operations

| File | Class | Description | Time Complexity |
| :--- | :--- | :--- | :--- |
| `arithmetic_progression.py` | `arithmetic_progression` | $a_n = a_1 + (n-1)d$; sum via pairing first and last terms | $\mathcal{O}(1)$ |
| `geometric_progression.py` | `geometric_progression` | $a_n = a_1 r^{n-1}$; finite sum, plus the infinite sum $\frac{a_1}{1-r}$ when $\lvert r \rvert < 1$ | $\mathcal{O}(1)$ |
| `fibonacci_binet.py` | `fibonacci_binet` | Closed-form $n$th Fibonacci number via Binet's formula (golden ratio $\phi$) — no recursion needed | $\mathcal{O}(1)$ |
| `summation_formulas.py` | `summation_formulas` | Closed forms for $\sum_{i=1}^n i$, $\sum i^2$, $\sum i^3$ | $\mathcal{O}(1)$ |

**Note:** `fibonacci_binet.py` gives the same numbers as [`dsa/basics/recursion/level2/fibonacci_recursive.py`](../dsa/basics/recursion/level2/fibonacci_recursive.py) but via a direct formula instead of recursion — a good side-by-side for comparing $\mathcal{O}(1)$ closed-form vs. $\mathcal{O}(2^n)$ naive-recursive approaches to the same sequence.

---

## How to Run

```bash
python ./mathmatics/sequences_series/arithmetic_progression.py
python ./mathmatics/sequences_series/geometric_progression.py
python ./mathmatics/sequences_series/fibonacci_binet.py
python ./mathmatics/sequences_series/summation_formulas.py
```
