"""
tests/mathmatics/test_mathmatics_number_theory.py
====================================================
Tests for every operation under mathmatics/number_theory/:
    gcd_lcm, prime_sieve, prime_factorization, euler_totient
"""

import pytest
from tests.utils import load_module


def _GcdLcm():
    return load_module('mathmatics/number_theory/gcd_lcm.py', [], alias='nt_gcdlcm').gcd_lcm

def _PrimeSieve():
    return load_module('mathmatics/number_theory/prime_sieve.py', [], alias='nt_sieve').prime_sieve

def _PrimeFactorization():
    return load_module('mathmatics/number_theory/prime_factorization.py', [], alias='nt_factor').prime_factorization

def _EulerTotient():
    return load_module('mathmatics/number_theory/euler_totient.py', [], alias='nt_totient').euler_totient


# ═════════════════════════════════════════════════════════════════════════════

class TestGcdLcm:

    @pytest.mark.parametrize("a, b, expected", [(24, 36, 12), (17, 5, 1), (0, 5, 5), (100, 75, 25)])
    def test_gcd(self, a, b, expected):
        assert _GcdLcm()().gcd(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [(24, 36, 72), (4, 6, 12), (7, 3, 21)])
    def test_lcm(self, a, b, expected):
        assert _GcdLcm()().lcm(a, b) == expected

    def test_lcm_with_zero(self):
        assert _GcdLcm()().lcm(0, 5) == 0


class TestPrimeSieve:

    def test_primes_up_to_20(self):
        assert _PrimeSieve()().calculate(20) == [2, 3, 5, 7, 11, 13, 17, 19]

    def test_below_two_returns_empty(self):
        assert _PrimeSieve()().calculate(1) == []

    def test_two_is_prime(self):
        assert 2 in _PrimeSieve()().calculate(2)


class TestPrimeFactorization:

    def test_composite(self):
        assert _PrimeFactorization()().calculate(360) == [2, 2, 2, 3, 3, 5]

    def test_prime_number(self):
        assert _PrimeFactorization()().calculate(17) == [17]

    def test_power_of_two(self):
        assert _PrimeFactorization()().calculate(64) == [2] * 6

    def test_product_reconstructs_n(self):
        factors = _PrimeFactorization()().calculate(9973 * 2)
        product = 1
        for f in factors:
            product *= f
        assert product == 9973 * 2


class TestEulerTotient:

    @pytest.mark.parametrize("n, expected", [(36, 12), (1, 1), (7, 6), (10, 4)])
    def test_calculate(self, n, expected):
        assert _EulerTotient()().calculate(n) == expected

    def test_prime_totient_is_n_minus_one(self):
        assert _EulerTotient()().calculate(13) == 12
