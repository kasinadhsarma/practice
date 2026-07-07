"""
tests/mathmatics/test_mathmatics_statistics.py
=================================================
Tests for every operation under mathmatics/statistics/:

    mean, median, mode, data_range, variance, standard_deviation,
    quartiles_iqr, covariance, correlation, z_score
"""

import pytest
from tests.utils import load_module


# ── Class loaders ──────────────────────────────────────────────────────────────
# None of these scripts shadow their class name, so load_module() + attribute
# access is sufficient (no load_class() needed). None call input().

def _Mean():
    return load_module('mathmatics/statistics/mean.py', [], alias='stat_mean').mean

def _Median():
    return load_module('mathmatics/statistics/median.py', [], alias='stat_median').median

def _Mode():
    return load_module('mathmatics/statistics/mode.py', [], alias='stat_mode').mode

def _DataRange():
    return load_module('mathmatics/statistics/data_range.py', [], alias='stat_range').data_range

def _Variance():
    return load_module('mathmatics/statistics/variance.py', [], alias='stat_variance').variance

def _StandardDeviation():
    return load_module('mathmatics/statistics/standard_deviation.py', [], alias='stat_stddev').standard_deviation

def _QuartilesIQR():
    return load_module('mathmatics/statistics/quartiles_iqr.py', [], alias='stat_quartiles').quartiles_iqr

def _Covariance():
    return load_module('mathmatics/statistics/covariance.py', [], alias='stat_covariance').covariance

def _Correlation():
    return load_module('mathmatics/statistics/correlation.py', [], alias='stat_correlation').correlation

def _ZScore():
    return load_module('mathmatics/statistics/z_score.py', [], alias='stat_zscore').z_score


# ═════════════════════════════════════════════════════════════════════════════

class TestMean:

    def test_basic(self):
        assert _Mean()().calculate([1, 2, 3, 4, 5]) == 3

    def test_single_value(self):
        assert _Mean()().calculate([7]) == 7

    def test_empty_returns_none(self):
        assert _Mean()().calculate([]) is None

    def test_negative_values(self):
        assert _Mean()().calculate([-2, -4, -6]) == -4


class TestMedian:

    def test_odd_length(self):
        assert _Median()().calculate([3, 1, 2]) == 2

    def test_even_length(self):
        assert _Median()().calculate([1, 2, 3, 4]) == 2.5

    def test_single_value(self):
        assert _Median()().calculate([9]) == 9

    def test_empty_returns_none(self):
        assert _Median()().calculate([]) is None

    def test_unsorted_input(self):
        assert _Median()().calculate([5, 1, 9, 3]) == 4.0


class TestMode:

    def test_single_mode(self):
        assert _Mode()().calculate([1, 2, 2, 3]) == [2]

    def test_multimodal(self):
        result = set(_Mode()().calculate([1, 1, 2, 2, 3]))
        assert result == {1, 2}

    def test_empty_returns_empty_list(self):
        assert _Mode()().calculate([]) == []

    def test_all_unique_returns_all(self):
        result = set(_Mode()().calculate([1, 2, 3]))
        assert result == {1, 2, 3}


class TestDataRange:

    def test_basic(self):
        assert _DataRange()().calculate([4, 8, 6, 5, 3]) == 5

    def test_empty_returns_none(self):
        assert _DataRange()().calculate([]) is None

    def test_all_same_value(self):
        assert _DataRange()().calculate([5, 5, 5]) == 0


class TestVariance:

    def test_population(self):
        result = _Variance()().calculate([2, 4, 4, 4, 5, 5, 7, 9], sample=False)
        assert result == pytest.approx(4.0)

    def test_sample(self):
        result = _Variance()().calculate([2, 4, 4, 4, 5, 5, 7, 9], sample=True)
        assert result == pytest.approx(4.571428571, rel=1e-6)

    def test_empty_returns_none(self):
        assert _Variance()().calculate([]) is None

    def test_sample_single_value_returns_none(self):
        assert _Variance()().calculate([5], sample=True) is None


class TestStandardDeviation:

    def test_population(self):
        result = _StandardDeviation()().calculate([2, 4, 4, 4, 5, 5, 7, 9], sample=False)
        assert result == pytest.approx(2.0)

    def test_empty_returns_none(self):
        assert _StandardDeviation()().calculate([]) is None


class TestQuartilesIQR:

    def test_basic(self):
        result = _QuartilesIQR()().calculate([2, 2, 3, 4, 5, 5, 6, 8, 8, 9])
        assert result["Q1"] == 3
        assert result["Q3"] == 8
        assert result["IQR"] == 5

    def test_empty_returns_none(self):
        assert _QuartilesIQR()().calculate([]) is None


class TestCovariance:

    def test_positive_relationship(self):
        result = _Covariance()().calculate([1, 2, 3, 4, 5], [2, 4, 6, 8, 10])
        assert result == pytest.approx(4.0)

    def test_mismatched_lengths_returns_none(self):
        assert _Covariance()().calculate([1, 2], [1, 2, 3]) is None

    def test_empty_returns_none(self):
        assert _Covariance()().calculate([], []) is None


class TestCorrelation:

    def test_perfect_positive_correlation(self):
        result = _Correlation()().calculate([1, 2, 3, 4, 5], [2, 4, 6, 8, 10])
        assert result == pytest.approx(1.0)

    def test_perfect_negative_correlation(self):
        result = _Correlation()().calculate([1, 2, 3, 4, 5], [10, 8, 6, 4, 2])
        assert result == pytest.approx(-1.0)

    def test_mismatched_lengths_returns_none(self):
        assert _Correlation()().calculate([1, 2], [1, 2, 3]) is None


class TestZScore:

    def test_basic(self):
        assert _ZScore()().calculate(8, 5.2, 2.4) == pytest.approx(1.1666666, rel=1e-6)

    def test_zero_std_dev_returns_none(self):
        assert _ZScore()().calculate(5, 5, 0) is None

    def test_value_equals_mean(self):
        assert _ZScore()().calculate(5, 5, 2) == 0
