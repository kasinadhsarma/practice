"""
Min Stack
---------
Technique : Stack + auxiliary tracking stack
Idea      : A normal stack only gives O(1) access to the top. To also get
            the minimum in O(1), keep a second stack that mirrors every
            push/pop but only ever holds the running minimum seen so far
            at that depth.

Operations
    push(val)
        Push val onto the main stack.
        Push min(val, current_min) onto the min-stack (or just val if the
        min-stack is empty).
        Time: O(1)

    pop()
        Pop both stacks together, keeping them in sync.
        Time: O(1)

    top()
        Return main_stack[-1].
        Time: O(1)

    get_min()
        Return min_stack[-1] — the minimum across all currently-present
        elements.
        Time: O(1)

Applications
    - Range-minimum queries restricted to stack-order insert/delete
    - Building blocks for monotonic-stack problems

Time  Complexity : push/pop/top/get_min all O(1)
Space Complexity : O(n) — two parallel stacks
"""

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        current_min = val if not self.min_stack else min(val, self.min_stack[-1])
        self.min_stack.append(current_min)

    def pop(self):
        if not self.stack:
            return None
        self.min_stack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1] if self.stack else None

    def get_min(self):
        return self.min_stack[-1] if self.min_stack else None


elements = list(map(int, input("enter elements to push, separated by space: ").split()))
ms = MinStack()
for e in elements:
    ms.push(e)
print("top       :", ms.top())
print("min       :", ms.get_min())
print("popped    :", ms.pop())
print("min after :", ms.get_min())
