"""
tests/dsa/test_dsa_arrays.py
=============================
Tests for every function under dsa/Arrays/ (11 files, function-based —
not class-based like the rest of dsa/). Each file executes demo code at
import time (prints), which is harmless; tests call the functions directly
after loading the module via tests.utils.load_module.

Known pre-existing limitations (documented via pytest.raises rather than
"fixed", since these files predate this test suite):
    - jump_search / exponential_search / fibonacci_search raise IndexError
      on an empty array (no empty-array guard in the original code).
    - interpolation_search raises ZeroDivisionError on a constant-valued
      array with more than one element (arr[hi] == arr[lo] denominator).
"""

import pytest
from tests.utils import load_module


def _m01():
    return load_module('dsa/Arrays/01_basics.py', [], alias='arr_01')

def _m02():
    return load_module('dsa/Arrays/02_searching.py', [], alias='arr_02')

def _m03():
    return load_module('dsa/Arrays/03_sorting.py', [], alias='arr_03')

def _m04():
    return load_module('dsa/Arrays/04_two_pointer_sliding_window.py', [], alias='arr_04')

def _m05():
    return load_module('dsa/Arrays/05_prefix_sum_difference_array.py', [], alias='arr_05')

def _m06():
    return load_module('dsa/Arrays/06_array_rotation.py', [], alias='arr_06')

def _m07():
    return load_module('dsa/Arrays/07_classic_problems.py', [], alias='arr_07')

def _m08():
    return load_module('dsa/Arrays/08_advanced_techniques.py', [], alias='arr_08')

def _m09():
    return load_module('dsa/Arrays/09_2d_matrix.py', [], alias='arr_09')

def _m10():
    return load_module('dsa/Arrays/10_special_arrays.py', [], alias='arr_10')

def _m11():
    return load_module('dsa/Arrays/11_remaining_topics.py', [], alias='arr_11')


# ═════════════════════════════════════════════════════════════════════════════
#  01_basics.py
# ═════════════════════════════════════════════════════════════════════════════

class TestRowMajorIndex:

    @pytest.mark.parametrize("r, c, cols, expected", [
        (1, 2, 3, 5),
        (0, 0, 3, 0),
        (2, 2, 3, 8),
        (0, 2, 5, 2),
        (3, 0, 4, 12),
    ])
    def test_index(self, r, c, cols, expected):
        assert _m01().row_major_index(r, c, cols) == expected


class TestBasicsLinearSearch:

    def test_found(self):
        assert _m01().linear_search([5, 20, 30, 40, 50], 30) == 2

    def test_not_found(self):
        assert _m01().linear_search([10, 20, 30], 99) == -1

    def test_empty(self):
        assert _m01().linear_search([], 1) == -1

    def test_first_element(self):
        assert _m01().linear_search([7, 8, 9], 7) == 0

    def test_last_element(self):
        assert _m01().linear_search([7, 8, 9], 9) == 2


# ═════════════════════════════════════════════════════════════════════════════
#  02_searching.py
# ═════════════════════════════════════════════════════════════════════════════

SORTED_ARR = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]


class TestLinearSearch:

    @pytest.mark.parametrize("target, expected", [(25, 2), (99, -1), (64, 0), (90, 6)])
    def test_search(self, target, expected):
        assert _m02().linear_search([64, 34, 25, 12, 22, 11, 90], target) == expected

    def test_empty(self):
        assert _m02().linear_search([], 1) == -1


class TestBinarySearchIterative:

    @pytest.mark.parametrize("target, expected_idx", [
        (23, 5), (72, 8), (2, 0), (91, 9), (99, -1), (0, -1),
    ])
    def test_search(self, target, expected_idx):
        assert _m02().binary_search_iterative(SORTED_ARR, target) == expected_idx

    def test_empty(self):
        assert _m02().binary_search_iterative([], 5) == -1

    def test_single_element_found(self):
        assert _m02().binary_search_iterative([5], 5) == 0

    def test_single_element_not_found(self):
        assert _m02().binary_search_iterative([5], 1) == -1


class TestBinarySearchRecursive:

    @pytest.mark.parametrize("target, expected_idx", [
        (23, 5), (72, 8), (2, 0), (91, 9), (99, -1), (0, -1),
    ])
    def test_search(self, target, expected_idx):
        assert _m02().binary_search_recursive(SORTED_ARR, target) == expected_idx

    def test_empty(self):
        assert _m02().binary_search_recursive([], 5) == -1

    def test_single_element_found(self):
        assert _m02().binary_search_recursive([5], 5) == 0

    def test_agrees_with_iterative(self):
        m = _m02()
        for target in [2, 16, 38, 91, 100, -5]:
            assert m.binary_search_recursive(SORTED_ARR, target) == m.binary_search_iterative(SORTED_ARR, target)


class TestJumpSearch:

    @pytest.mark.parametrize("target, expected_idx", [
        (56, 7), (2, 0), (91, 9), (99, -1), (8, 2),
    ])
    def test_search(self, target, expected_idx):
        assert _m02().jump_search(SORTED_ARR, target) == expected_idx

    def test_single_element_found(self):
        assert _m02().jump_search([5], 5) == 0

    def test_single_element_not_found(self):
        assert _m02().jump_search([5], 1) == -1

    def test_empty_array_raises(self):
        """Documented limitation: no empty-array guard in the original code."""
        with pytest.raises(IndexError):
            _m02().jump_search([], 5)


class TestInterpolationSearch:

    @pytest.mark.parametrize("target, expected_idx", [
        (91, 9), (2, 0), (16, 4), (99, -1), (-5, -1),
    ])
    def test_search(self, target, expected_idx):
        assert _m02().interpolation_search(SORTED_ARR, target) == expected_idx

    def test_single_element_found(self):
        assert _m02().interpolation_search([5], 5) == 0

    def test_empty_array(self):
        assert _m02().interpolation_search([], 5) == -1

    def test_constant_array_raises(self):
        """Documented limitation: arr[hi] == arr[lo] causes a ZeroDivisionError
        in the probe-position formula when the array has >1 element."""
        with pytest.raises(ZeroDivisionError):
            _m02().interpolation_search([5, 5, 5, 5], 5)


class TestExponentialSearch:

    @pytest.mark.parametrize("target, expected_idx", [
        (38, 6), (2, 0), (91, 9), (99, -1),
    ])
    def test_search(self, target, expected_idx):
        assert _m02().exponential_search(SORTED_ARR, target) == expected_idx

    def test_single_element_found(self):
        assert _m02().exponential_search([5], 5) == 0

    def test_empty_array_raises(self):
        """Documented limitation: accesses arr[0] without an empty-array guard."""
        with pytest.raises(IndexError):
            _m02().exponential_search([], 5)


class TestFibonacciSearch:

    @pytest.mark.parametrize("target, expected_idx", [
        (16, 4), (2, 0), (91, 9), (99, -1),
    ])
    def test_search(self, target, expected_idx):
        assert _m02().fibonacci_search(SORTED_ARR, target) == expected_idx

    def test_single_element_found(self):
        assert _m02().fibonacci_search([5], 5) == 0

    def test_empty_array(self):
        assert _m02().fibonacci_search([], 5) == -1

    def test_target_larger_than_all_elements(self):
        assert _m02().fibonacci_search(SORTED_ARR, 99) == -1


