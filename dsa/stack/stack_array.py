"""
Stack (Array-Based)
--------------------
Technique : LIFO (Last-In-First-Out) via a dynamic array (Python list)
Idea      : A stack only allows access at one end — the "top". The last
            element pushed is always the first one popped. Python's list
            already supports O(1) amortized append/pop from the end, so it
            is used directly as the backing array.

Operations
    push(val)
        Append val to the end of the list (the "top").
        Time: O(1) amortized

    pop()
        Remove and return the last element.
        Time: O(1)

    peek()
        Return the last element without removing it.
        Time: O(1)

    is_empty()
        Time: O(1)

Applications
    - Function call stack / recursion
    - Undo history, browser back button
    - Balanced-parentheses / expression evaluation (see valid_parentheses.py,
      evaluate_postfix.py)

Time  Complexity : push/pop/peek O(1)
Space Complexity : O(n) — stores all elements
"""

class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


elements = list(map(int, input("enter elements to push, separated by space: ").split()))
s = Stack()
for e in elements:
    s.push(e)
print("top element :", s.peek())
print("popped      :", s.pop())
print("stack after :", s.items)
