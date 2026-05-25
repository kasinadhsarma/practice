"""
tests/dsa/test_dsa_dp.py
=========================
Tests for dynamic-programming and greedy problems under dsa/dp/:
    Knapsack01         — 0/1 knapsack (DP bottom-up)
    FractionalKnapsack — fractional knapsack (Greedy by ratio)
"""

import pytest
from tests.utils import load_module


def _Knapsack01():
    return load_module('dsa/dp/knapsack_01.py',
                       ['2','1 2','3 4','5'], alias='dsa_ks01').Knapsack01

def _FractionalKnapsack():
    return load_module('dsa/dp/knapsack_fractional.py',
                       ['2','1 2','3 4','5'], alias='dsa_ksfrac').FractionalKnapsack


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
