# 📐 Python Programming Foundations & Practice

A structured, modular Python portfolio covering **Basic Calculations**, **Data Structures & Algorithms (DSA)**, and **Object-Oriented Programming (OOP)**. Each topic has its own dedicated documentation in the [`docs/`](./docs/) folder.

> 🗺️ **New here?** See [ROADMAP.md](./ROADMAP.md) for a suggested learning order through every chapter, with checkpoints along the way.

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
│   │   ├── stars/            # 🌟 Star pattern printing
│   │   │   ├── level1/       #   right_triangle, left_triangle,
│   │   │   │                 #   inverted_triangle, square
│   │   │   ├── level2/       #   pyramid, inverted_pyramid,
│   │   │   │                 #   hollow_square, hollow_triangle
│   │   │   └── level3/       #   diamond, butterfly, hourglass
│   │   ├── loops/            # 🔁 All Python loop constructs
│   │   │   ├── level1/       #   for_loop, while_loop, nested_loop
│   │   │   ├── level2/       #   break_statement, continue_statement,
│   │   │   │                 #   for_else, while_else, do_while_loop
│   │   │   └── level3/       #   enumerate_loop, zip_loop,
│   │   │                     #   comprehension_loop, range_step_loop
│   │   └── recursion/        # 🔄 Recursion — basics to backtracking
│   │       ├── level1/       #   factorial_recursive, sum_of_n, power_recursive
│   │       ├── level2/       #   fibonacci_recursive, tower_of_hanoi,
│   │       │                 #   tail_recursion, mutual_recursion
│   │       └── level3/       #   permutations, subsets, n_queens, grid_paths
│   ├── sorting/              # 📊 Sorting algorithms
│   │                         #   bubble, insertion, selection, merge, quick,
│   │                         #   heap, counting, radix, shell
│   ├── graphs/               # 🌐 Graph traversal, MST, shortest paths
│   │                         #   BFS, DFS, Kruskal's, Prim's, Dijkstra,
│   │                         #   Bellman-Ford, topological sort,
│   │                         #   Floyd-Warshall, cycle detection,
│   │                         #   connected components
│   ├── heaps/                # 🏔️  Heap data structure
│   │                         #   MaxHeap, MinHeap, kth_largest_element
│   ├── stack/                 # 📚 Stack (LIFO)
│   │                         #   stack_array, valid_parentheses,
│   │                         #   min_stack, evaluate_postfix
│   ├── queue/                  # 🎟️  Queue (FIFO)
│   │                         #   queue_array, circular_queue,
│   │                         #   queue_using_stacks, deque_basic
│   ├── linked_list/            # 🔗 Linked List
│   │                         #   singly_linked_list, doubly_linked_list,
│   │                         #   reverse_linked_list, detect_cycle,
│   │                         #   merge_two_sorted_lists
│   ├── hashing/               # 🔑 Hashmap-based algorithms
│   │                         #   isomorphic_strings, char_frequency_deficit,
│   │                         #   two_sum, group_anagrams,
│   │                         #   longest_consecutive_sequence,
│   │                         #   first_unique_character, subarray_sum_equals_k
│   ├── dp/                    # 💡 Dynamic Programming
│   │                          #   knapsack_01, knapsack_fractional, LCS, LIS,
│   │                          #   coin_change, edit_distance, house_robber,
│   │                          #   subset_sum, longest_palindromic_subsequence,
│   │                          #   matrix_chain_multiplication
│   └── Arrays/                # 📦 Arrays — 11 files, ~144 functions
│                              #   basics, searching, sorting, two-pointer/
│                              #   sliding-window, prefix-sum/diff-array,
│                              #   rotation, classic problems, segment/
│                              #   Fenwick/sparse trees, 2D matrix,
│                              #   special arrays, and more
├── oops/                      # 🧱 OOP fundamentals — 11 files, basics to advanced
│                              #   01_classes_objects, 02_encapsulation,
│                              #   03_inheritance, 04_polymorphism,
│                              #   05_abstraction, 06_magic_methods,
│                              #   07_class_static_methods_properties,
│                              #   08_composition_aggregation, 09_advanced_oop,
│                              #   10_design_patterns, 11_solid_principles
├── mathmatics/
│   ├── matrices/             # 🔢 Matrix operations
│   │                         #   addition, subtraction, multiplication,
│   │                         #   scalar_multiplication, transpose, determinant,
│   │                         #   identity, trace, is_symmetric, rotate90,
│   │                         #   rank, inverse, power
│   ├── algebra/
│   │   ├── linearalgebra/    # 📐 Vector algebra & linear systems
│   │   │                     #   vector_addition, vector_subtraction,
│   │   │                     #   scalar_vector_multiplication, dot_product,
│   │   │                     #   cross_product, vector_magnitude,
│   │   │                     #   vector_normalization, angle_between_vectors,
│   │   │                     #   vector_projection, linear_independence,
│   │   │                     #   solve_linear_system, cramers_rule
│   │   └── basicalgebra/     # ➗ Equations & polynomials
│   │                         #   linear_equation, quadratic_equation,
│   │                         #   polynomial_operations, exponents_roots
│   ├── trigonometry/          # 📐 Angles & triangles
│   │                         #   trig_ratios, pythagorean_identity,
│   │                         #   law_of_sines, law_of_cosines, unit_circle
│   ├── calculus/               # ∫ Limits, derivatives, integrals
│   │                         #   limit_numerical, derivative_numerical,
│   │                         #   power_rule_derivative, integral_numerical
│   ├── number_theory/          # 🔢 Primes & divisibility
│   │                         #   gcd_lcm, prime_sieve, prime_factorization,
│   │                         #   euler_totient
│   ├── coordinate_geometry/    # 📍 Points, lines, circles as equations
│   │                         #   distance_formula, midpoint_formula,
│   │                         #   slope_and_line_equation, circle_equation
│   ├── sequences_series/       # 🔁 Progressions & closed-form sums
│   │                         #   arithmetic_progression, geometric_progression,
│   │                         #   fibonacci_binet, summation_formulas
│   ├── geometry/               # 🧱 OOP shape classes — areas, perimeters,
│   │                         #   surface areas, volumes, vectors, Pythagorean theorem
│   ├── statistics/            # 📊 Descriptive statistics
│   │                         #   mean, median, mode, data_range, variance,
│   │                         #   standard_deviation, quartiles_iqr,
│   │                         #   covariance, correlation, z_score
│   ├── probability/            # 🎲 Probability & distributions
│   │                         #   probability_of_event, complement_rule,
│   │                         #   addition_rule, conditional_probability,
│   │                         #   bayes_theorem, permutations, combinations,
│   │                         #   binomial_distribution,
│   │                         #   expected_value_variance, normal_distribution
│   └── discrete/               # 🧩 Discrete mathematics
│                             #   set_operations, power_set, cartesian_product,
│                             #   truth_table, relations, functions_properties,
│                             #   modular_arithmetic, graph_theory_basics,
│                             #   pigeonhole_principle
├── sql/                      # 🗄️  SQL via sqlite3 (in-memory, testable)
│   ├── ddl/                  #   create_table, alter_drop_table
│   ├── dml/                  #   insert_update_delete
│   ├── queries/              #   select_where_orderby, aggregate_group_having
│   ├── joins/                #   all_joins (inner/left/right/full/cross/self)
│   ├── subqueries/           #   subqueries (scalar/correlated/IN/EXISTS)
│   ├── set_operations/       #   set_operations (union/intersect/except)
│   ├── window_functions/     #   window_functions (row_number/rank/lag/lead)
│   ├── views_and_indexes/    #   views_and_indexes
│   └── transactions/         #   transactions (commit/rollback)
└── docs/                     # 📖 Detailed docs per topic
```

---

## 📖 Documentation Index

| Topic | Doc | Description |
| :--- | :--- | :--- |
| 🧮 Basic Calculations | [docs/basic-calculations.md](./docs/basic-calculations.md) | Addition, subtraction, multiplication, division |
| 🧠 DSA — Logic Levels | [docs/dsa-logic.md](./docs/dsa-logic.md) | Level 1–3: even/odd → Armstrong → GCD, Fibonacci |
| 🔲 DSA — Patterns | [docs/dsa-patterns.md](./docs/dsa-patterns.md) | Stars & numbers: level 1–3 with class-based patterns |
| 🔁 DSA — Loops | [docs/dsa-loops.md](./docs/dsa-loops.md) | Level 1–3: for/while/nested → break/continue/for-else/do-while → enumerate/zip/comprehensions |
| 🔄 DSA — Recursion | [docs/dsa-recursion.md](./docs/dsa-recursion.md) | Level 1–3: factorial/power → Fibonacci/Hanoi/tail-recursion/mutual → permutations/subsets/N-Queens/grid-paths |
| 📊 DSA — Sorting | [docs/dsa-sorting.md](./docs/dsa-sorting.md) | Bubble, Insertion, Selection, Merge, Quick, Heap, Counting, Radix, Shell sort |
| 🌐 DSA — Graphs | [docs/dsa-graphs.md](./docs/dsa-graphs.md) | BFS, DFS, Kruskal's, Prim's, Dijkstra, Bellman-Ford, Topological Sort, Floyd-Warshall, Cycle Detection, Connected Components |
| 🏔️ DSA — Heaps | [docs/dsa-heaps.md](./docs/dsa-heaps.md) | MaxHeap, MinHeap, Kth Largest Element |
| 📚 DSA — Stack | [docs/dsa-stack.md](./docs/dsa-stack.md) | Array-based stack, Valid Parentheses, Min Stack, Evaluate Postfix |
| 🎟️ DSA — Queue | [docs/dsa-queue.md](./docs/dsa-queue.md) | Queue (deque-based), Circular Queue, Queue Using Two Stacks, Deque |
| 🔗 DSA — Linked List | [docs/dsa-linked-list.md](./docs/dsa-linked-list.md) | Singly & Doubly Linked List, Reverse, Detect Cycle (Floyd's), Merge Two Sorted Lists |
| 🔑 DSA — Hashing | [docs/dsa-hashing.md](./docs/dsa-hashing.md) | Isomorphic Strings, Two Sum, Group Anagrams, Longest Consecutive Sequence, and more |
| 💡 DSA — Dynamic Programming | [docs/dsa-dp.md](./docs/dsa-dp.md) | Knapsack (0/1 & Fractional), LCS, LIS, Coin Change, Edit Distance, House Robber, Subset Sum, and more |
| 📦 DSA — Arrays | [docs/dsa-arrays.md](./docs/dsa-arrays.md) | 11 files, ~144 functions — see [dsa/Arrays/README.md](./dsa/Arrays/README.md) for the full topic map |
| 🧱 OOP — Geometry | [docs/oops-geometry.md](./docs/oops-geometry.md) | Areas, perimeters, surface areas, volumes |
| 🔢 Mathematics — Matrices | [docs/mathmatics-matrices.md](./docs/mathmatics-matrices.md) | Addition → power: all 13 core matrix operations |
| 📐 Mathematics — Linear Algebra | [docs/mathmatics-linearalgebra.md](./docs/mathmatics-linearalgebra.md) | Vector arithmetic/geometry + Gaussian elimination & Cramer's Rule for solving systems |
| ➗ Mathematics — Algebra | [docs/mathmatics-algebra.md](./docs/mathmatics-algebra.md) | Linear & quadratic equations, polynomial operations, exponents/roots |
| 📐 Mathematics — Trigonometry | [docs/mathmatics-trigonometry.md](./docs/mathmatics-trigonometry.md) | Trig ratios, Pythagorean identity, Law of Sines/Cosines, unit circle |
| ∫ Mathematics — Calculus | [docs/mathmatics-calculus.md](./docs/mathmatics-calculus.md) | Numerical limits/derivatives/integrals, symbolic power-rule derivative |
| 🔢 Mathematics — Number Theory | [docs/mathmatics-number-theory.md](./docs/mathmatics-number-theory.md) | GCD/LCM, Sieve of Eratosthenes, prime factorization, Euler's totient |
| 📍 Mathematics — Coordinate Geometry | [docs/mathmatics-coordinate-geometry.md](./docs/mathmatics-coordinate-geometry.md) | Distance/midpoint formulas, slope & line equation, circle equation |
| 🔁 Mathematics — Sequences & Series | [docs/mathmatics-sequences-series.md](./docs/mathmatics-sequences-series.md) | Arithmetic/geometric progressions, Binet's formula, summation formulas |
| 🧱 Mathematics — Geometry | [docs/oops-geometry.md](./docs/oops-geometry.md) | Areas, perimeters, surface areas, volumes, vectors, Pythagorean theorem |
| 📊 Mathematics — Statistics | [docs/mathmatics-statistics.md](./docs/mathmatics-statistics.md) | Mean, median, mode, variance, standard deviation, quartiles/IQR, covariance, correlation, z-score |
| 🎲 Mathematics — Probability | [docs/mathmatics-probability.md](./docs/mathmatics-probability.md) | Core rules, conditional probability, Bayes' theorem, permutations/combinations, binomial & normal distributions |
| 🧩 Mathematics — Discrete Math | [docs/mathmatics-discrete.md](./docs/mathmatics-discrete.md) | Sets, power set, truth tables, relations, functions, modular arithmetic, graph theory basics, pigeonhole principle |
| 🗄️ SQL | [docs/sql.md](./docs/sql.md) | DDL, DML, joins, subqueries, set operations, window functions, views/indexes, transactions — via in-memory sqlite3 |

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

# Loops
python ./dsa/basics/loops/level1/for_loop.py
python ./dsa/basics/loops/level2/break_statement.py
python ./dsa/basics/loops/level3/enumerate_loop.py

# Recursion
python ./dsa/basics/recursion/level1/factorial_recursive.py
python ./dsa/basics/recursion/level2/tower_of_hanoi.py
python ./dsa/basics/recursion/level3/n_queens.py

# Algorithms
python ./dsa/dp/knapsack_01.py
python ./dsa/sorting/mergesort.py
python ./dsa/graphs/bfs.py
python ./oops/geometry/volume/cylinder.py

# Dynamic Programming
python ./dsa/dp/longest_common_subsequence.py
python ./dsa/dp/coin_change.py
python ./dsa/dp/edit_distance.py

# Sorting — non-comparison & heap-based
python ./dsa/sorting/heapsort.py
python ./dsa/sorting/countingsort.py
python ./dsa/sorting/radixsort.py

# Graphs — shortest paths & ordering
python ./dsa/graphs/dijkstra.py
python ./dsa/graphs/topological_sort.py
python ./dsa/graphs/connected_components.py

# Heaps
python ./dsa/heaps/minheap.py
python ./dsa/heaps/kth_largest_element.py

# Stack
python ./dsa/stack/valid_parentheses.py
python ./dsa/stack/min_stack.py
python ./dsa/stack/evaluate_postfix.py

# Queue
python ./dsa/queue/queue_array.py
python ./dsa/queue/circular_queue.py
python ./dsa/queue/queue_using_stacks.py

# Linked List
python ./dsa/linked_list/singly_linked_list.py
python ./dsa/linked_list/reverse_linked_list.py
python ./dsa/linked_list/detect_cycle.py

# Hashing
python ./dsa/hashing/two_sum.py
python ./dsa/hashing/group_anagrams.py
python ./dsa/hashing/isomorphic_strings.py

# Matrices
python ./mathmatics/matrices/determinant.py
python ./mathmatics/matrices/inverse.py
python ./mathmatics/matrices/rank.py

# Algebra
python ./mathmatics/algebra/basicalgebra/quadratic_equation.py
python ./mathmatics/algebra/basicalgebra/polynomial_operations.py

# Trigonometry
python ./mathmatics/trigonometry/trig_ratios.py
python ./mathmatics/trigonometry/law_of_cosines.py

# Calculus
python ./mathmatics/calculus/derivative_numerical.py
python ./mathmatics/calculus/integral_numerical.py

# Number Theory
python ./mathmatics/number_theory/prime_sieve.py
python ./mathmatics/number_theory/euler_totient.py

# Coordinate Geometry
python ./mathmatics/coordinate_geometry/distance_formula.py
python ./mathmatics/coordinate_geometry/circle_equation.py

# Sequences & Series
python ./mathmatics/sequences_series/geometric_progression.py
python ./mathmatics/sequences_series/fibonacci_binet.py

# Statistics
python ./mathmatics/statistics/mean.py
python ./mathmatics/statistics/variance.py
python ./mathmatics/statistics/correlation.py

# Probability
python ./mathmatics/probability/bayes_theorem.py
python ./mathmatics/probability/binomial_distribution.py
python ./mathmatics/probability/normal_distribution.py

# Discrete Mathematics
python ./mathmatics/discrete/set_operations.py
python ./mathmatics/discrete/truth_table.py
python ./mathmatics/discrete/graph_theory_basics.py

# Arrays
python ./dsa/Arrays/02_searching.py
python ./dsa/Arrays/04_two_pointer_sliding_window.py
python ./dsa/Arrays/08_advanced_techniques.py

# SQL
python ./sql/queries/select_where_orderby.py
python ./sql/joins/all_joins.py
python ./sql/window_functions/window_functions.py
```

