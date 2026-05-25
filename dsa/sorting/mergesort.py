"""
Merge Sort
----------
Technique : Divide and Conquer
Idea      : Recursively split the array into two halves, sort each half
            independently, then merge the two sorted halves into one sorted array.

Formula / Recurrence
    T(n) = 2·T(n/2) + O(n)
    Solved by Master Theorem (Case 2) → T(n) = O(n log n)

    Merge step : two pointers i, j walk left and right halves;
                 the smaller element is appended to result each step.

Steps
    1. Base case: array of length ≤ 1 is already sorted.
    2. Find mid = n // 2; split into left = arr[:mid], right = arr[mid:].
    3. Recursively sort left and right.
    4. Merge: compare front elements of left and right; pick the smaller one.
    5. Append remaining elements from whichever half is not exhausted.

Time  Complexity : O(n log n) — all cases
Space Complexity : O(n) — auxiliary arrays created during merge
"""

class MergeSort:
    def __init__(self, arr):
        self.arr = arr

    def _merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def sort(self, arr=None):
        if arr is None:
            arr = self.arr
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left  = self.sort(arr[:mid])
        right = self.sort(arr[mid:])
        return self._merge(left, right)


arr = list(map(int, input("enter elements separated by space: ").split()))
ms = MergeSort(arr)
print("sorted array:", ms.sort())
