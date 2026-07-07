"""
Circular Queue (Fixed-Capacity Array)
---------------------------------------
Technique : Ring buffer over a fixed-size array
Idea      : A naive array queue wastes space — once front advances past
            index 0, those slots are never reused. A circular queue wraps
            both front and rear around the array using modulo arithmetic,
            so freed slots at the beginning are reused once rear wraps
            around, all in a fixed-size buffer (no resizing needed).

Formula
    Given a fixed-size array of capacity C, front index f, rear index r,
    and count of elements n:
        next rear index  = (r + 1) % C
        next front index = (f + 1) % C
        full  when n == C
        empty when n == 0

Operations
    enqueue(val)
        If full, reject. Otherwise place val at rear, advance rear
        (mod C), increment count.
        Time: O(1)

    dequeue()
        If empty, return None. Otherwise read front, advance front
        (mod C), decrement count.
        Time: O(1)

Applications
    - Fixed-size buffers: keyboard input buffers, streaming/audio buffers
    - CPU scheduling ring buffers

Time  Complexity : enqueue/dequeue O(1)
Space Complexity : O(C) — fixed capacity, reused in place (no resizing)
"""

class CircularQueue:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = [None] * capacity
        self.front = 0
        self.rear = 0
        self.count = 0

    def is_full(self):
        return self.count == self.capacity

    def is_empty(self):
        return self.count == 0

    def enqueue(self, val):
        if self.is_full():
            return False
        self.data[self.rear] = val
        self.rear = (self.rear + 1) % self.capacity
        self.count += 1
        return True

    def dequeue(self):
        if self.is_empty():
            return None
        val = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return val

    def peek(self):
        return None if self.is_empty() else self.data[self.front]


capacity = int(input("enter queue capacity: "))
elements = list(map(int, input("enter elements to enqueue, separated by space: ").split()))
cq = CircularQueue(capacity)
for e in elements:
    print(f"enqueue {e}:", cq.enqueue(e))
print("front   :", cq.peek())
print("dequeued:", cq.dequeue())
