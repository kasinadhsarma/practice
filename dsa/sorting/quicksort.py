"""
Quick Sort
----------
Technique : Divide and Conquer with in-place partitioning (Lomuto scheme)
Idea      : Choose a pivot element. Rearrange the array so all elements smaller
            than the pivot are to its left and all larger are to its right
            (partition step). Recursively sort both sides.

Formula / Recurrence
    Average case : T(n) = 2·T(n/2) + O(n)  → O(n log n)
    Worst  case  : T(n) = T(n-1)   + O(n)  → O(n^2)
                   (occurs when pivot is always the smallest/largest element)

    Lomuto Partition:
        pivot = arr[high]
        i = low - 1
        for j in [low, high):
            if arr[j] <= pivot: i++, swap(arr[i], arr[j])
        swap(arr[i+1], arr[high])   ← place pivot in final position
        return i + 1

Steps
    1. Choose pivot as last element (Lomuto scheme).
    2. Partition: move all elements ≤ pivot to the left side.
    3. Place pivot at its correct sorted index.
    4. Recurse on left sub-array (indices < pivot index).
    5. Recurse on right sub-array (indices > pivot index).

Time  Complexity : O(n log n) average  |  O(n^2) worst case
Space Complexity : O(log n) — recursion stack (average)
"""

class QuickSort:
    def __init__(self, arr):
        self.arr = arr

    def _partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def _quicksort(self, arr, low, high):
        if low < high:
            pi = self._partition(arr, low, high)
            self._quicksort(arr, low, pi - 1)
            self._quicksort(arr, pi + 1, high)

    def sort(self):
        self._quicksort(self.arr, 0, len(self.arr) - 1)
        return self.arr


arr = list(map(int, input("enter elements separated by space: ").split()))
qs = QuickSort(arr)
print("sorted array:", qs.sort())
