"""
Breadth-First Search (BFS)
--------------------------
Technique : Level-order graph traversal using a FIFO queue
Idea      : Explore all neighbors of the current node before moving deeper.
            Visits nodes in order of their distance (number of edges) from
            the start node.

Formula / Property
    Level d contains all nodes reachable in exactly d edges from start.
    BFS visits levels 0, 1, 2, ... in order.
    Shortest path (unweighted graph): dist[v] = level at which v is first visited.

    Queue invariant:
        All nodes at level d are in the queue before any node at level d+1
        is enqueued.

Steps
    1. Enqueue the start node; mark it visited.
    2. While the queue is not empty:
       a. Dequeue node u.
       b. Record u in traversal order.
       c. For each unvisited neighbor v of u:
          - Mark v visited.
          - Enqueue v.
    3. Return traversal order.

Time  Complexity : O(V + E)  — every vertex and edge is processed once
Space Complexity : O(V)      — visited set + queue hold at most V nodes
"""

from collections import deque

class BFS:
    def __init__(self, graph):
        self.graph = graph

    def traverse(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return order


n = int(input("enter number of edges: "))
graph = {}
for _ in range(n):
    u, v = input("enter edge (u v): ").split()
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)
start = input("enter start node: ")
bfs = BFS(graph)
print("bfs traversal:", bfs.traverse(start))
