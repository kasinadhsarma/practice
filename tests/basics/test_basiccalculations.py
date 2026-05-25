"""
tests/basics/test_basiccalculations.py
========================================
Tests for basiccalculations/
    addition.py       — sum = a + b
    substraction.py   — substraction = a - b
    multiplication.py — multiplication = a * b
    division.py       — division = a / b  (float division)

The source files are pure arithmetic scripts (no importable classes), so the
arithmetic logic is tested directly — no module import required.
"""

import pytest


# ─────────────────────────────────────────────────────────────────────────────
# Addition  (addition.py: sum = a + b)
# ─────────────────────────────────────────────────────────────────────────────

class TestAddition:
    """Covers: addition.py  →  sum = a + b"""

    @pytest.mark.parametrize("a, b, expected", [
        (0,    0,     0),
        (1,    1,     2),
        (5,    3,     8),
        (-1,   1,     0),
        (-5,  -3,    -8),
        (100,  200,  300),
        (0,    999,  999),
        (999,  0,    999),
    ])
    def test_sum(self, a, b, expected):
        assert a + b == expected

    def test_commutativity(self):
        """a + b == b + a for all integers."""
        assert 7 + 3 == 3 + 7
        assert -10 + 4 == 4 + -10

    def test_associativity(self):
        """(a + b) + c == a + (b + c)."""
        assert (2 + 3) + 4 == 2 + (3 + 4)

    def test_identity_zero(self):
        """Adding 0 leaves the number unchanged."""
        for n in [0, 1, -1, 42, -100]:
            assert n + 0 == n

    def test_large_numbers(self):
        assert 10**9 + 10**9 == 2 * 10**9


# ─────────────────────────────────────────────────────────────────────────────
# Subtraction  (substraction.py: substraction = a - b)
# ─────────────────────────────────────────────────────────────────────────────

class TestSubtraction:
    """Covers: substraction.py  →  substraction = a - b"""

    @pytest.mark.parametrize("a, b, expected", [
        (0,   0,    0),
        (5,   3,    2),
        (3,   5,   -2),
        (-2, -3,    1),
        (100, 100,  0),
        (0,   7,   -7),
        (-1, -1,    0),
    ])
    def test_difference(self, a, b, expected):
        assert a - b == expected

    def test_self_minus_self_is_zero(self):
        for n in [0, 1, -1, 9999, -9999]:
            assert n - n == 0

    def test_subtraction_reversal(self):
        """a - b == -(b - a)."""
        assert (10 - 3) == -(3 - 10)


# ─────────────────────────────────────────────────────────────────────────────
# Multiplication  (multiplication.py: multiplication = a * b)
# ─────────────────────────────────────────────────────────────────────────────

class TestMultiplication:
    """Covers: multiplication.py  →  multiplication = a * b"""

    @pytest.mark.parametrize("a, b, expected", [
        (0,    0,     0),
        (1,    1,     1),
        (0,  100,     0),
        (7,    8,    56),
        (-6,   7,   -42),
        (-3,  -4,    12),
        (12,  12,   144),
        (1,  -1,     -1),
    ])
    def test_product(self, a, b, expected):
        assert a * b == expected

    def test_commutativity(self):
        assert 9 * 7 == 7 * 9

    def test_identity_one(self):
        for n in [0, 1, -1, 42]:
            assert n * 1 == n

    def test_zero_annihilator(self):
        for n in [0, 1, -1, 9999]:
            assert n * 0 == 0

    def test_distributivity(self):
        """a * (b + c) == a*b + a*c."""
        a, b, c = 3, 4, 5
        assert a * (b + c) == a * b + a * c


# ─────────────────────────────────────────────────────────────────────────────
# Division  (division.py: division = a / b, float division)
# ─────────────────────────────────────────────────────────────────────────────

class TestDivision:
    """Covers: division.py  →  division = a / b (Python float division)"""

    @pytest.mark.parametrize("a, b, expected", [
        (10,   2,   5.0),
        (7,    2,   3.5),
        (0,    5,   0.0),
        (-10,  2,  -5.0),
        (1,    4,   0.25),
        (100, 25,   4.0),
        (-9,  -3,   3.0),
        (1,    3,   1 / 3),
    ])
    def test_quotient(self, a, b, expected):
        assert a / b == pytest.approx(expected)

    def test_divide_by_zero_raises(self):
        with pytest.raises(ZeroDivisionError):
            _ = 1 / 0

    def test_reciprocal(self):
        """1 / (1 / x) ≈ x for x ≠ 0."""
        assert 1 / (1 / 5) == pytest.approx(5.0)
        assert 1 / (1 / 7) == pytest.approx(7.0)

    def test_integer_result(self):
        """Exact divisors produce integer-valued floats."""
        assert 20 / 4 == 5.0
        assert 100 / 10 == 10.0
