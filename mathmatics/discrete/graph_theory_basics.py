class graph_theory_basics:
    # graph given as an adjacency list: {node: [neighbors...]}
    # degree_sequence:   number of edges touching each node
    # handshake_lemma:   sum of all degrees always equals 2 * edge count
    #                    (every edge contributes exactly 2 to the total degree)
    # has_eulerian_circuit: a connected graph has a circuit using every edge
    #                    exactly once if and only if every vertex has even degree
    # time complexity O(V + E), space O(V)
    def degree_sequence(self,graph:dict)->dict:
        return {node: len(neighbors) for node, neighbors in graph.items()}

    def handshake_lemma_holds(self,graph:dict,edge_count:int)->bool:
        total_degree = sum(self.degree_sequence(graph).values())
        return total_degree == 2 * edge_count

    def has_eulerian_circuit(self,graph:dict)->bool:
        # assumes the graph is already known to be connected
        return all(degree % 2 == 0 for degree in self.degree_sequence(graph).values())

graph = {
    'A': ['B', 'D'],
    'B': ['A', 'C', 'D'],
    'C': ['B', 'D'],
    'D': ['A', 'B', 'C'],
}
gtb = graph_theory_basics()
result = (gtb.degree_sequence(graph), gtb.handshake_lemma_holds(graph, edge_count=5), gtb.has_eulerian_circuit(graph))
print(result)