> See the relevant doc in [`docs/`](./docs/) for full complexity analysis, formulas, and example inputs.

---

## 📚 Topics at a Glance

| Area | Algorithms / Classes | Key Concept |
| :--- | :--- | :--- |
| **Sorting** | Bubble, Insertion, Selection, Merge, Quick, Heap, Counting, Radix, Shell | Comparison & non-comparison sorting |
| **Graphs** | BFS, DFS, Kruskal's, Prim's, Dijkstra, Bellman-Ford, Topological Sort, Floyd-Warshall, Cycle Detection, Connected Components | Traversal, MST, shortest paths, ordering |
| **Heaps** | MaxHeap, MinHeap, Kth Largest Element | Priority queue, $\mathcal{O}(\log N)$ ops |
| **Stack** | Array-based Stack, Valid Parentheses, Min Stack, Evaluate Postfix | LIFO, single-end access, $\mathcal{O}(1)$ push/pop |
| **Queue** | Queue (deque), Circular Queue, Queue Using Two Stacks, Deque | FIFO, opposite-end access, $\mathcal{O}(1)$ enqueue/dequeue |
| **Linked List** | Singly & Doubly Linked List, Reverse, Detect Cycle, Merge Two Sorted Lists | Chained nodes, $\mathcal{O}(1)$ head insert, pointer manipulation |
| **Hashing** | Isomorphic Strings, Char Frequency Deficit, Two Sum, Group Anagrams, Longest Consecutive Sequence, First Unique Character, Subarray Sum Equals K | Hashmap / frequency-array lookups, $\mathcal{O}(1)$ average |
| **Dynamic Programming** | 0/1 & Fractional Knapsack, LCS, LIS, Coin Change, Edit Distance, House Robber, Subset Sum, LPS, Matrix Chain Mult. | Overlapping subproblems, optimal substructure |
| **Arrays** | ~144 functions across 11 files | Searching, sorting, two-pointer, sliding window, prefix sum, segment/Fenwick/sparse trees, 2D matrix, and more |
| **OOP Geometry** | 20+ shape classes | Encapsulation, formulas as methods |
| **Logic (DSA)** | 13 problems across levels 1–3 | Digit extraction, series, number theory |
| **Star Patterns** | 11 patterns across levels 1–3 | Loop bounds, space offsets, symmetry |
| **Number Patterns** | 10 patterns across levels 1–3 | Nested loops, binomial coefficients, Floyd filling |
| **Loops** | 12 constructs across levels 1–3 | `for`/`while`/nesting, `break`/`continue`/`for-else`/`while-else`/do-while, `enumerate`/`zip`/comprehensions |
| **Recursion** | 11 patterns across levels 1–3 | Basic self-reduction, recursion trees, tail/mutual recursion, backtracking |
| **Matrices** | 13 operations | Arithmetic, transpose, determinant, inverse, rank, power |
| **Linear Algebra** | 12 operations | Vector arithmetic/geometry, linear independence, Gaussian elimination, Cramer's Rule |
| **Algebra** | 4 operations | Linear/quadratic equations, polynomial add/multiply/evaluate, exponents & roots |
| **Trigonometry** | 5 operations | Right-triangle ratios, Pythagorean identity, Law of Sines/Cosines, unit circle |
| **Calculus** | 4 operations | Numerical limits/derivatives/integrals, symbolic power-rule derivative |
| **Number Theory** | 4 operations | GCD/LCM, prime sieve, prime factorization, Euler's totient |
| **Coordinate Geometry** | 4 operations | Distance/midpoint, slope & line equation, circle-point classification |
| **Sequences & Series** | 4 operations | Arithmetic/geometric progressions, Binet's formula, closed-form sums |
| **Geometry** | 20+ shape classes | Areas, perimeters, surface areas, volumes, vectors, Pythagorean theorem |
| **Statistics** | 10 operations | Central tendency, dispersion, covariance/correlation, z-score |
| **Probability** | 10 operations | Core rules, Bayes' theorem, combinatorics, binomial & normal distributions |
| **Discrete Math** | 9 operations | Sets, logic, relations/functions, modular arithmetic, graph theory, pigeonhole principle |
| **SQL** | 11 classes across 9 topics | DDL/DML, joins, subqueries, set operations, window functions, views/indexes, transactions |
