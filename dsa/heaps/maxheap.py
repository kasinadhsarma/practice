"""
Max-Heap
--------
Technique : Complete Binary Tree stored as an array (implicit tree structure)
Idea      : A max-heap is a complete binary tree where every parent node is
            greater than or equal to its children. The root always holds the
            maximum element, enabling O(1) access to the max.

Formula / Array Representation
    For a node at index i (0-based):
        parent      = (i - 1) // 2
        left child  = 2*i + 1
        right child = 2*i + 2

    Heap property : heap[parent] >= heap[child]  for every node

Operations
    insert(val)
        1. Append val to the end of the array.
        2. Bubble up (sift up): while val > its parent, swap them.
           Restores heap property from bottom to top.
        Time: O(log n)

    extract_max()
        1. Root (index 0) is the maximum.
        2. Replace root with the last element; remove last element.
        3. Bubble down (sift down / heapify-down):
           Swap root with its largest child until heap property is restored.
        Time: O(log n)

    get_max()
        1. Return heap[0].
        Time: O(1)

    Build heap from n elements: O(n)  — using repeated heapify-down from n//2-1

Applications
    - Priority queues
    - Heap sort (O(n log n))
    - Finding k largest elements
    - Prim's / Dijkstra's algorithms

Time  Complexity : insert O(log n)  |  extract_max O(log n)  |  get_max O(1)
Space Complexity : O(n) — array stores all elements
"""

class MaxHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, i): return (i - 1) // 2
    def _left(self, i):   return 2 * i + 1
    def _right(self, i):  return 2 * i + 2

    def insert(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        # bubble up
        while i > 0 and self.heap[self._parent(i)] < self.heap[i]:
            p = self._parent(i)
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            i = p

    def _heapify_down(self, i):
        n = len(self.heap)
        largest = i
        l, r = self._left(i), self._right(i)
        if l < n and self.heap[l] > self.heap[largest]:
            largest = l
        if r < n and self.heap[r] > self.heap[largest]:
            largest = r
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._heapify_down(largest)

    def extract_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()   # move last element to root
        self._heapify_down(0)            # restore heap property
        return root

    def get_max(self):
        return self.heap[0] if self.heap else None


elements = list(map(int, input("enter elements separated by space: ").split()))
mh = MaxHeap()
for e in elements:
    mh.insert(e)
print("max element :", mh.get_max())
print("extracted   :", mh.extract_max())
print("heap after  :", mh.heap)
