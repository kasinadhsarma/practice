"""
tests/dsa/test_dsa_logic.py
============================
Tests for all logic/math problems under dsa/basics/logic/:

Level 1  — LeapYear, EvenOdd
Level 2  — Armstrong, Palindrome, ReverseInteger, SumOfDigits, StrongNumber
Level 3  — Factorial, Fibonacci, PrimeCheck, PerfectNumber, GCD, DirectionTracker
"""

import math
import pytest
from tests.utils import load_module, load_class


# ── Class loaders ──────────────────────────────────────────────────────────────
# Shadowed (class name reused as variable) → load_class()
# Not shadowed → load_module().ClassName

def _LeapYear():     return load_class('dsa/basics/logic/level1/leapyear.py',          'leapyear')
def _EvenOdd():      return load_class('dsa/basics/logic/level1/even_odd.py',           'even_odd')
def _Armstrong():    return load_class('dsa/basics/logic/level2/armstrong_number.py',   'armstrong')
def _Palindrome():   return load_class('dsa/basics/logic/level2/palindrome_number.py',  'palindrome')
def _ReverseInt():   return load_class('dsa/basics/logic/level2/reversenumber.py',      'reverseInteger')

def _SumOfDigits():
    return load_module('dsa/basics/logic/level2/sum_of_digits.py', ['123'], alias='dsa_sodigits').SumOfDigits

def _StrongNumber():
    return load_module('dsa/basics/logic/level2/strong_number.py', ['145','200'], alias='dsa_strong').StrongNumber

def _Factorial():
    return load_module('dsa/basics/logic/level3/factorial.py',     ['5'],        alias='dsa_fact').Factorial

def _Fibonacci():
    return load_module('dsa/basics/logic/level3/fabonacci.py',     ['5','5'],    alias='dsa_fib').Fibonacci

def _PrimeCheck():
    return load_module('dsa/basics/logic/level3/prime_check.py',   ['7','20'],   alias='dsa_prime').PrimeCheck

def _PerfectNumber():
    return load_module('dsa/basics/logic/level3/perfectnumber.py', ['6','30'],   alias='dsa_perfect').PerfectNumber

def _GCD():
    return load_module('dsa/basics/logic/level3/gcd.py',           ['12','8'],   alias='dsa_gcd').GCD

def _DirectionTracker():  # no input() at module level
    return load_module('dsa/basics/logic/level3/direction_tracker.py', [], alias='dsa_dir').DirectionTracker


# ═════════════════════════════════════════════════════════════════════════════
#  LEVEL 1
# ═════════════════════════════════════════════════════════════════════════════

class TestLeapYear:
    """Simplified rule: year % 4 == 0  (note: ignores century exception)"""

    @pytest.mark.parametrize("year, expected", [
        (2000, "leap year"), (2024, "leap year"), (1600, "leap year"),
        (2001, "not a leap year"), (2019, "not a leap year"),
        (2100, "leap year"),   # per code only — real rule would say not leap
        (1900, "leap year"),   # same caveat
    ])
    def test_get_leapyear(self, year, expected):
        assert _LeapYear()(year).get_leapyear() == expected

    def test_year_zero(self):
        assert _LeapYear()(0).get_leapyear() == "leap year"


class TestEvenOdd:

    @pytest.mark.parametrize("num, expected", [
        (0,"even"),(2,"even"),(4,"even"),(-2,"even"),(100,"even"),
        (1,"odd"),(3,"odd"),(-1,"odd"),(-3,"odd"),(99,"odd"),
    ])
    def test_get_even_odd(self, num, expected):
        assert _EvenOdd()(num).get_even_odd() == expected


# ═════════════════════════════════════════════════════════════════════════════
#  LEVEL 2
# ═════════════════════════════════════════════════════════════════════════════

class TestArmstrong:

    @pytest.mark.parametrize("n, expected", [
        (1,True),(2,True),(9,True),
        (153,True),(370,True),(371,True),(407,True),(9474,True),
        (100,False),(123,False),(200,False),
    ])
    def test_get_armstrong(self, n, expected):
        assert _Armstrong()(n).get_armstrong() == expected


class TestPalindrome:

    @pytest.mark.parametrize("num, expected", [
        (1,"palindrome"),(11,"palindrome"),(121,"palindrome"),
        (1221,"palindrome"),(12321,"palindrome"),
        (123,"not a palindrome"),(10,"not a palindrome"),
        (100,"not a palindrome"),(1232,"not a palindrome"),
    ])
    def test_get_palindrome(self, num, expected):
        assert _Palindrome()(num).get_palindrome() == expected


class TestReverseInteger:
    INT32_MAX = 2**31 - 1

    @pytest.mark.parametrize("x, expected", [
        (123, 321), (-123, -321), (120, 21), (0, 0), (1, 1), (-1, -1),
        (1000000003, 0),   # overflow → 0
    ])
    def test_reverse(self, x, expected):
        ri = _ReverseInt()()
        assert ri.reverse(x) == expected

    def test_in_range_preserved(self):
        assert _ReverseInt()().reverse(12345) == 54321


