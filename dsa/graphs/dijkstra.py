"""
Dijkstra's Algorithm — Single-Source Shortest Path
----------------------------------------------------
Technique : Greedy + Min-Heap (priority queue)
Idea      : Find the shortest distance from a start node to every other node
            in a weighted graph with non-negative edge weights. Always expand
            the closest not-yet-finalised node next — once a node is popped
            from the heap with its current best distance, that distance can
            never be improved (because all remaining edge weights are >= 0).

Formula / Property
    dist[start] = 0, dist[v] = infinity for all other v initially.
    Relaxation step for edge (u, v, w):
        if dist[u] + w < dist[v]:  dist[v] = dist[u] + w

    Min-heap stores (distance, node); always pop the smallest distance next.
    A node may be pushed multiple times with different distances — the
    `visited` (finalised) check skips stale, superseded heap entries.

Steps
    1. Set dist[start] = 0, all others = infinity.
    2. Push (0, start) onto a min-heap.
    3. While the heap is not empty:
       a. Pop (d, node) with smallest distance.
       b. Skip if node is already finalised (visited).
       c. Mark node finalised.
       d. For each neighbor via edge weight w: relax dist[neighbor] and
          push (new distance, neighbor) if it improves on the best known.
    4. Return the dist map (unreachable nodes stay at infinity).

Requires   : non-negative edge weights (negative weights need Bellman-Ford)
Time  Complexity : O((V + E) log V)  — each edge may push once onto the heap
Space Complexity : O(V + E)          — dist map + adjacency list + heap
"""

import heapq

class Dijkstra:
    def __init__(self, graph):
        self.graph = graph

    def shortest_paths(self, start):
        dist = {node: float('inf') for node in self.graph}
        dist[start] = 0
        visited = set()
        min_heap = [(0, start)]

        while min_heap:
            d, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)

            for neighbor, weight in self.graph.get(node, []):
                new_dist = d + weight
                if new_dist < dist.get(neighbor, float('inf')):
                    dist[neighbor] = new_dist
                    heapq.heappush(min_heap, (new_dist, neighbor))

        return dist


n = int(input("enter number of directed edges: "))
graph = {}
for _ in range(n):
    u, v, w = input("enter edge (u v weight): ").split()
    w = int(w)
    graph.setdefault(u, []).append((v, w))
    graph.setdefault(v, [])
start = input("enter start node: ")
result = Dijkstra(graph).shortest_paths(start)
print("shortest distances:", result)
