"""
======================================================
  ARRAYS IN DSA — PART 6: ARRAY ROTATION & REARRANGEMENT
======================================================
  Rotation:
    1. Left rotate by d (brute force)
    2. Left rotate by d (reversal algorithm)  O(n) O(1)
    3. Right rotate by d
    4. Check if one is rotation of another

  Rearrangement:
    5. Rearrange positive and negative alternately
    6. Next Permutation
    7. Maximum product subarray
    8. Majority Element (Boyer-Moore)
    9. Leaders in array
    10. Sort array by frequency
    11. Segregate Even/Odd
    12. Merge intervals
"""

from collections import Counter
import math

# ---------------------------------------------
# 1. LEFT ROTATE BY d (brute — one-by-one)  O(n*d)
# ---------------------------------------------
def left_rotate_brute(arr, d):
    a = arr[:]
    n = len(a)
    d = d % n
    for _ in range(d):
        temp = a[0]
        for i in range(n - 1):
            a[i] = a[i + 1]
        a[n - 1] = temp
    return a

print("Left rotate [1..7] by 2 (brute):", left_rotate_brute([1,2,3,4,5,6,7], 2))

# ---------------------------------------------
# 2. LEFT ROTATE BY d — REVERSAL ALGORITHM  O(n) O(1)
#    reverse(0,d-1), reverse(d,n-1), reverse(0,n-1)
# ---------------------------------------------
def reverse_part(arr, lo, hi):
    while lo < hi:
        arr[lo], arr[hi] = arr[hi], arr[lo]
        lo += 1; hi -= 1

def left_rotate_reversal(arr, d):
    a = arr[:]
    n = len(a)
    d = d % n
    reverse_part(a, 0, d - 1)
    reverse_part(a, d, n - 1)
    reverse_part(a, 0, n - 1)
    return a

print("Left rotate [1..7] by 2 (reversal):", left_rotate_reversal([1,2,3,4,5,6,7], 2))

# Using slicing (Pythonic, but O(n) space)
def left_rotate_slice(arr, d):
    n = len(arr)
    d = d % n
    return arr[d:] + arr[:d]

print("Left rotate (slice):", left_rotate_slice([1,2,3,4,5,6,7], 2))

# ---------------------------------------------
# 3. RIGHT ROTATE BY d  O(n) O(1)
# ---------------------------------------------
def right_rotate(arr, d):
    a = arr[:]
    n = len(a)
    d = d % n
    reverse_part(a, 0, n - 1)
    reverse_part(a, 0, d - 1)
    reverse_part(a, d, n - 1)
    return a

print("\nRight rotate [1..7] by 2:", right_rotate([1,2,3,4,5,6,7], 2))
# [6,7,1,2,3,4,5]

# ---------------------------------------------
# 4. CHECK IF ONE ARRAY IS ROTATION OF ANOTHER  O(n)
# ---------------------------------------------
def is_rotation(a, b):
    if len(a) != len(b): return False
    doubled = a + a
    # check if b appears as subarray in doubled
    n = len(b)
    for i in range(n):
        if doubled[i:i+n] == b:
            return True
    return False

print("\nIs [3,4,5,1,2] rotation of [1..5]:", is_rotation([1,2,3,4,5],[3,4,5,1,2]))  # True

# ---------------------------------------------
# 5. REARRANGE POSITIVES & NEGATIVES ALTERNATELY  O(n)
#    Assumes equal count of both (otherwise fill remaining)
# ---------------------------------------------
def rearrange_alternate(arr):
    pos = [v for v in arr if v >= 0]
    neg = [v for v in arr if v < 0]
    result = []
    i = j = 0
    while i < len(pos) and j < len(neg):
        result.append(pos[i]); i += 1
        result.append(neg[j]); j += 1
    result.extend(pos[i:])
    result.extend(neg[j:])
    return result

print("\nAlternate +/-:", rearrange_alternate([1,-2,-3,4,-5,6,7,-8]))

