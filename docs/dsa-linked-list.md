# 🔗 DSA — Linked List

**Location:** [`dsa/linked_list/`](../dsa/linked_list/)

A **Linked List** stores elements as a chain of nodes, each pointing to the next (and, for the doubly-linked variant, the previous). Unlike an array, memory doesn't need to be contiguous — trading O(1) random access for O(1) insertion/deletion at known positions.

---

## Singly Linked List — `singly_linked_list.py`

Each `Node` holds a value and a `next` pointer.

| Operation | Time | Description |
|:---|:---|:---|
| `insert_at_head(val)` | $\mathcal{O}(1)$ | New node's `next` = old head |
| `insert_at_tail(val)` | $\mathcal{O}(N)$ | Walk to the end (no tail pointer kept) |
| `delete_value(val)` | $\mathcal{O}(N)$ | Walk + splice out |
| `search(val)` | $\mathcal{O}(N)$ | Linear walk |

**Applications:** building block for stacks/queues, hash-map bucket chaining.

---

## Doubly Linked List — `doubly_linked_list.py`

Each `DNode` adds a `prev` pointer, and the list keeps a `tail` reference — enabling O(1) tail insertion and O(1) backward traversal.

| Operation | Time | Description |
|:---|:---|:---|
| `insert_at_head` / `insert_at_tail` | $\mathcal{O}(1)$ | Tail pointer avoids the singly-list's O(N) tail insert |
| `delete_value(val)` | $\mathcal{O}(N)$ find + $\mathcal{O}(1)$ unlink | Once found, relinking neighbors is O(1) |
| `traverse_forward` / `traverse_backward` | $\mathcal{O}(N)$ | Via `next` or `prev` |

**Applications:** browser history, undo/redo, LRU cache (O(1) move-to-front / evict-from-back), deque implementations.

---

## Reverse a Linked List — `reverse_linked_list.py`

Two approaches to reversing every `next` pointer so the list runs backward:

| Approach | Time | Space | Idea |
|:---|:---|:---|:---|
| `reverse_iterative` | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | Walk forward, re-pointing `next` to the previous node as you go |
| `reverse_recursive` | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ call stack | Reverse everything after this node first, then fix this node's link |

**Applications:** palindrome-check on a linked list (reverse the second half, compare), "reverse in groups of k" variants.

---

## Detect Cycle — `detect_cycle.py` (Floyd's Algorithm)

Two pointers — `slow` (one step) and `fast` (two steps) — walk from the head. If there's a cycle, `fast` eventually laps `slow` inside the loop; if not, `fast` reaches `None` first. No extra memory (no visited-set) is needed.

| Method | Time | Space | Description |
|:---|:---|:---|:---|
| `has_cycle(head)` | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | `slow is fast` at any point ⇒ cycle |
| `find_cycle_start(head)` | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | After the meeting point, reset one pointer to `head` and advance both one step at a time — they meet again exactly at the cycle's start |

**Applications:** detecting corrupted/circular data structures.

---

## Merge Two Sorted Linked Lists — `merge_two_sorted_lists.py`

The merge step of merge sort, applied to linked lists: repeatedly attach whichever of the two current heads is smaller, then advance that list.

| Property | Detail |
|:---|:---|
| **Approach** | Two-pointer merge with a dummy head node |
| **Time Complexity** | $\mathcal{O}(N + M)$ |
| **Space Complexity** | $\mathcal{O}(1)$ extra — reuses existing nodes |

**Applications:** merging k sorted lists (pairwise, or with a heap — see [`dsa/heaps/`](../dsa/heaps/)).

---

## How to Run

```bash
python ./dsa/linked_list/singly_linked_list.py
python ./dsa/linked_list/doubly_linked_list.py
python ./dsa/linked_list/reverse_linked_list.py
python ./dsa/linked_list/detect_cycle.py
python ./dsa/linked_list/merge_two_sorted_lists.py
```
