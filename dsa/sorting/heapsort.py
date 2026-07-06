"""
Heap Sort
---------
Technique : Selection via a binary max-heap (array-based, in-place)
Idea      : Build a max-heap from the array so the largest element sits at
            the root. Repeatedly swap the root with the last unsorted
            element, shrink the heap by one, and sift the new root down to
            restore the heap property. This grows a sorted suffix from the
            back of the array.

Formula / Array Representation
    For a node at index i (0-based):
        left child  = 2*i + 1
        right child = 2*i + 2

    Build-heap: heapify every non-leaf node from n//2 - 1 down to 0.
    Extraction: swap arr[0] with arr[end]; heapify_down(0, end) on the
                shrinking heap of size `end`.

Steps
    1. Build a max-heap in place over the whole array: O(n).
    2. For end from n-1 down to 1:
       a. Swap arr[0] (the max) with arr[end] — puts it in final position.
       b. Sift arr[0] down within the heap of size `end` (excludes the
          already-sorted suffix).
    3. The array is now sorted in ascending order.

Time  Complexity : O(n log n) — all cases (build O(n) + n extractions O(log n))
Space Complexity : O(1)       — sorts in place, no auxiliary array
"""

class HeapSort:
    def __init__(self, arr):
        self.arr = arr

    def _heapify_down(self, arr, size, i):
        largest = i
        left, right = 2 * i + 1, 2 * i + 2
        if left < size and arr[left] > arr[largest]:
            largest = left
        if right < size and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self._heapify_down(arr, size, largest)

    def sort(self):
        arr = self.arr
        n = len(arr)

        # build max-heap
        for i in range(n // 2 - 1, -1, -1):
            self._heapify_down(arr, n, i)

        # repeatedly extract the max to the end
        for end in range(n - 1, 0, -1):
            arr[0], arr[end] = arr[end], arr[0]
            self._heapify_down(arr, end, 0)

        return arr


arr = list(map(int, input("enter elements separated by space: ").split()))
hs = HeapSort(arr)
print("sorted array:", hs.sort())
