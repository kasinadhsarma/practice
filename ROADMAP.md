# 🗺️ Learning Roadmap

A suggested path through this repo, ordered by dependency and difficulty — each stage assumes you're comfortable with the one before it. Every topic links to its `docs/` page for the full breakdown (formulas, complexity, examples).

Check off each stage as you go. Skip a stage only if you can already solve its "you should be able to" checkpoint without looking anything up.

---

## Stage 0 — Absolute Basics

**Goal:** comfortable with variables, arithmetic, and running a Python script.

| Topic | Path | Doc |
| :--- | :--- | :--- |
| Basic Calculations | [`basiccalculations/`](./basiccalculations/) | [docs/basic-calculations.md](./docs/basic-calculations.md) |

✅ **You should be able to:** write a script that takes two numbers as input and prints their sum, difference, product, and quotient.

---

## Stage 1 — Control Flow Foundations

**Goal:** the building blocks every later algorithm is made of — conditionals, loops, and recursion.

| Order | Topic | Path | Doc |
| :---: | :--- | :--- | :--- |
| 1 | Logic (if/else, digit math) | [`dsa/basics/logic/`](./dsa/basics/logic/) | [docs/dsa-logic.md](./docs/dsa-logic.md) |
| 2 | Loops (`for`/`while`/control flow) | [`dsa/basics/loops/`](./dsa/basics/loops/) | [docs/dsa-loops.md](./docs/dsa-loops.md) |
| 3 | Recursion (self-calling functions → backtracking) | [`dsa/basics/recursion/`](./dsa/basics/recursion/) | [docs/dsa-recursion.md](./docs/dsa-recursion.md) |
| 4 | Patterns (star/number printing — loop practice) | [`dsa/basics/numbers/`](./dsa/basics/numbers/), [`dsa/basics/stars/`](./dsa/basics/stars/) | [docs/dsa-patterns.md](./docs/dsa-patterns.md) |

**Why this order:** logic teaches branching in isolation before loops add repetition on top of it. Recursion comes right after loops because it's the "other" way to repeat — doing both back-to-back makes the contrast (and when to reach for which) obvious. Patterns are last in this stage because they're pure loop-nesting practice, not new concepts — use them as a fluency check.

✅ **You should be able to:** write a recursive function AND an equivalent loop for the same problem (e.g. factorial), and explain why one uses more call-stack memory.

---

## Stage 2 — Object-Oriented Practice

**Goal:** comfortable writing a class with state and methods before every later chapter uses that as the default style.

| Topic | Path | Doc |
| :--- | :--- | :--- |
| OOP Geometry (shapes as classes) | [`oops/geometry/`](./oops/geometry/) | [docs/oops-geometry.md](./docs/oops-geometry.md) |

✅ **You should be able to:** write a class with an `__init__`, at least one method that computes something from `self`, and a demo that instantiates it.

---

## Stage 3 — Arrays (the big one)

**Goal:** the single most-tested topic in technical interviews. This chapter alone covers searching, sorting, two-pointer, sliding window, prefix sums, and more — go slowly.

| Topic | Path | Doc |
| :--- | :--- | :--- |
| Arrays (11 files, ~144 functions) | [`dsa/Arrays/`](./dsa/Arrays/) | [docs/dsa-arrays.md](./docs/dsa-arrays.md), full topic map in [dsa/Arrays/README.md](./dsa/Arrays/README.md) |

**Suggested internal order** (the files are numbered for a reason):
1. `01_basics` → `02_searching` — access patterns, then linear/binary search and its variants
2. `03_sorting` → `04_two_pointer_sliding_window` — sorting first, since two-pointer techniques often assume a sorted array
3. `05_prefix_sum_difference_array` → `06_array_rotation` — running-sum tricks, then in-place rearrangement
4. `07_classic_problems` — the interview staples (stock problems, trapping rain water, jump game, etc.) once the toolkit above is familiar
5. `08_advanced_techniques` — Segment Tree, Fenwick Tree, Sparse Table, monotonic stack/deque (revisit this one after Stage 5, Heaps, if it feels heavy)
6. `09_2d_matrix` → `10_special_arrays` → `11_remaining_topics` — everything else, roughly in difficulty order

✅ **You should be able to:** solve two-pointer, sliding-window, and prefix-sum problems without checking the file first, and explain why binary search needs a sorted input.

---

## Stage 4 — Hashing

