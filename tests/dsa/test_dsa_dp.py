"""
tests/dsa/test_dsa_dp.py
=========================
Tests for dynamic-programming and greedy problems under dsa/dp/:
    Knapsack01                     — 0/1 knapsack (DP bottom-up)
    FractionalKnapsack             — fractional knapsack (Greedy by ratio)
    LongestCommonSubsequence       — LCS length + sequence reconstruction
    LongestIncreasingSubsequence   — LIS length (O(N^2) tabulation)
    CoinChange                     — min coins + combination count
    EditDistance                   — Levenshtein distance
    HouseRobber                    — max non-adjacent sum
    SubsetSum                      — subset-sum reachability
    LongestPalindromicSubsequence  — interval DP
    MatrixChainMultiplication      — interval DP, optimal parenthesisation cost
"""

import pytest
from tests.utils import load_module


def _Knapsack01():
    return load_module('dsa/dp/knapsack_01.py',
                       ['2','1 2','3 4','5'], alias='dsa_ks01').Knapsack01

def _FractionalKnapsack():
    return load_module('dsa/dp/knapsack_fractional.py',
                       ['2','1 2','3 4','5'], alias='dsa_ksfrac').FractionalKnapsack

def _LCS():
    return load_module('dsa/dp/longest_common_subsequence.py',
                       ['a','b'], alias='dsa_lcs').LongestCommonSubsequence

def _LIS():
    return load_module('dsa/dp/longest_increasing_subsequence.py',
                       ['1 2'], alias='dsa_lis').LongestIncreasingSubsequence

def _CoinChange():
    return load_module('dsa/dp/coin_change.py',
                       ['1 2','3'], alias='dsa_coinchange').CoinChange

def _EditDistance():
    return load_module('dsa/dp/edit_distance.py',
                       ['a','b'], alias='dsa_editdistance').EditDistance

def _HouseRobber():
    return load_module('dsa/dp/house_robber.py',
                       ['1 2'], alias='dsa_houserobber').HouseRobber

def _SubsetSum():
    return load_module('dsa/dp/subset_sum.py',
                       ['1 2','3'], alias='dsa_subsetsum').SubsetSum

def _LPS():
    return load_module('dsa/dp/longest_palindromic_subsequence.py',
                       ['a'], alias='dsa_lps').LongestPalindromicSubsequence

def _MatrixChain():
    return load_module('dsa/dp/matrix_chain_multiplication.py',
                       ['1 2 3'], alias='dsa_matrixchain').MatrixChainMultiplication


# ═════════════════════════════════════════════════════════════════════════════

class TestKnapsack01:

    def test_classic(self):
        """weights=[1,3,4,5] values=[1,4,5,7] capacity=7 → 9"""
        assert _Knapsack01()([1,3,4,5],[1,4,5,7],7).max_value() == 9

    def test_empty_items(self):
        assert _Knapsack01()([],[],10).max_value() == 0

    def test_zero_capacity(self):
        assert _Knapsack01()([1,2],[10,20],0).max_value() == 0

    def test_single_item_fits(self):
        assert _Knapsack01()([5],[10],10).max_value() == 10

    def test_single_item_too_heavy(self):
        assert _Knapsack01()([10],[10],5).max_value() == 0

    def test_all_items_fit(self):
        assert _Knapsack01()([1,2,3],[4,5,6],100).max_value() == 15

    def test_greedy_not_optimal(self):
        """Greedy picks item-0 (value=10, w=5).  DP picks items 1+2 (12, w=6)."""
        assert _Knapsack01()([5,3,3],[10,6,6],6).max_value() == 12

    @pytest.mark.parametrize("w, v, cap, expected", [
        ([2,3,4,5],  [3,4,5,6],  5,   7),
        ([1,2,3],    [6,10,12],  5,  22),
        ([10,20,30], [60,100,120],50,220),
    ])
    def test_parametrized(self, w, v, cap, expected):
        assert _Knapsack01()(w, v, cap).max_value() == expected

    def test_exact_capacity_match(self):
        assert _Knapsack01()([7],[42],7).max_value() == 42

    def test_all_same_weight_pick_best(self):
        """capacity=4, weight=2 each → take 2 items → best pair = 8+5=13"""
        assert _Knapsack01()([2,2,2,2],[5,3,8,1],4).max_value() == 13


