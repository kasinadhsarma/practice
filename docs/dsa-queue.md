# 🎟️ DSA — Queue

**Location:** [`dsa/queue/`](../dsa/queue/)

A **Queue** is a FIFO (First-In-First-Out) structure — the first element enqueued is the first one dequeued. Unlike a stack, insertion and removal happen at opposite ends.

---

## Queue (via `collections.deque`) — `queue_array.py`

A plain Python list is a poor backing structure for a queue — `list.pop(0)` is O(N) since every remaining element has to shift. `collections.deque` gives O(1) at both ends, so it backs this implementation.

| Operation | Time | Description |
|:---|:---|:---|
| `enqueue(val)` | $\mathcal{O}(1)$ | Append to the rear |
| `dequeue()` | $\mathcal{O}(1)$ | Remove and return the front |
| `peek()` | $\mathcal{O}(1)$ | — |
| `is_empty()` | $\mathcal{O}(1)$ | — |

**Applications:** task scheduling, print queues, BFS traversal (see [`dsa/graphs/bfs.py`](../dsa/graphs/bfs.py)).

---

## Circular Queue — `circular_queue.py`

A fixed-capacity ring buffer over an array — `front` and `rear` wrap around via modulo arithmetic, so slots freed near the beginning get reused once `rear` wraps back around, with no resizing.

### Formula

```
next_rear  = (rear + 1) % capacity
next_front = (front + 1) % capacity
full  when count == capacity
empty when count == 0
```

| Operation | Time |
|:---|:---|
| `enqueue(val)` | $\mathcal{O}(1)$ |
| `dequeue()` | $\mathcal{O}(1)$ |

**Applications:** fixed-size input/streaming buffers, CPU scheduling ring buffers.

---

## Queue Using Two Stacks — `queue_using_stacks.py`

Demonstrates building a FIFO purely from LIFO primitives: push everything onto `stack_in`; when `stack_out` runs dry, pour all of `stack_in` into it (this reversal puts the oldest element on top).

| Operation | Time |
|:---|:---|
| `enqueue(val)` | $\mathcal{O}(1)$ |
| `dequeue()` | $\mathcal{O}(1)$ amortized, $\mathcal{O}(N)$ worst case |

---

## Deque (Double-Ended Queue) — `deque_basic.py`

Generalizes stack (one end) and queue (opposite ends) — push/pop is O(1) at **either** end.

| Operation | Time |
|:---|:---|
| `add_front` / `add_rear` | $\mathcal{O}(1)$ |
| `remove_front` / `remove_rear` | $\mathcal{O}(1)$ |

**Applications:** sliding window maximum/minimum via a monotonic deque (see [`dsa/Arrays/08_advanced_techniques.py`](../dsa/Arrays/08_advanced_techniques.py) → `sliding_window_max`), palindrome checking from both ends inward.

---

## How to Run

```bash
python ./dsa/queue/queue_array.py
python ./dsa/queue/circular_queue.py
python ./dsa/queue/queue_using_stacks.py
python ./dsa/queue/deque_basic.py
```
