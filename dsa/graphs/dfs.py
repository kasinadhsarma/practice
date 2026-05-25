"""
Depth-First Search (DFS)
------------------------
Technique : Recursive graph traversal using the call stack (implicit LIFO stack)
Idea      : Explore as far as possible along each branch before backtracking.
            Goes deep into the graph before visiting siblings.

Formula / Property
    DFS tree edges classify graph edges into:
        Tree edges   — edges in the DFS tree
        Back edges   — point to an ancestor (indicate cycles in directed graphs)
        Forward/Cross edges — in directed graphs only

    Recursion relation:
        DFS(u):
            mark u as visited
            for each neighbor v of u:
                if v not visited: DFS(v)

Steps
    1. Start from the given node; mark it visited.
    2. Add node to traversal order.
    3. For each unvisited neighbor, recurse (DFS).
    4. Backtrack when all neighbors are visited.
    5. Return traversal order.

Applications
    - Cycle detection
    - Topological sorting
    - Finding connected components
    - Solving mazes / puzzles

Time  Complexity : O(V + E)  — every vertex and edge visited once
Space Complexity : O(V)      — recursion stack depth up to V in worst case
"""

class DFS:
    def __init__(self, graph):
        self.graph = graph

    def _dfs(self, node, visited, order):
        visited.add(node)
        order.append(node)
        for neighbor in self.graph.get(node, []):
            if neighbor not in visited:
                self._dfs(neighbor, visited, order)

    def traverse(self, start):
        visited = set()
        order = []
        self._dfs(start, visited, order)
        return order


n = int(input("enter number of edges: "))
graph = {}
for _ in range(n):
    u, v = input("enter edge (u v): ").split()
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)
start = input("enter start node: ")
dfs = DFS(graph)
print("dfs traversal:", dfs.traverse(start))
