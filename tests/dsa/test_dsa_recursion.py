"""
tests/dsa/test_dsa_recursion.py
================================
Tests for all recursion patterns under dsa/basics/recursion/:

Level 1  — FactorialRecursive, SumOfN, PowerRecursive
Level 2  — FibonacciRecursive, TowerOfHanoi, TailRecursion, MutualRecursion
Level 3  — Permutations, Subsets, NQueens, GridPaths
"""

import pytest
from tests.utils import load_module


def _FactorialRecursive():
    return load_module('dsa/basics/recursion/level1/factorial_recursive.py', ['5'], alias='rec_factorial').FactorialRecursive

def _SumOfN():
    return load_module('dsa/basics/recursion/level1/sum_of_n.py', ['5'], alias='rec_sumofn').SumOfN

def _PowerRecursive():
    return load_module('dsa/basics/recursion/level1/power_recursive.py', ['2', '5'], alias='rec_power').PowerRecursive

def _FibonacciRecursive():
    return load_module('dsa/basics/recursion/level2/fibonacci_recursive.py', ['5'], alias='rec_fib').FibonacciRecursive

def _TowerOfHanoi():
    return load_module('dsa/basics/recursion/level2/tower_of_hanoi.py', ['3'], alias='rec_hanoi').TowerOfHanoi

def _TailRecursion():
    return load_module('dsa/basics/recursion/level2/tail_recursion.py', ['5'], alias='rec_tailrec').TailRecursion

def _MutualRecursion():
    return load_module('dsa/basics/recursion/level2/mutual_recursion.py', ['5'], alias='rec_mutual').MutualRecursion

def _Permutations():
    return load_module('dsa/basics/recursion/level3/permutations.py', ['a b'], alias='rec_perms').Permutations

def _Subsets():
    return load_module('dsa/basics/recursion/level3/subsets.py', ['a b'], alias='rec_subsets').Subsets

def _NQueens():
    return load_module('dsa/basics/recursion/level3/n_queens.py', ['4'], alias='rec_nqueens').NQueens

def _GridPaths():
    return load_module('dsa/basics/recursion/level3/grid_paths.py', ['1', '0'], alias='rec_gridpaths').GridPaths


# ═════════════════════════════════════════════════════════════════════════════
#  LEVEL 1 — Basics
# ═════════════════════════════════════════════════════════════════════════════

class TestFactorialRecursive:

    @pytest.mark.parametrize("n, expected", [(0, 1), (1, 1), (2, 2), (5, 120), (10, 3628800)])
    def test_calculate(self, n, expected):
        assert _FactorialRecursive()(n).calculate() == expected


class TestSumOfN:

    @pytest.mark.parametrize("n, expected", [(0, 0), (1, 1), (5, 15), (10, 55)])
    def test_calculate(self, n, expected):
        assert _SumOfN()(n).calculate() == expected


class TestPowerRecursive:

    @pytest.mark.parametrize("x, n, expected", [
        (2, 0, 1), (2, 1, 2), (2, 10, 1024), (3, 4, 81), (5, 3, 125),
    ])
    def test_calculate(self, x, n, expected):
        assert _PowerRecursive()(x, n).calculate() == expected

    @pytest.mark.parametrize("x, n, expected", [
        (2, 0, 1), (2, 1, 2), (2, 10, 1024), (3, 4, 81), (5, 3, 125),
    ])
    def test_calculate_fast(self, x, n, expected):
        assert _PowerRecursive()(x, n).calculate_fast() == expected

    def test_fast_agrees_with_linear(self):
        m = _PowerRecursive()
        for n in range(8):
            assert m(2, n).calculate() == m(2, n).calculate_fast()


# ═════════════════════════════════════════════════════════════════════════════
#  LEVEL 2 — Recursion patterns
# ═════════════════════════════════════════════════════════════════════════════

class TestFibonacciRecursive:

    @pytest.mark.parametrize("n, expected", [(0, 0), (1, 1), (2, 1), (5, 5), (10, 55)])
    def test_calculate(self, n, expected):
        assert _FibonacciRecursive()(n).calculate() == expected

    def test_call_count_grows_exponentially(self):
        m = _FibonacciRecursive()
        assert m(1).call_count() == 1
        assert m(5).call_count() > m(4).call_count() > m(3).call_count()


