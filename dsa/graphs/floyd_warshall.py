"""
Floyd-Warshall Algorithm — All-Pairs Shortest Path
------------------------------------------------------
Technique : Dynamic Programming over intermediate vertices
Idea      : Compute the shortest distance between EVERY pair of vertices at
            once. The key idea: for each vertex k, check whether routing a
            path through k gives a shorter distance than the current best
            known distance between every pair (i, j).

Formula / Recurrence
    dist[i][j] represents the shortest distance from i to j found so far,
    allowing intermediate vertices from {1, ..., k}.

    Recurrence (as k grows from 0 to V-1):
        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    Base case: dist[i][j] = edge weight (i, j) if it exists, 0 if i == j,
               infinity otherwise.

Steps
    1. Initialise dist[i][j] from direct edges (infinity if no edge, 0 on
       the diagonal).
    2. For each candidate intermediate vertex k (0 to V-1):
       For each pair (i, j):
           If going i -> k -> j is shorter than the current i -> j,
           update dist[i][j].
    3. After considering all vertices as intermediates, dist[i][j] holds
       the true shortest distance between every pair.
    4. A negative value on the diagonal (dist[i][i] < 0) indicates a
       negative-weight cycle.

Time  Complexity : O(V^3)  — three nested loops over all vertices
Space Complexity : O(V^2)  — the full distance matrix
"""

class FloydWarshall:
    def __init__(self, vertices, edges):
        self.vertices = list(vertices)   # list of all vertex labels
        self.edges = edges               # list of (u, v, weight) tuples

    def all_pairs_shortest_paths(self):
        vertices = self.vertices
        dist = {u: {v: float('inf') for v in vertices} for u in vertices}
        for v in vertices:
            dist[v][v] = 0
        for u, v, w in self.edges:
            dist[u][v] = min(dist[u][v], w)

        for k in vertices:
            for i in vertices:
                for j in vertices:
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        return dist


n = int(input("enter number of directed edges: "))
vertices = set()
edges = []
for _ in range(n):
    u, v, w = input("enter edge (u v weight): ").split()
    vertices.update([u, v])
    edges.append((u, v, int(w)))
result = FloydWarshall(vertices, edges).all_pairs_shortest_paths()
print("all-pairs shortest distances:")
for u in result:
    print(f"  {u}: {result[u]}")
