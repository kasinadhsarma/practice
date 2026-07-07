"""
Queue Using Two Stacks
------------------------
Technique : Amortized-O(1) queue built purely from stack operations
Idea      : A stack reverses order (LIFO); reversing an already-reversed
            order gives back the original order (FIFO). Push everything
            onto an "in" stack. When a dequeue is needed and the "out"
            stack is empty, pour the entire "in" stack into "out" — this
            reverses the order once, making "out"'s top the oldest element.

Steps
    enqueue(val)
        Push val onto stack_in.
        Time: O(1)

    dequeue()
        If stack_out is empty, pop everything from stack_in and push it
        onto stack_out (reverses order — oldest ends up on top).
        Pop and return the top of stack_out.
        Time: O(1) amortized — the expensive transfer only happens once
              per element over its lifetime, so the average is O(1),
              even though a single call can be O(N).

Applications
    - Demonstrates how two LIFO primitives compose into a FIFO one
    - Useful when only stack-like primitives are available (e.g. certain
      hardware / language-restricted environments)

Time  Complexity : enqueue O(1)  |  dequeue O(1) amortized, O(N) worst case
Space Complexity : O(n) — two stacks together hold all elements
"""

class QueueUsingStacks:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, val):
        self.stack_in.append(val)

    def _transfer_if_needed(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

    def dequeue(self):
        self._transfer_if_needed()
        if not self.stack_out:
            return None
        return self.stack_out.pop()

    def peek(self):
        self._transfer_if_needed()
        return self.stack_out[-1] if self.stack_out else None

    def is_empty(self):
        return not self.stack_in and not self.stack_out


elements = list(map(int, input("enter elements to enqueue, separated by space: ").split()))
q = QueueUsingStacks()
for e in elements:
    q.enqueue(e)
print("front   :", q.peek())
print("dequeued:", q.dequeue())