class TestTowerOfHanoi:

    def test_minimum_moves(self):
        assert _TowerOfHanoi()(3).minimum_moves() == 7

    def test_move_count_matches_minimum(self):
        h = _TowerOfHanoi()(4)
        assert len(h.solve()) == h.minimum_moves()

    def test_zero_disks(self):
        assert _TowerOfHanoi()(0).solve() == []

    def test_largest_disk_moves_exactly_once_direct_to_target(self):
        h = _TowerOfHanoi()(3)
        moves = h.solve()
        largest_disk_moves = [mv for mv in moves if mv[0] == 3]
        assert largest_disk_moves == [(3, 'A', 'C')]

    def test_last_move_completes_the_target_peg(self):
        h = _TowerOfHanoi()(3)
        moves = h.solve()
        assert moves[-1][2] == 'C'


class TestTailRecursion:

    @pytest.mark.parametrize("n, expected", [(0, 0), (1, 1), (5, 15), (10, 55)])
    def test_sum_non_tail(self, n, expected):
        assert _TailRecursion()(n).sum_non_tail() == expected

    @pytest.mark.parametrize("n, expected", [(0, 0), (1, 1), (5, 15), (10, 55)])
    def test_sum_tail_recursive(self, n, expected):
        assert _TailRecursion()(n).sum_tail_recursive() == expected

    def test_both_agree(self):
        m = _TailRecursion()
        for n in range(10):
            assert m(n).sum_non_tail() == m(n).sum_tail_recursive()


class TestMutualRecursion:

    @pytest.mark.parametrize("n, is_even, is_odd", [
        (0, True, False), (1, False, True), (2, True, False),
        (7, False, True), (10, True, False),
    ])
    def test_is_even_and_is_odd(self, n, is_even, is_odd):
        mr = _MutualRecursion()()
        assert mr.is_even(n) == is_even
        assert mr.is_odd(n) == is_odd


# ═════════════════════════════════════════════════════════════════════════════
#  LEVEL 3 — Backtracking
# ═════════════════════════════════════════════════════════════════════════════

class TestPermutations:

    def test_count_matches_factorial(self):
        result = _Permutations()(['a', 'b', 'c']).generate()
        assert len(result) == 6

    def test_all_unique(self):
        result = _Permutations()(['a', 'b', 'c']).generate()
        assert len(set(map(tuple, result))) == len(result)

    def test_single_item(self):
        assert _Permutations()(['a']).generate() == [['a']]

    def test_empty(self):
        assert _Permutations()([]).generate() == [[]]

    def test_two_items(self):
        result = _Permutations()(['a', 'b']).generate()
        assert sorted(map(tuple, result)) == sorted([('a', 'b'), ('b', 'a')])


class TestSubsets:

    def test_count_matches_power_of_two(self):
        result = _Subsets()(['a', 'b', 'c']).generate()
        assert len(result) == 8

    def test_contains_empty_and_full_set(self):
        result = _Subsets()(['a', 'b']).generate()
        sets = [set(s) for s in result]
        assert set() in sets
        assert {'a', 'b'} in sets

    def test_empty_input(self):
        assert _Subsets()([]).generate() == [[]]

    def test_all_unique(self):
        result = _Subsets()(['a', 'b', 'c']).generate()
        as_sets = [frozenset(s) for s in result]
        assert len(set(as_sets)) == len(as_sets)


class TestNQueens:

    @pytest.mark.parametrize("n, expected_count", [
        (1, 1), (2, 0), (3, 0), (4, 2), (5, 10),
    ])
    def test_count_solutions(self, n, expected_count):
        assert _NQueens()(n).count_solutions() == expected_count

    def test_solution_is_valid(self):
        nq = _NQueens()(4)
        solution = nq.solve()[0]
        for row1 in range(len(solution)):
            for row2 in range(row1 + 1, len(solution)):
                col1, col2 = solution[row1], solution[row2]
                assert col1 != col2
                assert abs(col1 - col2) != abs(row1 - row2)


class TestGridPaths:

    def test_no_obstacles_3x3(self):
        grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        assert _GridPaths()(grid).count_paths() == 6

    def test_with_center_obstacle(self):
        grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        assert _GridPaths()(grid).count_paths() == 2

    def test_start_blocked(self):
        grid = [[1, 0], [0, 0]]
        assert _GridPaths()(grid).count_paths() == 0

    def test_single_cell(self):
        assert _GridPaths()([[0]]).count_paths() == 1

    def test_single_row(self):
        assert _GridPaths()([[0, 0, 0]]).count_paths() == 1
