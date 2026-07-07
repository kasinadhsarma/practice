"""
tests/mathmatics/test_mathmatics_sequences_series.py
=======================================================
Tests for every operation under mathmatics/sequences_series/:
    arithmetic_progression, geometric_progression, fibonacci_binet, summation_formulas
"""

import pytest
from tests.utils import load_module


def _ArithmeticProgression():
    return load_module('mathmatics/sequences_series/arithmetic_progression.py', [], alias='ss_ap').arithmetic_progression

def _GeometricProgression():
    return load_module('mathmatics/sequences_series/geometric_progression.py', [], alias='ss_gp').geometric_progression

def _FibonacciBinet():
    return load_module('mathmatics/sequences_series/fibonacci_binet.py', [], alias='ss_fib').fibonacci_binet

def _SummationFormulas():
    return load_module('mathmatics/sequences_series/summation_formulas.py', [], alias='ss_sum').summation_formulas


# ═════════════════════════════════════════════════════════════════════════════

class TestArithmeticProgression:

    def test_nth_term(self):
        assert _ArithmeticProgression()().nth_term(3, 5, 10) == 48

    def test_sum_n_terms(self):
        assert _ArithmeticProgression()().sum_n_terms(3, 5, 10) == 255.0

    def test_zero_common_difference(self):
        assert _ArithmeticProgression()().nth_term(7, 0, 100) == 7


class TestGeometricProgression:

    def test_nth_term(self):
        assert _GeometricProgression()().nth_term(2, 0.5, 5) == pytest.approx(0.125)

    def test_sum_n_terms(self):
        assert _GeometricProgression()().sum_n_terms(2, 0.5, 5) == pytest.approx(3.875)

    def test_sum_to_infinity_converges(self):
        assert _GeometricProgression()().sum_to_infinity(2, 0.5) == pytest.approx(4.0)

    def test_sum_to_infinity_diverges_returns_none(self):
        assert _GeometricProgression()().sum_to_infinity(2, 1.5) is None

    def test_sum_n_terms_ratio_one(self):
        assert _GeometricProgression()().sum_n_terms(3, 1, 4) == 12


class TestFibonacciBinet:

    @pytest.mark.parametrize("n, expected", [(0, 0), (1, 1), (2, 1), (10, 55), (15, 610)])
    def test_calculate(self, n, expected):
        assert _FibonacciBinet()().calculate(n) == expected


class TestSummationFormulas:

    def test_sum_natural_numbers(self):
        assert _SummationFormulas()().sum_natural_numbers(5) == 15

    def test_sum_of_squares(self):
        assert _SummationFormulas()().sum_of_squares(5) == 55

    def test_sum_of_cubes(self):
        assert _SummationFormulas()().sum_of_cubes(5) == 225

    def test_cubes_equals_square_of_naturals_sum(self):
        sf = _SummationFormulas()()
        n = 6
        assert sf.sum_of_cubes(n) == sf.sum_natural_numbers(n) ** 2
