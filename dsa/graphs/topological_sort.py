"""
Topological Sort — Kahn's Algorithm
--------------------------------------
Technique : BFS using in-degree counting
Idea      : For a Directed Acyclic Graph (DAG), produce a linear ordering of
            vertices such that every directed edge (u, v) has u appearing
            before v. Repeatedly remove vertices that have no remaining
            incoming edges (in-degree 0) — they can safely go next in the
            order since nothing depends on them anymore.

Formula / Property
    in_degree[v] = number of edges pointing INTO v.
    A vertex can be placed in the ordering only once in_degree[v] == 0.

    If the algorithm processes fewer than V vertices before the queue empties,
    the graph contains a cycle — no valid topological order exists.

Steps
    1. Compute in_degree[v] for every vertex.
    2. Enqueue every vertex with in_degree 0 (no prerequisites).
    3. While the queue is not empty:
       a. Dequeue node u; append it to the result order.
       b. For each neighbor v of u: decrement in_degree[v].
          If in_degree[v] becomes 0, enqueue v.
    4. If the result contains all V vertices, return it; otherwise the
       graph has a cycle and no topological order exists.

Time  Complexity : O(V + E)  — every vertex and edge processed once
Space Complexity : O(V)      — in-degree map + queue + result order
"""

from collections import deque

class TopologicalSort:
    def __init__(self, graph):
        self.graph = graph

    def sort(self):
        in_degree = {node: 0 for node in self.graph}
        for node in self.graph:
            for neighbor in self.graph[node]:
                in_degree[neighbor] = in_degree.get(neighbor, 0) + 1

        queue = deque([node for node in in_degree if in_degree[node] == 0])
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in self.graph.get(node, []):
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(order) != len(in_degree):
            return "Graph has a cycle — no topological order exists"
        return order


n = int(input("enter number of directed edges: "))
graph = {}
for _ in range(n):
    u, v = input("enter edge (u v): ").split()
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, [])
result = TopologicalSort(graph).sort()
print("topological order:", result)