class TestOccurrenceVariants:

    DUP_ARR = [1, 2, 2, 2, 3, 4, 4, 5]

    def test_first_occurrence(self):
        assert _m02().first_occurrence(self.DUP_ARR, 2) == 1

    def test_last_occurrence(self):
        assert _m02().last_occurrence(self.DUP_ARR, 2) == 3

    def test_count_occurrences(self):
        assert _m02().count_occurrences(self.DUP_ARR, 2) == 3

    def test_first_occurrence_not_found(self):
        assert _m02().first_occurrence(self.DUP_ARR, 99) == -1

    def test_last_occurrence_not_found(self):
        assert _m02().last_occurrence(self.DUP_ARR, 99) == -1

    def test_count_not_found_is_zero(self):
        assert _m02().count_occurrences(self.DUP_ARR, 99) == 0

    def test_single_occurrence(self):
        assert _m02().first_occurrence(self.DUP_ARR, 5) == 7
        assert _m02().last_occurrence(self.DUP_ARR, 5) == 7
        assert _m02().count_occurrences(self.DUP_ARR, 5) == 1

    def test_count_of_4s(self):
        assert _m02().count_occurrences(self.DUP_ARR, 4) == 2


class TestSearchRotated:

    ROTATED = [4, 5, 6, 7, 0, 1, 2]

    @pytest.mark.parametrize("target, expected_idx", [
        (0, 4), (4, 0), (2, 6), (7, 3), (99, -1),
    ])
    def test_search(self, target, expected_idx):
        assert _m02().search_rotated(self.ROTATED, target) == expected_idx

    def test_single_element_found(self):
        assert _m02().search_rotated([5], 5) == 0

    def test_single_element_not_found(self):
        assert _m02().search_rotated([5], 1) == -1

    def test_not_actually_rotated(self):
        assert _m02().search_rotated([1, 2, 3, 4, 5], 4) == 3


class TestFloorSqrt:

    @pytest.mark.parametrize("n, expected", [
        (26, 5), (25, 5), (0, 0), (1, 1), (2, 1), (99, 9), (100, 10),
    ])
    def test_floor_sqrt(self, n, expected):
        assert _m02().floor_sqrt(n) == expected


class TestFindPeak:

    def test_middle_peak(self):
        arr = [1, 3, 20, 4, 1, 0]
        idx = _m02().find_peak(arr)
        assert arr[idx] == 20

    def test_strictly_increasing_peak_at_end(self):
        arr = [1, 2, 3, 4, 5]
        assert _m02().find_peak(arr) == 4

    def test_strictly_decreasing_peak_at_start(self):
        arr = [5, 4, 3, 2, 1]
        assert _m02().find_peak(arr) == 0

    def test_single_element(self):
        assert _m02().find_peak([5]) == 0

    def test_two_elements(self):
        assert _m02().find_peak([1, 2]) == 1
        assert _m02().find_peak([2, 1]) == 0


# ═════════════════════════════════════════════════════════════════════════════
#  03_sorting.py
# ═════════════════════════════════════════════════════════════════════════════

SORT_CASES = [
    ([5, 2, 8, 1, 9],          [1, 2, 5, 8, 9]),
    ([1, 2, 3, 4, 5],          [1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1],          [1, 2, 3, 4, 5]),
    ([42],                     [42]),
    ([],                       []),
    ([3, 1, 4, 1, 5, 9, 2, 6], [1, 1, 2, 3, 4, 5, 6, 9]),
    ([1, 1, 1, 1],             [1, 1, 1, 1]),
    ([-3, 0, 1, -1, 2],        [-3, -1, 0, 1, 2]),
]

NONNEGATIVE_SORT_CASES = [
    ([5, 2, 8, 1, 9],          [1, 2, 5, 8, 9]),
    ([1, 2, 3, 4, 5],          [1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1],          [1, 2, 3, 4, 5]),
    ([42],                     [42]),
    ([],                       []),
    ([3, 1, 4, 1, 5, 9, 2, 6], [1, 1, 2, 3, 4, 5, 6, 9]),
    ([170, 45, 75, 90, 802, 24, 2, 66], [2, 24, 45, 66, 75, 90, 170, 802]),
    ([0, 0, 0],                [0, 0, 0]),
]


class TestBubbleSort:
    @pytest.mark.parametrize("arr, expected", SORT_CASES)
    def test_sort(self, arr, expected):
        assert _m03().bubble_sort(arr) == expected

    def test_does_not_mutate_input(self):
        arr = [3, 1, 2]
        _m03().bubble_sort(arr)
        assert arr == [3, 1, 2]


class TestSelectionSort:
    @pytest.mark.parametrize("arr, expected", SORT_CASES)
    def test_sort(self, arr, expected):
        assert _m03().selection_sort(arr) == expected


class TestInsertionSort:
    @pytest.mark.parametrize("arr, expected", SORT_CASES)
    def test_sort(self, arr, expected):
        assert _m03().insertion_sort(arr) == expected


class TestShellSort:
    @pytest.mark.parametrize("arr, expected", SORT_CASES)
    def test_sort(self, arr, expected):
        assert _m03().shell_sort(arr) == expected


class TestMergeSort:
    @pytest.mark.parametrize("arr, expected", SORT_CASES)
    def test_sort(self, arr, expected):
        assert _m03().merge_sort(arr) == expected

    def test_merge_helper(self):
        assert _m03().merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]


class TestQuickSort:
    @pytest.mark.parametrize("arr, expected", SORT_CASES)
    def test_sort_in_place(self, arr, expected):
        a = arr[:]
        _m03().quick_sort(a)
        assert a == expected

    def test_partition(self):
        m = _m03()
        arr = [3, 6, 8, 10, 1, 2, 1]
        pi = m.partition(arr, 0, len(arr) - 1)
        assert all(arr[j] <= arr[pi] for j in range(pi))
        assert all(arr[j] >= arr[pi] for j in range(pi + 1, len(arr)))


class TestQuickSortRandomized:
    @pytest.mark.parametrize("arr, expected", SORT_CASES)
    def test_sort_in_place(self, arr, expected):
        a = arr[:]
        _m03().quick_sort_rand(a)
        assert a == expected


class TestHeapSort:
    @pytest.mark.parametrize("arr, expected", SORT_CASES)
    def test_sort(self, arr, expected):
        assert _m03().heap_sort(arr) == expected


class TestCountingSort:
    @pytest.mark.parametrize("arr, expected", NONNEGATIVE_SORT_CASES)
    def test_sort(self, arr, expected):
        assert _m03().counting_sort(arr) == expected


class TestRadixSort:
    @pytest.mark.parametrize("arr, expected", NONNEGATIVE_SORT_CASES)
    def test_sort(self, arr, expected):
        assert _m03().radix_sort(arr) == expected


class TestBucketSort:

    def test_floats_in_unit_range(self):
        result = _m03().bucket_sort([0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434])
        assert result == sorted([0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434])

    def test_empty(self):
        assert _m03().bucket_sort([]) == []

    def test_single_element(self):
        assert _m03().bucket_sort([0.5]) == [0.5]


# ═════════════════════════════════════════════════════════════════════════════
#  04_two_pointer_sliding_window.py
# ═════════════════════════════════════════════════════════════════════════════

class TestTwoSumSorted:

    def test_classic(self):
        assert _m04().two_sum_sorted([2, 7, 11, 15], 9) == (1, 2)

    def test_not_found(self):
        assert _m04().two_sum_sorted([1, 2, 3], 100) == (-1, -1)

    def test_middle_pair(self):
        assert _m04().two_sum_sorted([1, 2, 3, 4, 6], 6) == (2, 4)


