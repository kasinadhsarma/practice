"""
tests/dsa/test_dsa_linked_list.py
====================================
Tests for all classes under dsa/linked_list/:
    SinglyLinkedList · DoublyLinkedList · ReverseLinkedList ·
    DetectCycle · MergeTwoSortedLists
"""

import pytest
from tests.utils import load_module


def _singly_mod():
    return load_module('dsa/linked_list/singly_linked_list.py', ['1 2 3'], alias='dsa_singly')

def _doubly_mod():
    return load_module('dsa/linked_list/doubly_linked_list.py', ['1 2 3'], alias='dsa_doubly')

def _reverse_mod():
    return load_module('dsa/linked_list/reverse_linked_list.py', ['1 2 3'], alias='dsa_reverse')

def _cycle_mod():
    return load_module('dsa/linked_list/detect_cycle.py', ['1 2 3', ''], alias='dsa_cycle')

def _merge_mod():
    return load_module('dsa/linked_list/merge_two_sorted_lists.py', ['1 3 5', '2 4 6'], alias='dsa_merge')


# ═════════════════════════════════════════════════════════════════════════════

class TestSinglyLinkedList:

    def test_insert_at_tail(self):
        sll = _singly_mod().SinglyLinkedList()
        for v in [1, 2, 3]: sll.insert_at_tail(v)
        assert sll.to_list() == [1, 2, 3]

    def test_insert_at_head(self):
        sll = _singly_mod().SinglyLinkedList()
        sll.insert_at_head(2)
        sll.insert_at_head(1)
        assert sll.to_list() == [1, 2]

    def test_delete_value(self):
        sll = _singly_mod().SinglyLinkedList()
        for v in [1, 2, 3]: sll.insert_at_tail(v)
        assert sll.delete_value(2) is True
        assert sll.to_list() == [1, 3]

    def test_delete_head(self):
        sll = _singly_mod().SinglyLinkedList()
        for v in [1, 2, 3]: sll.insert_at_tail(v)
        assert sll.delete_value(1) is True
        assert sll.to_list() == [2, 3]

    def test_delete_missing_returns_false(self):
        sll = _singly_mod().SinglyLinkedList()
        sll.insert_at_tail(1)
        assert sll.delete_value(99) is False

    def test_search(self):
        sll = _singly_mod().SinglyLinkedList()
        for v in [1, 2, 3]: sll.insert_at_tail(v)
        assert sll.search(2) is True
        assert sll.search(99) is False

    def test_length(self):
        sll = _singly_mod().SinglyLinkedList()
        for v in [1, 2, 3, 4]: sll.insert_at_tail(v)
        assert sll.length() == 4

    def test_empty_list(self):
        sll = _singly_mod().SinglyLinkedList()
        assert sll.to_list() == []
        assert sll.length() == 0
        assert sll.delete_value(1) is False


class TestDoublyLinkedList:

    def test_insert_at_tail_forward(self):
        dll = _doubly_mod().DoublyLinkedList()
        for v in [1, 2, 3]: dll.insert_at_tail(v)
        assert dll.traverse_forward() == [1, 2, 3]

    def test_traverse_backward(self):
        dll = _doubly_mod().DoublyLinkedList()
        for v in [1, 2, 3]: dll.insert_at_tail(v)
        assert dll.traverse_backward() == [3, 2, 1]

    def test_insert_at_head(self):
        dll = _doubly_mod().DoublyLinkedList()
        dll.insert_at_head(2)
        dll.insert_at_head(1)
        assert dll.traverse_forward() == [1, 2]
        assert dll.traverse_backward() == [2, 1]

    def test_delete_middle(self):
        dll = _doubly_mod().DoublyLinkedList()
        for v in [1, 2, 3]: dll.insert_at_tail(v)
        assert dll.delete_value(2) is True
        assert dll.traverse_forward() == [1, 3]
        assert dll.traverse_backward() == [3, 1]

    def test_delete_head_updates_head(self):
        dll = _doubly_mod().DoublyLinkedList()
        for v in [1, 2, 3]: dll.insert_at_tail(v)
        dll.delete_value(1)
        assert dll.traverse_forward() == [2, 3]

    def test_delete_tail_updates_tail(self):
        dll = _doubly_mod().DoublyLinkedList()
        for v in [1, 2, 3]: dll.insert_at_tail(v)
        dll.delete_value(3)
        assert dll.traverse_backward() == [2, 1]

    def test_delete_missing_returns_false(self):
        dll = _doubly_mod().DoublyLinkedList()
        dll.insert_at_tail(1)
        assert dll.delete_value(99) is False


