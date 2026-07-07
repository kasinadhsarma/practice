"""
tests/mathmatics/test_mathmatics_calculus.py
===============================================
Tests for every operation under mathmatics/calculus/:
    limit_numerical, derivative_numerical, power_rule_derivative, integral_numerical
"""

import pytest
from tests.utils import load_module


def _LimitNumerical():
    return load_module('mathmatics/calculus/limit_numerical.py', [], alias='calc_limit').limit_numerical

def _DerivativeNumerical():
    return load_module('mathmatics/calculus/derivative_numerical.py', [], alias='calc_derivative').derivative_numerical

def _PowerRuleDerivative():
    return load_module('mathmatics/calculus/power_rule_derivative.py', [], alias='calc_powerrule').power_rule_derivative

def _IntegralNumerical():
    return load_module('mathmatics/calculus/integral_numerical.py', [], alias='calc_integral').integral_numerical


# ═════════════════════════════════════════════════════════════════════════════

class TestLimitNumerical:

    def test_removable_discontinuity(self):
        f = lambda x: (x ** 2 - 1) / (x - 1)
        assert _LimitNumerical()().calculate(f, 1) == pytest.approx(2.0, abs=1e-4)

    def test_continuous_function(self):
        f = lambda x: x ** 2
        assert _LimitNumerical()().calculate(f, 3) == pytest.approx(9.0, abs=1e-4)


class TestDerivativeNumerical:

    def test_x_squared(self):
        f = lambda x: x ** 2
        assert _DerivativeNumerical()().calculate(f, 3) == pytest.approx(6.0, abs=1e-3)

    def test_constant_function(self):
        f = lambda x: 5
        assert _DerivativeNumerical()().calculate(f, 10) == pytest.approx(0.0, abs=1e-3)

    def test_linear_function(self):
        f = lambda x: 3 * x + 2
        assert _DerivativeNumerical()().calculate(f, 1) == pytest.approx(3.0, abs=1e-3)


class TestPowerRuleDerivative:

    def test_cubic(self):
        result = _PowerRuleDerivative()().calculate([5, 3, 4, 2])
        assert result == [3, 8, 6]

    def test_constant_only(self):
        result = _PowerRuleDerivative()().calculate([7])
        assert result == [0]

    def test_linear(self):
        result = _PowerRuleDerivative()().calculate([1, 5])
        assert result == [5]


class TestIntegralNumerical:

    def test_x_squared_area(self):
        f = lambda x: x ** 2
        result = _IntegralNumerical()().calculate(f, 0, 3)
        assert result == pytest.approx(9.0, abs=1e-2)

    def test_constant_function_area(self):
        f = lambda x: 4
        result = _IntegralNumerical()().calculate(f, 0, 5)
        assert result == pytest.approx(20.0, abs=1e-6)