class TestThreeSum:

    def test_classic(self):
        result = _m04().three_sum([-1, 0, 1, 2, -1, -4])
        assert sorted(map(tuple, result)) == sorted(map(tuple, [[-1, -1, 2], [-1, 0, 1]]))

    def test_no_triplet(self):
        assert _m04().three_sum([1, 2, 3]) == []

    def test_all_zeros(self):
        assert _m04().three_sum([0, 0, 0, 0]) == [[0, 0, 0]]


class TestMaxWater:

    def test_classic(self):
        assert _m04().max_water([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49

    def test_two_elements(self):
        assert _m04().max_water([1, 1]) == 1

    def test_empty(self):
        assert _m04().max_water([]) == 0


class TestMoveZeroes:

    def test_classic(self):
        assert _m04().move_zeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]

    def test_no_zeroes(self):
        assert _m04().move_zeroes([1, 2, 3]) == [1, 2, 3]

    def test_all_zeroes(self):
        assert _m04().move_zeroes([0, 0, 0]) == [0, 0, 0]


class TestRemoveDuplicates:

    def test_classic(self):
        assert _m04().remove_duplicates([1, 1, 2, 2, 3, 4, 4, 5]) == 5

    def test_empty(self):
        assert _m04().remove_duplicates([]) == 0

    def test_no_duplicates(self):
        assert _m04().remove_duplicates([1, 2, 3]) == 3

    def test_all_same(self):
        assert _m04().remove_duplicates([7, 7, 7]) == 1


class TestReverseArray:

    def test_classic(self):
        assert _m04().reverse_array([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]

    def test_empty(self):
        assert _m04().reverse_array([]) == []

    def test_single(self):
        assert _m04().reverse_array([1]) == [1]


class TestMergeSortedArrays:

    def test_classic(self):
        assert _m04().merge_sorted([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]

    def test_one_empty(self):
        assert _m04().merge_sorted([], [1, 2]) == [1, 2]
        assert _m04().merge_sorted([1, 2], []) == [1, 2]


class TestDutchFlag:

    def test_classic(self):
        assert _m04().dutch_flag([2, 0, 2, 1, 1, 0]) == [0, 0, 1, 1, 2, 2]

    def test_already_sorted(self):
        assert _m04().dutch_flag([0, 0, 1, 1, 2, 2]) == [0, 0, 1, 1, 2, 2]

    def test_single_value(self):
        assert _m04().dutch_flag([1, 1, 1]) == [1, 1, 1]


class TestMaxSumSubarrayK:

    def test_classic(self):
        assert _m04().max_sum_subarray_k([2, 1, 5, 1, 3, 2], 3) == 9

    def test_k_equals_length(self):
        assert _m04().max_sum_subarray_k([1, 2, 3], 3) == 6


class TestSmallestSubarraySum:

    def test_classic(self):
        assert _m04().smallest_subarray_sum([2, 1, 5, 2, 3, 2], 7) == 2

    def test_no_valid_subarray(self):
        assert _m04().smallest_subarray_sum([1, 2, 3], 100) == 0


class TestLongestSubstringNoRepeat:

    @pytest.mark.parametrize("s, expected", [
        ("abcabcbb", 3), ("pwwkew", 3), ("bbbbb", 1), ("", 0), ("abcdef", 6),
    ])
    def test_length(self, s, expected):
        assert _m04().length_of_longest_substring(s) == expected


class TestMaxOnesWithKFlips:

    def test_classic(self):
        # only 2 zeros fit in any length-7 window here; the source file's
        # inline comment claiming 9 is itself wrong — 7 is the correct answer
        assert _m04().max_ones_with_k_flips([1,1,0,0,1,1,1,0,1,1], 2) == 7

    def test_zero_flips(self):
        assert _m04().max_ones_with_k_flips([1, 1, 0, 1, 1], 0) == 2


class TestTotalFruit:

    def test_classic(self):
        assert _m04().total_fruit([1, 2, 1, 2, 3]) == 4

    def test_all_same(self):
        assert _m04().total_fruit([1, 1, 1]) == 3


class TestMinWindow:

    def test_classic(self):
        assert _m04().min_window("ADOBECODEBANC", "ABC") == "BANC"

    def test_no_valid_window(self):
        assert _m04().min_window("a", "aa") == ""

    def test_exact_match(self):
        assert _m04().min_window("a", "a") == "a"


# ═════════════════════════════════════════════════════════════════════════════
#  05_prefix_sum_difference_array.py
# ═════════════════════════════════════════════════════════════════════════════

class TestBuildPrefixSum:

    def test_classic(self):
        assert _m05().build_prefix_sum([2, 4, 6, 8, 10]) == [0, 2, 6, 12, 20, 30]

    def test_empty(self):
        assert _m05().build_prefix_sum([]) == [0]

    def test_single(self):
        assert _m05().build_prefix_sum([5]) == [0, 5]


class TestRangeSum:

    def test_classic(self):
        prefix = _m05().build_prefix_sum([2, 4, 6, 8, 10])
        assert _m05().range_sum(prefix, 1, 3) == 18
        assert _m05().range_sum(prefix, 0, 4) == 30

    def test_single_element_range(self):
        prefix = _m05().build_prefix_sum([2, 4, 6, 8, 10])
        assert _m05().range_sum(prefix, 2, 2) == 6


class TestSubarraySumEqualsK:

    @pytest.mark.parametrize("arr, k, expected", [
        ([1, 1, 1], 3, 1),
        ([1, 2, 3], 3, 2),
        ([1, -1, 2, -2], 0, 3),
        ([], 0, 0),
    ])
    def test_count(self, arr, k, expected):
        assert _m05().subarray_sum_equals_k(arr, k) == expected


class TestKadane:

    def test_classic(self):
        ms, s, e = _m05().kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        assert ms == 6
        assert (s, e) == (3, 6)

    def test_all_negative(self):
        ms, s, e = _m05().kadane([-3, -1, -2])
        assert ms == -1

    def test_single_element(self):
        ms, s, e = _m05().kadane([5])
        assert (ms, s, e) == (5, 0, 0)


class TestMaxCircularSubarray:

    def test_classic(self):
        assert _m05().max_circular_subarray([5, -3, 5]) == 10

    def test_all_negative(self):
        assert _m05().max_circular_subarray([-3, -1, -2]) == -1


class TestEquilibriumIndex:

    def test_classic(self):
        assert _m05().equilibrium_index([-7, 1, 5, 2, -4, 3, 0]) == 3

    def test_no_equilibrium(self):
        assert _m05().equilibrium_index([1, 2, 3]) == -1

    def test_first_index(self):
        assert _m05().equilibrium_index([0, 1, -1]) == 0


class TestBuild2DPrefixAndRangeSum:

    MATRIX = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5],
    ]

    def test_range_query(self):
        m = _m05()
        P = m.build_2d_prefix(self.MATRIX)
        assert m.matrix_range_sum(P, 2, 1, 4, 3) == 8

    def test_full_matrix_sum(self):
        m = _m05()
        P = m.build_2d_prefix(self.MATRIX)
        assert m.matrix_range_sum(P, 0, 0, 4, 4) == sum(sum(row) for row in self.MATRIX)

    def test_empty_matrix(self):
        assert _m05().build_2d_prefix([]) == []

    def test_single_cell(self):
        m = _m05()
        P = m.build_2d_prefix([[7]])
        assert m.matrix_range_sum(P, 0, 0, 0, 0) == 7


class TestRangeUpdateDemo:

    def test_classic(self):
        assert _m05().range_update_demo() == [3, 13, 18, 15, 5, 5]


class TestCarPooling:

    def test_over_capacity(self):
        assert _m05().car_pooling([[2, 1, 5], [3, 3, 7]], 4) is False

    def test_within_capacity(self):
        assert _m05().car_pooling([[2, 1, 5], [3, 3, 7]], 5) is True

    def test_no_trips(self):
        assert _m05().car_pooling([], 1) is True


class TestProductExceptSelf:

    def test_classic(self):
        assert _m05().product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]

    def test_with_zero(self):
        assert _m05().product_except_self([1, 2, 0, 4]) == [0, 0, 8, 0]

    def test_two_elements(self):
        assert _m05().product_except_self([3, 5]) == [5, 3]


