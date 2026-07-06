"""
Kth Largest Element
--------------------
Technique : Min-heap of bounded size k
Idea      : To find the k-th largest element without fully sorting, keep a
            min-heap that never grows past size k. Push every number in; if
            the heap exceeds size k, pop the smallest. After processing the
            whole array, the heap's root (its minimum) is exactly the k-th
            largest element overall — everything smaller was already popped.

Formula / Property
    Maintain a min-heap H with |H| <= k.
    For each incoming value v:
        push v onto H
        if |H| > k: pop the minimum of H
    After processing all values, min(H) == the k-th largest overall value.

Steps
    1. Build a size-bounded min-heap (Python's `heapq` gives a min-heap).
    2. For each number, push it, then pop if the heap grew past size k.
    3. Return the heap's smallest element (heap[0]) — the k-th largest.

Time  Complexity : O(n log k)  — n pushes/pops on a heap of size at most k
Space Complexity : O(k)        — heap holds at most k elements
"""

import heapq

class KthLargestElement:
    def __init__(self, nums: list, k: int):
        self.nums = nums
        self.k = k

    def find(self):
        if self.k > len(self.nums) or self.k < 1:
            return None

        heap = []
        for num in self.nums:
            heapq.heappush(heap, num)
            if len(heap) > self.k:
                heapq.heappop(heap)

        return heap[0]


nums = list(map(int, input("enter elements separated by space: ").split()))
k = int(input("enter k: "))
result = KthLargestElement(nums, k).find()
print(f"{k}th largest element:", result)