class TestSumOfDigits:

    @pytest.mark.parametrize("n, expected_sum", [
        (0,0),(1,1),(9,9),(10,1),(123,6),(999,27),(100,1),
    ])
    def test_get_sum(self, n, expected_sum):
        assert _SumOfDigits()(n).get_sum() == expected_sum

    def test_negative_uses_abs(self):
        assert _SumOfDigits()(-123).get_sum() == 6

    @pytest.mark.parametrize("n, root", [
        (0,0),(9,9),(10,1),(19,1),(999,9),(123,6),
    ])
    def test_digital_root(self, n, root):
        assert _SumOfDigits()(n).get_digital_root() == root


class TestStrongNumber:

    @pytest.mark.parametrize("n, expected", [
        (1,True),(2,True),(145,True),
        (100,False),(10,False),(50,False),
    ])
    def test_is_strong(self, n, expected):
        assert _StrongNumber()(n).is_strong() == expected

    def test_find_up_to_200(self):
        assert _StrongNumber()(1).find_strong_numbers(200) == [1, 2, 145]

    def test_find_empty(self):
        assert _StrongNumber()(0).find_strong_numbers(0) == []


# ═════════════════════════════════════════════════════════════════════════════
#  LEVEL 3
# ═════════════════════════════════════════════════════════════════════════════

class TestFactorial:

    @pytest.mark.parametrize("n, expected", [
        (0,1),(1,1),(2,2),(3,6),(5,120),(10,3628800),
    ])
    def test_iterative(self, n, expected):
        assert _Factorial()(n).iterative() == expected

    @pytest.mark.parametrize("n, expected", [
        (0,1),(1,1),(5,120),(7,5040),
    ])
    def test_recursive(self, n, expected):
        assert _Factorial()(n).recursive() == expected

    def test_negative_raises(self):
        with pytest.raises(ValueError):
            _Factorial()(-1)

    @pytest.mark.parametrize("n, zeros", [
        (0,0),(4,0),(5,1),(10,2),(25,6),(100,24),
    ])
    def test_trailing_zeros(self, n, zeros):
        assert _Factorial()(n).trailing_zeros() == zeros


class TestFibonacci:

    @pytest.mark.parametrize("n, expected", [
        (0,0),(1,1),(2,1),(5,5),(10,55),(15,610),
    ])
    def test_iterative(self, n, expected):
        assert _Fibonacci()(n).iterative() == expected

    @pytest.mark.parametrize("n, expected", [
        (0,0),(1,1),(7,13),(10,55),
    ])
    def test_memoised(self, n, expected):
        assert _Fibonacci()(n).memoised() == expected

    @pytest.mark.parametrize("n, series", [
        (0,[0]),(1,[0,1]),(5,[0,1,1,2,3,5]),(8,[0,1,1,2,3,5,8,13,21]),
    ])
    def test_generate_series(self, n, series):
        assert _Fibonacci()(n).generate_series() == series

    def test_negative_raises(self):
        with pytest.raises(ValueError):
            _Fibonacci()(-1)

    def test_iterative_memoised_agree(self):
        for n in range(21):
            fib = _Fibonacci()(n)
            assert fib.iterative() == fib.memoised()

    @pytest.mark.parametrize("num, is_fib", [
        (0,True),(1,True),(2,True),(8,True),(13,True),
        (4,False),(6,False),(9,False),
    ])
    def test_is_fibonacci(self, num, is_fib):
        def perfect_sq(x): return int(x**0.5)**2 == x
        expected = perfect_sq(5*num*num+4) or perfect_sq(5*num*num-4)
        assert _Fibonacci().is_fibonacci(num) == expected


class TestPrimeCheck:

    @pytest.mark.parametrize("n, expected", [
        (0,False),(1,False),(2,True),(3,True),(4,False),
        (17,True),(97,True),(-5,False),(49,False),(101,True),
    ])
    def test_is_prime(self, n, expected):
        assert _PrimeCheck()(n).is_prime() == expected

    @pytest.mark.parametrize("n, factors", [
        (12,[2,2,3]),(28,[2,2,7]),(7,[7]),(60,[2,2,3,5]),(2,[2]),
    ])
    def test_prime_factors(self, n, factors):
        assert _PrimeCheck()(n).prime_factors() == factors

    @pytest.mark.parametrize("limit, primes", [
        (0,[]),(1,[]),(10,[2,3,5,7]),(20,[2,3,5,7,11,13,17,19]),(2,[2]),
    ])
    def test_sieve(self, limit, primes):
        assert _PrimeCheck().sieve(limit) == primes

    @pytest.mark.parametrize("n, nxt", [
        (2,3),(10,11),(14,17),(20,23),(1,2),
    ])
    def test_next_prime(self, n, nxt):
        assert _PrimeCheck()(n).next_prime() == nxt

    def test_sieve_all_prime(self):
        for p in _PrimeCheck().sieve(50):
            assert _PrimeCheck()(p).is_prime()


