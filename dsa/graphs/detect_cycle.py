"""
Cycle Detection in a Directed Graph
--------------------------------------
Technique : DFS with three-colour vertex marking
Idea      : A directed graph has a cycle if and only if DFS ever encounters
            a "back edge" — an edge pointing to a vertex that is currently
            on the active recursion stack (an ancestor in the DFS tree).
            Three colours distinguish "still exploring" from "fully done":

Formula / Property
    WHITE (unvisited)  : not yet reached by DFS.
    GRAY  (in progress): on the current recursion stack — an ancestor.
    BLACK (finished)    : this vertex and everything reachable from it has
                          been fully explored; safe to revisit from anywhere.

    An edge (u, v) is a back edge — and therefore proves a cycle exists —
    exactly when v is GRAY at the moment u examines it.

Steps
    1. Mark every vertex WHITE initially.
    2. For each unvisited (WHITE) vertex, run DFS:
       a. Mark the current vertex GRAY (entering the recursion stack).
       b. For each neighbor:
          - If GRAY: a back edge was found — the graph has a cycle.
          - If WHITE: recurse into it.
       c. Mark the current vertex BLACK once all neighbors are processed
          (leaving the recursion stack).
    3. If no back edge is ever found, the graph is acyclic (a DAG).

Time  Complexity : O(V + E)  — every vertex and edge visited once
Space Complexity : O(V)      — colour map + recursion stack
"""

WHITE, GRAY, BLACK = 0, 1, 2

class DetectCycle:
    def __init__(self, graph):
        self.graph = graph

    def _has_cycle_from(self, node, color):
        color[node] = GRAY
        for neighbor in self.graph.get(node, []):
            if color.get(neighbor, WHITE) == GRAY:
                return True
            if color.get(neighbor, WHITE) == WHITE and self._has_cycle_from(neighbor, color):
                return True
        color[node] = BLACK
        return False

    def has_cycle(self):
        color = {node: WHITE for node in self.graph}
        for node in self.graph:
            if color[node] == WHITE:
                if self._has_cycle_from(node, color):
                    return True
        return False


n = int(input("enter number of directed edges: "))
graph = {}
for _ in range(n):
    u, v = input("enter edge (u v): ").split()
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, [])
print("graph has a cycle:", DetectCycle(graph).has_cycle())
