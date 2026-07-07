"""
Deque (Double-Ended Queue)
----------------------------
Technique : O(1) insertion/removal at BOTH ends
Idea      : A deque generalizes stack (one end) and queue (opposite ends)
            into a single structure that allows push/pop at either end.
            Python's collections.deque is implemented as a doubly linked
            list of fixed-size blocks, giving O(1) at both ends (unlike a
            plain list, where inserting/removing at index 0 is O(N)).

Operations
    add_front(val) / add_rear(val)
        Time: O(1) each

    remove_front() / remove_rear()
        Time: O(1) each

Applications
    - Sliding window maximum/minimum (monotonic deque) — see
      dsa/Arrays/08_advanced_techniques.py -> sliding_window_max
    - Palindrome checking (compare from both ends inward)
    - Undo/redo with bounded history (evict oldest from one end)

Time  Complexity : all four core ops O(1)
Space Complexity : O(n)
"""

from collections import deque

class Deque:
    def __init__(self):
        self.items = deque()

    def add_front(self, val):
        self.items.appendleft(val)

    def add_rear(self, val):
        self.items.append(val)

    def remove_front(self):
        if self.is_empty():
            return None
        return self.items.popleft()

    def remove_rear(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek_front(self):
        return self.items[0] if self.items else None

    def peek_rear(self):
        return self.items[-1] if self.items else None

    def is_empty(self):
        return len(self.items) == 0


elements = list(map(int, input("enter elements to add at rear, separated by space: ").split()))
dq = Deque()
for e in elements:
    dq.add_rear(e)
print("front       :", dq.peek_front())
print("rear        :", dq.peek_rear())
dq.add_front(0)
print("after add_front(0):", list(dq.items))