# ---------------------------------------------
# 6. NEXT PERMUTATION  O(n) in-place
#    Find next lexicographically greater permutation
# ---------------------------------------------
def next_permutation(arr):
    a = arr[:]
    n = len(a)
    # Step 1: find rightmost element smaller than its next
    i = n - 2
    while i >= 0 and a[i] >= a[i + 1]:
        i -= 1
    if i >= 0:
        # Step 2: find smallest element to right of i that is > a[i]
        j = n - 1
        while a[j] <= a[i]:
            j -= 1
        a[i], a[j] = a[j], a[i]
    # Step 3: reverse from i+1 to end
    a[i+1:] = a[i+1:][::-1]
    return a

print("\nNext permutation [1,2,3]:", next_permutation([1,2,3]))    # [1,3,2]
print("Next permutation [3,2,1]:", next_permutation([3,2,1]))    # [1,2,3]
print("Next permutation [1,1,5]:", next_permutation([1,1,5]))    # [1,5,1]

# ---------------------------------------------
# 7. MAXIMUM PRODUCT SUBARRAY  O(n)
# ---------------------------------------------
def max_product_subarray(arr):
    max_p = min_p = result = arr[0]
    for v in arr[1:]:
        candidates = (v, max_p * v, min_p * v)
        max_p = max(candidates)
        min_p = min(candidates)
        result = max(result, max_p)
    return result

print("\nMax product [2,3,-2,4]:", max_product_subarray([2,3,-2,4]))      # 6
print("Max product [-2,0,-1]:", max_product_subarray([-2,0,-1]))         # 0
print("Max product [-2,3,-4]:", max_product_subarray([-2,3,-4]))         # 24

# ---------------------------------------------
# 8. MAJORITY ELEMENT (appears > n/2 times)  O(n) O(1)
#    Boyer-Moore Voting Algorithm
# ---------------------------------------------
def majority_element(arr):
    candidate, count = None, 0
    for v in arr:
        if count == 0:
            candidate = v
        count += 1 if v == candidate else -1
    # Optional: verify (if majority not guaranteed)
    if arr.count(candidate) > len(arr) // 2:
        return candidate
    return None

print("\nMajority element [3,2,3]:", majority_element([3,2,3]))            # 3
print("Majority element [2,2,1,1,1,2,2]:", majority_element([2,2,1,1,1,2,2]))  # 2

# ---------------------------------------------
# 9. LEADERS IN ARRAY  O(n)
#    Element is leader if all elements to its right are smaller
# ---------------------------------------------
def find_leaders(arr):
    n = len(arr)
    leaders = [arr[-1]]         # last element is always a leader
    max_from_right = arr[-1]
    for i in range(n - 2, -1, -1):
        if arr[i] >= max_from_right:
            max_from_right = arr[i]
            leaders.append(arr[i])
    return leaders[::-1]

print("\nLeaders in [16,17,4,3,5,2]:", find_leaders([16,17,4,3,5,2]))  # [17,5,2]

# ---------------------------------------------
# 10. SORT BY FREQUENCY  O(n log n)
# ---------------------------------------------
def sort_by_frequency(arr):
    freq = Counter(arr)
    return sorted(arr, key=lambda x: (-freq[x], x))

print("\nSort by freq [2,3,2,4,5,12,2,3,3,3,12]:",
      sort_by_frequency([2,3,2,4,5,12,2,3,3,3,12]))

# ---------------------------------------------
# 11. SEGREGATE EVEN AND ODD  O(n) O(1)
# ---------------------------------------------
def segregate_even_odd(arr):
    a = arr[:]
    lo, hi = 0, len(a) - 1
    while lo < hi:
        while lo < hi and a[lo] % 2 == 0: lo += 1
        while lo < hi and a[hi] % 2 != 0: hi -= 1
        if lo < hi:
            a[lo], a[hi] = a[hi], a[lo]
            lo += 1; hi -= 1
    return a

print("\nSeggregate even/odd [1,2,3,4,5,6]:", segregate_even_odd([1,2,3,4,5,6]))

# ---------------------------------------------
# 12. MERGE OVERLAPPING INTERVALS  O(n log n)
# ---------------------------------------------
def merge_intervals(intervals):
    if not intervals: return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged

print("\nMerge [[1,3],[2,6],[8,10],[15,18]]:",
      merge_intervals([[1,3],[2,6],[8,10],[15,18]]))  # [[1,6],[8,10],[15,18]]

print("\n[Y] Rotation & Rearrangement Done!")
