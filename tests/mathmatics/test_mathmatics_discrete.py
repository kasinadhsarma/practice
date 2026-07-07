"""
tests/mathmatics/test_mathmatics_discrete.py
===============================================
Tests for every operation under mathmatics/discrete/:

    set_operations, power_set, cartesian_product, truth_table, relations,
    functions_properties, modular_arithmetic, graph_theory_basics,
    pigeonhole_principle
"""

import pytest
from tests.utils import load_module


def _SetOperations():
    return load_module('mathmatics/discrete/set_operations.py', [], alias='disc_setops').set_operations

def _PowerSet():
    return load_module('mathmatics/discrete/power_set.py', [], alias='disc_powerset').power_set

def _CartesianProduct():
    return load_module('mathmatics/discrete/cartesian_product.py', [], alias='disc_cartesian').cartesian_product

def _TruthTable():
    return load_module('mathmatics/discrete/truth_table.py', [], alias='disc_truthtable').truth_table

def _Relations():
    return load_module('mathmatics/discrete/relations.py', [], alias='disc_relations').relations

def _FunctionsProperties():
    return load_module('mathmatics/discrete/functions_properties.py', [], alias='disc_functions').functions_properties

def _ModularArithmetic():
    return load_module('mathmatics/discrete/modular_arithmetic.py', [], alias='disc_modular').modular_arithmetic

def _GraphTheoryBasics():
    return load_module('mathmatics/discrete/graph_theory_basics.py', [], alias='disc_graph').graph_theory_basics

def _PigeonholePrinciple():
    return load_module('mathmatics/discrete/pigeonhole_principle.py', [], alias='disc_pigeonhole').pigeonhole_principle


# ═════════════════════════════════════════════════════════════════════════════

class TestSetOperations:

    def setup_ops(self):
        return _SetOperations()(), {1, 2, 3, 4}, {3, 4, 5, 6}

    def test_union(self):
        ops, a, b = self.setup_ops()
        assert ops.union(a, b) == {1, 2, 3, 4, 5, 6}

    def test_intersection(self):
        ops, a, b = self.setup_ops()
        assert ops.intersection(a, b) == {3, 4}

    def test_difference(self):
        ops, a, b = self.setup_ops()
        assert ops.difference(a, b) == {1, 2}

    def test_symmetric_difference(self):
        ops, a, b = self.setup_ops()
        assert ops.symmetric_difference(a, b) == {1, 2, 5, 6}


class TestPowerSet:

    def test_size_is_two_to_the_n(self):
        result = _PowerSet()().calculate([1, 2, 3])
        assert len(result) == 8

    def test_includes_empty_set(self):
        result = _PowerSet()().calculate([1, 2])
        assert [] in result

    def test_includes_full_set(self):
        result = _PowerSet()().calculate([1, 2])
        assert sorted(result, key=len)[-1] == [1, 2]

    def test_empty_input(self):
        result = _PowerSet()().calculate([])
        assert result == [[]]


class TestCartesianProduct:

    def test_basic(self):
        result = _CartesianProduct()().calculate([1, 2], ['x', 'y'])
        assert result == [(1, 'x'), (1, 'y'), (2, 'x'), (2, 'y')]

    def test_size(self):
        result = _CartesianProduct()().calculate([1, 2, 3], ['a', 'b'])
        assert len(result) == 6

    def test_empty_first_set(self):
        assert _CartesianProduct()().calculate([], [1, 2]) == []


class TestTruthTable:

    def test_has_four_rows(self):
        assert len(_TruthTable()().generate()) == 4

    def test_and_row(self):
        rows = _TruthTable()().generate()
        true_true = next(r for r in rows if r["p"] and r["q"])
        assert true_true["AND"] is True

    def test_xor_row(self):
        rows = _TruthTable()().generate()
        true_false = next(r for r in rows if r["p"] and not r["q"])
        assert true_false["XOR"] is True

    def test_implies_false_only_when_p_true_q_false(self):
        rows = _TruthTable()().generate()
        for row in rows:
            expected = not (row["p"] and not row["q"])
            assert row["IMPLIES (p->q)"] == expected


