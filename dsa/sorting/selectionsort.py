"""
Selection Sort
--------------
Technique : Comparison-based, in-place selection
Idea      : Divide the array into a sorted and an unsorted region. Repeatedly
            find the minimum element from the unsorted region and move it to
            the end of the sorted region.

Formula / Recurrence
    Pass i selects minimum of arr[i..n-1] and places it at index i.
    Total comparisons = (n-1) + (n-2) + ... + 1 = n(n-1)/2
    Total swaps       = exactly (n-1)  — fewer swaps than bubble sort

Steps
    1. For i from 0 to n-2:
       a. Assume arr[i] is the minimum.
       b. Scan arr[i+1..n-1] for a smaller value; update min_idx.
       c. Swap arr[i] with arr[min_idx].
    2. After n-1 passes the array is sorted.

Time  Complexity : O(n^2) always (no early exit possible)
Space Complexity : O(1) — in-place
"""

class SelectionSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        n = len(self.arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if self.arr[j] < self.arr[min_idx]:
                    min_idx = j
            self.arr[i], self.arr[min_idx] = self.arr[min_idx], self.arr[i]
        return self.arr


arr = list(map(int, input("enter elements separated by space: ").split()))
sel = SelectionSort(arr)
print("sorted array:", sel.sort())