**Goal:** recognize when a hashmap turns an O(N²) brute force into O(N).

| Topic | Path | Doc |
| :--- | :--- | :--- |
| Hashing | [`dsa/hashing/`](./dsa/hashing/) | [docs/dsa-hashing.md](./docs/dsa-hashing.md) |

✅ **You should be able to:** look at a "count pairs/subarrays with property X" problem and recognize the hashmap-frequency pattern before writing any code.

---

## Stage 5 — Heaps

**Goal:** understand priority queues and when "always process the smallest/largest next" beats sorting everything upfront.

| Topic | Path | Doc |
| :--- | :--- | :--- |
| Heaps | [`dsa/heaps/`](./dsa/heaps/) | [docs/dsa-heaps.md](./docs/dsa-heaps.md) |
| (revisit) Segment/Fenwick Tree | [`dsa/Arrays/08_advanced_techniques.py`](./dsa/Arrays/08_advanced_techniques.py) | [docs/dsa-arrays.md](./docs/dsa-arrays.md) |

✅ **You should be able to:** implement "kth largest element" using a bounded min-heap without looking it up.

---

## Stage 6 — Graphs

**Goal:** traversal, shortest paths, and spanning trees — the largest conceptual jump so far. Do this after arrays/hashing/heaps, since graph algorithms lean on all three (queues, hashmaps for visited-sets, heaps for Dijkstra/Prim's).

| Topic | Path | Doc |
| :--- | :--- | :--- |
| Graphs | [`dsa/graphs/`](./dsa/graphs/) | [docs/dsa-graphs.md](./docs/dsa-graphs.md) |

**Suggested internal order:** BFS → DFS (traversal basics) → Connected Components → Cycle Detection → Topological Sort → Kruskal's/Prim's (MST) → Dijkstra → Bellman-Ford → Floyd-Warshall (shortest paths, easiest to hardest).

✅ **You should be able to:** explain when you'd reach for Dijkstra vs Bellman-Ford vs Floyd-Warshall for a given problem.

---

## Stage 7 — Dynamic Programming

**Goal:** the hardest conceptual topic here — save it for last among the DSA chapters. It leans directly on recursion (Stage 1) and requires genuine comfort with "define the subproblem" thinking.

| Topic | Path | Doc |
| :--- | :--- | :--- |
| Dynamic Programming | [`dsa/dp/`](./dsa/dp/) | [docs/dsa-dp.md](./docs/dsa-dp.md) |

**Suggested internal order:** Fibonacci-style thinking (recall `dsa/basics/recursion/level2/fibonacci_recursive.py` — this is the exponential version DP is fixing) → House Robber (simplest 1D DP) → Subset Sum → 0/1 Knapsack → Coin Change → LCS → LIS → Edit Distance → Longest Palindromic Subsequence → Matrix Chain Multiplication (hardest — interval DP) → Fractional Knapsack (greedy, not DP — a good "which technique applies here" checkpoint).

✅ **You should be able to:** write the recurrence relation for a new DP problem on paper before writing any code.

---

## Stage 8 — Mathematics (optional, parallel track)

**Goal:** these don't block anything above — treat as an independent track you can pick up any time after Stage 2, if the domain (graphics, ML, physics) interests you.

| Order | Topic | Path | Doc |
| :---: | :--- | :--- | :--- |
| 1 | Matrices | [`mathmatics/matrices/`](./mathmatics/matrices/) | [docs/mathmatics-matrices.md](./docs/mathmatics-matrices.md) |
| 2 | Linear Algebra (vectors, solving systems) | [`mathmatics/algebra/linearalgebra/`](./mathmatics/algebra/linearalgebra/) | [docs/mathmatics-linearalgebra.md](./docs/mathmatics-linearalgebra.md) |

✅ **You should be able to:** solve a 3-variable linear system by hand using Gaussian elimination, then verify your code's answer against it.

---

## Quick Reference — Full Order

```
0. Basic Calculations
1. Logic → Loops → Recursion → Patterns
2. OOP Geometry
3. Arrays (01 → 11, in file order)
4. Hashing
5. Heaps
6. Graphs
7. Dynamic Programming
8. Matrices → Linear Algebra   (parallel track, any time after stage 2)
```

If you only have time for one thing: **do Arrays properly (Stage 3)**. It's the biggest chapter for a reason — most interview prep and most later chapters (heaps, graphs, DP) assume its patterns are second nature.
