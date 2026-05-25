"""
tests/dsa/test_dsa_graphs.py
=============================
Tests for graph algorithms under dsa/graphs/:
    BFS · DFS · KruskalsMST · PrimsMST
"""

import pytest
from tests.utils import load_module

# ── Module loaders ─────────────────────────────────────────────────────────────

def _BFS():
    return load_module('dsa/graphs/bfs.py',                        ['0','A'], alias='dsa_bfs').BFS

def _DFS():
    return load_module('dsa/graphs/dfs.py',                        ['0','A'], alias='dsa_dfs').DFS

def _KruskalsMST():
    return load_module('dsa/graphs/krushkals_algorithm.py',        ['0'],     alias='dsa_kruskal').KruskalsMST

def _PrimsMST():
    return load_module('dsa/graphs/prims_minimum_spanning_tree.py',['0','A'], alias='dsa_prims').PrimsMST


# ── Shared graphs ─────────────────────────────────────────────────────────────

GRAPH_LINEAR = {
    'A': ['B'], 'B': ['A', 'C'], 'C': ['B', 'D'], 'D': ['C'],
}
GRAPH_DIAMOND = {
    'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'D'], 'D': ['B', 'C'],
}


# ═════════════════════════════════════════════════════════════════════════════

class TestBFS:

    def test_linear_from_a(self):
        assert _BFS()(GRAPH_LINEAR).traverse('A') == ['A', 'B', 'C', 'D']

    def test_linear_from_c(self):
        assert _BFS()(GRAPH_LINEAR).traverse('C') == ['C', 'B', 'D', 'A']

    def test_diamond_visits_all(self):
        assert set(_BFS()(GRAPH_DIAMOND).traverse('A')) == {'A', 'B', 'C', 'D'}

    def test_diamond_start_is_first(self):
        assert _BFS()(GRAPH_DIAMOND).traverse('A')[0] == 'A'

    def test_diamond_level_order(self):
        order = _BFS()(GRAPH_DIAMOND).traverse('A')
        a, b, c, d = (order.index(n) for n in 'ABCD')
        assert a < b and a < c and b < d and c < d

    def test_single_node(self):
        assert _BFS()({'Z': []}).traverse('Z') == ['Z']

    def test_no_duplicates(self):
        order = _BFS()(GRAPH_DIAMOND).traverse('A')
        assert len(order) == len(set(order))

    def test_isolated_start(self):
        assert _BFS()({}).traverse('X') == ['X']


class TestDFS:

    def test_linear_from_a(self):
        assert _DFS()(GRAPH_LINEAR).traverse('A') == ['A', 'B', 'C', 'D']

    def test_diamond_visits_all(self):
        assert set(_DFS()(GRAPH_DIAMOND).traverse('A')) == {'A', 'B', 'C', 'D'}

    def test_diamond_start_is_first(self):
        assert _DFS()(GRAPH_DIAMOND).traverse('A')[0] == 'A'

    def test_depth_before_breadth(self):
        order = _DFS()(GRAPH_DIAMOND).traverse('A')
        a, b, d = order.index('A'), order.index('B'), order.index('D')
        assert a < b < d   # goes deep through B before backtracking

    def test_single_node(self):
        assert _DFS()({'Z': []}).traverse('Z') == ['Z']

    def test_no_duplicates(self):
        order = _DFS()(GRAPH_DIAMOND).traverse('A')
        assert len(order) == len(set(order))

    def test_isolated_start(self):
        assert _DFS()({}).traverse('X') == ['X']


class TestKruskalsMST:
    """
    Reference graph (4 vertices):
        0─10─1
        │╲    │
        6  5  15
        │    ╲│
        2──4──3
    MST: edges (2,3,4)+(0,3,5)+(0,1,10)  total=19
    """

    def _graph(self):
        v = {'0','1','2','3'}
        k = _KruskalsMST()(v)
        for u, w, wt in [('0','1',10),('0','2',6),('0','3',5),('1','3',15),('2','3',4)]:
            k.add_edge(u, w, wt)
        return k

    def test_edge_count(self):
        assert len(self._graph().minimum_spanning_tree()) == 3   # V-1

    def test_total_weight(self):
        mst = self._graph().minimum_spanning_tree()
        assert sum(w for _, _, w in mst) == 19

    def test_cheapest_edge_included(self):
        mst   = self._graph().minimum_spanning_tree()
        pairs = {(u, v) for u, v, _ in mst} | {(v, u) for u, v, _ in mst}
        assert ('2', '3') in pairs

    def test_single_vertex(self):
        assert _KruskalsMST()({'A'}).minimum_spanning_tree() == []

    def test_two_vertices(self):
        k = _KruskalsMST()({'A', 'B'})
        k.add_edge('A', 'B', 7)
        mst = k.minimum_spanning_tree()
        assert len(mst) == 1 and mst[0][2] == 7

    def test_mst_spans_all_vertices(self):
        mst = self._graph().minimum_spanning_tree()
        adj = {}
        for u, v, _ in mst:
            adj.setdefault(u, []).append(v)
            adj.setdefault(v, []).append(u)
        visited, stack = set(), [mst[0][0]]
        while stack:
            n = stack.pop()
            if n not in visited:
                visited.add(n); stack.extend(adj.get(n, []))
        assert visited == {'0', '1', '2', '3'}


class TestPrimsMST:
    """
    Reference triangle graph:  A─1─B─2─C─3─A
    MST: (A-B,1)+(B-C,2)  total=3
    """

    TRIANGLE = {
        'A': [('B', 1), ('C', 3)],
        'B': [('A', 1), ('C', 2)],
        'C': [('A', 3), ('B', 2)],
    }

    def test_total_cost(self):
        _, cost = _PrimsMST()(self.TRIANGLE).minimum_spanning_tree('A')
        assert cost == 3

    def test_edge_count(self):
        mst, _ = _PrimsMST()(self.TRIANGLE).minimum_spanning_tree('A')
        assert len(mst) == 2

    def test_all_vertices_connected(self):
        mst, _ = _PrimsMST()(self.TRIANGLE).minimum_spanning_tree('A')
        verts = {u for u, _, _ in mst} | {v for _, v, _ in mst}
        assert 'B' in verts and 'C' in verts

    def test_single_vertex(self):
        mst, cost = _PrimsMST()({'A': []}).minimum_spanning_tree('A')
        assert mst == [] and cost == 0

    def test_four_vertex_graph(self):
        graph = {
            'A': [('B',1),('C',4)], 'B': [('A',1),('C',2),('D',5)],
            'C': [('A',4),('B',2),('D',1)], 'D': [('B',5),('C',1)],
        }
        mst, cost = _PrimsMST()(graph).minimum_spanning_tree('A')
        assert cost == 4 and len(mst) == 3
