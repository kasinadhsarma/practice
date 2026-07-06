"""
Radix Sort
----------
Technique : Non-comparison sort — LSD (Least Significant Digit) digit-by-digit
Idea      : Sort non-negative integers one digit position at a time, from the
            least significant digit to the most significant, using a stable
            counting sort as the subroutine for each digit. After processing
            every digit of the largest number, the whole array is sorted.

Formula / Property
    digit(num, place) = (num // place) % 10        (place = 1, 10, 100, ...)

    Stability is essential: each pass must preserve the relative order
    established by all previous (less significant) digit passes, otherwise
    the final result would not be fully sorted.

Steps
    1. Find the maximum value to know how many digit positions exist.
    2. For place = 1, 10, 100, ... while place <= max_val:
       a. Run a stable counting sort keyed on digit(num, place).
    3. After the most significant digit's pass, the array is fully sorted.

Time  Complexity : O(d * (n + b))  — d = number of digits, b = base (10)
Space Complexity : O(n + b)        — output array + digit-bucket counts
"""

class RadixSort:
    def __init__(self, arr):
        self.arr = arr

    def _counting_sort_by_digit(self, arr, place):
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        for num in arr:
            digit = (num // place) % 10
            count[digit] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for num in reversed(arr):
            digit = (num // place) % 10
            count[digit] -= 1
            output[count[digit]] = num

        return output

    def sort(self):
        arr = self.arr
        if not arr:
            return arr

        max_val = max(arr)
        place = 1
        while max_val // place > 0:
            arr = self._counting_sort_by_digit(arr, place)
            place *= 10

        return arr


arr = list(map(int, input("enter non-negative elements separated by space: ").split()))
rs = RadixSort(arr)
print("sorted array:", rs.sort())
