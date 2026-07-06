"""
Shell Sort
----------
Technique : Gap-sequence generalisation of Insertion Sort
Idea      : Insertion sort is efficient on nearly-sorted arrays but slow when
            small values are far from their correct position (they must shift
            one step at a time). Shell sort first sorts elements far apart
            (using a large gap), progressively shrinking the gap down to 1,
            so that by the final pass — plain insertion sort — the array is
            already almost sorted.

Formula / Gap Sequence
    This implementation uses the classic halving sequence:
        gap = n // 2, n // 4, n // 8, ..., 1

    For each gap, elements at distance `gap` apart form an independent
    "gap-sorted" sub-array, sorted using insertion-sort-style shifting.

Steps
    1. Start with gap = n // 2.
    2. While gap > 0:
       a. Perform a gapped insertion sort: for each index i from gap to n-1,
          shift back elements that are `gap` apart and greater than arr[i],
          then insert arr[i] into its correct gapped position.
       b. Halve the gap (integer division) and repeat.
    3. When gap reaches 0 (after the gap=1 pass), the array is fully sorted.

Time  Complexity : O(n log n) to O(n^2) depending on gap sequence (halving: ~O(n^1.5) worst case)
Space Complexity : O(1) — sorts in place
"""

class ShellSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        arr = self.arr
        n = len(arr)
        gap = n // 2

        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 2

        return arr


arr = list(map(int, input("enter elements separated by space: ").split()))
ss = ShellSort(arr)
print("sorted array:", ss.sort())
