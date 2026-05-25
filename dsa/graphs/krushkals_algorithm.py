"""
Kruskal's Algorithm — Minimum Spanning Tree
--------------------------------------------
Technique : Greedy + Disjoint Set Union (Union-Find)
Idea      : Sort all edges by weight. Add an edge to the MST only if it does
            NOT form a cycle with the edges already chosen. Use Union-Find to
            detect cycles in O(α(n)) ≈ O(1) amortised time.

Formula / Property
    MST has exactly (V - 1) edges for a connected graph with V vertices.
    Total MST weight is minimised — greedy choice is safe because:
        Adding the cheapest edge that connects two different components
        never prevents a globally optimal solution (matroid property).

    Union-Find with path compression + union by rank:
        find(x) : follow parent pointers to root; compress path on the way back
        union(x, y): attach smaller-rank tree under larger-rank root

Steps
    1. Sort all edges in non-decreasing order of weight.
    2. Initialise each vertex as its own component (parent[v] = v).
    3. For each edge (u, v, w) in sorted order:
       a. If find(u) ≠ find(v)  →  they are in different components.
          - Add edge to MST.
          - union(u, v) to merge the two components.
    4. Stop when MST has (V - 1) edges.

Time  Complexity : O(E log E)  — dominated by sorting edges
Space Complexity : O(V)        — parent and rank arrays
"""

class KruskalsMST:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))

    def _find(self, parent, node):
        # path compression
        if parent[node] != node:
            parent[node] = self._find(parent, parent[node])
        return parent[node]

    def _union(self, parent, rank, u, v):
        ru, rv = self._find(parent, u), self._find(parent, v)
        if rank[ru] < rank[rv]:
            parent[ru] = rv
        elif rank[ru] > rank[rv]:
            parent[rv] = ru
        else:
            parent[rv] = ru
            rank[ru] += 1

    def minimum_spanning_tree(self):
        self.edges.sort()
        parent = {v: v for v in self.vertices}
        rank   = {v: 0 for v in self.vertices}
        mst = []
        for weight, u, v in self.edges:
            if self._find(parent, u) != self._find(parent, v):
                self._union(parent, rank, u, v)
                mst.append((u, v, weight))
        return mst


n = int(input("enter number of edges: "))
vertices = set()
kmst = KruskalsMST(vertices)
for _ in range(n):
    u, v, w = input("enter edge (u v weight): ").split()
    vertices.update([u, v])
    kmst.add_edge(u, v, int(w))
kmst.vertices = vertices
result = kmst.minimum_spanning_tree()
print("minimum spanning tree edges:")
for u, v, w in result:
    print(f"  {u} -- {v}  weight: {w}")
