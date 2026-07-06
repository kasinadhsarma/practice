"""
tests/mathmatics/test_mathmatics_matrices.py
=============================================
Tests for every matrix operation under mathmatics/matrices/:

    addition, subtraction, multiplication, scalar_multiplication,
    transpose, determinant, identity, trace, is_symmetric, rotate90,
    rank, inverse, power
"""

import pytest
from tests.utils import load_module


# ── Class loaders ──────────────────────────────────────────────────────────────
# None of these scripts shadow their class name, so load_module() + attribute
# access is sufficient (no load_class() needed). None call input().

def _Addition():
    return load_module('mathmatics/matrices/addition.py', [], alias='mat_addition').addition

def _Subtraction():
    return load_module('mathmatics/matrices/subtraction.py', [], alias='mat_subtraction').subtraction

def _Multiplication():
    return load_module('mathmatics/matrices/multiplication.py', [], alias='mat_multiplication').multiplication

def _ScalarMultiplication():
    return load_module('mathmatics/matrices/scalar_multiplication.py', [], alias='mat_scalarmul').scalar_multiplication

def _Transpose():
    return load_module('mathmatics/matrices/transpose.py', [], alias='mat_transpose').transpose

def _Determinant():
    return load_module('mathmatics/matrices/determinant.py', [], alias='mat_determinant').determinant

def _Identity():
    return load_module('mathmatics/matrices/identity.py', [], alias='mat_identity').identity

def _Trace():
    return load_module('mathmatics/matrices/trace.py', [], alias='mat_trace').trace

def _IsSymmetric():
    return load_module('mathmatics/matrices/is_symmetric.py', [], alias='mat_issymmetric').is_symmetric

def _Rotate90():
    return load_module('mathmatics/matrices/rotate90.py', [], alias='mat_rotate90').rotate90

def _Rank():
    return load_module('mathmatics/matrices/rank.py', [], alias='mat_rank').rank

def _Inverse():
    return load_module('mathmatics/matrices/inverse.py', [], alias='mat_inverse').inverse

def _Power():
    return load_module('mathmatics/matrices/power.py', [], alias='mat_power').power


# ═════════════════════════════════════════════════════════════════════════════
#  ARITHMETIC
# ═════════════════════════════════════════════════════════════════════════════

class TestAddition:

    def test_add(self):
        a = [[1, 2], [3, 4]]
        b = [[5, 6], [7, 8]]
        assert _Addition()().add(a, b) == [[6, 8], [10, 12]]

    def test_mismatched_dimensions(self):
        a = [[1, 2]]
        b = [[1, 2, 3]]
        assert _Addition()().add(a, b) == "Matrices cannot be added"


class TestSubtraction:

    def test_sub(self):
        a = [[5, 6], [7, 8]]
        b = [[1, 2], [3, 4]]
        assert _Subtraction()().sub(a, b) == [[4, 4], [4, 4]]

    def test_mismatched_dimensions(self):
        a = [[1, 2]]
        b = [[1, 2, 3]]
        assert _Subtraction()().sub(a, b) == "Matrices cannot be subtracted"


class TestMultiplication:

    def test_mul(self):
        a = [[1, 2], [3, 4]]
        b = [[5, 6], [7, 8]]
        assert _Multiplication()().mul(a, b) == [[19, 22], [43, 50]]

    def test_incompatible_dimensions(self):
        a = [[1, 2, 3]]
        b = [[1, 2, 3]]
        assert _Multiplication()().mul(a, b) == "Matrices cannot be multiplied"


class TestScalarMultiplication:

    def test_multiply(self):
        matrix = [[1, 2], [3, 4]]
        assert _ScalarMultiplication()().multiply(matrix, 3) == [[3, 6], [9, 12]]

    def test_multiply_by_zero(self):
        matrix = [[1, 2], [3, 4]]
        assert _ScalarMultiplication()().multiply(matrix, 0) == [[0, 0], [0, 0]]


# ═════════════════════════════════════════════════════════════════════════════
#  STRUCTURE
# ═════════════════════════════════════════════════════════════════════════════

class TestTranspose:

    def test_square(self):
        matrix = [[1, 2], [3, 4]]
        assert _Transpose()().get_transpose(matrix) == [[1, 3], [2, 4]]

    def test_non_square(self):
        matrix = [[1, 2, 3], [4, 5, 6]]
        assert _Transpose()().get_transpose(matrix) == [[1, 4], [2, 5], [3, 6]]

    def test_double_transpose_returns_original(self):
        matrix = [[1, 2, 3], [4, 5, 6]]
        t = _Transpose()()
        assert t.get_transpose(t.get_transpose(matrix)) == matrix


