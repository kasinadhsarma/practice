"""
tests/mathmatics/test_mathmatics_coordinate_geometry.py
==========================================================
Tests for every operation under mathmatics/coordinate_geometry/:
    distance_formula, midpoint_formula, slope_and_line_equation, circle_equation
"""

import pytest
from tests.utils import load_module


def _DistanceFormula():
    return load_module('mathmatics/coordinate_geometry/distance_formula.py', [], alias='cg_distance').distance_formula

def _MidpointFormula():
    return load_module('mathmatics/coordinate_geometry/midpoint_formula.py', [], alias='cg_midpoint').midpoint_formula

def _SlopeAndLineEquation():
    return load_module('mathmatics/coordinate_geometry/slope_and_line_equation.py', [], alias='cg_slope').slope_and_line_equation

def _CircleEquation():
    return load_module('mathmatics/coordinate_geometry/circle_equation.py', [], alias='cg_circle').circle_equation


# ═════════════════════════════════════════════════════════════════════════════

class TestDistanceFormula:

    def test_3_4_5_triangle(self):
        assert _DistanceFormula()().calculate((0, 0), (3, 4)) == 5.0

    def test_same_point(self):
        assert _DistanceFormula()().calculate((2, 2), (2, 2)) == 0.0


class TestMidpointFormula:

    def test_basic(self):
        assert _MidpointFormula()().calculate((2, 3), (8, 7)) == (5.0, 5.0)

    def test_negative_coordinates(self):
        assert _MidpointFormula()().calculate((-4, -2), (4, 2)) == (0.0, 0.0)


class TestSlopeAndLineEquation:

    def test_slope(self):
        assert _SlopeAndLineEquation()().slope((1, 2), (4, 11)) == pytest.approx(3.0)

    def test_vertical_line_returns_none(self):
        assert _SlopeAndLineEquation()().slope((2, 1), (2, 9)) is None

    def test_slope_intercept_form(self):
        m, b = _SlopeAndLineEquation()().slope_intercept_form((1, 2), (4, 11))
        assert m == pytest.approx(3.0)
        assert b == pytest.approx(-1.0)


class TestCircleEquation:

    def test_point_on_circle(self):
        assert _CircleEquation()().classify_point((3, 4), (0, 0), 5) == "on"

    def test_point_inside_circle(self):
        assert _CircleEquation()().classify_point((1, 1), (0, 0), 5) == "inside"

    def test_point_outside_circle(self):
        assert _CircleEquation()().classify_point((10, 10), (0, 0), 5) == "outside"
