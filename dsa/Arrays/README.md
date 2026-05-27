# 📦 Arrays in DSA — Complete Coverage

A fully self-contained, runnable reference for **every important array topic** in Data Structures & Algorithms.

---

## 📂 File Structure

| File | Topics |
|------|--------|
| `01_basics.py` | Array types, memory layout, basic CRUD operations, static vs dynamic |
| `02_searching.py` | Linear, Binary, Jump, Interpolation, Exponential, Fibonacci search + 7 Binary Search variants |
| `03_sorting.py` | Bubble, Selection, Insertion, Shell, Merge, Quick, Heap, Counting, Radix, Bucket, Tim sort |
| `04_two_pointer_sliding_window.py` | Two Sum, Three Sum, Container Water, Move Zeroes, Dutch Flag, Fixed/Variable window, Min Window Substring |
| `05_prefix_sum_difference_array.py` | Prefix sum, Range Sum Query, Kadane's, 2D prefix, Difference array, Car Pooling, Product Except Self |
| `06_array_rotation.py` | Left/Right rotate, Reversal algorithm, Next Permutation, Max Product Subarray, Majority Element, Leaders, Sort by Frequency, Merge Intervals |
| `07_classic_problems.py` | Missing number, Duplicate (Floyd), Stock I/II/III, Trapping Rain Water, Jump Game, 4-Sum, Longest Consecutive, Spiral Matrix, Kth Largest |
| `08_advanced_techniques.py` | Segment Tree, Lazy Propagation, Fenwick/BIT, Sparse Table (RMQ), Monotonic Stack/Queue, Bitwise tricks |
| `09_2d_matrix.py` | Transpose, Rotation, Spiral, Diagonal traversal, Sorted matrix search, Word Search, Matrix multiply, Islands, Flood Fill, BFS shortest path |
| `10_special_arrays.py` | Jagged, Sparse, Circular Buffer, Prefix Max/Suffix Min, Non-adjacent sum, Activity Selection, Stock Span, Min Platforms |

---

## 🗺️ Topic Map