class TestReverseLinkedList:

    def _build(self, mod, values):
        return mod.build_list(values)

    @pytest.mark.parametrize("values", [
        [1, 2, 3], [1], [], [5, 4, 3, 2, 1], [7, 7, 7],
    ])
    def test_reverse_iterative(self, values):
        mod = _reverse_mod()
        head = self._build(mod, values)
        reversed_head = mod.ReverseLinkedList.reverse_iterative(head)
        assert mod.to_list(reversed_head) == list(reversed(values))

    @pytest.mark.parametrize("values", [
        [1, 2, 3], [1], [], [5, 4, 3, 2, 1], [7, 7, 7],
    ])
    def test_reverse_recursive(self, values):
        mod = _reverse_mod()
        head = self._build(mod, values)
        reversed_head = mod.ReverseLinkedList.reverse_recursive(head)
        assert mod.to_list(reversed_head) == list(reversed(values))

    def test_both_approaches_agree(self):
        mod = _reverse_mod()
        values = [3, 1, 4, 1, 5, 9]
        r1 = mod.to_list(mod.ReverseLinkedList.reverse_iterative(self._build(mod, values)))
        r2 = mod.to_list(mod.ReverseLinkedList.reverse_recursive(self._build(mod, values)))
        assert r1 == r2 == list(reversed(values))


class TestDetectCycle:

    def test_no_cycle(self):
        mod = _cycle_mod()
        head = mod.build_list_with_cycle([1, 2, 3, 4])
        assert mod.DetectCycle.has_cycle(head) is False

    def test_cycle_at_head(self):
        mod = _cycle_mod()
        head = mod.build_list_with_cycle([1, 2, 3, 4], cycle_index=0)
        assert mod.DetectCycle.has_cycle(head) is True

    def test_cycle_in_middle(self):
        mod = _cycle_mod()
        head = mod.build_list_with_cycle([1, 2, 3, 4, 5], cycle_index=2)
        assert mod.DetectCycle.has_cycle(head) is True

    def test_find_cycle_start(self):
        mod = _cycle_mod()
        values = [1, 2, 3, 4, 5]
        head = mod.build_list_with_cycle(values, cycle_index=2)
        start = mod.DetectCycle.find_cycle_start(head)
        assert start.val == values[2]

    def test_find_cycle_start_no_cycle_returns_none(self):
        mod = _cycle_mod()
        head = mod.build_list_with_cycle([1, 2, 3])
        assert mod.DetectCycle.find_cycle_start(head) is None

    def test_empty_list_no_cycle(self):
        mod = _cycle_mod()
        head = mod.build_list_with_cycle([])
        assert mod.DetectCycle.has_cycle(head) is False

    def test_single_node_no_cycle(self):
        mod = _cycle_mod()
        head = mod.build_list_with_cycle([1])
        assert mod.DetectCycle.has_cycle(head) is False

    def test_single_node_self_cycle(self):
        mod = _cycle_mod()
        head = mod.build_list_with_cycle([1], cycle_index=0)
        assert mod.DetectCycle.has_cycle(head) is True

    def test_out_of_range_cycle_index_does_not_crash(self):
        mod = _cycle_mod()
        head = mod.build_list_with_cycle([1, 2, 3], cycle_index=99)
        assert mod.DetectCycle.has_cycle(head) is False

    def test_negative_cycle_index_does_not_crash(self):
        mod = _cycle_mod()
        head = mod.build_list_with_cycle([1, 2, 3], cycle_index=-1)
        assert mod.DetectCycle.has_cycle(head) is False


class TestMergeTwoSortedLists:

    def _build(self, mod, values):
        return mod.build_list(values)

    @pytest.mark.parametrize("a, b, expected", [
        ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
        ([], [1, 2, 3], [1, 2, 3]),
        ([1, 2, 3], [], [1, 2, 3]),
        ([], [], []),
        ([1, 1, 2], [1, 3], [1, 1, 1, 2, 3]),
        ([5], [1], [1, 5]),
    ])
    def test_merge(self, a, b, expected):
        mod = _merge_mod()
        merged = mod.MergeTwoSortedLists.merge(self._build(mod, a), self._build(mod, b))
        assert mod.to_list(merged) == expected
