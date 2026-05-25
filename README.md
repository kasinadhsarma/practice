# 📐 Python Programming Foundations & Practice

A structured, modular Python portfolio covering **Basic Calculations**, **Data Structures & Algorithms (DSA)**, and **Object-Oriented Programming (OOP)**. Each topic has its own dedicated documentation in the [`docs/`](./docs/) folder.

---

## 📂 Repository Structure

```text
pratice/
├── basiccalculations/        # 🧮 Procedural arithmetic
├── dsa/
│   ├── basics/
│   │   ├── logic/            # 🧠 Logic levels 1–3
│   │   │   ├── level1/       #   even_odd, leapyear
│   │   │   ├── level2/       #   sum_of_digits, reversenumber, palindrome,
│   │   │   │                 #   armstrong, strong_number
│   │   │   └── level3/       #   factorial, fibonacci, prime_check,
│   │   │                     #   perfectnumber, gcd, direction_tracker
│   │   ├── numbers/          # 🔢 Number pattern printing
│   │   │   ├── level1/       #   right_triangle, left_triangle,
│   │   │   │                 #   inverted_triangle, square
│   │   │   ├── level2/       #   pyramid, floyd_triangle, middle_triangle
│   │   │   └── level3/       #   diamond, pascal_triangle, butterfly
│   │   └── stars/            # 🌟 Star pattern printing
│   │       ├── level1/       #   right_triangle, left_triangle,
│   │       │                 #   inverted_triangle, square
│   │       ├── level2/       #   pyramid, inverted_pyramid,
│   │       │                 #   hollow_square, hollow_triangle
│   │       └── level3/       #   diamond, butterfly, hourglass
│   ├── sorting/              # 📊 Sorting algorithms
│   ├── graphs/               # 🌐 Graph traversal & MST
│   ├── heaps/                # 🏔️  Heap data structure
│   └── dp/                   # 💡 Dynamic Programming
├── oops/
│   └── geometry/             # 🧱 OOP geometry classes
│       ├── areas/
│       ├── perimeter/
│       ├── surface/
│       ├── surfacearea/
│       └── volume/
└── docs/                     # 📖 Detailed docs per topic
```

---

## 📖 Documentation Index

| Topic | Doc | Description |
| :--- | :--- | :--- |
| 🧮 Basic Calculations | [docs/basic-calculations.md](./docs/basic-calculations.md) | Addition, subtraction, multiplication, division |
| 🧠 DSA — Logic Levels | [docs/dsa-logic.md](./docs/dsa-logic.md) | Level 1–3: even/odd → Armstrong → GCD, Fibonacci |
| 🔲 DSA — Patterns | [docs/dsa-patterns.md](./docs/dsa-patterns.md) | Stars & numbers: level 1–3 with class-based patterns |
| 📊 DSA — Sorting | [docs/dsa-sorting.md](./docs/dsa-sorting.md) | Bubble, Insertion, Selection, Merge, Quick sort |
| 🌐 DSA — Graphs | [docs/dsa-graphs.md](./docs/dsa-graphs.md) | BFS, DFS, Kruskal's, Prim's |
| 🏔️ DSA — Heaps | [docs/dsa-heaps.md](./docs/dsa-heaps.md) | Max-Heap: insert, extract_max, get_max |
| 💡 DSA — Dynamic Programming | [docs/dsa-dp.md](./docs/dsa-dp.md) | 0/1 Knapsack (DP), Fractional Knapsack (Greedy) |
| 🧱 OOP — Geometry | [docs/oops-geometry.md](./docs/oops-geometry.md) | Areas, perimeters, surface areas, volumes |

---

## 🚀 Quick Start

```bash
# Logic
python ./dsa/basics/logic/level1/even_odd.py
python ./dsa/basics/logic/level2/strong_number.py
python ./dsa/basics/logic/level3/gcd.py
python ./dsa/basics/logic/level3/prime_check.py

# Patterns — Stars
python ./dsa/basics/stars/level1/right_triangle.py
python ./dsa/basics/stars/level2/pyramid.py
python ./dsa/basics/stars/level3/diamond.py

# Patterns — Numbers
python ./dsa/basics/numbers/level1/right_triangle.py
python ./dsa/basics/numbers/level2/floyd_triangle.py
python ./dsa/basics/numbers/level3/pascal_triangle.py

# Algorithms
python ./dsa/dp/knapsack_01.py
python ./dsa/sorting/mergesort.py
python ./dsa/graphs/bfs.py
python ./oops/geometry/volume/cylinder.py
```

> See the relevant doc in [`docs/`](./docs/) for full complexity analysis, formulas, and example inputs.

---

## 📚 Topics at a Glance

| Area | Algorithms / Classes | Key Concept |
| :--- | :--- | :--- |
| **Sorting** | Bubble, Insertion, Selection, Merge, Quick | Comparison-based sorting |
| **Graphs** | BFS, DFS, Kruskal's, Prim's | Traversal & MST |
| **Heaps** | MaxHeap | Priority queue, $\mathcal{O}(\log N)$ ops |
| **Dynamic Programming** | 0/1 Knapsack, Fractional Knapsack | Overlapping subproblems, optimal substructure |
| **OOP Geometry** | 20+ shape classes | Encapsulation, formulas as methods |
| **Logic (DSA)** | 13 problems across levels 1–3 | Digit extraction, series, number theory |
| **Star Patterns** | 11 patterns across levels 1–3 | Loop bounds, space offsets, symmetry |
| **Number Patterns** | 10 patterns across levels 1–3 | Nested loops, binomial coefficients, Floyd filling |