class TestIdentity:

    @pytest.mark.parametrize("n, expected", [
        (1, [[1]]),
        (2, [[1, 0], [0, 1]]),
        (3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]]),
    ])
    def test_generate(self, n, expected):
        assert _Identity()().generate(n) == expected


class TestIsSymmetric:

    def test_symmetric_matrix(self):
        matrix = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]
        assert _IsSymmetric()().check(matrix) is True

    def test_non_symmetric_matrix(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        assert _IsSymmetric()().check(matrix) is False

    def test_non_square_matrix(self):
        matrix = [[1, 2, 3], [4, 5, 6]]
        assert _IsSymmetric()().check(matrix) is False

    def test_identity_is_symmetric(self):
        matrix = _Identity()().generate(4)
        assert _IsSymmetric()().check(matrix) is True


class TestRotate90:

    def test_clockwise_3x3(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        assert _Rotate90()().clockwise(matrix) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    def test_four_rotations_return_original(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        r = _Rotate90()()
        rotated = matrix
        for _ in range(4):
            rotated = r.clockwise(rotated)
        assert rotated == matrix

    def test_non_square(self):
        matrix = [[1, 2, 3], [4, 5, 6]]
        assert _Rotate90()().clockwise(matrix) == [[4, 1], [5, 2], [6, 3]]


# ═════════════════════════════════════════════════════════════════════════════
#  DETERMINANT, RANK, INVERSE, POWER
# ═════════════════════════════════════════════════════════════════════════════

class TestDeterminant:

    def test_1x1(self):
        assert _Determinant()().calculate([[5]]) == 5

    def test_2x2(self):
        assert _Determinant()().calculate([[1, 2], [3, 4]]) == -2

    def test_3x3(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 10]]
        assert _Determinant()().calculate(matrix) == -3

    def test_singular_matrix(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        assert _Determinant()().calculate(matrix) == 0

    def test_identity_determinant_is_one(self):
        matrix = _Identity()().generate(4)
        assert _Determinant()().calculate(matrix) == 1


class TestRank:

    def test_full_rank(self):
        matrix = [[1, 2], [3, 4]]
        assert _Rank()().calculate(matrix) == 2

    def test_rank_deficient(self):
        matrix = [[1, 2, 3], [2, 4, 6], [1, 0, 1]]
        assert _Rank()().calculate(matrix) == 2

    def test_zero_matrix(self):
        matrix = [[0, 0], [0, 0]]
        assert _Rank()().calculate(matrix) == 0

    def test_identity_is_full_rank(self):
        matrix = _Identity()().generate(3)
        assert _Rank()().calculate(matrix) == 3


class TestInverse:

    def test_2x2(self):
        matrix = [[4, 7], [2, 6]]
        result = _Inverse()().calculate(matrix)
        expected = [[0.6, -0.7], [-0.2, 0.4]]
        for r, e in zip(result, expected):
            for rv, ev in zip(r, e):
                assert rv == pytest.approx(ev)

    def test_singular_matrix_has_no_inverse(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        assert _Inverse()().calculate(matrix) == "Matrix is singular and has no inverse"

    def test_inverse_times_original_is_identity(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 10]]
        inv = _Inverse()().calculate(matrix)
        product = _Multiplication()().mul(matrix, inv)
        identity_matrix = _Identity()().generate(3)
        for r, e in zip(product, identity_matrix):
            for rv, ev in zip(r, e):
                assert rv == pytest.approx(ev, abs=1e-9)


class TestPower:

    def test_power_zero_is_identity(self):
        matrix = [[2, 0], [0, 2]]
        assert _Power()().calculate(matrix, 0) == [[1, 0], [0, 1]]

    def test_power_one_is_self(self):
        matrix = [[1, 2], [3, 4]]
        assert _Power()().calculate(matrix, 1) == matrix

    def test_fibonacci_matrix_power(self):
        matrix = [[1, 1], [1, 0]]
        assert _Power()().calculate(matrix, 5) == [[8, 5], [5, 3]]

    def test_negative_power_rejected(self):
        matrix = [[1, 2], [3, 4]]
        assert _Power()().calculate(matrix, -1) == "Only non-negative integer powers are supported"
