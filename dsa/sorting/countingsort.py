"""
Counting Sort
-------------
Technique : Non-comparison sort using key-frequency counting
Idea      : Instead of comparing elements, count how many times each value
            occurs, then use those counts (turned into a running/cumulative
            sum) to place every element directly into its final sorted
            position. Works for integers within a known, reasonably small
            range — handles negative numbers via an offset.

Formula / Property
    offset = -min(arr)                      (shifts values to start at 0)
    count[v] = number of occurrences of value v (after offset shift)
    cumulative[v] = count[0] + count[1] + ... + count[v]
                    → cumulative[v] is the last output index for value v

    Placing elements back-to-front keeps the sort STABLE (equal elements
    keep their relative order).

Steps
    1. Find min/max to build a count array covering the value range.
    2. Count occurrences of every (offset) value.
    3. Convert counts to a cumulative/prefix-sum array.
    4. Walk the input from right to left; place each element at
       cumulative[value]-1 in the output, then decrement that count.
    5. Return the output array.

Time  Complexity : O(n + k)  — n = array length, k = value range size
Space Complexity : O(n + k)  — count array + output array
"""

class CountingSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        arr = self.arr
        if not arr:
            return arr

        min_val, max_val = min(arr), max(arr)
        k = max_val - min_val + 1
        count = [0] * k

        for num in arr:
            count[num - min_val] += 1

        for i in range(1, k):
            count[i] += count[i - 1]

        output = [0] * len(arr)
        for num in reversed(arr):
            count[num - min_val] -= 1
            output[count[num - min_val]] = num

        return output


arr = list(map(int, input("enter elements separated by space: ").split()))
cs = CountingSort(arr)
print("sorted array:", cs.sort())
