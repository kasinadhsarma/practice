"""
tests/mathmatics/test_mathmatics_algebra.py
==============================================
Tests for every operation under mathmatics/algebra/basicalgebra/:
    linear_equation, quadratic_equation, polynomial_operations, exponents_roots
"""

import pytest
from tests.utils import load_module


def _LinearEquation():
    return load_module('mathmatics/algebra/basicalgebra/linear_equation.py', [], alias='alg_linear').linear_equation

def _QuadraticEquation():
    return load_module('mathmatics/algebra/basicalgebra/quadratic_equation.py', [], alias='alg_quadratic').quadratic_equation

def _PolynomialOperations():
    return load_module('mathmatics/algebra/basicalgebra/polynomial_operations.py', [], alias='alg_poly').polynomial_operations

def _ExponentsRoots():
    return load_module('mathmatics/algebra/basicalgebra/exponents_roots.py', [], alias='alg_exp').exponents_roots


# ═════════════════════════════════════════════════════════════════════════════

class TestLinearEquation:

    def test_basic(self):
        assert _LinearEquation()().solve(2, -10) == 5.0

    def test_negative_a(self):
        assert _LinearEquation()().solve(-2, 4) == 2.0

    def test_zero_a_returns_none(self):
        assert _LinearEquation()().solve(0, 5) is None


class TestQuadraticEquation:

    def test_two_real_roots(self):
        roots = _QuadraticEquation()().solve(1, -3, 2)
        assert set(root.real for root in roots) == {1.0, 2.0}

    def test_repeated_root(self):
        roots = _QuadraticEquation()().solve(1, -2, 1)
        assert roots[0] == roots[1] == 1.0

    def test_complex_roots(self):
        roots = _QuadraticEquation()().solve(1, 0, 1)
        assert roots[0].imag != 0

    def test_zero_a_returns_none(self):
        assert _QuadraticEquation()().solve(0, 2, 3) is None


class TestPolynomialOperations:

    def test_add_same_length(self):
        ops = _PolynomialOperations()()
        assert ops.add([1, 2], [3, 4]) == [4, 6]

    def test_add_different_length(self):
        ops = _PolynomialOperations()()
        assert ops.add([1, 2], [3, 0, 1]) == [4, 2, 1]

    def test_multiply(self):
        ops = _PolynomialOperations()()
        assert ops.multiply([1, 2], [3, 0, 1]) == [3, 6, 1, 2]

    def test_evaluate(self):
        ops = _PolynomialOperations()()
        assert ops.evaluate([1, 2, 3], 2) == 1 + 2 * 2 + 3 * 4


class TestExponentsRoots:

    def test_power(self):
        assert _ExponentsRoots()().power(2, 10) == 1024

    def test_nth_root(self):
        assert _ExponentsRoots()().nth_root(27, 3) == pytest.approx(3.0)

    def test_negative_odd_root(self):
        assert _ExponentsRoots()().nth_root(-8, 3) == pytest.approx(-2.0)

    def test_negative_even_root_returns_none(self):
        assert _ExponentsRoots()().nth_root(-4, 2) is None
