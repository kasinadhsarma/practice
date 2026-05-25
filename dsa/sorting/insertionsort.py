"""
Insertion Sort
--------------
Technique : Comparison-based, incremental (builds sorted array one element at a time)
Idea      : Treat the first element as a sorted sub-array. For each subsequent
            element, shift all larger sorted elements one position right and
            insert the current element into its correct position.

Formula / Recurrence
    Invariant : arr[0..i-1] is sorted before processing index i
    Shifts per insertion = at most i comparisons
    Total comparisons   = 0 + 1 + 2 + ... + (n-1) = n(n-1)/2

Steps
    1. Start from index 1; treat arr[0] as sorted.
    2. Store arr[i] as key.
    3. Shift all arr[j] > key one position to the right.
    4. Place key in the vacated position.
    5. Repeat for i = 1 to n-1.

Time  Complexity : O(n^2) worst/average  |  O(n) best (already sorted)
Space Complexity : O(1) — in-place
"""

class InsertionSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        for i in range(1, len(self.arr)):
            key = self.arr[i]
            j = i - 1
            while j >= 0 and self.arr[j] > key:
                self.arr[j + 1] = self.arr[j]
                j -= 1
            self.arr[j + 1] = key
        return self.arr


arr = list(map(int, input("enter elements separated by space: ").split()))
ins = InsertionSort(arr)
print("sorted array:", ins.sort())
