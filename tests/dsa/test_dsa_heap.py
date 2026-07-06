"""
tests/dsa/test_dsa_heap.py
===========================
Tests for all classes under dsa/heaps/:
    MaxHeap · MinHeap · KthLargestElement

Operations:  insert · extract_max/extract_min · get_max/get_min
Heap property (max): heap[parent] >= heap[child] for every node.
Heap property (min): heap[parent] <= heap[child] for every node.
"""

import pytest
from tests.utils import load_module


def _MaxHeap():
    return load_module('dsa/heaps/maxheap.py', ['3 1 4 1 5'], alias='dsa_maxheap').MaxHeap

def _MinHeap():
    return load_module('dsa/heaps/minheap.py', ['3 1 4 1 5'], alias='dsa_minheap').MinHeap

def _KthLargestElement():
    return load_module('dsa/heaps/kth_largest_element.py', ['3 2 1 5 6 4', '2'], alias='dsa_kthlargest').KthLargestElement


def _valid_heap(arr):
    return all(arr[(i-1)//2] >= arr[i] for i in range(1, len(arr)))


def _valid_min_heap(arr):
    return all(arr[(i-1)//2] <= arr[i] for i in range(1, len(arr)))


# ═════════════════════════════════════════════════════════════════════════════

class TestMaxHeapInsert:

    def test_single_element(self):
        mh = _MaxHeap()(); mh.insert(42)
        assert mh.get_max() == 42

    def test_ascending_inserts(self):
        mh = _MaxHeap()()
        for v in [1,2,3,4,5]: mh.insert(v)
        assert mh.get_max() == 5

    def test_descending_inserts(self):
        mh = _MaxHeap()()
        for v in [5,4,3,2,1]: mh.insert(v)
        assert mh.get_max() == 5

    def test_random_order(self):
        mh = _MaxHeap()()
        for v in [3,1,4,1,5,9,2,6]: mh.insert(v)
        assert mh.get_max() == 9

    def test_heap_property_maintained(self):
        mh = _MaxHeap()()
        for v in [10,4,7,1,13,5,8]: mh.insert(v)
        assert _valid_heap(mh.heap)

    def test_duplicates(self):
        mh = _MaxHeap()()
        for v in [5,5,5,5]: mh.insert(v)
        assert mh.get_max() == 5 and len(mh.heap) == 4

    def test_negative_values(self):
        mh = _MaxHeap()()
        for v in [-3,-1,-7,-2]: mh.insert(v)
        assert mh.get_max() == -1

    def test_mixed_signs(self):
        mh = _MaxHeap()()
        for v in [-5,3,-1,7,0]: mh.insert(v)
        assert mh.get_max() == 7


class TestMaxHeapGetMax:

    def test_does_not_remove(self):
        mh = _MaxHeap()(); mh.insert(10); mh.insert(20)
        _ = mh.get_max()
        assert len(mh.heap) == 2

    def test_empty_returns_none(self):
        assert _MaxHeap()().get_max() is None

    def test_equals_heap_zero(self):
        mh = _MaxHeap()()
        for v in [3,7,1,9,4]: mh.insert(v)
        assert mh.get_max() == mh.heap[0]


class TestMaxHeapExtractMax:

    def test_returns_largest(self):
        mh = _MaxHeap()()
        for v in [3,1,4,1,5,9,2,6]: mh.insert(v)
        assert mh.extract_max() == 9

    def test_removes_element(self):
        mh = _MaxHeap()()
        for v in [5,3,8]: mh.insert(v)
        n = len(mh.heap); mh.extract_max()
        assert len(mh.heap) == n - 1

    def test_empty_returns_none(self):
        assert _MaxHeap()().extract_max() is None

    def test_single_element(self):
        mh = _MaxHeap()(); mh.insert(42)
        assert mh.extract_max() == 42 and len(mh.heap) == 0

    def test_heap_property_after_extract(self):
        mh = _MaxHeap()()
        for v in [10,4,7,1,13,5,8]: mh.insert(v)
        mh.extract_max()
        assert _valid_heap(mh.heap)

    def test_sorted_descending_on_repeated_extract(self):
        """All extractions yield elements in descending order."""
        mh = _MaxHeap()()
        data = [5,3,8,1,9,2,7]
        for v in data: mh.insert(v)
        result = []
        while mh.heap: result.append(mh.extract_max())
        assert result == sorted(data, reverse=True)

    def test_two_consecutive_extracts(self):
        mh = _MaxHeap()()
        for v in [4,7,2,9,1]: mh.insert(v)
        assert mh.extract_max() == 9
        assert mh.extract_max() == 7
        assert _valid_heap(mh.heap)


class TestHeapProperty:

    @pytest.mark.parametrize("values", [
        [1], [5,3], [1,2,3,4,5], [10,9,8,7,6,5],
        [3,1,4,1,5,9,2,6,5,3], [-1,-5,-3,-2], [0,0,0,0],
    ])
    def test_property_holds_after_all_inserts(self, values):
        mh = _MaxHeap()()
        for v in values: mh.insert(v)
        assert _valid_heap(mh.heap)

    def test_large_stress(self):
        import random; random.seed(42)
        data = [random.randint(-500, 500) for _ in range(200)]
        mh = _MaxHeap()()
        for v in data: mh.insert(v)
        assert mh.get_max() == max(data)
        assert _valid_heap(mh.heap)


class TestMinHeapInsert:

    def test_single_element(self):
        mh = _MinHeap()(); mh.insert(42)
        assert mh.get_min() == 42

    def test_ascending_inserts(self):
        mh = _MinHeap()()
        for v in [1,2,3,4,5]: mh.insert(v)
        assert mh.get_min() == 1

    def test_descending_inserts(self):
        mh = _MinHeap()()
        for v in [5,4,3,2,1]: mh.insert(v)
        assert mh.get_min() == 1

    def test_random_order(self):
        mh = _MinHeap()()
        for v in [3,1,4,1,5,9,2,6]: mh.insert(v)
        assert mh.get_min() == 1

    def test_heap_property_maintained(self):
        mh = _MinHeap()()
        for v in [10,4,7,1,13,5,8]: mh.insert(v)
        assert _valid_min_heap(mh.heap)

    def test_negative_values(self):
        mh = _MinHeap()()
        for v in [-3,-1,-7,-2]: mh.insert(v)
        assert mh.get_min() == -7


class TestMinHeapExtractMin:

    def test_returns_smallest(self):
        mh = _MinHeap()()
        for v in [3,1,4,1,5,9,2,6]: mh.insert(v)
        assert mh.extract_min() == 1

    def test_removes_element(self):
        mh = _MinHeap()()
        for v in [5,3,8]: mh.insert(v)
        n = len(mh.heap); mh.extract_min()
        assert len(mh.heap) == n - 1

    def test_empty_returns_none(self):
        assert _MinHeap()().extract_min() is None

    def test_single_element(self):
        mh = _MinHeap()(); mh.insert(42)
        assert mh.extract_min() == 42 and len(mh.heap) == 0

    def test_heap_property_after_extract(self):
        mh = _MinHeap()()
        for v in [10,4,7,1,13,5,8]: mh.insert(v)
        mh.extract_min()
        assert _valid_min_heap(mh.heap)

    def test_sorted_ascending_on_repeated_extract(self):
        mh = _MinHeap()()
        data = [5,3,8,1,9,2,7]
        for v in data: mh.insert(v)
        result = []
        while mh.heap: result.append(mh.extract_min())
        assert result == sorted(data)


class TestMinHeapProperty:

    @pytest.mark.parametrize("values", [
        [1], [5,3], [1,2,3,4,5], [10,9,8,7,6,5],
        [3,1,4,1,5,9,2,6,5,3], [-1,-5,-3,-2], [0,0,0,0],
    ])
    def test_property_holds_after_all_inserts(self, values):
        mh = _MinHeap()()
        for v in values: mh.insert(v)
        assert _valid_min_heap(mh.heap)

    def test_large_stress(self):
        import random; random.seed(43)
        data = [random.randint(-500, 500) for _ in range(200)]
        mh = _MinHeap()()
        for v in data: mh.insert(v)
        assert mh.get_min() == min(data)
        assert _valid_min_heap(mh.heap)


class TestKthLargestElement:

    @pytest.mark.parametrize("nums, k, expected", [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([1], 1, 1),
        ([7, 6, 5, 4, 3, 2, 1], 1, 7),
        ([7, 6, 5, 4, 3, 2, 1], 7, 1),
    ])
    def test_find(self, nums, k, expected):
        assert _KthLargestElement()(nums, k).find() == expected

    def test_k_larger_than_array_returns_none(self):
        assert _KthLargestElement()([1, 2, 3], 5).find() is None

    def test_k_zero_returns_none(self):
        assert _KthLargestElement()([1, 2, 3], 0).find() is None
