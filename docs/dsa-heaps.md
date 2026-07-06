# 🏔️ DSA — Heap Data Structure

**Location:** [`dsa/heaps/`](../dsa/heaps/)

A **Heap** is a complete binary tree stored as an implicit array. The heap property guarantees $\mathcal{O}(1)$ access to the maximum (or minimum) element and $\mathcal{O}(\log N)$ insertion and removal.

---

## Max-Heap — `maxheap.py`

Every parent node is **greater than or equal to** its children. The **root always holds the maximum element**.

### Array Representation

For a node at index `i` (0-based):

```
parent(i)      = (i - 1) // 2
left_child(i)  = 2*i + 1
right_child(i) = 2*i + 2
```

**Heap Property:** `heap[parent] >= heap[child]` for every node.

---

### Operations

#### `insert(val)` — $\mathcal{O}(\log N)$
1. Append `val` to the end of the array.
2. **Bubble up (sift up):** while `val > parent`, swap them.
   Restores heap property from bottom to top.

#### `extract_max()` — $\mathcal{O}(\log N)$
1. Root (`index 0`) is the maximum.
2. Replace root with the last element; remove last element.
3. **Bubble down (heapify-down):** swap root with its largest child until heap property is restored.

#### `get_max()` — $\mathcal{O}(1)$
1. Return `heap[0]`.

#### Build heap from $N$ elements — $\mathcal{O}(N)$
Using repeated `heapify-down` from index `n//2 - 1` to `0`.

---

### Complexity Summary

| Operation | Time | Space |
|:---|:---|:---|
| `insert` | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| `extract_max` | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| `get_max` | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ |
| Build heap | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

---

### Applications

- **Priority Queues** — always process the highest-priority item first
- **Heap Sort** — see [`dsa/sorting/heapsort.py`](../dsa/sorting/heapsort.py) ($\mathcal{O}(N \log N)$ in-place sort using this same array-heap technique)
- **K Largest / K Smallest Elements** — see `kth_largest_element.py` below
- **Graph Algorithms** — Prim's MST, Dijkstra's Shortest Path

---

## Min-Heap — `minheap.py`

The mirror image of Max-Heap: every parent node is **less than or equal to** its children, so the **root always holds the minimum element**. Every comparison in Max-Heap is simply flipped.

**Heap Property:** `heap[parent] <= heap[child]` for every node.

### Operations

| Operation | Time | Description |
|:---|:---|:---|
| `insert(val)` | $\mathcal{O}(\log N)$ | Append then bubble up while smaller than parent |
| `extract_min()` | $\mathcal{O}(\log N)$ | Swap root with last element, remove, then sift down |
| `get_min()` | $\mathcal{O}(1)$ | Return `heap[0]` |

---

## Kth Largest Element — `kth_largest_element.py`

Finds the k-th largest value in an array **without fully sorting it**, by maintaining a min-heap bounded to size `k`. Every element is pushed; once the heap exceeds size `k`, the smallest is popped. After processing everything, the heap's minimum is exactly the k-th largest value overall.

| Property | Detail |
|:---|:---|
| **Approach** | Bounded min-heap (via `heapq`) |
| **Time Complexity** | $\mathcal{O}(N \log K)$ |
| **Space Complexity** | $\mathcal{O}(K)$ |

---

## How to Run

```bash
python ./dsa/heaps/maxheap.py
python ./dsa/heaps/minheap.py
python ./dsa/heaps/kth_largest_element.py
# Input: space-separated integers to build the heap
# Output: max/min element, extracted value, remaining heap
```
