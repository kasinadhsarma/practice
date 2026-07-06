"""
Bellman-Ford Algorithm — Single-Source Shortest Path (with negative weights)
------------------------------------------------------------------------------
Technique : Dynamic Programming — repeated edge relaxation
Idea      : Unlike Dijkstra, Bellman-Ford tolerates negative edge weights by
            relaxing every edge, repeatedly, V-1 times. After V-1 rounds, the
            shortest path to any node (at most V-1 edges long, since a
            shortest path never repeats a vertex) is guaranteed to be found.
            One extra round detects negative-weight cycles.

Formula / Property
    dist[start] = 0, dist[v] = infinity for all other v initially.
    Relaxation step for edge (u, v, w):
        if dist[u] + w < dist[v]:  dist[v] = dist[u] + w

    Any simple shortest path has at most (V - 1) edges, so after (V - 1)
    full relaxation passes over every edge, all distances are final —
    UNLESS a negative-weight cycle is reachable from start, in which case
    distances could keep shrinking forever.

Steps
    1. Set dist[start] = 0, all others = infinity.
    2. Repeat (V - 1) times: relax every edge (u, v, w) in the graph.
    3. Run one more relaxation pass: if any distance can still improve,
       a negative-weight cycle exists (reachable from start).
    4. Return the dist map, plus whether a negative cycle was detected.

Time  Complexity : O(V * E)  — V-1 (+1 check) passes over all E edges
Space Complexity : O(V)      — dist map
"""

class BellmanFord:
    def __init__(self, vertices, edges):
        self.vertices = vertices          # list of all vertex labels
        self.edges = edges                # list of (u, v, weight) tuples

    def shortest_paths(self, start):
        dist = {v: float('inf') for v in self.vertices}
        dist[start] = 0

        for _ in range(len(self.vertices) - 1):
            for u, v, w in self.edges:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        has_negative_cycle = False
        for u, v, w in self.edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                has_negative_cycle = True
                break

        return dist, has_negative_cycle


n = int(input("enter number of directed edges: "))
vertices = set()
edges = []
for _ in range(n):
    u, v, w = input("enter edge (u v weight): ").split()
    vertices.update([u, v])
    edges.append((u, v, int(w)))
start = input("enter start node: ")
dist, has_negative_cycle = BellmanFord(vertices, edges).shortest_paths(start)
print("shortest distances:", dist)
print("negative cycle detected:", has_negative_cycle)
