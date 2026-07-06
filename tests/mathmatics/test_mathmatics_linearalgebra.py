"""
tests/mathmatics/test_mathmatics_linearalgebra.py
==================================================
Tests for every operation under mathmatics/algebra/linearalgebra/:

    Vectors — vector_addition, vector_subtraction, scalar_vector_multiplication,
              dot_product, cross_product, vector_magnitude, vector_normalization,
              angle_between_vectors, vector_projection, linear_independence
    Systems — solve_linear_system, cramers_rule
"""

import pytest
from tests.utils import load_module


# ── Class loaders ──────────────────────────────────────────────────────────────
# None of these scripts shadow their class name, so load_module() + attribute
# access is sufficient (no load_class() needed). None call input().

def _VectorAddition():
    return load_module('mathmatics/algebra/linearalgebra/vector_addition.py', [], alias='la_vecadd').vector_addition

def _VectorSubtraction():
    return load_module('mathmatics/algebra/linearalgebra/vector_subtraction.py', [], alias='la_vecsub').vector_subtraction

def _ScalarVectorMultiplication():
    return load_module('mathmatics/algebra/linearalgebra/scalar_vector_multiplication.py', [], alias='la_scalarvec').scalar_vector_multiplication

def _DotProduct():
    return load_module('mathmatics/algebra/linearalgebra/dot_product.py', [], alias='la_dot').dot_product

def _CrossProduct():
    return load_module('mathmatics/algebra/linearalgebra/cross_product.py', [], alias='la_cross').cross_product

def _VectorMagnitude():
    return load_module('mathmatics/algebra/linearalgebra/vector_magnitude.py', [], alias='la_magnitude').vector_magnitude

def _VectorNormalization():
    return load_module('mathmatics/algebra/linearalgebra/vector_normalization.py', [], alias='la_normalize').vector_normalization

def _AngleBetweenVectors():
    return load_module('mathmatics/algebra/linearalgebra/angle_between_vectors.py', [], alias='la_angle').angle_between_vectors

def _VectorProjection():
    return load_module('mathmatics/algebra/linearalgebra/vector_projection.py', [], alias='la_projection').vector_projection

def _LinearIndependence():
    return load_module('mathmatics/algebra/linearalgebra/linear_independence.py', [], alias='la_independence').linear_independence

def _SolveLinearSystem():
    return load_module('mathmatics/algebra/linearalgebra/solve_linear_system.py', [], alias='la_solve').solve_linear_system

def _CramersRule():
    return load_module('mathmatics/algebra/linearalgebra/cramers_rule.py', [], alias='la_cramers').cramers_rule


# ═════════════════════════════════════════════════════════════════════════════
#  VECTOR ARITHMETIC
# ═════════════════════════════════════════════════════════════════════════════

class TestVectorAddition:

    def test_add(self):
        assert _VectorAddition()().add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]

    def test_mismatched_lengths(self):
        assert _VectorAddition()().add([1, 2], [1, 2, 3]) == "Vectors must be the same length to add"


class TestVectorSubtraction:

    def test_subtract(self):
        assert _VectorSubtraction()().subtract([4, 5, 6], [1, 2, 3]) == [3, 3, 3]

    def test_mismatched_lengths(self):
        assert _VectorSubtraction()().subtract([1, 2], [1, 2, 3]) == "Vectors must be the same length to subtract"


class TestScalarVectorMultiplication:

    def test_multiply(self):
        assert _ScalarVectorMultiplication()().multiply([1, 2, 3], 3) == [3, 6, 9]

    def test_multiply_by_zero(self):
        assert _ScalarVectorMultiplication()().multiply([1, 2, 3], 0) == [0, 0, 0]


class TestDotProduct:

    @pytest.mark.parametrize("v1, v2, expected", [
        ([1, 2, 3], [4, 5, 6], 32),
        ([1, 0], [0, 1], 0),
        ([2, 2], [2, 2], 8),
    ])
    def test_calculate(self, v1, v2, expected):
        assert _DotProduct()().calculate(v1, v2) == expected

    def test_mismatched_lengths(self):
        assert _DotProduct()().calculate([1, 2], [1, 2, 3]) == "Vectors must be the same length for a dot product"


class TestCrossProduct:

    @pytest.mark.parametrize("v1, v2, expected", [
        ([1, 0, 0], [0, 1, 0], [0, 0, 1]),
        ([0, 1, 0], [0, 0, 1], [1, 0, 0]),
        ([1, 2, 3], [4, 5, 6], [-3, 6, -3]),
    ])
    def test_calculate(self, v1, v2, expected):
        assert _CrossProduct()().calculate(v1, v2) == expected

    def test_non_3d_vectors(self):
        assert _CrossProduct()().calculate([1, 2], [3, 4]) == "Cross product is only defined for 3D vectors"


