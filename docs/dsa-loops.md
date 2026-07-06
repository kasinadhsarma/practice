# 🔁 DSA Basics — Loops

**Location:** [`dsa/basics/loops/`](../dsa/basics/loops/)

Every core Python loop construct, structured into **three progressive levels**: the fundamentals, control-flow statements, and advanced iteration patterns.
All scripts use **OOP classes** for clean encapsulation and include complexity comments plus a runnable demo.

---

## 🟢 Level 1 — Basic Loop Constructs

**Location:** [`dsa/basics/loops/level1/`](../dsa/basics/loops/level1/)

The two fundamental loop types, plus nesting one loop inside another.

- **Time Complexity:** $\mathcal{O}(N)$ — $\mathcal{O}(N^2)$ for the nested case
- **Space Complexity:** $\mathcal{O}(1)$ — $\mathcal{O}(N)$ where results are collected

| File | Class | Description | Key Construct |
| :--- | :--- | :--- | :--- |
| `for_loop.py` | `ForLoop` | Sums 1..n and finds multiples of k | `for i in range(...)` |
| `while_loop.py` | `WhileLoop` | Counts down and sums 1..n | `while condition:` |
| `nested_loop.py` | `NestedLoop` | Builds an n×n multiplication table | loop inside a loop |

---

## 🟡 Level 2 — Loop Control Statements

**Location:** [`dsa/basics/loops/level2/`](../dsa/basics/loops/level2/)

Covers early exit, skipping iterations, the `for...else` construct, and emulating a `do...while` loop (which Python has no native syntax for).

- **Time Complexity:** $\mathcal{O}(N)$
- **Space Complexity:** $\mathcal{O}(1)$ — $\mathcal{O}(N)$ where results are collected

| File | Class | Description | Key Construct |
| :--- | :--- | :--- | :--- |
| `break_statement.py` | `BreakDemo` | Finds the first divisor of n, then stops | `break` |
| `continue_statement.py` | `ContinueDemo` | Sums only even numbers, skipping odds | `continue` |
| `for_else.py` | `ForElseDemo` | Prime check — `else` fires only if no `break` occurred | `for...else` |
| `do_while_loop.py` | `DoWhileEmulator` | Runs the body at least once before checking the stop condition | `while True:` + `break` |

---

## 🔴 Level 3 — Advanced Iteration Patterns

**Location:** [`dsa/basics/loops/level3/`](../dsa/basics/loops/level3/)

Pythonic ways to loop: pairing index with value, iterating multiple sequences in lockstep, comprehensions as loop shorthand, and customising `range()`.

- **Time Complexity:** $\mathcal{O}(N)$
- **Space Complexity:** $\mathcal{O}(N)$

| File | Class | Description | Key Construct |
| :--- | :--- | :--- | :--- |
| `enumerate_loop.py` | `EnumerateDemo` | Pairs each item with its index | `enumerate()` |
| `zip_loop.py` | `ZipDemo` | Iterates two lists in parallel; computes dot product | `zip()` |
| `comprehension_loop.py` | `ComprehensionDemo` | Squares, filters, and maps using comprehensions | `[... for ... in ...]` |
| `range_step_loop.py` | `RangeStepDemo` | Custom step size and reverse iteration | `range(start, stop, step)` |

---

## Complexity Quick-Reference

| Level | Typical Time | Typical Space | Core Technique |
| :---: | :---: | :---: | :--- |
| 1 | $\mathcal{O}(N)$ – $\mathcal{O}(N^2)$ | $\mathcal{O}(1)$ | `for` / `while` / nesting |
| 2 | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | `break`, `continue`, `for...else` |
| 3 | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ | `enumerate`, `zip`, comprehensions, custom `range` |

---

## How to Run

```bash
# Level 1
python ./dsa/basics/loops/level1/for_loop.py
python ./dsa/basics/loops/level1/while_loop.py
python ./dsa/basics/loops/level1/nested_loop.py

# Level 2
python ./dsa/basics/loops/level2/break_statement.py
python ./dsa/basics/loops/level2/continue_statement.py
python ./dsa/basics/loops/level2/for_else.py
python ./dsa/basics/loops/level2/do_while_loop.py

# Level 3
python ./dsa/basics/loops/level3/enumerate_loop.py
python ./dsa/basics/loops/level3/zip_loop.py
python ./dsa/basics/loops/level3/comprehension_loop.py
python ./dsa/basics/loops/level3/range_step_loop.py
```
