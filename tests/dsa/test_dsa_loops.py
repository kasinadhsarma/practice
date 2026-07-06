"""
tests/dsa/test_dsa_loops.py
============================
Tests for all loop constructs under dsa/basics/loops/:

Level 1  — ForLoop, WhileLoop, NestedLoop
Level 2  — BreakDemo, ContinueDemo, ForElseDemo, DoWhileEmulator
Level 3  — EnumerateDemo, ZipDemo, ComprehensionDemo, RangeStepDemo
"""

import pytest
from tests.utils import load_module


# ── Class loaders ──────────────────────────────────────────────────────────────
# None of these scripts shadow their class name, so load_module() + attribute
# access is sufficient (no load_class() needed).

def _ForLoop():
    return load_module('dsa/basics/loops/level1/for_loop.py', ['5'], alias='dsa_forloop').ForLoop

def _WhileLoop():
    return load_module('dsa/basics/loops/level1/while_loop.py', ['5'], alias='dsa_whileloop').WhileLoop

def _NestedLoop():
    return load_module('dsa/basics/loops/level1/nested_loop.py', ['3'], alias='dsa_nestedloop').NestedLoop

def _BreakDemo():
    return load_module('dsa/basics/loops/level2/break_statement.py', ['12'], alias='dsa_break').BreakDemo

def _ContinueDemo():
    return load_module('dsa/basics/loops/level2/continue_statement.py', ['10'], alias='dsa_continue').ContinueDemo

def _ForElseDemo():
    return load_module('dsa/basics/loops/level2/for_else.py', ['7'], alias='dsa_forelse').ForElseDemo

def _WhileElseDemo():
    return load_module('dsa/basics/loops/level2/while_else.py', ['7', '10'], alias='dsa_whileelse').WhileElseDemo

def _DoWhileEmulator():
    return load_module('dsa/basics/loops/level2/do_while_loop.py', ['1 2 -3 4'], alias='dsa_dowhile').DoWhileEmulator

def _EnumerateDemo():
    return load_module('dsa/basics/loops/level3/enumerate_loop.py', ['a b c'], alias='dsa_enumerate').EnumerateDemo

def _ZipDemo():
    return load_module('dsa/basics/loops/level3/zip_loop.py', ['1 2 3', '4 5 6'], alias='dsa_zip').ZipDemo

def _ComprehensionDemo():
    return load_module('dsa/basics/loops/level3/comprehension_loop.py', ['5'], alias='dsa_compr').ComprehensionDemo

def _RangeStepDemo():
    return load_module('dsa/basics/loops/level3/range_step_loop.py', ['5'], alias='dsa_rangestep').RangeStepDemo


# ═════════════════════════════════════════════════════════════════════════════
#  LEVEL 1 — Basic loop constructs
# ═════════════════════════════════════════════════════════════════════════════

class TestForLoop:

    @pytest.mark.parametrize("n, expected", [(1, 1), (5, 15), (10, 55), (0, 0)])
    def test_sum_range(self, n, expected):
        assert _ForLoop()(n).sum_range() == expected

    def test_multiples_of(self):
        assert _ForLoop()(12).multiples_of(3) == [3, 6, 9, 12]

    def test_multiples_of_none_found(self):
        assert _ForLoop()(2).multiples_of(5) == []


class TestWhileLoop:

    def test_countdown(self):
        assert _WhileLoop()(5).countdown() == [5, 4, 3, 2, 1]

    def test_countdown_zero(self):
        assert _WhileLoop()(0).countdown() == []

    @pytest.mark.parametrize("n, expected", [(1, 1), (5, 15), (10, 55), (0, 0)])
    def test_sum_upto(self, n, expected):
        assert _WhileLoop()(n).sum_upto() == expected


class TestNestedLoop:

    def test_multiplication_table_3x3(self):
        assert _NestedLoop()(3).multiplication_table() == [
            [1, 2, 3],
            [2, 4, 6],
            [3, 6, 9],
        ]

    def test_multiplication_table_1x1(self):
        assert _NestedLoop()(1).multiplication_table() == [[1]]

    def test_table_dimensions(self):
        table = _NestedLoop()(5).multiplication_table()
        assert len(table) == 5
        assert all(len(row) == 5 for row in table)


# ═════════════════════════════════════════════════════════════════════════════
#  LEVEL 2 — Loop control statements
# ═════════════════════════════════════════════════════════════════════════════

class TestBreakDemo:

    @pytest.mark.parametrize("n, expected", [
        (12, 2), (15, 3), (7, 7), (17, 17), (9, 3),
    ])
    def test_first_divisor(self, n, expected):
        assert _BreakDemo()(n).first_divisor() == expected


