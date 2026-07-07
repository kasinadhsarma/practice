"""
Queue (Array-Based, via deque)
--------------------------------
Technique : FIFO (First-In-First-Out)
Idea      : A queue only allows insertion at the "rear" and removal at the
            "front" — the opposite discipline from a stack. A plain Python
            list is a poor fit because list.pop(0) is O(N) (it has to shift
            every remaining element). collections.deque is a doubly linked
            list of blocks, giving O(1) operations at BOTH ends, so it is
            used as the backing structure here.

Operations
    enqueue(val)
        Append val to the rear.
        Time: O(1)

    dequeue()
        Remove and return the front element.
        Time: O(1)   (O(N) if backed by a plain list — the reason for deque)

    peek()
        Return the front element without removing it.
        Time: O(1)

    is_empty()
        Time: O(1)

Applications
    - Task scheduling, print queues, BFS traversal (see dsa/graphs/bfs.py)
    - Buffering (producer/consumer pipelines)

Time  Complexity : enqueue/dequeue/peek O(1)
Space Complexity : O(n)
"""

from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, val):
        self.items.append(val)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.popleft()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


elements = list(map(int, input("enter elements to enqueue, separated by space: ").split()))
q = Queue()
for e in elements:
    q.enqueue(e)
print("front element :", q.peek())
print("dequeued      :", q.dequeue())
print("queue after   :", list(q.items))
