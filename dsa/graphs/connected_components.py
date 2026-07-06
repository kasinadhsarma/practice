"""
Connected Components (Undirected Graph)
-------------------------------------------
Technique : Repeated BFS/DFS from every unvisited vertex
Idea      : A connected component is a maximal set of vertices that can all
            reach each other. Running a traversal (BFS here) from any
            unvisited vertex discovers its entire component; repeating this
            from the next unvisited vertex finds the next component, and so
            on until every vertex has been assigned to some component.

Formula / Property
    Number of connected components = number of times a traversal must be
    restarted from a fresh, unvisited vertex.

    A graph is fully connected (single component) iff exactly one restart
    is ever needed, i.e. the first BFS/DFS already visits every vertex.

Steps
    1. Mark all vertices unvisited.
    2. For each vertex not yet visited:
       a. Start a new component; run BFS from that vertex, marking every
          reachable vertex as visited and adding it to this component.
       b. Store the completed component.
    3. Return the list of components found.

Time  Complexity : O(V + E)  — every vertex and edge visited exactly once overall
Space Complexity : O(V)      — visited set + queue + component lists
"""

from collections import deque

class ConnectedComponents:
    def __init__(self, graph):
        self.graph = graph

    def _bfs_component(self, start, visited):
        component = []
        queue = deque([start])
        visited.add(start)
        while queue:
            node = queue.popleft()
            component.append(node)
            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return component

    def find_components(self):
        visited = set()
        components = []
        for node in self.graph:
            if node not in visited:
                components.append(self._bfs_component(node, visited))
        return components

    def count(self):
        return len(self.find_components())


n = int(input("enter number of edges: "))
graph = {}
for _ in range(n):
    u, v = input("enter edge (u v): ").split()
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)
cc = ConnectedComponents(graph)
print("components:", cc.find_components())
print("count:", cc.count())
