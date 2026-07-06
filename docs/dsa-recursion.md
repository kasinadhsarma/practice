# 🔄 DSA — Recursion

**Location:** [`dsa/basics/recursion/`](../dsa/basics/recursion/)

Recursion as its own fundamental topic — structured into **three progressive levels**, from basic self-calling functions through classic recursion patterns to backtracking. All scripts use **OOP classes** for clean encapsulation and include complexity comments plus a runnable demo.

Recursion shows up implicitly all over this repo (`binary_search_recursive`, `merge_sort`, `quick_sort`, DFS, DP backtracking) — this chapter is where it's taught directly.

---

## 🟢 Level 1 — Basics

**Location:** [`dsa/basics/recursion/level1/`](../dsa/basics/recursion/level1/)

The simplest form: a function that calls itself on a smaller version of the same problem until it hits a base case.

| File | Class | Description | Key Idea |
| :--- | :--- | :--- | :--- |
| `factorial_recursive.py` | `FactorialRecursive` | $N! = N \times (N-1)!$ | Base case `n <= 1` |
| `sum_of_n.py` | `SumOfN` | $1 + 2 + \cdots + n$ | Base case `n <= 0` |
| `power_recursive.py` | `PowerRecursive` | $x^n$, linear and $O(\log N)$ fast-exponentiation variants | Repeated squaring |

---

## 🟡 Level 2 — Recursion Patterns

**Location:** [`dsa/basics/recursion/level2/`](../dsa/basics/recursion/level2/)

Patterns that go beyond simple self-reduction: exponential recursion trees, multi-branch decomposition, the tail-call shape, and functions that call each other instead of themselves.

| File | Class | Description | Key Idea |
| :--- | :--- | :--- | :--- |
| `fibonacci_recursive.py` | `FibonacciRecursive` | Naive $O(2^N)$ Fibonacci — contrast with the memoised DP version | Overlapping subproblems, no cache |
| `tower_of_hanoi.py` | `TowerOfHanoi` | Move N disks between pegs, never a larger disk on a smaller one | Three-way recursive decomposition |
| `tail_recursion.py` | `TailRecursion` | Non-tail vs tail-recursive sum (accumulator pattern) | Python doesn't optimise tail calls — the pattern still matters conceptually |
| `mutual_recursion.py` | `MutualRecursion` | `is_even`/`is_odd` defined in terms of each other | Two functions recursing into one another |

---

## 🔴 Level 3 — Backtracking

**Location:** [`dsa/basics/recursion/level3/`](../dsa/basics/recursion/level3/)

Recursion combined with "try, recurse, undo" — the backtracking pattern used for generating combinatorial structures and searching constrained spaces.

| File | Class | Description | Key Idea |
| :--- | :--- | :--- | :--- |
| `permutations.py` | `Permutations` | All $N!$ orderings of a list | Pick each remaining element next, recurse on what's left |
| `subsets.py` | `Subsets` | The power set ($2^N$ subsets) | Include/exclude branching per element |
| `n_queens.py` | `NQueens` | Place N queens with no shared row/column/diagonal | Place, recurse, backtrack on conflict |
| `grid_paths.py` | `GridPaths` | Count right/down paths through a grid avoiding obstacles | Branch on each move, dead ends return 0 |

---

## Complexity Quick-Reference

| Level | Typical Time | Typical Space | Core Technique |
| :---: | :---: | :---: | :--- |
| 1 | $\mathcal{O}(N)$ – $\mathcal{O}(\log N)$ | $\mathcal{O}(N)$ | Direct self-reduction |
| 2 | $\mathcal{O}(N)$ – $\mathcal{O}(2^N)$ | $\mathcal{O}(N)$ | Recursion trees, tail calls, mutual recursion |
| 3 | $\mathcal{O}(N!)$ – $\mathcal{O}(2^N)$ | $\mathcal{O}(N)$ | Backtracking (try / recurse / undo) |

---

## How to Run

```bash
# Level 1
python ./dsa/basics/recursion/level1/factorial_recursive.py
python ./dsa/basics/recursion/level1/sum_of_n.py
python ./dsa/basics/recursion/level1/power_recursive.py

# Level 2
python ./dsa/basics/recursion/level2/fibonacci_recursive.py
python ./dsa/basics/recursion/level2/tower_of_hanoi.py
python ./dsa/basics/recursion/level2/tail_recursion.py
python ./dsa/basics/recursion/level2/mutual_recursion.py

# Level 3
python ./dsa/basics/recursion/level3/permutations.py
python ./dsa/basics/recursion/level3/subsets.py
python ./dsa/basics/recursion/level3/n_queens.py
python ./dsa/basics/recursion/level3/grid_paths.py
```
