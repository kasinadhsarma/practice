# 📚 DSA — Stack

**Location:** [`dsa/stack/`](../dsa/stack/)

A **Stack** is a LIFO (Last-In-First-Out) structure — the last element pushed is the first one popped. Access is restricted to a single end (the "top"), which is exactly what makes push/pop O(1).

---

## Stack (Array-Based) — `stack_array.py`

Backed directly by a Python list, using `append`/`pop` on the end (both O(1) amortized).

| Operation | Time | Description |
|:---|:---|:---|
| `push(val)` | $\mathcal{O}(1)$ | Append to the end |
| `pop()` | $\mathcal{O}(1)$ | Remove and return the last element |
| `peek()` | $\mathcal{O}(1)$ | Return the last element without removing it |
| `is_empty()` | $\mathcal{O}(1)$ | — |

**Applications:** function call stack / recursion, undo history, browser back button.

---

## Valid Parentheses — `valid_parentheses.py`

Checks whether a string of brackets is balanced, by pushing every opening bracket and popping (and matching) on every closing bracket.

| Property | Detail |
|:---|:---|
| **Approach** | Stack matching — closing bracket must match current top |
| **Time Complexity** | $\mathcal{O}(N)$ |
| **Space Complexity** | $\mathcal{O}(N)$ worst case |

---

## Min Stack — `min_stack.py`

A stack that also answers "what's the minimum currently in the stack?" in O(1), by keeping a second stack that mirrors every push/pop with the running minimum.

| Operation | Time | Description |
|:---|:---|:---|
| `push(val)` | $\mathcal{O}(1)$ | Push onto both the main stack and the min-stack |
| `pop()` | $\mathcal{O}(1)$ | Pop both stacks in sync |
| `top()` | $\mathcal{O}(1)$ | — |
| `get_min()` | $\mathcal{O}(1)$ | Top of the min-stack |

---

## Evaluate Postfix Expression — `evaluate_postfix.py`

Evaluates a Reverse Polish Notation expression (e.g. `"3 4 + 2 *"` → `14`) — numbers are pushed, and each operator pops its two operands, applies itself, and pushes the result back.

| Property | Detail |
|:---|:---|
| **Approach** | Single stack, single left-to-right pass |
| **Time Complexity** | $\mathcal{O}(N)$ |
| **Space Complexity** | $\mathcal{O}(N)$ worst case |

---

## How to Run

```bash
python ./dsa/stack/stack_array.py
python ./dsa/stack/valid_parentheses.py
python ./dsa/stack/min_stack.py
python ./dsa/stack/evaluate_postfix.py
```
