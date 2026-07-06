"""
tests/dsa/test_dsa_sorting.py
==============================
Tests for all sorting algorithms under dsa/sorting/:
    BubbleSort · InsertionSort · SelectionSort · MergeSort · QuickSort ·
    HeapSort · CountingSort · RadixSort · ShellSort
"""

import pytest
from tests.utils import load_module

# ── Module loaders ─────────────────────────────────────────────────────────────

def _BubbleSort():
    return load_module('dsa/sorting/bubblesort.py',    ['1 2 3'], alias='dsa_bubble').BubbleSort

def _InsertionSort():
    return load_module('dsa/sorting/insertionsort.py', ['1 2 3'], alias='dsa_insertion').InsertionSort

def _SelectionSort():
    return load_module('dsa/sorting/selectionsort.py', ['1 2 3'], alias='dsa_selection').SelectionSort

def _MergeSort():
    return load_module('dsa/sorting/mergesort.py',     ['1 2 3'], alias='dsa_merge').MergeSort

def _QuickSort():
    return load_module('dsa/sorting/quicksort.py',     ['1 2 3'], alias='dsa_quick').QuickSort

def _HeapSort():
    return load_module('dsa/sorting/heapsort.py',      ['1 2 3'], alias='dsa_heapsort').HeapSort

def _CountingSort():
    return load_module('dsa/sorting/countingsort.py',  ['1 2 3'], alias='dsa_countingsort').CountingSort

def _RadixSort():
    return load_module('dsa/sorting/radixsort.py',     ['1 2 3'], alias='dsa_radixsort').RadixSort

def _ShellSort():
    return load_module('dsa/sorting/shellsort.py',     ['1 2 3'], alias='dsa_shellsort').ShellSort


# ── Shared test cases ──────────────────────────────────────────────────────────

SORT_CASES = [
    ([5, 2, 8, 1, 9],            [1, 2, 5, 8, 9]),
    ([1, 2, 3, 4, 5],            [1, 2, 3, 4, 5]),          # already sorted
    ([5, 4, 3, 2, 1],            [1, 2, 3, 4, 5]),          # reverse sorted
    ([42],                        [42]),                      # single element
    ([],                          []),                        # empty
    ([3, 1, 4, 1, 5, 9, 2, 6],   [1, 1, 2, 3, 4, 5, 6, 9]), # duplicates
    ([1, 1, 1, 1],                [1, 1, 1, 1]),             # all same
    ([-3, 0, 1, -1, 2],          [-3, -1, 0, 1, 2]),        # negatives
    ([-5, -1, -3, -2, -4],       [-5, -4, -3, -2, -1]),     # all negative
    ([2, 1],                      [1, 2]),                   # two elements
]

# RadixSort only supports non-negative integers (documented limitation)
NONNEGATIVE_SORT_CASES = [
    ([5, 2, 8, 1, 9],            [1, 2, 5, 8, 9]),
    ([1, 2, 3, 4, 5],            [1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1],            [1, 2, 3, 4, 5]),
    ([42],                        [42]),
    ([],                          []),
    ([3, 1, 4, 1, 5, 9, 2, 6],   [1, 1, 2, 3, 4, 5, 6, 9]),
    ([1, 1, 1, 1],                [1, 1, 1, 1]),
    ([170, 45, 75, 90, 802, 24, 2, 66], [2, 24, 45, 66, 75, 90, 170, 802]),
    ([0, 0, 0],                   [0, 0, 0]),
    ([2, 1],                      [1, 2]),
]


# ═════════════════════════════════════════════════════════════════════════════

class TestBubbleSort:

    @pytest.mark.parametrize("arr, expected", SORT_CASES)
    def test_sort(self, arr, expected):
        assert _BubbleSort()(arr.copy()).sort() == expected

    def test_early_exit_on_sorted(self):
        assert _BubbleSort()([1, 2, 3]).sort() == [1, 2, 3]

    def test_returns_same_list_object(self):
        arr = [3, 1, 2]
        bs  = _BubbleSort()(arr)
        assert bs.sort() is arr


