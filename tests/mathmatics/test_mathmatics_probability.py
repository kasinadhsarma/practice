"""
tests/mathmatics/test_mathmatics_probability.py
==================================================
Tests for every operation under mathmatics/probability/:

    probability_of_event, complement_rule, addition_rule,
    conditional_probability, bayes_theorem, permutations, combinations,
    binomial_distribution, expected_value_variance, normal_distribution
"""

import pytest
from tests.utils import load_module


def _ProbabilityOfEvent():
    return load_module('mathmatics/probability/probability_of_event.py', [], alias='prob_event').probability_of_event

def _ComplementRule():
    return load_module('mathmatics/probability/complement_rule.py', [], alias='prob_complement').complement_rule

def _AdditionRule():
    return load_module('mathmatics/probability/addition_rule.py', [], alias='prob_addition').addition_rule

def _ConditionalProbability():
    return load_module('mathmatics/probability/conditional_probability.py', [], alias='prob_conditional').conditional_probability

def _BayesTheorem():
    return load_module('mathmatics/probability/bayes_theorem.py', [], alias='prob_bayes').bayes_theorem

def _Permutations():
    return load_module('mathmatics/probability/permutations.py', [], alias='prob_permutations').permutations

def _Combinations():
    return load_module('mathmatics/probability/combinations.py', [], alias='prob_combinations').combinations

def _BinomialDistribution():
    return load_module('mathmatics/probability/binomial_distribution.py', [], alias='prob_binomial').binomial_distribution

def _ExpectedValueVariance():
    return load_module('mathmatics/probability/expected_value_variance.py', [], alias='prob_evv').expected_value_variance

def _NormalDistribution():
    return load_module('mathmatics/probability/normal_distribution.py', [], alias='prob_normal').normal_distribution


# ═════════════════════════════════════════════════════════════════════════════

class TestProbabilityOfEvent:

    def test_basic(self):
        assert _ProbabilityOfEvent()().calculate(4, 52) == pytest.approx(4 / 52)

    def test_certain_event(self):
        assert _ProbabilityOfEvent()().calculate(10, 10) == 1.0

    def test_impossible_event(self):
        assert _ProbabilityOfEvent()().calculate(0, 10) == 0.0

    def test_invalid_favorable_greater_than_total(self):
        assert _ProbabilityOfEvent()().calculate(20, 10) is None

    def test_zero_total_returns_none(self):
        assert _ProbabilityOfEvent()().calculate(0, 0) is None


class TestComplementRule:

    def test_basic(self):
        assert _ComplementRule()().calculate(0.3) == pytest.approx(0.7)

    def test_zero(self):
        assert _ComplementRule()().calculate(0) == 1

    def test_one(self):
        assert _ComplementRule()().calculate(1) == 0

    def test_out_of_range_returns_none(self):
        assert _ComplementRule()().calculate(1.5) is None


class TestAdditionRule:

    def test_mutually_exclusive(self):
        assert _AdditionRule()().calculate(0.2, 0.3) == pytest.approx(0.5)

    def test_with_overlap(self):
        assert _AdditionRule()().calculate(0.5, 0.33, 1/6) == pytest.approx(0.6633333, rel=1e-6)


class TestConditionalProbability:

    def test_basic(self):
        assert _ConditionalProbability()().calculate(0.15, 0.5) == pytest.approx(0.3)

    def test_zero_p_b_returns_none(self):
        assert _ConditionalProbability()().calculate(0.1, 0) is None


class TestBayesTheorem:

    def test_disease_test_example(self):
        priors = [0.01, 0.99]
        likelihoods = [0.99, 0.05]
        result = _BayesTheorem()().calculate(likelihoods[0], priors[0], priors, likelihoods)
        assert result == pytest.approx(0.16666667, rel=1e-6)

    def test_zero_evidence_returns_none(self):
        result = _BayesTheorem()().calculate(0, 0.5, [0.5, 0.5], [0, 0])
        assert result is None

    def test_mismatched_lengths_returns_none(self):
        result = _BayesTheorem()().calculate(0.99, 0.01, [0.01, 0.99], [0.99])
        assert result is None


class TestPermutations:

    @pytest.mark.parametrize("n, r, expected", [
        (5, 2, 20), (5, 0, 1), (5, 5, 120), (10, 3, 720),
    ])
    def test_calculate(self, n, r, expected):
        assert _Permutations()().calculate(n, r) == expected

    def test_r_greater_than_n_returns_none(self):
        assert _Permutations()().calculate(3, 5) is None


class TestCombinations:

    @pytest.mark.parametrize("n, r, expected", [
        (5, 2, 10), (5, 0, 1), (5, 5, 1), (10, 3, 120),
    ])
    def test_calculate(self, n, r, expected):
        assert _Combinations()().calculate(n, r) == expected

    def test_r_greater_than_n_returns_none(self):
        assert _Combinations()().calculate(3, 5) is None


class TestBinomialDistribution:

    def test_pmf(self):
        bd = _BinomialDistribution()()
        assert bd.pmf(10, 6, 0.5) == pytest.approx(0.205078125)

    def test_pmf_out_of_range_returns_zero(self):
        bd = _BinomialDistribution()()
        assert bd.pmf(5, 6, 0.5) == 0

    def test_cdf_equals_sum_of_pmfs(self):
        bd = _BinomialDistribution()()
        manual = sum(bd.pmf(10, i, 0.5) for i in range(4))
        assert bd.cdf(10, 3, 0.5) == pytest.approx(manual)

    def test_cdf_full_range_is_one(self):
        bd = _BinomialDistribution()()
        assert bd.cdf(10, 10, 0.5) == pytest.approx(1.0)


class TestExpectedValueVariance:

    def test_fair_die_expected_value(self):
        values = [1, 2, 3, 4, 5, 6]
        probabilities = [1/6] * 6
        evv = _ExpectedValueVariance()()
        assert evv.expected_value(values, probabilities) == pytest.approx(3.5)

    def test_fair_die_variance(self):
        values = [1, 2, 3, 4, 5, 6]
        probabilities = [1/6] * 6
        evv = _ExpectedValueVariance()()
        assert evv.variance(values, probabilities) == pytest.approx(2.9166667, rel=1e-6)


class TestNormalDistribution:

    def test_standard_normal_pdf_at_mean(self):
        nd = _NormalDistribution()()
        assert nd.pdf(0, 0, 1) == pytest.approx(0.3989423, rel=1e-6)

    def test_standard_normal_cdf_at_mean(self):
        nd = _NormalDistribution()()
        assert nd.cdf(0, 0, 1) == pytest.approx(0.5)

    def test_cdf_far_right_approaches_one(self):
        nd = _NormalDistribution()()
        assert nd.cdf(5, 0, 1) > 0.999

    def test_invalid_sigma_returns_none(self):
        nd = _NormalDistribution()()
        assert nd.pdf(0, 0, -1) is None
        assert nd.cdf(0, 0, 0) is None