```
ARRAYS
├── Types
│   ├── 1D, 2D, 3D, nD
│   ├── Static, Dynamic
│   ├── Jagged (Ragged)
│   ├── Sparse
│   └── Circular Buffer
│
├── Memory
│   ├── Row-major vs Col-major
│   └── Index formula: base + (r*cols + c) * size
│
├── Basic Operations         Complexity
│   ├── Access arr[i]        O(1)
│   ├── Update               O(1)
│   ├── Append               O(1) amortised
│   ├── Insert (middle)      O(n)
│   ├── Delete (middle)      O(n)
│   └── Traverse             O(n)
│
├── Searching
│   ├── Linear               O(n)
│   ├── Binary               O(log n)
│   ├── Jump                 O(√n)
│   ├── Interpolation        O(log log n) avg
│   ├── Exponential          O(log n)
│   ├── Fibonacci            O(log n)
│   └── Variants
│       ├── First occurrence
│       ├── Last occurrence
│       ├── Count occurrences
│       ├── Rotated sorted array
│       ├── Floor sqrt
│       └── Peak element
│
├── Sorting
│   ├── Comparison-based
│   │   ├── Bubble Sort      O(n²)
│   │   ├── Selection Sort   O(n²)
│   │   ├── Insertion Sort   O(n²) / O(n) best
│   │   ├── Shell Sort       O(n^1.5)
│   │   ├── Merge Sort       O(n log n)
│   │   ├── Quick Sort       O(n log n) avg
│   │   ├── Heap Sort        O(n log n)
│   │   └── Tim Sort         O(n log n) — Python built-in
│   └── Non-comparison
│       ├── Counting Sort    O(n + k)
│       ├── Radix Sort       O(d * n)
│       └── Bucket Sort      O(n + k) avg
│
├── Two Pointer
│   ├── Two Sum (sorted)
│   ├── Three Sum / Four Sum
│   ├── Container with Most Water
│   ├── Move Zeroes
│   ├── Remove Duplicates (sorted)
│   ├── Reverse Array
│   ├── Merge Two Sorted Arrays
│   └── Dutch National Flag (3-way partition)
│
├── Sliding Window
│   ├── Fixed size — max/min/sum of window
│   ├── Variable size — smallest subarray with sum ≥ S
│   ├── Longest substring without repeat
│   ├── Max consecutive ones with k flips
│   ├── Fruit into baskets (at most 2 distinct)
│   └── Minimum window substring
│
├── Prefix Sum
│   ├── Range Sum Query     O(1) after O(n) build
│   ├── Subarray sum = k   O(n)
│   ├── Kadane's Algorithm  O(n) max subarray
│   ├── Equilibrium index
│   └── 2D Matrix Range Sum
│
├── Difference Array
│   ├── Range Update        O(1) per update
│   └── Car Pooling / Meeting Rooms
│
├── Rotation & Rearrangement
│   ├── Left / Right rotate
│   ├── Reversal algorithm  O(n) O(1)
│   ├── Next Permutation
│   ├── Max Product Subarray
│   ├── Majority Element (Boyer-Moore)
│   ├── Leaders in Array
│   ├── Sort by Frequency
│   ├── Segregate Even/Odd
│   └── Merge Intervals
│
├── Classic Problems
│   ├── Find missing number (sum / XOR)
│   ├── Find duplicate (Floyd's)
│   ├── Find all duplicates
│   ├── Find missing & repeating
│   ├── Stock buy & sell I, II, III
│   ├── Trapping Rain Water
│   ├── Jump Game I & II
│   ├── Subarray with given sum
│   ├── Longest consecutive sequence
│   ├── Spiral Matrix
│   ├── Rotate Matrix 90°
│   ├── Set Matrix Zeroes
│   └── Kth largest / smallest (heap / quickselect)
│
├── Advanced Data Structures on Arrays
│   ├── Segment Tree            O(log n) query/update
│   ├── Segment Tree + Lazy     O(log n) range update
│   ├── Fenwick Tree (BIT)      O(log n) prefix sum
│   └── Sparse Table (RMQ)     O(1) query, O(n log n) build
│
├── Monotonic Structures
│   ├── Monotonic Stack — Next Greater/Smaller Element
│   ├── Largest Rectangle in Histogram
│   └── Monotonic Deque — Sliding Window Maximum
│
├── 2D Arrays / Matrices
│   ├── Transpose
│   ├── Rotation 90° CW / CCW
│   ├── Spiral traversal
│   ├── Diagonal traversal
│   ├── Search in sorted matrix  O(m+n)
│   ├── Word Search (DFS + backtrack)
│   ├── Matrix multiplication   O(n³)
│   ├── Count Islands (DFS/BFS)
│   ├── Flood Fill
│   └── Shortest path BFS
│
└── Bitwise on Arrays
    ├── Single number (XOR)
    ├── Two non-repeating numbers
    └── Count set bits (dp)
```

---

## ⚡ Quick Complexity Reference

| Algorithm / Structure | Time | Space |
|-----------------------|------|-------|
| Array access          | O(1) | O(1) |
| Linear Search         | O(n) | O(1) |
| Binary Search         | O(log n) | O(1) |
| Sorting (best)        | O(n log n) | varies |
| Kadane's Algorithm    | O(n) | O(1) |
| Prefix Sum build      | O(n) | O(n) |
| Sliding Window        | O(n) | O(1) |
| Two Pointer           | O(n) or O(n²) | O(1) |
| Segment Tree          | O(log n) per op | O(n) |
| Fenwick Tree          | O(log n) per op | O(n) |
| Sparse Table (RMQ)    | O(1) query | O(n log n) |

---

## 🚀 How to Run

```bash
# Run any file individually
python 01_basics.py
python 02_searching.py
python 03_sorting.py
# ... etc
```

---

## 📌 Common Patterns Cheat-Sheet

| Problem Pattern | Technique |
|-----------------|-----------|
| Range sum/min/max queries | Prefix Sum / Segment Tree / Sparse Table |
| Range update + queries | Fenwick Tree / Lazy Segment Tree / Difference Array |
| Sliding window (fixed k) | Two deque pointers |
| Sliding window (dynamic) | Shrinkable window with condition |
| Find pair with property | Sort + Two Pointers or HashMap |
| Subarray count problems | Prefix Sum + HashMap |
| Order statistics | QuickSelect or Heap |
| Interval problems | Sort by start/end + Sweep Line |
| Matrix problems | DFS/BFS + visited array |
| Duplicates/missing | XOR or index marking |
