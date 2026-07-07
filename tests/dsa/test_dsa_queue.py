"""
tests/dsa/test_dsa_queue.py
=============================
Tests for all classes under dsa/queue/:
    Queue · CircularQueue · QueueUsingStacks · Deque
"""

import pytest
from tests.utils import load_module


def _Queue():
    return load_module('dsa/queue/queue_array.py', ['1 2 3'], alias='dsa_queue').Queue

def _CircularQueue():
    return load_module('dsa/queue/circular_queue.py', ['3', '1 2 3'], alias='dsa_circular_queue').CircularQueue

def _QueueUsingStacks():
    return load_module('dsa/queue/queue_using_stacks.py', ['1 2 3'], alias='dsa_queue_stacks').QueueUsingStacks

def _Deque():
    return load_module('dsa/queue/deque_basic.py', ['1 2 3'], alias='dsa_deque').Deque


# ═════════════════════════════════════════════════════════════════════════════

class TestQueue:

    def test_fifo_order(self):
        q = _Queue()()
        q.enqueue(1); q.enqueue(2); q.enqueue(3)
        assert q.dequeue() == 1
        assert q.dequeue() == 2
        assert q.dequeue() == 3

    def test_peek_does_not_remove(self):
        q = _Queue()()
        q.enqueue(10); q.enqueue(20)
        assert q.peek() == 10
        assert q.size() == 2

    def test_empty_queue(self):
        q = _Queue()()
        assert q.is_empty()
        assert q.dequeue() is None
        assert q.peek() is None


class TestCircularQueue:

    def test_enqueue_dequeue_order(self):
        cq = _CircularQueue()(3)
        assert cq.enqueue(1)
        assert cq.enqueue(2)
        assert cq.dequeue() == 1
        assert cq.dequeue() == 2

    def test_full_rejects_enqueue(self):
        cq = _CircularQueue()(2)
        cq.enqueue(1); cq.enqueue(2)
        assert cq.is_full()
        assert cq.enqueue(3) is False

    def test_wraparound_reuses_slots(self):
        cq = _CircularQueue()(3)
        cq.enqueue(1); cq.enqueue(2); cq.enqueue(3)
        cq.dequeue()               # frees slot 0
        assert cq.enqueue(4)       # wraps around into freed slot
        assert cq.dequeue() == 2
        assert cq.dequeue() == 3
        assert cq.dequeue() == 4

    def test_empty_dequeue_returns_none(self):
        cq = _CircularQueue()(2)
        assert cq.dequeue() is None

    def test_peek(self):
        cq = _CircularQueue()(2)
        cq.enqueue(7)
        assert cq.peek() == 7


class TestQueueUsingStacks:

    def test_fifo_order(self):
        q = _QueueUsingStacks()()
        q.enqueue(1); q.enqueue(2); q.enqueue(3)
        assert q.dequeue() == 1
        assert q.dequeue() == 2
        assert q.dequeue() == 3

    def test_interleaved_enqueue_dequeue(self):
        q = _QueueUsingStacks()()
        q.enqueue(1); q.enqueue(2)
        assert q.dequeue() == 1
        q.enqueue(3)
        assert q.dequeue() == 2
        assert q.dequeue() == 3

    def test_empty(self):
        q = _QueueUsingStacks()()
        assert q.is_empty()
        assert q.dequeue() is None


class TestDeque:

    def test_add_and_remove_both_ends(self):
        dq = _Deque()()
        dq.add_rear(1); dq.add_rear(2)
        dq.add_front(0)
        assert dq.peek_front() == 0
        assert dq.peek_rear() == 2
        assert dq.remove_front() == 0
        assert dq.remove_rear() == 2
        assert dq.remove_front() == 1

    def test_empty(self):
        dq = _Deque()()
        assert dq.is_empty()
        assert dq.remove_front() is None
        assert dq.remove_rear() is None
