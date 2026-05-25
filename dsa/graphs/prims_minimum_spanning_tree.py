"""
Prim's Algorithm — Minimum Spanning Tree
-----------------------------------------
Technique : Greedy + Min-Heap (priority queue)
Idea      : Grow the MST one vertex at a time. Start from any vertex. At each
            step, add the minimum-weight edge that connects a visited vertex to
            an unvisited vertex.

Formula / Property
    MST has exactly (V - 1) edges for a connected graph with V vertices.
    Cut property (correctness proof):
        For any cut (S, V-S) of the graph, the minimum weight crossing edge
        belongs to some MST. Prim's greedily picks this edge at every step.

    Min-heap stores (weight, neighbor, parent):
        Always extract the edge with the smallest weight.

Steps
    1. Start from any vertex; push (0, start, None) into the min-heap.
    2. While heap is not empty:
       a. Pop (weight, node, parent) — minimum weight edge.
       b. If node already visited, skip.
       c. Mark node visited; add edge (parent→node) to MST.
       d. Push all (w, neighbor, node) for unvisited neighbors into heap.
    3. Return MST edges and total cost.

Difference from Kruskal's
    Kruskal sorts ALL edges globally; Prim grows locally from one vertex.
    Prim is better for dense graphs; Kruskal for sparse graphs.

Time  Complexity : O(E log V)  — each edge pushed/popped once from heap
Space Complexity : O(V + E)    — heap + adjacency list
"""

import heapq

class PrimsMST:
    def __init__(self, graph):
        self.graph = graph

    def minimum_spanning_tree(self, start):
        visited = set()
        min_heap = [(0, start, None)]
        mst = []
        total_cost = 0
        while min_heap:
            weight, node, parent = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            if parent is not None:
                mst.append((parent, node, weight))
                total_cost += weight
            for neighbor, w in self.graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(min_heap, (w, neighbor, node))
        return mst, total_cost


n = int(input("enter number of edges: "))
graph = {}
for _ in range(n):
    u, v, w = input("enter edge (u v weight): ").split()
    w = int(w)
    graph.setdefault(u, []).append((v, w))
    graph.setdefault(v, []).append((u, w))
start = input("enter start node: ")
prims = PrimsMST(graph)
mst, cost = prims.minimum_spanning_tree(start)
print("minimum spanning tree edges:")
for u, v, w in mst:
    print(f"  {u} -- {v}  weight: {w}")
print("total cost:", cost)