# ═════════════════════════════════════════════════════════════════════════════
#  06_array_rotation.py
# ═════════════════════════════════════════════════════════════════════════════

class TestLeftRotateBrute:

    def test_classic(self):
        assert _m06().left_rotate_brute([1,2,3,4,5,6,7], 2) == [3,4,5,6,7,1,2]

    def test_d_zero(self):
        assert _m06().left_rotate_brute([1, 2, 3], 0) == [1, 2, 3]

    def test_d_equals_n(self):
        assert _m06().left_rotate_brute([1, 2, 3], 3) == [1, 2, 3]

    def test_d_greater_than_n(self):
        assert _m06().left_rotate_brute([1, 2, 3], 4) == [2, 3, 1]


class TestLeftRotateReversal:

    def test_classic(self):
        assert _m06().left_rotate_reversal([1,2,3,4,5,6,7], 2) == [3,4,5,6,7,1,2]

    def test_agrees_with_brute(self):
        m = _m06()
        arr = [1, 2, 3, 4, 5, 6, 7]
        for d in range(7):
            assert m.left_rotate_reversal(arr, d) == m.left_rotate_brute(arr, d)


class TestLeftRotateSlice:

    def test_classic(self):
        assert _m06().left_rotate_slice([1,2,3,4,5,6,7], 2) == [3,4,5,6,7,1,2]

    def test_agrees_with_brute(self):
        m = _m06()
        arr = [1, 2, 3, 4, 5, 6, 7]
        for d in range(7):
            assert m.left_rotate_slice(arr, d) == m.left_rotate_brute(arr, d)


class TestRightRotate:

    def test_classic(self):
        assert _m06().right_rotate([1,2,3,4,5,6,7], 2) == [6,7,1,2,3,4,5]

    def test_d_zero(self):
        assert _m06().right_rotate([1, 2, 3], 0) == [1, 2, 3]

    def test_undoes_left_rotate(self):
        m = _m06()
        arr = [1, 2, 3, 4, 5]
        rotated_left = m.left_rotate_reversal(arr, 2)
        assert m.right_rotate(rotated_left, 2) == arr


class TestIsRotation:

    def test_true_case(self):
        assert _m06().is_rotation([1,2,3,4,5], [3,4,5,1,2]) is True

    def test_false_case(self):
        assert _m06().is_rotation([1, 2, 3], [1, 3, 2]) is False

    def test_different_lengths(self):
        assert _m06().is_rotation([1, 2, 3], [1, 2]) is False

    def test_identical(self):
        assert _m06().is_rotation([1, 2, 3], [1, 2, 3]) is True


class TestRearrangeAlternate:

    def test_classic(self):
        assert _m06().rearrange_alternate([1,-2,-3,4,-5,6,7,-8]) == [1, -2, 4, -3, 6, -5, 7, -8]

    def test_more_positives(self):
        result = _m06().rearrange_alternate([1, 2, 3, -1])
        assert sorted(result) == sorted([1, 2, 3, -1])


class TestNextPermutation:

    @pytest.mark.parametrize("arr, expected", [
        ([1, 2, 3], [1, 3, 2]),
        ([3, 2, 1], [1, 2, 3]),
        ([1, 1, 5], [1, 5, 1]),
        ([1], [1]),
    ])
    def test_next(self, arr, expected):
        assert _m06().next_permutation(arr) == expected


class TestMaxProductSubarray:

    @pytest.mark.parametrize("arr, expected", [
        ([2, 3, -2, 4], 6),
        ([-2, 0, -1], 0),
        ([-2, 3, -4], 24),
        ([5], 5),
    ])
    def test_max_product(self, arr, expected):
        assert _m06().max_product_subarray(arr) == expected


class TestMajorityElement:

    def test_simple_majority(self):
        assert _m06().majority_element([3, 2, 3]) == 3

    def test_alternating_majority(self):
        assert _m06().majority_element([2,2,1,1,1,2,2]) == 2

    def test_no_majority(self):
        assert _m06().majority_element([1, 2, 3, 4]) is None

    def test_all_same(self):
        assert _m06().majority_element([5, 5, 5]) == 5


class TestFindLeaders:

    def test_classic(self):
        assert _m06().find_leaders([16,17,4,3,5,2]) == [17, 5, 2]

    def test_strictly_increasing(self):
        assert _m06().find_leaders([1, 2, 3]) == [3]

    def test_strictly_decreasing(self):
        assert _m06().find_leaders([3, 2, 1]) == [3, 2, 1]

    def test_single_element(self):
        assert _m06().find_leaders([5]) == [5]


class TestSortByFrequency:

    def test_classic(self):
        result = _m06().sort_by_frequency([2,3,2,4,5,12,2,3,3,3,12])
        assert result == [3, 3, 3, 3, 2, 2, 2, 12, 12, 4, 5]

    def test_empty(self):
        assert _m06().sort_by_frequency([]) == []


class TestSegregateEvenOdd:

    def test_classic(self):
        result = _m06().segregate_even_odd([1,2,3,4,5,6])
        assert set(result) == {1,2,3,4,5,6}
        evens_end = sum(1 for v in result if v % 2 == 0)
        assert all(v % 2 == 0 for v in result[:evens_end])
        assert all(v % 2 != 0 for v in result[evens_end:])

    def test_all_even(self):
        assert set(_m06().segregate_even_odd([2, 4, 6])) == {2, 4, 6}

    def test_all_odd(self):
        assert set(_m06().segregate_even_odd([1, 3, 5])) == {1, 3, 5}


class TestMergeIntervals:

    def test_classic(self):
        result = _m06().merge_intervals([[1,3],[2,6],[8,10],[15,18]])
        assert result == [[1,6],[8,10],[15,18]]

    def test_no_overlap(self):
        assert _m06().merge_intervals([[1, 2], [3, 4]]) == [[1, 2], [3, 4]]

    def test_empty(self):
        assert _m06().merge_intervals([]) == []

    def test_all_overlap(self):
        assert _m06().merge_intervals([[1, 4], [2, 5], [3, 6]]) == [[1, 6]]


# ═════════════════════════════════════════════════════════════════════════════
#  07_classic_problems.py
# ═════════════════════════════════════════════════════════════════════════════

class TestMissingNumber:

    def test_classic(self):
        assert _m07().missing_number([3, 0, 1]) == 2

    def test_missing_is_last(self):
        assert _m07().missing_number([0, 1]) == 2

    def test_missing_is_zero(self):
        assert _m07().missing_number([1, 2]) == 0