class TestContinueDemo:

    @pytest.mark.parametrize("n, expected", [
        (1, 0), (2, 2), (10, 30), (0, 0), (5, 6),
    ])
    def test_sum_even(self, n, expected):
        assert _ContinueDemo()(n).sum_even() == expected


class TestForElseDemo:

    @pytest.mark.parametrize("n, expected", [
        (2, True), (3, True), (17, True), (97, True),
        (4, False), (1, False), (0, False), (-5, False), (100, False),
    ])
    def test_is_prime(self, n, expected):
        assert _ForElseDemo()(n).is_prime() == expected


class TestWhileElseDemo:

    @pytest.mark.parametrize("n, limit, expected", [
        (12, 10, True),   # 2 divides 12, found before limit
        (7, 7, False),    # prime, no factor found in [2,7)
        (17, 17, False),  # prime
        (15, 4, True),    # 3 divides 15, found at i=3 (< limit 4)
        (17, 3, False),   # limit too small to find any factor
    ])
    def test_has_factor_below(self, n, limit, expected):
        assert _WhileElseDemo()(n).has_factor_below(limit) == expected


class TestDoWhileEmulator:

    def test_stops_after_first_negative(self):
        assert _DoWhileEmulator()([1, 2, -3, 4]).collect_until_negative() == [1, 2, -3]

    def test_runs_at_least_once(self):
        assert _DoWhileEmulator()([-1, 2, 3]).collect_until_negative() == [-1]

    def test_no_negative_consumes_all(self):
        assert _DoWhileEmulator()([1, 2, 3]).collect_until_negative() == [1, 2, 3]

    def test_empty_input(self):
        assert _DoWhileEmulator()([]).collect_until_negative() == []


# ═════════════════════════════════════════════════════════════════════════════
#  LEVEL 3 — Advanced iteration patterns
# ═════════════════════════════════════════════════════════════════════════════

class TestEnumerateDemo:

    def test_indexed_items(self):
        assert _EnumerateDemo()(['a', 'b', 'c']).indexed_items() == [
            (0, 'a'), (1, 'b'), (2, 'c'),
        ]

    @pytest.mark.parametrize("items, target, expected", [
        (['a', 'b', 'c'], 'b', 1),
        (['a', 'b', 'c'], 'z', -1),
        ([], 'a', -1),
    ])
    def test_find_index(self, items, target, expected):
        assert _EnumerateDemo()(items).find_index(target) == expected


class TestZipDemo:

    def test_pair_up(self):
        assert _ZipDemo()([1, 2, 3], [4, 5, 6]).pair_up() == [(1, 4), (2, 5), (3, 6)]

    def test_pair_up_uneven_lengths(self):
        assert _ZipDemo()([1, 2, 3], [4, 5]).pair_up() == [(1, 4), (2, 5)]

    @pytest.mark.parametrize("a, b, expected", [
        ([1, 2, 3], [4, 5, 6], 32),
        ([1, 1, 1], [1, 1, 1], 3),
        ([], [], 0),
    ])
    def test_dot_product(self, a, b, expected):
        assert _ZipDemo()(a, b).dot_product() == expected


class TestComprehensionDemo:

    @pytest.mark.parametrize("n, expected", [
        (1, [1]), (3, [1, 4, 9]), (5, [1, 4, 9, 16, 25]), (0, []),
    ])
    def test_squares(self, n, expected):
        assert _ComprehensionDemo()(n).squares() == expected

    def test_evens(self):
        assert _ComprehensionDemo()(0).evens([1, 2, 3, 4, 5, 6]) == [2, 4, 6]

    def test_length_map(self):
        assert _ComprehensionDemo()(0).length_map(['a', 'bb', 'ccc']) == {
            'a': 1, 'bb': 2, 'ccc': 3,
        }


class TestRangeStepDemo:

    @pytest.mark.parametrize("start, stop, step, expected", [
        (0, 10, 2, [0, 2, 4, 6, 8]),
        (1, 10, 3, [1, 4, 7]),
        (10, 0, -2, [10, 8, 6, 4, 2]),
    ])
    def test_step_range(self, start, stop, step, expected):
        assert _RangeStepDemo()(0).step_range(start, stop, step) == expected

    def test_reverse_range(self):
        assert _RangeStepDemo()(5).reverse_range() == [5, 4, 3, 2, 1]

    def test_reverse_range_zero(self):
        assert _RangeStepDemo()(0).reverse_range() == []