class TestFractionalKnapsack:

    def test_classic(self):
        """weights=[10,20,30] values=[60,100,120] cap=50 → 240"""
        assert _FractionalKnapsack()([10,20,30],[60,100,120],50).max_value() == pytest.approx(240.0)

    def test_all_items_fit(self):
        assert _FractionalKnapsack()([1,2,3],[5,10,15],100).max_value() == pytest.approx(30.0)

    def test_zero_capacity(self):
        assert _FractionalKnapsack()([1,2],[10,20],0).max_value() == pytest.approx(0.0)

    def test_single_item_full(self):
        assert _FractionalKnapsack()([5],[25],5).max_value() == pytest.approx(25.0)

    def test_single_item_fraction(self):
        """Take half the item: 5/10 × 50 = 25."""
        assert _FractionalKnapsack()([10],[50],5).max_value() == pytest.approx(25.0)

    def test_fraction_computed_correctly(self):
        """weights=[2,2] values=[10,4] cap=3 → 10 + 0.5×4 = 12"""
        assert _FractionalKnapsack()([2,2],[10,4],3).max_value() == pytest.approx(12.0)

    @pytest.mark.parametrize("w, v, cap, expected", [
        ([10,40,20,30], [60,40,100,120], 50, 240.0),
        ([5,10,15,20],  [50,60,70,80],  25, 156.67),
    ])
    def test_parametrized(self, w, v, cap, expected):
        assert _FractionalKnapsack()(w, v, cap).max_value() == pytest.approx(expected, rel=1e-2)

    def test_returns_float(self):
        assert isinstance(_FractionalKnapsack()([3],[9],3).max_value(), float)

    def test_greedy_optimal(self):
        """item-1 ratio=3 > item-0 ratio=2, cap=7: take all item-1 (2kg,6) then item-0 (5kg,10)."""
        assert _FractionalKnapsack()([5,2],[10,6],7).max_value() == pytest.approx(16.0)


class TestLongestCommonSubsequence:

    @pytest.mark.parametrize("s1, s2, expected_len", [
        ("ABCBDAB", "BDCABA", 4),
        ("abc", "abc", 3),
        ("abc", "def", 0),
        ("", "abc", 0),
        ("", "", 0),
        ("abcde", "ace", 3),
    ])
    def test_length(self, s1, s2, expected_len):
        assert _LCS()(s1, s2).length() == expected_len

    def test_sequence_is_valid_subsequence_of_both(self):
        lcs = _LCS()("ABCBDAB", "BDCABA")
        seq = lcs.sequence()
        assert len(seq) == lcs.length()
        # verify it's actually a subsequence of both strings
        def is_subsequence(sub, s):
            it = iter(s)
            return all(c in it for c in sub)
        assert is_subsequence(seq, "ABCBDAB")
        assert is_subsequence(seq, "BDCABA")

    def test_identical_strings_sequence(self):
        assert _LCS()("hello", "hello").sequence() == "hello"


class TestLongestIncreasingSubsequence:

    @pytest.mark.parametrize("arr, expected", [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7], 1),
        ([], 0),
        ([5], 1),
        ([1, 2, 3, 4, 5], 5),
        ([5, 4, 3, 2, 1], 1),
    ])
    def test_length(self, arr, expected):
        assert _LIS()(arr).length() == expected


class TestCoinChange:

    @pytest.mark.parametrize("coins, amount, expected", [
        ([1, 2, 5], 11, 3),
        ([2], 3, -1),
        ([1], 0, 0),
        ([1, 3, 4], 6, 2),
    ])
    def test_min_coins(self, coins, amount, expected):
        assert _CoinChange()(coins, amount).min_coins() == expected

    @pytest.mark.parametrize("coins, amount, expected", [
        ([1, 2, 5], 5, 4),
        ([2, 3], 5, 1),
        ([1, 2, 3], 4, 4),
        ([1], 0, 1),
    ])
    def test_count_combinations(self, coins, amount, expected):
        assert _CoinChange()(coins, amount).count_combinations() == expected


class TestEditDistance:

    @pytest.mark.parametrize("s1, s2, expected", [
        ("horse", "ros", 3),
        ("intention", "execution", 5),
        ("", "", 0),
        ("abc", "", 3),
        ("", "abc", 3),
        ("abc", "abc", 0),
    ])
    def test_calculate(self, s1, s2, expected):
        assert _EditDistance()(s1, s2).calculate() == expected


class TestHouseRobber:

    @pytest.mark.parametrize("money, expected", [
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([], 0),
        ([5], 5),
        ([2, 1], 2),
        ([1, 2], 2),
        ([5, 5, 10, 100, 10, 5], 110),
    ])
    def test_max_amount(self, money, expected):
        assert _HouseRobber()(money).max_amount() == expected


class TestSubsetSum:

    @pytest.mark.parametrize("nums, target, expected", [
        ([3, 34, 4, 12, 5, 2], 9, True),
        ([3, 34, 4, 12, 5, 2], 30, False),
        ([1, 2, 3], 0, True),
        ([], 0, True),
        ([], 5, False),
        ([5], 5, True),
    ])
    def test_has_subset_with_sum(self, nums, target, expected):
        assert _SubsetSum()(nums).has_subset_with_sum(target) == expected


class TestLongestPalindromicSubsequence:

    @pytest.mark.parametrize("s, expected", [
        ("bbbab", 4),
        ("cbbd", 2),
        ("a", 1),
        ("", 0),
        ("racecar", 7),
        ("abcd", 1),
    ])
    def test_length(self, s, expected):
        assert _LPS()(s).length() == expected


class TestMatrixChainMultiplication:

    @pytest.mark.parametrize("dims, expected", [
        ([40, 20, 30, 10, 30], 26000),
        ([10, 20, 30], 6000),
        ([10, 20], 0),
        ([5], 0),
        ([1, 2, 3, 4], 18),
    ])
    def test_min_cost(self, dims, expected):
        assert _MatrixChain()(dims).min_cost() == expected
