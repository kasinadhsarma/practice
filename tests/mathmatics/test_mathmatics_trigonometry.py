"""
tests/mathmatics/test_mathmatics_trigonometry.py
===================================================
Tests for every operation under mathmatics/trigonometry/:
    trig_ratios, pythagorean_identity, law_of_sines, law_of_cosines, unit_circle
"""

import pytest
from tests.utils import load_module


def _TrigRatios():
    return load_module('mathmatics/trigonometry/trig_ratios.py', [], alias='trig_ratios_mod').trig_ratios

def _PythagoreanIdentity():
    return load_module('mathmatics/trigonometry/pythagorean_identity.py', [], alias='trig_pyth').pythagorean_identity

def _LawOfSines():
    return load_module('mathmatics/trigonometry/law_of_sines.py', [], alias='trig_sines').law_of_sines

def _LawOfCosines():
    return load_module('mathmatics/trigonometry/law_of_cosines.py', [], alias='trig_cosines').law_of_cosines

def _UnitCircle():
    return load_module('mathmatics/trigonometry/unit_circle.py', [], alias='trig_unit').unit_circle


# ═════════════════════════════════════════════════════════════════════════════

class TestTrigRatios:

    def test_3_4_5_triangle(self):
        tr = _TrigRatios()()
        assert tr.sin(3, 5) == pytest.approx(0.6)
        assert tr.cos(4, 5) == pytest.approx(0.8)
        assert tr.tan(3, 4) == pytest.approx(0.75)

    def test_angle_from_sides(self):
        tr = _TrigRatios()()
        assert tr.angle_from_sides(1, 1) == pytest.approx(45.0)


class TestPythagoreanIdentity:

    @pytest.mark.parametrize("angle", [0, 30, 45, 60, 90, 137, 270])
    def test_holds_for_any_angle(self, angle):
        assert _PythagoreanIdentity()().verify(angle) is True


class TestLawOfSines:

    def test_known_ratio(self):
        result = _LawOfSines()().find_side(10, 30, 90)
        assert result == pytest.approx(20.0)

    def test_equal_angles_equal_sides(self):
        result = _LawOfSines()().find_side(5, 60, 60)
        assert result == pytest.approx(5.0)


class TestLawOfCosines:

    def test_right_angle_matches_pythagoras(self):
        loc = _LawOfCosines()()
        result = loc.find_side(3, 4, 90)
        assert result == pytest.approx(5.0)

    def test_find_angle_recovers_right_angle(self):
        loc = _LawOfCosines()()
        angle = loc.find_angle(3, 4, 5)
        assert angle == pytest.approx(90.0)

    def test_round_trip(self):
        loc = _LawOfCosines()()
        side = loc.find_side(7, 10, 60)
        angle = loc.find_angle(7, 10, side)
        assert angle == pytest.approx(60.0)


class TestUnitCircle:

    def test_zero_degrees(self):
        result = _UnitCircle()().coordinates(0)
        assert result == pytest.approx((1.0, 0.0))

    def test_ninety_degrees(self):
        x, y = _UnitCircle()().coordinates(90)
        assert x == pytest.approx(0.0, abs=1e-9)
        assert y == pytest.approx(1.0)

    def test_forty_five_degrees(self):
        x, y = _UnitCircle()().coordinates(45)
        assert x == pytest.approx(y)