class TestInsertionSort:

    @pytest.mark.parametrize("arr, expected", SORT_CASES)
    def test_sort(self, arr, expected):
        assert _InsertionSort()(arr.copy()).sort() == expected

    def test_output_is_non_decreasing(self):
        out = _InsertionSort()([9, 3, 7, 1, 5]).sort()
        assert all(out[i] <= out[i + 1] for i in range(len(out) - 1))


class TestSelectionSort:

    @pytest.mark.parametrize("arr, expected", SORT_CASES)
    def test_sort(self, arr, expected):
        assert _SelectionSort()(arr.copy()).sort() == expected

    def test_elements_preserved(self):
        arr = [4, 2, 7, 1, 9, 3]
        assert _SelectionSort()(arr.copy()).sort() == sorted(arr)


class TestMergeSort:

    @pytest.mark.parametrize("arr, expected", SORT_CASES)
    def test_sort(self, arr, expected):
        assert _MergeSort()(arr.copy()).sort() == expected

    def test_internal_merge(self):
        ms = _MergeSort()([])
        assert ms._merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]

    def test_merge_with_empty(self):
        ms = _MergeSort()([])
        assert ms._merge([], [1, 2]) == [1, 2]
        assert ms._merge([1, 2], []) == [1, 2]


class TestQuickSort:

    @pytest.mark.parametrize("arr, expected", SORT_CASES)
    def test_sort(self, arr, expected):
        assert _QuickSort()(arr.copy()).sort() == expected

    def test_partition_places_pivot_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        qs  = _QuickSort()(arr.copy())
        pi  = qs._partition(qs.arr, 0, len(qs.arr) - 1)
        assert all(qs.arr[j] <= qs.arr[pi] for j in range(pi))
        assert all(qs.arr[j] >= qs.arr[pi] for j in range(pi + 1, len(qs.arr)))

    def test_large_input(self):
        import random
        random.seed(0)
        arr = [random.randint(-1000, 1000) for _ in range(500)]
        assert _QuickSort()(arr.copy()).sort() == sorted(arr)


class TestHeapSort:

    @pytest.mark.parametrize("arr, expected", SORT_CASES)
    def test_sort(self, arr, expected):
        assert _HeapSort()(arr.copy()).sort() == expected

    def test_large_input(self):
        import random
        random.seed(1)
        arr = [random.randint(-1000, 1000) for _ in range(500)]
        assert _HeapSort()(arr.copy()).sort() == sorted(arr)


class TestCountingSort:

    @pytest.mark.parametrize("arr, expected", SORT_CASES)
    def test_sort(self, arr, expected):
        assert _CountingSort()(arr.copy()).sort() == expected

    def test_is_stable_preserves_element_counts(self):
        arr = [4, 2, 2, 8, 4, 1]
        result = _CountingSort()(arr.copy()).sort()
        assert sorted(result) == sorted(arr)
        assert result == sorted(arr)


class TestRadixSort:

    @pytest.mark.parametrize("arr, expected", NONNEGATIVE_SORT_CASES)
    def test_sort(self, arr, expected):
        assert _RadixSort()(arr.copy()).sort() == expected

    def test_large_input(self):
        import random
        random.seed(2)
        arr = [random.randint(0, 100000) for _ in range(500)]
        assert _RadixSort()(arr.copy()).sort() == sorted(arr)


class TestShellSort:

    @pytest.mark.parametrize("arr, expected", SORT_CASES)
    def test_sort(self, arr, expected):
        assert _ShellSort()(arr.copy()).sort() == expected

    def test_large_input(self):
        import random
        random.seed(3)
        arr = [random.randint(-1000, 1000) for _ in range(500)]
        assert _ShellSort()(arr.copy()).sort() == sorted(arr)