class TestMissingNumberXor:

    def test_classic(self):
        assert _m07().missing_number_xor([9,6,4,2,3,5,7,0,1]) == 8

    def test_agrees_with_sum_version(self):
        m = _m07()
        for nums in ([3, 0, 1], [0, 1], [1, 2]):
            assert m.missing_number_xor(nums) == m.missing_number(nums)


class TestFindDuplicateFloyd:

    def test_classic(self):
        assert _m07().find_duplicate_floyd([1, 3, 4, 2, 2]) == 2

    def test_duplicate_at_start(self):
        assert _m07().find_duplicate_floyd([2, 2, 1, 3]) == 2


class TestFindAllDuplicates:

    def test_classic(self):
        assert sorted(_m07().find_all_duplicates([4,3,2,7,8,2,3,1])) == [2, 3]

    def test_no_duplicates(self):
        assert _m07().find_all_duplicates([1, 2, 3]) == []

    def test_restores_original_array(self):
        arr = [4, 3, 2, 7, 8, 2, 3, 1]
        _m07().find_all_duplicates(arr)
        assert arr == [4, 3, 2, 7, 8, 2, 3, 1]


class TestFindMissingRepeating:

    def test_classic(self):
        assert _m07().find_missing_repeating([3, 1, 3]) == (3, 2)


class TestMaxProfit:

    PRICES = [3, 3, 5, 0, 0, 3, 1, 4]

    def test_one_transaction(self):
        assert _m07().max_profit_I(self.PRICES) == 4

    def test_unlimited_transactions(self):
        # sum of every positive day-to-day gain: (5-3)+(3-0)+(4-1) = 8;
        # the source file's inline comment claiming 6 is itself wrong
        assert _m07().max_profit_II(self.PRICES) == 8

    def test_two_transactions(self):
        assert _m07().max_profit_III(self.PRICES) == 6

    def test_decreasing_prices_no_profit(self):
        assert _m07().max_profit_I([5, 4, 3, 2, 1]) == 0


class TestTrapWater:

    def test_classic(self):
        assert _m07().trap_water([0,1,0,2,1,0,1,3,2,1,2,1]) == 6

    def test_no_water(self):
        assert _m07().trap_water([1, 2, 3, 4]) == 0

    def test_empty(self):
        assert _m07().trap_water([]) == 0


class TestJumpGame:

    def test_can_jump_true(self):
        assert _m07().can_jump([2,3,1,1,4]) is True

    def test_can_jump_false(self):
        assert _m07().can_jump([3,2,1,0,4]) is False

    def test_min_jumps(self):
        assert _m07().jump_game_II([2,3,1,1,4]) == 2

    def test_min_jumps_single_element(self):
        assert _m07().jump_game_II([0]) == 0


