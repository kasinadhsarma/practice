"""
tests/dsa/test_dsa_graphs.py
=============================
Tests for graph algorithms under dsa/graphs/:
    BFS · DFS · KruskalsMST · PrimsMST · Dijkstra · BellmanFord ·
    TopologicalSort · FloydWarshall · DetectCycle · ConnectedComponents
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

def _Dijkstra():
    return load_module('dsa/graphs/dijkstra.py', ['0','A'], alias='dsa_dijkstra').Dijkstra

def _BellmanFord():
    return load_module('dsa/graphs/bellman_ford.py', ['0','A'], alias='dsa_bellmanford').BellmanFord

def _TopologicalSort():
    return load_module('dsa/graphs/topological_sort.py', ['0'], alias='dsa_toposort').TopologicalSort

def _FloydWarshall():
    return load_module('dsa/graphs/floyd_warshall.py', ['0'], alias='dsa_floydwarshall').FloydWarshall

def _DetectCycle():
    return load_module('dsa/graphs/detect_cycle.py', ['0'], alias='dsa_detectcycle').DetectCycle

def _ConnectedComponents():
    return load_module('dsa/graphs/connected_components.py', ['0'], alias='dsa_components').ConnectedComponents


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


class TestDijkstra:
    """
    Directed graph:
        A -4-> B      A -1-> C -2-> B      B -1-> D      C -5-> D
    Shortest: A=0, C=1 (direct), B=3 (via C), D=4 (via C,B)
    """

    GRAPH = {
        'A': [('B', 4), ('C', 1)],
        'B': [('D', 1)],
        'C': [('B', 2), ('D', 5)],
        'D': [],
    }

    def test_shortest_distances(self):
        dist = _Dijkstra()(self.GRAPH).shortest_paths('A')
        assert dist == {'A': 0, 'B': 3, 'C': 1, 'D': 4}

    def test_unreachable_node_is_infinity(self):
        graph = {'A': [('B', 1)], 'B': [], 'C': []}
        dist = _Dijkstra()(graph).shortest_paths('A')
        assert dist['C'] == float('inf')

    def test_single_node(self):
        dist = _Dijkstra()({'A': []}).shortest_paths('A')
        assert dist == {'A': 0}

    def test_direct_edge_beaten_by_shorter_path(self):
        # A->B direct is 4, but A->C->B is 1+2=3, so 3 must win
        dist = _Dijkstra()(self.GRAPH).shortest_paths('A')
        assert dist['B'] == 3


class TestBellmanFord:

    def test_shortest_distances(self):
        vertices = {'A', 'B', 'C', 'D'}
        edges = [('A', 'B', 4), ('A', 'C', 1), ('C', 'B', 2), ('B', 'D', 1), ('C', 'D', 5)]
        dist, has_cycle = _BellmanFord()(vertices, edges).shortest_paths('A')
        assert dist == {'A': 0, 'B': 3, 'C': 1, 'D': 4}
        assert has_cycle is False

    def test_handles_negative_weights(self):
        vertices = {'A', 'B', 'C'}
        edges = [('A', 'B', 5), ('A', 'C', 2), ('C', 'B', -3)]
        dist, has_cycle = _BellmanFord()(vertices, edges).shortest_paths('A')
        assert dist == {'A': 0, 'B': -1, 'C': 2}
        assert has_cycle is False

    def test_detects_negative_cycle(self):
        vertices = {'A', 'B', 'C'}
        edges = [('A', 'B', 1), ('B', 'C', -1), ('C', 'A', -1)]
        _, has_cycle = _BellmanFord()(vertices, edges).shortest_paths('A')
        assert has_cycle is True

    def test_unreachable_node_is_infinity(self):
        vertices = {'A', 'B', 'C'}
        edges = [('A', 'B', 1)]
        dist, _ = _BellmanFord()(vertices, edges).shortest_paths('A')
        assert dist['C'] == float('inf')


class TestTopologicalSort:

    def test_valid_dag_ordering(self):
        graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
        order = _TopologicalSort()(graph).sort()
        assert order.index('A') < order.index('B')
        assert order.index('A') < order.index('C')
        assert order.index('B') < order.index('D')
        assert order.index('C') < order.index('D')

    def test_all_vertices_present(self):
        graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
        order = _TopologicalSort()(graph).sort()
        assert set(order) == {'A', 'B', 'C', 'D'}

    def test_cycle_detected(self):
        graph = {'A': ['B'], 'B': ['C'], 'C': ['A']}
        result = _TopologicalSort()(graph).sort()
        assert result == "Graph has a cycle — no topological order exists"

    def test_disconnected_dag(self):
        graph = {'A': ['B'], 'B': [], 'C': ['D'], 'D': []}
        order = _TopologicalSort()(graph).sort()
        assert order.index('A') < order.index('B')
        assert order.index('C') < order.index('D')


class TestFloydWarshall:

    def test_all_pairs_shortest_paths(self):
        vertices = {'A', 'B', 'C', 'D'}
        edges = [('A', 'B', 4), ('A', 'C', 1), ('C', 'B', 2), ('B', 'D', 1), ('C', 'D', 5)]
        dist = _FloydWarshall()(vertices, edges).all_pairs_shortest_paths()
        assert dist['A']['D'] == 4
        assert dist['A']['B'] == 3
        assert dist['A']['A'] == 0

    def test_unreachable_pair_is_infinity(self):
        vertices = {'A', 'B', 'C'}
        edges = [('A', 'B', 1)]
        dist = _FloydWarshall()(vertices, edges).all_pairs_shortest_paths()
        assert dist['A']['C'] == float('inf')
        assert dist['C']['A'] == float('inf')

    def test_agrees_with_dijkstra(self):
        vertices = {'A', 'B', 'C', 'D'}
        edge_list = [('A', 'B', 4), ('A', 'C', 1), ('C', 'B', 2), ('B', 'D', 1), ('C', 'D', 5)]
        fw_dist = _FloydWarshall()(vertices, edge_list).all_pairs_shortest_paths()

        adjacency = {'A': [('B', 4), ('C', 1)], 'B': [('D', 1)], 'C': [('B', 2), ('D', 5)], 'D': []}
        dijkstra_dist = _Dijkstra()(adjacency).shortest_paths('A')

        for node in vertices:
            assert fw_dist['A'][node] == dijkstra_dist[node]


class TestDetectCycle:

    def test_acyclic_graph(self):
        graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
        assert _DetectCycle()(graph).has_cycle() is False

    def test_cyclic_graph(self):
        graph = {'A': ['B'], 'B': ['C'], 'C': ['A']}
        assert _DetectCycle()(graph).has_cycle() is True

    def test_self_loop_is_a_cycle(self):
        graph = {'A': ['A']}
        assert _DetectCycle()(graph).has_cycle() is True

    def test_single_node_no_edges(self):
        assert _DetectCycle()({'A': []}).has_cycle() is False

    def test_disconnected_with_cycle_in_one_component(self):
        graph = {'A': ['B'], 'B': [], 'C': ['D'], 'D': ['C']}
        assert _DetectCycle()(graph).has_cycle() is True


class TestConnectedComponents:

    def test_three_separate_pairs(self):
        graph = {}
        for u, v in [('A', 'B'), ('C', 'D'), ('E', 'F')]:
            graph.setdefault(u, []).append(v)
            graph.setdefault(v, []).append(u)
        cc = _ConnectedComponents()(graph)
        assert cc.count() == 3

    def test_fully_connected_graph_is_one_component(self):
        graph = {
            'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['A', 'B'], 'D': ['A'],
        }
        # patch D into A's list too, so the graph is fully connected
        graph['A'].append('D')
        cc = _ConnectedComponents()(graph)
        assert cc.count() == 1

    def test_component_contents(self):
        graph = {'A': ['B'], 'B': ['A'], 'C': []}
        components = _ConnectedComponents()(graph).find_components()
        component_sets = [set(c) for c in components]
        assert {'A', 'B'} in component_sets
        assert {'C'} in component_sets

    def test_single_node(self):
        assert _ConnectedComponents()({'A': []}).count() == 1
