# 📊 DSA — Sorting Algorithms

**Location:** [`dsa/sorting/`](../dsa/sorting/)

Nine sorting algorithms — five comparison-based, plus Heap Sort and three non-comparison (counting/radix/shell) sorts — each implemented as a standalone OOP class with detailed docstring explanations.

---

## Algorithms

### 🫧 Bubble Sort — `bubblesort.py`

Repeatedly compares adjacent elements and swaps them if out of order. After each pass the largest unsorted element "bubbles" to its final position.

| | |
|:---|:---|
| **Best Case** | $\mathcal{O}(N)$ — already sorted (early exit on no swaps) |
| **Average / Worst** | $\mathcal{O}(N^2)$ |
| **Space** | $\mathcal{O}(1)$ — in-place |
| **Stable** | ✅ Yes |

---

### 📌 Insertion Sort — `insertionsort.py`

Builds the sorted array one item at a time by inserting each new element into its correct position among the already-sorted elements.

| | |
|:---|:---|
| **Best Case** | $\mathcal{O}(N)$ — already sorted |
| **Average / Worst** | $\mathcal{O}(N^2)$ |
| **Space** | $\mathcal{O}(1)$ — in-place |
| **Stable** | ✅ Yes |

---

### 🔍 Selection Sort — `selectionsort.py`

Repeatedly finds the minimum element from the unsorted portion and swaps it to the front.

| | |
|:---|:---|
| **Best / Average / Worst** | $\mathcal{O}(N^2)$ — always scans remaining elements |
| **Space** | $\mathcal{O}(1)$ — in-place |
| **Stable** | ❌ No (swaps can disrupt equal-element order) |

---

### ⚡ Merge Sort — `mergesort.py`

Divide-and-conquer: recursively splits the array in half, sorts each half, then merges the sorted halves.

| | |
|:---|:---|
| **Best / Average / Worst** | $\mathcal{O}(N \log N)$ |
| **Space** | $\mathcal{O}(N)$ — auxiliary arrays during merge |
| **Stable** | ✅ Yes |

**Recurrence:** $T(N) = 2T(N/2) + \mathcal{O}(N)$ → $\mathcal{O}(N \log N)$ by Master Theorem.

---

### 🏹 Quick Sort — `quicksort.py`

Divide-and-conquer: picks a pivot, partitions the array so smaller elements go left and larger go right, then recursively sorts each partition.

| | |
|:---|:---|
| **Best / Average** | $\mathcal{O}(N \log N)$ |
| **Worst Case** | $\mathcal{O}(N^2)$ — sorted input with bad pivot choice |
| **Space** | $\mathcal{O}(\log N)$ — recursion stack |
| **Stable** | ❌ No |

---

### 🏗️ Heap Sort — `heapsort.py`

Builds a max-heap in place, then repeatedly swaps the root (the max) with the last unsorted element and re-heapifies the shrinking heap. See [Heaps](./dsa-heaps.md) for the heap mechanics this relies on.

| | |
|:---|:---|
| **Best / Average / Worst** | $\mathcal{O}(N \log N)$ |
| **Space** | $\mathcal{O}(1)$ — sorts in place |
| **Stable** | ❌ No |

---

### 🪣 Counting Sort — `countingsort.py`

Non-comparison sort: counts occurrences of each value (offset to handle negatives), then uses a cumulative/prefix-sum count array to place every element directly into its sorted position.

| | |
|:---|:---|
| **Best / Average / Worst** | $\mathcal{O}(N + K)$ — $K$ = value range size |
| **Space** | $\mathcal{O}(N + K)$ |
| **Stable** | ✅ Yes |

---

### 🔢 Radix Sort — `radixsort.py`

Non-comparison sort for non-negative integers: repeatedly runs a stable counting sort keyed on one digit at a time, from least to most significant.

| | |
|:---|:---|
| **Best / Average / Worst** | $\mathcal{O}(D \times (N + B))$ — $D$ = digit count, $B$ = base (10) |
| **Space** | $\mathcal{O}(N + B)$ |
| **Stable** | ✅ Yes |
| **Limitation** | Non-negative integers only |

---

### 🐚 Shell Sort — `shellsort.py`

Generalises insertion sort with a shrinking gap sequence ($n/2, n/4, ..., 1$), so far-apart out-of-order elements move into place quickly before the final gap-1 pass (plain insertion sort) finishes the job.

| | |
|:---|:---|
| **Best Case** | $\mathcal{O}(N \log N)$ |
| **Worst Case** | $\mathcal{O}(N^2)$ (halving gap sequence) |
| **Space** | $\mathcal{O}(1)$ — in-place |
| **Stable** | ❌ No |

---

## Comparison Summary

| Algorithm | Best | Average | Worst | Space | Stable |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Bubble Sort | $O(N)$ | $O(N^2)$ | $O(N^2)$ | $O(1)$ | ✅ |
| Insertion Sort | $O(N)$ | $O(N^2)$ | $O(N^2)$ | $O(1)$ | ✅ |
| Selection Sort | $O(N^2)$ | $O(N^2)$ | $O(N^2)$ | $O(1)$ | ❌ |
| Merge Sort | $O(N \log N)$ | $O(N \log N)$ | $O(N \log N)$ | $O(N)$ | ✅ |
| Quick Sort | $O(N \log N)$ | $O(N \log N)$ | $O(N^2)$ | $O(\log N)$ | ❌ |
| Heap Sort | $O(N \log N)$ | $O(N \log N)$ | $O(N \log N)$ | $O(1)$ | ❌ |
| Counting Sort | $O(N + K)$ | $O(N + K)$ | $O(N + K)$ | $O(N + K)$ | ✅ |
| Radix Sort | $O(D(N+B))$ | $O(D(N+B))$ | $O(D(N+B))$ | $O(N + B)$ | ✅ |
| Shell Sort | $O(N \log N)$ | $O(N^{1.5})$ | $O(N^2)$ | $O(1)$ | ❌ |

---

## How to Run

```bash
python ./dsa/sorting/bubblesort.py
python ./dsa/sorting/insertionsort.py
python ./dsa/sorting/selectionsort.py
python ./dsa/sorting/mergesort.py
python ./dsa/sorting/quicksort.py
python ./dsa/sorting/heapsort.py
python ./dsa/sorting/countingsort.py
python ./dsa/sorting/radixsort.py
python ./dsa/sorting/shellsort.py
```
