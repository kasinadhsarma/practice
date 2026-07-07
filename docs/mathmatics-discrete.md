# 🧩 Mathematics — Discrete Mathematics

**Location:** [`mathmatics/discrete/`](../mathmatics/discrete/)

The structural, non-continuous side of mathematics that underpins computer science: sets, logic, relations, functions, modular arithmetic, and graph theory. Each file is a standalone, self-contained class (no cross-file imports) with a runnable demo.

---

## Sets

| File | Class | Description | Time Complexity |
| :--- | :--- | :--- | :--- |
| `set_operations.py` | `set_operations` | Union, intersection, difference, symmetric difference | $\mathcal{O}(N + M)$ |
| `power_set.py` | `power_set` | Every subset of a set — $2^N$ of them, generated via bitmasking | $\mathcal{O}(N \times 2^N)$ |
| `cartesian_product.py` | `cartesian_product` | Every ordered pair $(a, b)$ with $a \in A$, $b \in B$ | $\mathcal{O}(N \times M)$ |

## Logic & Structure

| File | Class | Description | Time Complexity |
| :--- | :--- | :--- | :--- |
| `truth_table.py` | `truth_table` | Enumerates AND/OR/NOT/XOR/IMPLIES/IFF over two boolean variables | $\mathcal{O}(1)$ |
| `relations.py` | `relations` | Checks reflexive / symmetric / transitive / equivalence properties of a relation | $\mathcal{O}(N^3)$ |
| `functions_properties.py` | `functions_properties` | Checks injective / surjective / bijective for a mapping | $\mathcal{O}(N)$ |

## Number Theory & Counting

| File | Class | Description | Time Complexity |
| :--- | :--- | :--- | :--- |
| `modular_arithmetic.py` | `modular_arithmetic` | Fast modular exponentiation, and modular inverse via Extended Euclid | $\mathcal{O}(\log N)$ |
| `pigeonhole_principle.py` | `pigeonhole_principle` | Guaranteed minimum items in the fullest of $M$ containers holding $N$ items: $\lceil N/M \rceil$ | $\mathcal{O}(1)$ |

## Graph Theory

| File | Class | Description | Time Complexity |
| :--- | :--- | :--- | :--- |
| `graph_theory_basics.py` | `graph_theory_basics` | Degree sequence, handshake lemma check, Eulerian circuit condition (all-even-degree) | $\mathcal{O}(V + E)$ |

> For traversal, shortest-path, and MST algorithms on graphs, see [`dsa/graphs/`](../dsa/graphs/) and [docs/dsa-graphs.md](./dsa-graphs.md) — this module covers the structural/counting side, not algorithms.

---

## How to Run

```bash
python ./mathmatics/discrete/set_operations.py
python ./mathmatics/discrete/power_set.py
python ./mathmatics/discrete/cartesian_product.py
python ./mathmatics/discrete/truth_table.py
python ./mathmatics/discrete/relations.py
python ./mathmatics/discrete/functions_properties.py
python ./mathmatics/discrete/modular_arithmetic.py
python ./mathmatics/discrete/pigeonhole_principle.py
python ./mathmatics/discrete/graph_theory_basics.py
```