class TestPerfectNumber:

    @pytest.mark.parametrize("n, expected", [
        (6,True),(28,True),(496,True),
        (1,False),(2,False),(12,False),(100,False),
    ])
    def test_is_perfect(self, n, expected):
        assert _PerfectNumber()(n).is_perfect() == expected

    @pytest.mark.parametrize("n, cls", [
        (6,"Perfect"),(28,"Perfect"),
        (12,"Abundant"),(18,"Abundant"),
        (10,"Deficient"),(15,"Deficient"),
    ])
    def test_classify(self, n, cls):
        assert _PerfectNumber()(n).classify() == cls

    @pytest.mark.parametrize("n, divs", [
        (6,[1,2,3]),(12,[1,2,3,4,6]),(28,[1,2,4,7,14]),(4,[1,2]),
    ])
    def test_proper_divisors(self, n, divs):
        assert _PerfectNumber()(n).get_proper_divisors() == divs

    def test_find_up_to_30(self):
        assert _PerfectNumber().find_perfect_numbers(30) == [6, 28]

    def test_find_up_to_1000(self):
        assert _PerfectNumber().find_perfect_numbers(1000) == [6, 28, 496]


class TestGCD:

    @pytest.mark.parametrize("a, b, g", [
        (12,8,4),(48,18,6),(0,5,5),(5,0,5),(7,7,7),(1,1,1),(100,75,25),(17,13,1),
    ])
    def test_gcd_iterative(self, a, b, g):
        assert _GCD()(a, b).gcd_iterative() == g

    @pytest.mark.parametrize("a, b, g", [
        (12,8,4),(48,18,6),(0,5,5),(5,0,5),(21,14,7),
    ])
    def test_gcd_recursive(self, a, b, g):
        assert _GCD()(a, b).gcd_recursive() == g

    def test_negative_inputs_use_abs(self):
        assert _GCD()(-12, 8).gcd_iterative()  == 4
        assert _GCD()(12, -8).gcd_iterative()  == 4
        assert _GCD()(-12,-8).gcd_iterative()  == 4

    @pytest.mark.parametrize("a, b, lcm", [
        (4,6,12),(3,7,21),(5,10,10),(0,5,0),
    ])
    def test_lcm(self, a, b, lcm):
        assert _GCD()(a, b).lcm() == lcm

    def test_extended_gcd_bezout(self):
        for a, b in [(3,4),(12,8),(35,15),(7,13)]:
            g, x, y = _GCD()(a, b).extended_gcd()
            assert a * x + b * y == g

    def test_extended_gcd_matches_iterative(self):
        for a, b in [(3,4),(12,8),(7,5)]:
            calc = _GCD()(a, b)
            g, _, _ = calc.extended_gcd()
            assert g == calc.gcd_iterative()

    @pytest.mark.parametrize("nums, expected", [
        ([4,8,16],4),([12,18,24],6),([6],6),([5,15,25],5),([7,11,13],1),
    ])
    def test_gcd_of_list(self, nums, expected):
        assert _GCD().gcd_of_list(nums) == expected


class TestDirectionTracker:

    def test_initial_state(self):
        t = _DirectionTracker()()
        assert t.x == 0 and t.y == 0
        assert t.directions[t.dir_idx] == "North"

    def test_move_north(self):
        t = _DirectionTracker()()
        t.move_forward(5)
        assert t.x == 0 and t.y == 5

    def test_turn_right_then_move(self):
        t = _DirectionTracker()()
        t.turn_right()
        assert t.directions[t.dir_idx] == "East"
        t.move_forward(3)
        assert t.x == 3 and t.y == 0

    def test_turn_left_then_move(self):
        t = _DirectionTracker()()
        t.turn_left()
        assert t.directions[t.dir_idx] == "West"
        t.move_forward(4)
        assert t.x == -4 and t.y == 0

    def test_full_sequence(self):
        """Move 5N → turn right → 3E → turn left → 2N → at (3,7) facing North."""
        t = _DirectionTracker()()
        t.move_forward(5); t.turn_right(); t.move_forward(3)
        t.turn_left();     t.move_forward(2)
        assert t.x == 3 and t.y == 7
        assert t.directions[t.dir_idx] == "North"

    def test_four_rights_return_north(self):
        t = _DirectionTracker()()
        for _ in range(4): t.turn_right()
        assert t.directions[t.dir_idx] == "North"

    def test_four_lefts_return_north(self):
        t = _DirectionTracker()()
        for _ in range(4): t.turn_left()
        assert t.directions[t.dir_idx] == "North"

    def test_opposite_moves_cancel(self):
        t = _DirectionTracker()()
        t.move_forward(5); t.turn_right(); t.turn_right()  # now South
        t.move_forward(5)
        assert t.x == 0 and t.y == 0

    def test_get_position_format(self):
        t = _DirectionTracker()()
        t.move_forward(3)
        pos = t.get_position()
        assert "3" in pos and "North" in pos