class TestFourSum:

    def test_classic(self):
        result = _m07().four_sum([1,0,-1,0,-2,2], 0)
        expected = [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
        assert sorted(map(tuple, result)) == sorted(map(tuple, expected))

    def test_no_quadruplet(self):
        assert _m07().four_sum([1, 2, 3], 100) == []


class TestSubarrayWithSum:

    def test_classic(self):
        assert _m07().subarray_with_sum([1,4,20,3,10,5], 15) == (4, 5)

    def test_not_found(self):
        assert _m07().subarray_with_sum([1, 2, 3], 100) == (-1, -1)


class TestLongestConsecutive:

    def test_classic(self):
        assert _m07().longest_consecutive([100,4,200,1,3,2]) == 4

    def test_empty(self):
        assert _m07().longest_consecutive([]) == 0


class TestSpiralOrder:

    def test_classic(self):
        assert _m07().spiral_order([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]

    def test_empty(self):
        assert _m07().spiral_order([]) == []

    def test_single_row(self):
        assert _m07().spiral_order([[1, 2, 3]]) == [1, 2, 3]

    def test_single_column(self):
        assert _m07().spiral_order([[1], [2], [3]]) == [1, 2, 3]


class TestRotate90:

    def test_classic(self):
        assert _m07().rotate_90([[1,2,3],[4,5,6],[7,8,9]]) == [[7,4,1],[8,5,2],[9,6,3]]

    def test_single_element(self):
        assert _m07().rotate_90([[5]]) == [[5]]

    def test_four_rotations_restore_original(self):
        m = _m07()
        matrix = [[1, 2], [3, 4]]
        original = [row[:] for row in matrix]
        for _ in range(4):
            matrix = m.rotate_90(matrix)
        assert matrix == original


class TestSetZeroes:

    def test_classic(self):
        assert _m07().set_zeroes([[1,1,1],[1,0,1],[1,1,1]]) == [[1,0,1],[0,0,0],[1,0,1]]

    def test_no_zeroes(self):
        assert _m07().set_zeroes([[1, 2], [3, 4]]) == [[1, 2], [3, 4]]

    def test_zero_in_corner(self):
        assert _m07().set_zeroes([[0, 1], [1, 1]]) == [[0, 0], [0, 1]]


class TestKthLargest:

    def test_classic(self):
        assert _m07().kth_largest([3, 2, 1, 5, 6, 4], 2) == 5

    def test_k_equals_one(self):
        assert _m07().kth_largest([3, 2, 1, 5, 6, 4], 1) == 6


class TestKthSmallestQuickselect:

    def test_classic(self):
        assert _m07().kth_smallest_quickselect([3, 2, 1, 5, 6, 4], 2) == 2

    def test_k_equals_one(self):
        assert _m07().kth_smallest_quickselect([3, 2, 1, 5, 6, 4], 1) == 1

    def test_agrees_with_sorted(self):
        m = _m07()
        arr = [7, 3, 9, 1, 5, 2, 8]
        for k in range(1, len(arr) + 1):
            assert m.kth_smallest_quickselect(arr, k) == sorted(arr)[k - 1]


# ═════════════════════════════════════════════════════════════════════════════
#  08_advanced_techniques.py
# ═════════════════════════════════════════════════════════════════════════════

class TestSegmentTree:

    def test_initial_query(self):
        st = _m08().SegmentTree([1, 3, 5, 7, 9, 11])
        assert st.query(1, 4) == 24

    def test_update_then_query(self):
        st = _m08().SegmentTree([1, 3, 5, 7, 9, 11])
        st.update(1, 10)
        assert st.query(1, 4) == 31

    def test_full_range(self):
        st = _m08().SegmentTree([1, 2, 3, 4])
        assert st.query(0, 3) == 10

    def test_single_element_range(self):
        st = _m08().SegmentTree([1, 2, 3, 4])
        assert st.query(2, 2) == 3


class TestLazySegTree:

    def test_initial_query(self):
        lst = _m08().LazySegTree([1, 2, 3, 4, 5])
        assert lst.range_query(0, 4) == 15

    def test_range_update_then_query(self):
        lst = _m08().LazySegTree([1, 2, 3, 4, 5])
        lst.range_update(1, 3, 10)
        assert lst.range_query(0, 4) == 45

    def test_partial_range_after_update(self):
        lst = _m08().LazySegTree([1, 2, 3, 4, 5])
        lst.range_update(1, 3, 10)
        assert lst.range_query(1, 3) == (2+10) + (3+10) + (4+10)


class TestFenwickTree:

    def test_range_sum(self):
        bit = _m08().FenwickTree(6)
        for idx, v in enumerate([1, 3, 5, 7, 9, 11], start=1):
            bit.update(idx, v)
        assert bit.range_sum(1, 4) == 16

    def test_update_then_range_sum(self):
        bit = _m08().FenwickTree(6)
        for idx, v in enumerate([1, 3, 5, 7, 9, 11], start=1):
            bit.update(idx, v)
        bit.update(1, 5)
        assert bit.range_sum(1, 4) == 21

    def test_prefix_sum(self):
        bit = _m08().FenwickTree(4)
        for idx, v in enumerate([2, 4, 6, 8], start=1):
            bit.update(idx, v)
        assert bit.prefix_sum(4) == 20
        assert bit.prefix_sum(2) == 6


class TestSparseTable:

    def test_range_min(self):
        sp = _m08().SparseTable([2, 4, 3, 1, 6, 7, 8, 9, 1, 7])
        assert sp.query_min(0, 4) == 1
        assert sp.query_min(2, 7) == 1

    def test_single_element_range(self):
        sp = _m08().SparseTable([2, 4, 3, 1, 6])
        assert sp.query_min(2, 2) == 3

    def test_full_range(self):
        sp = _m08().SparseTable([5, 3, 8, 1, 9])
        assert sp.query_min(0, 4) == 1


class TestNextGreaterElement:

    def test_classic(self):
        assert _m08().next_greater_element([4,5,2,25]) == [5,25,25,-1]

    def test_decreasing_no_greater(self):
        assert _m08().next_greater_element([5, 4, 3]) == [-1, -1, -1]


class TestNextSmallerElement:

    def test_classic(self):
        assert _m08().next_smaller_element([4,5,2,10,8]) == [2,2,-1,8,-1]

    def test_increasing_no_smaller(self):
        assert _m08().next_smaller_element([1, 2, 3]) == [-1, -1, -1]


class TestLargestRectangle:

    def test_classic(self):
        assert _m08().largest_rectangle([2,1,5,6,2,3]) == 10

    def test_all_same_height(self):
        assert _m08().largest_rectangle([3, 3, 3]) == 9

    def test_single_bar(self):
        assert _m08().largest_rectangle([5]) == 5


class TestSlidingWindowMax:

    def test_classic(self):
        assert _m08().sliding_window_max([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]

    def test_k_equals_length(self):
        assert _m08().sliding_window_max([1, 2, 3], 3) == [3]


class TestSingleNumber:

    @pytest.mark.parametrize("nums, expected", [
        ([2, 2, 1], 1), ([4, 1, 2, 1, 2], 4), ([1], 1),
    ])
    def test_single_number(self, nums, expected):
        assert _m08().single_number(nums) == expected


class TestTwoSingleNumbers:

    def test_classic(self):
        assert _m08().two_single_numbers([1,2,3,2,1,4]) == [3, 4]


class TestCountBits:

    def test_classic(self):
        assert _m08().count_bits(5) == [0,1,1,2,1,2]

    def test_zero(self):
        assert _m08().count_bits(0) == [0]


# ═════════════════════════════════════════════════════════════════════════════
#  09_2d_matrix.py
# ═════════════════════════════════════════════════════════════════════════════

class TestTranspose:

    def test_classic(self):
        assert _m09().transpose([[1,2,3],[4,5,6],[7,8,9]]) == [[1,4,7],[2,5,8],[3,6,9]]

    def test_single_element(self):
        assert _m09().transpose([[5]]) == [[5]]


class TestRotateCW:

    def test_classic(self):
        assert _m09().rotate_cw([[1,2,3],[4,5,6],[7,8,9]]) == [[7,4,1],[8,5,2],[9,6,3]]

    def test_does_not_mutate_input(self):
        sq = [[1,2,3],[4,5,6],[7,8,9]]
        _m09().rotate_cw(sq)
        assert sq == [[1,2,3],[4,5,6],[7,8,9]]


class TestRotateCCW:

    def test_classic(self):
        assert _m09().rotate_ccw([[1,2,3],[4,5,6],[7,8,9]]) == [[3,6,9],[2,5,8],[1,4,7]]

    def test_cw_then_ccw_restores(self):
        m = _m09()
        sq = [[1,2,3],[4,5,6],[7,8,9]]
        assert m.rotate_ccw(m.rotate_cw(sq)) == sq


class TestSpiralOrder09:

    def test_classic(self):
        assert _m09().spiral_order([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]

    def test_empty(self):
        assert _m09().spiral_order([]) == []


class TestSpiralMatrixGen:

    def test_3x3(self):
        assert _m09().spiral_matrix_gen(3) == [[1,2,3],[8,9,4],[7,6,5]]

    def test_1x1(self):
        assert _m09().spiral_matrix_gen(1) == [[1]]


class TestDiagonalTraverse:

    def test_classic(self):
        assert _m09().diagonal_traverse([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,4,7,5,3,6,8,9]

    def test_empty(self):
        assert _m09().diagonal_traverse([]) == []


class TestSearchMatrix:

    SORTED_MAT = [[1,4,7,11],[2,5,8,12],[3,6,9,16],[10,13,14,17]]

    def test_found(self):
        assert _m09().search_matrix(self.SORTED_MAT, 5) == (1, 1)

    def test_not_found(self):
        assert _m09().search_matrix(self.SORTED_MAT, 20) == (-1, -1)

    def test_empty_matrix(self):
        assert _m09().search_matrix([], 5) is False


class TestSearchMatrixBS:
    """search_matrix_bs requires a FULLY sorted matrix (flattened row-major
    order is sorted), a stricter precondition than the row/col-sorted
    staircase matrix used for search_matrix above."""

    FULLY_SORTED_MAT = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]

    def test_found(self):
        assert _m09().search_matrix_bs(self.FULLY_SORTED_MAT, 9) is True

    def test_not_found(self):
        assert _m09().search_matrix_bs(self.FULLY_SORTED_MAT, 4) is False

    def test_corners(self):
        m = _m09()
        assert m.search_matrix_bs(self.FULLY_SORTED_MAT, 1) is True
        assert m.search_matrix_bs(self.FULLY_SORTED_MAT, 17) is True


class TestWordSearch:

    BOARD = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]

    def test_found_straight(self):
        board = [row[:] for row in self.BOARD]
        assert _m09().word_search(board, "SEE") is True

    def test_found_bent(self):
        board = [row[:] for row in self.BOARD]
        assert _m09().word_search(board, "ABCCED") is True

    def test_not_found(self):
        board = [row[:] for row in self.BOARD]
        assert _m09().word_search(board, "ABCB") is False

    def test_restores_board(self):
        board = [row[:] for row in self.BOARD]
        _m09().word_search(board, "ABCCED")
        assert board == self.BOARD


class TestMatMul:

    def test_classic(self):
        assert _m09().mat_mul([[1,2],[3,4]], [[5,6],[7,8]]) == [[19,22],[43,50]]

    def test_non_square(self):
        assert _m09().mat_mul([[1,2,3]], [[1],[2],[3]]) == [[14]]


class TestCountIslands:

    GRID = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"],
    ]

    def test_classic(self):
        assert _m09().count_islands([row[:] for row in self.GRID]) == 3

    def test_no_islands(self):
        assert _m09().count_islands([["0","0"],["0","0"]]) == 0

    def test_single_island(self):
        assert _m09().count_islands([["1","1"],["1","1"]]) == 1

    def test_empty_grid(self):
        assert _m09().count_islands([]) == 0


class TestFloodFill:

    def test_classic(self):
        result = _m09().flood_fill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)
        assert result == [[2,2,2],[2,2,0],[2,0,1]]

    def test_same_color_noop(self):
        image = [[1, 1], [1, 1]]
        assert _m09().flood_fill(image, 0, 0, 1) == [[1, 1], [1, 1]]

    def test_does_not_mutate_input(self):
        image = [[1, 1], [1, 1]]
        _m09().flood_fill(image, 0, 0, 9)
        assert image == [[1, 1], [1, 1]]


class TestShortestPathBinary:

    def test_classic(self):
        assert _m09().shortest_path_binary([[0,0,0],[1,1,0],[1,1,0]]) == 4

    def test_start_blocked(self):
        assert _m09().shortest_path_binary([[1, 0], [0, 0]]) == -1

    def test_end_blocked(self):
        assert _m09().shortest_path_binary([[0, 0], [0, 1]]) == -1

    def test_no_path(self):
        assert _m09().shortest_path_binary([[0,1,0],[1,1,0],[0,1,0]]) == -1

    def test_single_cell(self):
        assert _m09().shortest_path_binary([[0]]) == 1


# ═════════════════════════════════════════════════════════════════════════════
#  10_special_arrays.py
# ═════════════════════════════════════════════════════════════════════════════

class TestSparseArray:

    def test_get_default(self):
        sa = _m10().SparseArray(10)
        assert sa[5] == 0

    def test_set_and_get(self):
        sa = _m10().SparseArray(10)
        sa[0] = 5
        sa[7] = 3
        sa[9] = 8
        assert sa[0] == 5 and sa[7] == 3 and sa[9] == 8

    def test_custom_default(self):
        sa = _m10().SparseArray(5, default=-1)
        assert sa[2] == -1

    def test_setting_to_default_removes_entry(self):
        sa = _m10().SparseArray(10)
        sa[3] = 7
        sa[3] = 0
        assert 3 not in sa.data


class TestCircularBuffer:

    def test_fifo_order(self):
        cb = _m10().CircularBuffer(3)
        cb.enqueue(1); cb.enqueue(2); cb.enqueue(3)
        assert cb.dequeue() == 1
        assert cb.dequeue() == 2

    def test_wraps_around(self):
        cb = _m10().CircularBuffer(3)
        cb.enqueue(1); cb.enqueue(2); cb.enqueue(3)
        cb.dequeue(); cb.dequeue()
        cb.enqueue(4)
        assert cb.peek() == 3

    def test_overflow_raises(self):
        cb = _m10().CircularBuffer(2)
        cb.enqueue(1); cb.enqueue(2)
        with pytest.raises(OverflowError):
            cb.enqueue(3)

    def test_underflow_raises(self):
        cb = _m10().CircularBuffer(2)
        with pytest.raises(IndexError):
            cb.dequeue()


class TestPrintAllSubarrays:

    def test_classic(self):
        result = _m10().print_all_subarrays([1, 2, 3])
        assert sorted(map(tuple, result)) == sorted(map(tuple, [[1],[2],[3],[1,2],[2,3],[1,2,3]]))

    def test_count_matches_formula(self):
        n = 5
        result = _m10().print_all_subarrays(list(range(n)))
        assert len(result) == n * (n + 1) // 2


class TestMinSubarraySum:

    def test_classic(self):
        assert _m10().min_subarray_sum([3,-4,2,-3,-1,7,-5]) == -6

    def test_all_positive(self):
        assert _m10().min_subarray_sum([1, 2, 3]) == 1

    def test_single_element(self):
        assert _m10().min_subarray_sum([5]) == 5


class TestMaxNonAdjacentSum:

    def test_classic(self):
        assert _m10().max_non_adjacent_sum([5,5,10,100,10,5]) == 110

    def test_empty(self):
        assert _m10().max_non_adjacent_sum([]) == 0

    def test_single_element(self):
        assert _m10().max_non_adjacent_sum([5]) == 5

    def test_all_negative(self):
        assert _m10().max_non_adjacent_sum([-1, -2, -3]) == 0


class TestRearrangeBySign:

    def test_classic(self):
        assert _m10().rearrange_by_sign([3,1,-2,-5,2,-4]) == [3, -2, 1, -5, 2, -4]


class TestFindPairsWithSum:

    def test_classic(self):
        result = _m10().find_pairs_with_sum([1,5,3,2,4,6,0], 6)
        assert sorted(map(tuple, result)) == sorted([(1,5),(2,4),(6,0)])

    def test_no_pairs(self):
        assert _m10().find_pairs_with_sum([1, 2, 3], 100) == []


class TestFindPairDifference:

    def test_classic(self):
        result = _m10().find_pair_difference([1,5,3,4,2], 3)
        assert sorted(result) == sorted([(1,4),(2,5)])

    def test_no_pairs(self):
        assert _m10().find_pair_difference([1, 2, 3], 100) == []


class TestMinSwapsToSort:

    def test_classic(self):
        assert _m10().min_swaps_to_sort([4,3,2,1]) == 2

    def test_already_sorted(self):
        assert _m10().min_swaps_to_sort([1, 2, 3]) == 0

    def test_single_element(self):
        assert _m10().min_swaps_to_sort([1]) == 0


class TestMinPlatforms:

    def test_classic(self):
        arrival = [900,940,950,1100,1500,1800]
        departure = [910,1200,1120,1130,1900,2000]
        assert _m10().min_platforms(arrival, departure) == 3

    def test_no_overlap(self):
        assert _m10().min_platforms([900, 1000], [950, 1050]) == 1

    def test_all_overlap(self):
        assert _m10().min_platforms([900, 900, 900], [1000, 1000, 1000]) == 3


class TestActivitySelection:

    def test_classic(self):
        s = [1, 3, 0, 5, 8, 5]
        f = [2, 4, 6, 7, 9, 9]
        assert _m10().activity_selection(s, f) == [(1,2),(3,4),(5,7),(8,9)]

    def test_no_overlap(self):
        assert _m10().activity_selection([1, 5], [2, 6]) == [(1,2),(5,6)]


class TestStockSpan:

    def test_classic(self):
        assert _m10().stock_span([100,80,60,70,60,75,85]) == [1,1,1,2,1,4,6]

    def test_increasing_prices(self):
        assert _m10().stock_span([1, 2, 3, 4]) == [1, 2, 3, 4]

    def test_decreasing_prices(self):
        assert _m10().stock_span([4, 3, 2, 1]) == [1, 1, 1, 1]


class TestMaxSubarrayKSparse:

    def test_classic(self):
        assert _m10().max_subarray_k_sparse([1,2,3,1,4,5,2,3,6], 3) == [3,3,4,5,5,5,6]

    def test_k_equals_length(self):
        assert _m10().max_subarray_k_sparse([1, 5, 3], 3) == [5]


# ═════════════════════════════════════════════════════════════════════════════
#  11_remaining_topics.py
# ═════════════════════════════════════════════════════════════════════════════

class TestLisDp:

    def test_classic(self):
        length, seq = _m11().lis_dp([10,9,2,5,3,7,101,18])
        assert length == 4
        assert seq == [2, 5, 7, 101]

    def test_sequence_is_strictly_increasing(self):
        _, seq = _m11().lis_dp([3, 1, 4, 1, 5, 9, 2, 6])
        assert all(seq[i] < seq[i+1] for i in range(len(seq)-1))

    def test_single_element(self):
        assert _m11().lis_dp([5]) == (1, [5])


class TestLisFast:

    def test_classic(self):
        assert _m11().lis_fast([10,9,2,5,3,7,101,18]) == 4

    def test_agrees_with_dp(self):
        m = _m11()
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        assert m.lis_fast(arr) == m.lis_dp(arr)[0]

    def test_strictly_decreasing(self):
        assert _m11().lis_fast([5, 4, 3, 2, 1]) == 1


class TestLds:

    def test_classic(self):
        assert _m11().lds([10,9,2,5,3,7,101,18]) == 4


class TestLongestBitonicSubsequence:

    def test_classic(self):
        assert _m11().longest_bitonic_subsequence([1,11,2,10,4,5,2,1]) == 6

    def test_strictly_increasing(self):
        assert _m11().longest_bitonic_subsequence([1, 2, 3, 4]) == 4


class TestCountInversions:

    @pytest.mark.parametrize("arr, expected", [
        ([8, 4, 2, 1], 6),
        ([1, 20, 6, 4, 5], 5),
        ([1, 2, 3], 0),
        ([], 0),
    ])
    def test_count(self, arr, expected):
        _, inv = _m11().count_inversions(arr)
        assert inv == expected

    def test_returns_sorted_array(self):
        merged, _ = _m11().count_inversions([8, 4, 2, 1])
        assert merged == [1, 2, 4, 8]


class TestFindMedianSorted:

    def test_odd_total(self):
        assert _m11().find_median_sorted([1, 3], [2]) == 2

    def test_even_total(self):
        assert _m11().find_median_sorted([1, 2], [3, 4]) == 2.5

    def test_all_zeros(self):
        assert _m11().find_median_sorted([0, 0], [0, 0]) == 0.0

    def test_one_empty(self):
        assert _m11().find_median_sorted([], [1]) == 1

    def test_order_independent(self):
        m = _m11()
        assert m.find_median_sorted([1, 2], [3, 4]) == m.find_median_sorted([3, 4], [1, 2])


class TestMergeKSorted:

    def test_classic(self):
        assert _m11().merge_k_sorted([[1,4,7],[2,5,8],[3,6,9]]) == [1,2,3,4,5,6,7,8,9]

    def test_with_empty_array(self):
        assert _m11().merge_k_sorted([[1, 3], [], [2]]) == [1, 2, 3]

    def test_single_array(self):
        assert _m11().merge_k_sorted([[1, 2, 3]]) == [1, 2, 3]

    def test_no_arrays(self):
        assert _m11().merge_k_sorted([]) == []


class TestMaxSumRectangle:

    def test_classic(self):
        # brute-force verified: true max is 25 at (top=1,left=1,bottom=2,right=2);
        # the source file's inline comment claiming 29 is itself wrong
        mat = [
            [ 1, -2, -1,  4],
            [-8,  3,  4,  2],
            [ 3,  8, 10, -8],
            [-4,  4, -6,  5],
        ]
        max_sum, rect = _m11().max_sum_rectangle(mat)
        assert max_sum == 25
        assert rect == (1, 1, 2, 2)

    def test_single_cell(self):
        max_sum, _ = _m11().max_sum_rectangle([[5]])
        assert max_sum == 5

    def test_all_negative(self):
        max_sum, _ = _m11().max_sum_rectangle([[-1, -2], [-3, -4]])
        assert max_sum == -1


class TestWaveArray:

    def test_v1_produces_valid_wave(self):
        m = _m11()
        result = m.wave_array([3,6,5,10,7,20])
        assert m.is_wave(result)
        assert sorted(result) == sorted([3,6,5,10,7,20])

    def test_v2_produces_valid_wave(self):
        m = _m11()
        result = m.wave_array_v2([3,6,5,10,7,20])
        assert m.is_wave(result)
        assert sorted(result) == sorted([3,6,5,10,7,20])

    def test_v2_classic_value(self):
        assert _m11().wave_array_v2([3,6,5,10,7,20]) == [5, 3, 7, 6, 20, 10]


class TestIsWave:

    def test_valid_wave(self):
        assert _m11().is_wave([5, 3, 7, 6, 20, 10]) is True

    def test_sorted_ascending_not_wave(self):
        assert _m11().is_wave([1, 2, 3, 4]) is False

    def test_single_element(self):
        assert _m11().is_wave([5]) is True


class TestCycleSort:

    def test_classic(self):
        sorted_arr, writes = _m11().cycle_sort([3, 1, 5, 4, 2])
        assert sorted_arr == [1, 2, 3, 4, 5]
        assert writes == 4

    def test_already_sorted_zero_writes(self):
        sorted_arr, writes = _m11().cycle_sort([1, 2, 3])
        assert sorted_arr == [1, 2, 3]
        assert writes == 0

    def test_with_duplicates(self):
        sorted_arr, _ = _m11().cycle_sort([2, 2, 1, 1])
        assert sorted_arr == [1, 1, 2, 2]


class TestPancakeSort:

    def test_classic(self):
        result, _ = _m11().pancake_sort([3, 6, 2, 7, 4, 5, 1])
        assert result == [1, 2, 3, 4, 5, 6, 7]

    def test_already_sorted(self):
        result, flips = _m11().pancake_sort([1, 2, 3])
        assert result == [1, 2, 3]

    def test_single_element(self):
        result, _ = _m11().pancake_sort([5])
        assert result == [5]


class TestMajorityElementsN3:

    def test_single_majority(self):
        assert _m11().majority_elements_n3([3, 2, 3]) == [3]

    def test_two_majorities(self):
        assert sorted(_m11().majority_elements_n3([1,1,1,3,3,2,2,2])) == [1, 2]

    def test_no_majority(self):
        assert _m11().majority_elements_n3([1, 2, 3]) == []


class TestRearrangeMaxMin:

    def test_classic(self):
        assert _m11().rearrange_max_min([1,2,3,4,5,6,7]) == [7,1,6,2,5,3,4]

    def test_single_element(self):
        assert _m11().rearrange_max_min([5]) == [5]

    def test_two_elements(self):
        assert _m11().rearrange_max_min([1, 2]) == [2, 1]


class TestAddOne:

    @pytest.mark.parametrize("digits, expected", [
        ([1, 2, 3], [1, 2, 4]),
        ([9, 9, 9], [1, 0, 0, 0]),
        ([9], [1, 0]),
        ([0], [1]),
        ([1, 9], [2, 0]),
    ])
    def test_add_one(self, digits, expected):
        assert _m11().add_one(digits) == expected


class TestMultiplyArrays:

    def test_classic(self):
        assert _m11().multiply_arrays([1, 2, 3], [4, 5, 6]) == [5, 6, 0, 8, 8]

    def test_multiply_by_zero(self):
        assert _m11().multiply_arrays([0], [5]) == [0]

    def test_single_digits(self):
        assert _m11().multiply_arrays([9], [9]) == [8, 1]


class TestLongestBitonicSubarray:

    def test_classic_1(self):
        assert _m11().longest_bitonic_subarray([12,4,78,90,45,23]) == 5

    def test_classic_2(self):
        assert _m11().longest_bitonic_subarray([20,4,1,2,3,4,2,10]) == 5

    def test_empty(self):
        assert _m11().longest_bitonic_subarray([]) == 0

    def test_single_element(self):
        assert _m11().longest_bitonic_subarray([5]) == 1

    def test_strictly_increasing(self):
        assert _m11().longest_bitonic_subarray([1, 2, 3, 4]) == 4
