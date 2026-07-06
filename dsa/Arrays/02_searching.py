"""
======================================================
  ARRAYS IN DSA — PART 2: SEARCHING ALGORITHMS
======================================================
  1. Linear Search
  2. Binary Search (iterative + recursive)
  3. Jump Search
  4. Interpolation Search
  5. Exponential Search
  6. Fibonacci Search
  7. Binary Search Variants (first/last occurrence, count, rotated)
"""

import math

# ---------------------------------------------
# 1. LINEAR SEARCH  O(n)
# ---------------------------------------------
def linear_search(arr, target):
    """Returns index of target, or -1 if not found."""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [64, 34, 25, 12, 22, 11, 90]
print("Linear Search 25 ->", linear_search(arr, 25))   # 2
print("Linear Search 99 ->", linear_search(arr, 99))   # -1

# ---------------------------------------------
# 2. BINARY SEARCH  O(log n)  — array must be SORTED
# ---------------------------------------------
def binary_search_iterative(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2      # avoid overflow
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

def binary_search_recursive(arr, target, lo=0, hi=None):
    if hi is None:
        hi = len(arr) - 1
    if lo > hi:
        return -1
    mid = lo + (hi - lo) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, hi)
    else:
        return binary_search_recursive(arr, target, lo, mid - 1)

sorted_arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print("\nBinary Search (iter) 23 ->", binary_search_iterative(sorted_arr, 23))  # 5
print("Binary Search (rec)  72 ->", binary_search_recursive(sorted_arr, 72))   # 8

# ---------------------------------------------
# 3. JUMP SEARCH  O(√n)  — sorted array
# ---------------------------------------------
def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    # jump until block containing target is found
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    # linear search in the block
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[prev] == target:
        return prev
    return -1

print("\nJump Search 56 ->", jump_search(sorted_arr, 56))   # 7

# ---------------------------------------------
# 4. INTERPOLATION SEARCH  O(log log n) avg, O(n) worst
#    Best for uniformly distributed sorted arrays
# ---------------------------------------------
def interpolation_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi and arr[lo] <= target <= arr[hi]:
        if lo == hi:
            return lo if arr[lo] == target else -1
        # Probe position formula
        pos = lo + ((target - arr[lo]) * (hi - lo) // (arr[hi] - arr[lo]))
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            lo = pos + 1
        else:
            hi = pos - 1
    return -1

print("\nInterpolation Search 91 ->", interpolation_search(sorted_arr, 91))  # 9

# ---------------------------------------------
# 5. EXPONENTIAL SEARCH  O(log n)  — sorted array
#    Finds range then binary searches in it
# ---------------------------------------------
def exponential_search(arr, target):
    n = len(arr)
    if arr[0] == target:
        return 0
    i = 1
    while i < n and arr[i] <= target:
        i *= 2
    lo = i // 2
    hi = min(i, n - 1)
    result = binary_search_iterative(arr[lo:hi+1], target)
    return result + lo if result != -1 else -1

print("\nExponential Search 38 ->", exponential_search(sorted_arr, 38))  # 6

# ---------------------------------------------
# 6. FIBONACCI SEARCH  O(log n)  — sorted array
#    Divides array into unequal Fibonacci parts
# ---------------------------------------------
def fibonacci_search(arr, target):
    n = len(arr)
    fib2, fib1, fib = 0, 1, 1   # fib(k-2), fib(k-1), fib(k)
    while fib < n:
        fib2, fib1, fib = fib1, fib, fib1 + fib

    offset = -1
    while fib > 1:
        i = min(offset + fib2, n - 1)
        if arr[i] < target:
            fib, fib1, fib2 = fib1, fib2, fib1 - fib2
            offset = i
        elif arr[i] > target:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            return i
    if fib1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1
    return -1

print("\nFibonacci Search 16 ->", fibonacci_search(sorted_arr, 16))   # 4

# ---------------------------------------------
# 7. BINARY SEARCH VARIANTS
# ---------------------------------------------

dup_arr = [1, 2, 2, 2, 3, 4, 4, 5]

# 7a. First occurrence of target
def first_occurrence(arr, target):
    lo, hi, result = 0, len(arr) - 1, -1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            result = mid
            hi = mid - 1         # keep searching LEFT
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return result

# 7b. Last occurrence of target
def last_occurrence(arr, target):
    lo, hi, result = 0, len(arr) - 1, -1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            result = mid
            lo = mid + 1         # keep searching RIGHT
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return result

# 7c. Count occurrences
def count_occurrences(arr, target):
    first = first_occurrence(arr, target)
    if first == -1:
        return 0
    return last_occurrence(arr, target) - first + 1

print("\nFirst occurrence of 2:", first_occurrence(dup_arr, 2))    # 1
print("Last occurrence of 2:", last_occurrence(dup_arr, 2))        # 3
print("Count of 2:", count_occurrences(dup_arr, 2))                # 3

# 7d. Search in rotated sorted array  e.g. [4,5,6,7,0,1,2]
def search_rotated(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            return mid
        # left half is sorted
        if arr[lo] <= arr[mid]:
            if arr[lo] <= target < arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        # right half is sorted
        else:
            if arr[mid] < target <= arr[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1

rotated = [4, 5, 6, 7, 0, 1, 2]
print("\nSearch in rotated [4,5,6,7,0,1,2] for 0 ->", search_rotated(rotated, 0))  # 4

# 7e. Find square root (floor) using binary search
def floor_sqrt(n):
    if n < 2:
        return n
    lo, hi = 1, n // 2
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        sq = mid * mid
        if sq == n:
            return mid
        elif sq < n:
            lo = mid + 1
        else:
            hi = mid - 1
    return hi  # floor

print("\nFloor sqrt(26) ->", floor_sqrt(26))  # 5

# 7f. Find peak element (element > both neighbours)
def find_peak(arr):
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] < arr[mid + 1]:
            lo = mid + 1
        else:
            hi = mid
    return lo   # index of peak

peak_arr = [1, 3, 20, 4, 1, 0]
print("Peak element at index:", find_peak(peak_arr), "->", peak_arr[find_peak(peak_arr)])  # 2 -> 20

print("\n[Y] All Searching Algorithms Done!")
