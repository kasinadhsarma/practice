# 🌐 DSA — Graph Algorithms

**Location:** [`dsa/graphs/`](../dsa/graphs/)

Ten graph algorithms — traversal, minimum spanning trees, shortest paths, topological ordering, cycle detection, and connected components — each implemented as an OOP class with detailed complexity analysis.

---

## Algorithms

### 🔵 Breadth-First Search (BFS) — `bfs.py`

Explores all neighbors of the current node before moving deeper. Uses a FIFO **queue** to process nodes level by level.

| Property | Detail |
|:---|:---|
| **Data Structure** | Queue (`collections.deque`) |
| **Traversal Order** | Level-order (by distance from start) |
| **Shortest Path** | ✅ Finds shortest path in unweighted graphs |
| **Time Complexity** | $\mathcal{O}(V + E)$ — every vertex and edge processed once |
| **Space Complexity** | $\mathcal{O}(V)$ — visited set + queue |

**Queue Invariant:** All nodes at level $d$ are in the queue before any node at level $d+1$ is enqueued.

---

### 🔴 Depth-First Search (DFS) — `dfs.py`

Explores as far as possible along each branch before backtracking. Uses a **stack** (or recursion).

| Property | Detail |
|:---|:---|
| **Data Structure** | Stack (implicit via recursion or explicit) |
| **Traversal Order** | Deep-branch first |
| **Use Cases** | Cycle detection, topological sort, connected components |
| **Time Complexity** | $\mathcal{O}(V + E)$ |
| **Space Complexity** | $\mathcal{O}(V)$ — visited set + call stack |

---

### 🌲 Kruskal's Algorithm — `krushkals_algorithm.py`

Finds the **Minimum Spanning Tree (MST)** by greedily adding the cheapest edge that doesn't create a cycle. Uses **Union-Find (Disjoint Set Union)** for cycle detection.

| Property | Detail |
|:---|:---|
| **Approach** | Greedy — sort edges by weight |
| **Cycle Detection** | Union-Find (DSU) |
| **Time Complexity** | $\mathcal{O}(E \log E)$ — dominated by edge sorting |
| **Space Complexity** | $\mathcal{O}(V)$ — parent/rank arrays |
| **Best For** | Sparse graphs (few edges) |

**Steps:**
1. Sort all edges by weight ascending.
2. For each edge `(u, v, w)`: if `u` and `v` are in different components, add edge to MST and union them.
3. Stop when MST has `V - 1` edges.

---

### 🟢 Prim's Algorithm — `prims_minimum_spanning_tree.py`

Finds the **MST** by growing the tree one vertex at a time, always picking the cheapest edge connecting the current tree to a new vertex. Uses a **min-heap (priority queue)**.

| Property | Detail |
|:---|:---|
| **Approach** | Greedy — always pick min-weight edge from tree frontier |
| **Data Structure** | Min-heap (priority queue) |
| **Time Complexity** | $\mathcal{O}(E \log V)$ with min-heap |
| **Space Complexity** | $\mathcal{O}(V + E)$ |
| **Best For** | Dense graphs (many edges) |

**Key Difference from Kruskal's:**
- Kruskal's works on **edges** globally.
- Prim's grows a **connected tree** starting from one vertex.

---

### 🛣️ Dijkstra's Algorithm — `dijkstra.py`

Single-source shortest path for graphs with **non-negative** edge weights. Greedily finalises the closest not-yet-visited node using a min-heap.

| Property | Detail |
|:---|:---|
| **Approach** | Greedy + min-heap |
| **Requires** | Non-negative edge weights |
| **Time Complexity** | $\mathcal{O}((V + E) \log V)$ |
| **Space Complexity** | $\mathcal{O}(V + E)$ |

---

### ⚖️ Bellman-Ford Algorithm — `bellman_ford.py`

Single-source shortest path that tolerates **negative** edge weights, by relaxing every edge $V-1$ times. One extra pass detects negative-weight cycles.

| Property | Detail |
|:---|:---|
| **Approach** | Dynamic Programming — repeated edge relaxation |
| **Handles Negative Weights** | ✅ Yes |
| **Detects Negative Cycles** | ✅ Yes |
| **Time Complexity** | $\mathcal{O}(V \times E)$ |
| **Space Complexity** | $\mathcal{O}(V)$ |

---

### 📋 Topological Sort (Kahn's Algorithm) — `topological_sort.py`

Produces a linear ordering of a DAG's vertices such that every edge `(u, v)` has `u` before `v`. Repeatedly removes vertices with in-degree 0.

| Property | Detail |
|:---|:---|
| **Approach** | BFS via in-degree counting |
| **Requires** | Directed Acyclic Graph (DAG) |
| **Cycle Handling** | Returns an error message if a cycle prevents a valid ordering |
| **Time Complexity** | $\mathcal{O}(V + E)$ |
| **Space Complexity** | $\mathcal{O}(V)$ |

---

### 🗺️ Floyd-Warshall Algorithm — `floyd_warshall.py`

Computes shortest distances between **every pair** of vertices at once, by considering each vertex as a potential intermediate stop.

| Property | Detail |
|:---|:---|
| **Approach** | Dynamic Programming over intermediate vertices |
| **Result** | Full $V \times V$ shortest-distance matrix |
| **Time Complexity** | $\mathcal{O}(V^3)$ |
| **Space Complexity** | $\mathcal{O}(V^2)$ |

---

### 🔁 Cycle Detection (Directed) — `detect_cycle.py`

Detects whether a directed graph contains a cycle using three-colour DFS marking (white/gray/black) — a back edge to a GRAY (in-progress) vertex proves a cycle exists.

| Property | Detail |
|:---|:---|
| **Approach** | DFS with three-colour marking |
| **Time Complexity** | $\mathcal{O}(V + E)$ |
| **Space Complexity** | $\mathcal{O}(V)$ |

---

### 🧩 Connected Components — `connected_components.py`

Finds all connected components of an undirected graph by restarting BFS from every unvisited vertex.

| Property | Detail |
|:---|:---|
| **Approach** | Repeated BFS from unvisited vertices |
| **Time Complexity** | $\mathcal{O}(V + E)$ |
| **Space Complexity** | $\mathcal{O}(V)$ |

---

## BFS vs DFS — Quick Reference

| | BFS | DFS |
|:---|:---|:---|
| Strategy | Breadth-first (level-by-level) | Depth-first (branch-by-branch) |
| Data Structure | Queue | Stack / Recursion |
| Shortest Path | ✅ (unweighted) | ❌ |
| Memory Usage | More (holds whole frontier) | Less (holds current path) |
| Use Case | Shortest path, level-order | Cycle detection, topological sort |

---

## Kruskal's vs Prim's — Quick Reference

| | Kruskal's | Prim's |
|:---|:---|:---|
| Approach | Sort all edges | Grow tree greedily |
| Data Structure | Union-Find | Min-Heap |
| Best For | Sparse graphs | Dense graphs |
| Time Complexity | $O(E \log E)$ | $O(E \log V)$ |

---

## How to Run

```bash
python ./dsa/graphs/bfs.py
python ./dsa/graphs/dfs.py
python ./dsa/graphs/krushkals_algorithm.py
python ./dsa/graphs/prims_minimum_spanning_tree.py
python ./dsa/graphs/dijkstra.py
python ./dsa/graphs/bellman_ford.py
python ./dsa/graphs/topological_sort.py
python ./dsa/graphs/floyd_warshall.py
python ./dsa/graphs/detect_cycle.py
python ./dsa/graphs/connected_components.py
```