# ═════════════════════════════════════════════════════════════════════════════
#  VECTOR GEOMETRY
# ═════════════════════════════════════════════════════════════════════════════

class TestVectorMagnitude:

    @pytest.mark.parametrize("vector, expected", [
        ([3, 4], 5.0),
        ([0, 0], 0.0),
        ([1, 0, 0], 1.0),
    ])
    def test_calculate(self, vector, expected):
        assert _VectorMagnitude()().calculate(vector) == pytest.approx(expected)


class TestVectorNormalization:

    def test_normalize(self):
        result = _VectorNormalization()().normalize([3, 4])
        assert result == pytest.approx([0.6, 0.8])

    def test_zero_vector(self):
        assert _VectorNormalization()().normalize([0, 0]) == "Cannot normalize the zero vector"

    def test_normalized_magnitude_is_one(self):
        result = _VectorNormalization()().normalize([3, 4])
        magnitude = _VectorMagnitude()().calculate(result)
        assert magnitude == pytest.approx(1.0)


class TestAngleBetweenVectors:

    @pytest.mark.parametrize("v1, v2, expected", [
        ([1, 0], [0, 1], 90.0),
        ([1, 0], [1, 0], 0.0),
        ([1, 0], [-1, 0], 180.0),
    ])
    def test_calculate(self, v1, v2, expected):
        assert _AngleBetweenVectors()().calculate(v1, v2) == pytest.approx(expected)

    def test_zero_vector_undefined(self):
        assert _AngleBetweenVectors()().calculate([0, 0], [1, 0]) == "Angle is undefined for a zero vector"


class TestVectorProjection:

    def test_project_onto_axis(self):
        assert _VectorProjection()().project([3, 4], [1, 0]) == [3.0, 0.0]

    def test_project_onto_zero_vector(self):
        assert _VectorProjection()().project([3, 4], [0, 0]) == "Cannot project onto the zero vector"

    def test_project_parallel_vector_is_identity(self):
        result = _VectorProjection()().project([2, 2], [1, 1])
        assert result == pytest.approx([2.0, 2.0])


class TestLinearIndependence:

    def test_identity_basis_is_independent(self):
        assert _LinearIndependence()().check([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) is True

    def test_duplicate_vector_is_dependent(self):
        assert _LinearIndependence()().check([[1, 2], [2, 4]]) is False

    def test_zero_vector_is_dependent(self):
        assert _LinearIndependence()().check([[1, 0], [0, 0]]) is False

    def test_two_independent_vectors(self):
        assert _LinearIndependence()().check([[1, 0], [0, 1]]) is True


# ═════════════════════════════════════════════════════════════════════════════
#  SOLVING LINEAR SYSTEMS
# ═════════════════════════════════════════════════════════════════════════════

class TestSolveLinearSystem:

    def test_3x3_system(self):
        coefficients = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
        constants = [8, -11, -3]
        result = _SolveLinearSystem()().solve(coefficients, constants)
        assert result == pytest.approx([2.0, 3.0, -1.0])

    def test_2x2_system(self):
        coefficients = [[1, 1], [1, -1]]
        constants = [10, 2]
        result = _SolveLinearSystem()().solve(coefficients, constants)
        assert result == pytest.approx([6.0, 4.0])

    def test_singular_system_has_no_unique_solution(self):
        coefficients = [[1, 2], [2, 4]]
        constants = [3, 6]
        assert _SolveLinearSystem()().solve(coefficients, constants) == "System has no unique solution"


class TestCramersRule:

    def test_2x2_system(self):
        result = _CramersRule()().solve([[2, 1], [1, 3]], [5, 10])
        assert result == pytest.approx([1.0, 3.0])

    def test_3x3_system(self):
        coefficients = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
        constants = [8, -11, -3]
        result = _CramersRule()().solve(coefficients, constants)
        assert result == pytest.approx([2.0, 3.0, -1.0])

    def test_singular_system_has_no_unique_solution(self):
        assert _CramersRule()().solve([[1, 2], [2, 4]], [3, 6]) == "System has no unique solution"

    def test_agrees_with_gaussian_elimination(self):
        coefficients = [[4, 3], [6, 3]]
        constants = [10, 12]
        gaussian = _SolveLinearSystem()().solve(coefficients, constants)
        cramers = _CramersRule()().solve(coefficients, constants)
        assert gaussian == pytest.approx(cramers)
