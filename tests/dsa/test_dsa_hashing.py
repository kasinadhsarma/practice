"""
tests/dsa/test_dsa_hashing.py
==============================
Tests for all hashing algorithms under dsa/hashing/:
    IsomorphicStrings · CharFrequencyDeficit · TwoSum · GroupAnagrams ·
    LongestConsecutiveSequence · FirstUniqueCharacter · SubarraySumEqualsK
"""

import pytest
from tests.utils import load_module


def _IsomorphicStrings():
    return load_module('dsa/hashing/isomorphic_strings.py', ['1', 'a', 'a'], alias='dsa_isomorphic').IsomorphicStrings

def _CharFrequencyDeficit():
    return load_module('dsa/hashing/char_frequency_deficit.py', ['a', 'a'], alias='dsa_chardeficit').CharFrequencyDeficit

def _TwoSum():
    return load_module('dsa/hashing/two_sum.py', ['1 2', '3'], alias='dsa_twosum').TwoSum

def _GroupAnagrams():
    return load_module('dsa/hashing/group_anagrams.py', ['a'], alias='dsa_groupanagrams').GroupAnagrams

def _LongestConsecutiveSequence():
    return load_module('dsa/hashing/longest_consecutive_sequence.py', ['1'], alias='dsa_longestrun').LongestConsecutiveSequence

def _FirstUniqueCharacter():
    return load_module('dsa/hashing/first_unique_character.py', ['a'], alias='dsa_firstunique').FirstUniqueCharacter

def _SubarraySumEqualsK():
    return load_module('dsa/hashing/subarray_sum_equals_k.py', ['1', '1'], alias='dsa_subarraysum').SubarraySumEqualsK


class TestIsomorphicStrings:

    @pytest.mark.parametrize("s1, s2, expected", [
        ("egg", "add", True),
        ("foo", "bar", False),
        ("foo", "add", True),
        ("paper", "title", True),
        ("badc", "baba", False),
    ])
    def test_is_isomorphic(self, s1, s2, expected):
        assert _IsomorphicStrings()().is_isomorphic(s1, s2) == expected

    def test_different_lengths(self):
        assert _IsomorphicStrings()().is_isomorphic("ab", "abc") is False

    def test_count_matches(self):
        # egg~add and foo~add are isomorphic, "add"~"add" trivially is too, bar~add is not
        candidates = ["egg", "foo", "bar", "add"]
        assert _IsomorphicStrings()().count_matches(candidates, "add") == 3


class TestCharFrequencyDeficit:

    @pytest.mark.parametrize("s, r, expected", [
        ("abc", "cbabadcbbd", 0),
        ("aab", "b", 2),
        ("xyz", "xyz", 0),
        ("aaaa", "aa", 2),
        ("", "abc", 0),
    ])
    def test_calculate(self, s, r, expected):
        assert _CharFrequencyDeficit()().calculate(s, r) == expected


class TestTwoSum:

    def test_finds_pair(self):
        assert _TwoSum()([2, 7, 11, 15]).find_indices(9) == (0, 1)

    def test_finds_pair_not_adjacent(self):
        assert _TwoSum()([3, 2, 4]).find_indices(6) == (1, 2)

    def test_no_pair_found(self):
        assert _TwoSum()([1, 2, 3]).find_indices(100) is None

    def test_duplicate_values(self):
        assert _TwoSum()([3, 3]).find_indices(6) == (0, 1)


class TestGroupAnagrams:

    def test_groups_correctly(self):
        words = ["eat", "tea", "tan", "ate", "nat", "bat"]
        result = _GroupAnagrams()(words).group()
        groups = [sorted(group) for group in result]
        assert sorted(groups) == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]

    def test_empty_list(self):
        assert _GroupAnagrams()([]).group() == []

    def test_no_anagrams(self):
        result = _GroupAnagrams()(["abc", "def"]).group()
        assert len(result) == 2


class TestLongestConsecutiveSequence:

    @pytest.mark.parametrize("nums, expected", [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([], 0),
        ([5], 1),
        ([1, 2, 0, 1], 3),
    ])
    def test_longest_run(self, nums, expected):
        assert _LongestConsecutiveSequence()(nums).longest_run() == expected


class TestFirstUniqueCharacter:

    @pytest.mark.parametrize("s, expected", [
        ("leetcode", 0),
        ("loveleetcode", 2),
        ("aabb", -1),
        ("", -1),
        ("z", 0),
    ])
    def test_find_index(self, s, expected):
        assert _FirstUniqueCharacter()(s).find_index() == expected


class TestSubarraySumEqualsK:

    @pytest.mark.parametrize("nums, k, expected", [
        ([1, 1, 1], 2, 2),
        ([1, 2, 3], 3, 2),
        ([1, -1, 0], 0, 3),
        ([], 0, 0),
        ([3, 4, 7, 2, -3, 1, 4, 2], 7, 4),
    ])
    def test_count_subarrays(self, nums, k, expected):
        assert _SubarraySumEqualsK()(nums).count_subarrays(k) == expected
