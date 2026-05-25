"""
Bubble Sort
-----------
Technique : Comparison-based iterative sorting
Idea      : Repeatedly compare adjacent elements and swap them if they are
            in the wrong order. After each pass the largest unsorted element
            "bubbles up" to its correct position at the end of the array.

Formula / Recurrence
    After pass i  →  last i elements are in their final position
    Number of comparisons = (n-1) + (n-2) + ... + 1 = n(n-1)/2

Steps
    1. Outer loop runs (n-1) times.
    2. Inner loop compares arr[j] and arr[j+1] for j in [0, n-1-i).
    3. Swap if arr[j] > arr[j+1].
    4. Repeat until no swaps occur (array is sorted).

Time  Complexity : O(n^2) worst/average  |  O(n) best (already sorted)
Space Complexity : O(1) — in-place, no extra memory used
"""

class BubbleSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        n = len(self.arr)
        for i in range(n - 1):
            swapped = False
            for j in range(n - 1 - i):
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
                    swapped = True
            if not swapped:   # early exit if already sorted
                break
        return self.arr


arr = list(map(int, input("enter elements separated by space: ").split()))
bs = BubbleSort(arr)
print("sorted array:", bs.sort())