class TestRelations:

    def test_equivalence_relation(self):
        rel = _Relations()()
        elements = {1, 2, 3}
        pairs = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1)}
        assert rel.is_equivalence(elements, pairs) is True

    def test_not_reflexive(self):
        rel = _Relations()()
        elements = {1, 2}
        pairs = {(1, 1)}
        assert rel.is_reflexive(elements, pairs) is False

    def test_not_symmetric(self):
        rel = _Relations()()
        pairs = {(1, 2)}
        assert rel.is_symmetric(pairs) is False

    def test_not_transitive(self):
        rel = _Relations()()
        pairs = {(1, 2), (2, 3)}
        assert rel.is_transitive(pairs) is False


class TestFunctionsProperties:

    def test_bijective(self):
        fp = _FunctionsProperties()()
        mapping = {1: 'a', 2: 'b', 3: 'c'}
        codomain = {'a', 'b', 'c'}
        assert fp.is_bijective(mapping, codomain) is True

    def test_not_injective(self):
        fp = _FunctionsProperties()()
        mapping = {1: 'a', 2: 'a'}
        assert fp.is_injective(mapping) is False

    def test_not_surjective(self):
        fp = _FunctionsProperties()()
        mapping = {1: 'a', 2: 'b'}
        codomain = {'a', 'b', 'c'}
        assert fp.is_surjective(mapping, codomain) is False


class TestModularArithmetic:

    def test_mod_pow(self):
        ma = _ModularArithmetic()()
        assert ma.mod_pow(4, 13, 497) == 445

    def test_mod_pow_matches_builtin(self):
        ma = _ModularArithmetic()()
        assert ma.mod_pow(7, 128, 13) == pow(7, 128, 13)

    def test_mod_inverse(self):
        ma = _ModularArithmetic()()
        assert ma.mod_inverse(3, 11) == 4

    def test_mod_inverse_verifies(self):
        ma = _ModularArithmetic()()
        inv = ma.mod_inverse(7, 26)
        assert (7 * inv) % 26 == 1

    def test_mod_inverse_no_inverse_returns_none(self):
        ma = _ModularArithmetic()()
        assert ma.mod_inverse(4, 8) is None


class TestGraphTheoryBasics:

    def graph(self):
        return {
            'A': ['B', 'D'],
            'B': ['A', 'C', 'D'],
            'C': ['B', 'D'],
            'D': ['A', 'B', 'C'],
        }

    def test_degree_sequence(self):
        gtb = _GraphTheoryBasics()()
        degrees = gtb.degree_sequence(self.graph())
        assert degrees == {'A': 2, 'B': 3, 'C': 2, 'D': 3}

    def test_handshake_lemma_holds(self):
        gtb = _GraphTheoryBasics()()
        assert gtb.handshake_lemma_holds(self.graph(), edge_count=5) is True

    def test_handshake_lemma_fails_with_wrong_count(self):
        gtb = _GraphTheoryBasics()()
        assert gtb.handshake_lemma_holds(self.graph(), edge_count=4) is False

    def test_no_eulerian_circuit_with_odd_degree(self):
        gtb = _GraphTheoryBasics()()
        assert gtb.has_eulerian_circuit(self.graph()) is False

    def test_eulerian_circuit_all_even_degree(self):
        gtb = _GraphTheoryBasics()()
        square_graph = {'A': ['B', 'D'], 'B': ['A', 'C'], 'C': ['B', 'D'], 'D': ['A', 'C']}
        assert gtb.has_eulerian_circuit(square_graph) is True


class TestPigeonholePrinciple:

    @pytest.mark.parametrize("items, containers, expected", [
        (13, 12, 2), (10, 5, 2), (11, 5, 3), (5, 5, 1),
    ])
    def test_guaranteed_minimum(self, items, containers, expected):
        assert _PigeonholePrinciple()().guaranteed_minimum(items, containers) == expected

    def test_zero_containers_returns_none(self):
        assert _PigeonholePrinciple()().guaranteed_minimum(5, 0) is None
