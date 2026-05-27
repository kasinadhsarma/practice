"""
======================================================
  ARRAYS IN DSA — PART 4: TWO POINTERS & SLIDING WINDOW
======================================================
  Two Pointer Technique:
    1. Two Sum (sorted)
    2. Three Sum
    3. Container With Most Water
    4. Move Zeroes
    5. Remove Duplicates (sorted)
    6. Reverse Array
    7. Merge Two Sorted Arrays
    8. Dutch National Flag (3-way partition)

  Sliding Window:
    9.  Max Sum Subarray of size k (fixed)
    10. Smallest Subarray with sum >= S (variable)
    11. Longest Substring Without Repeating Characters
    12. Max Consecutive Ones III (with at most k flips)
    13. Fruit Into Baskets (at most 2 distinct)
    14. Minimum Window Substring
"""

from collections import defaultdict

# ===================================================
#  TWO POINTER TECHNIQUE
# ===================================================

# ---------------------------------------------
# 1. TWO SUM in sorted array  O(n)
# ---------------------------------------------
def two_sum_sorted(arr, target):
    """Returns indices (1-based) of two numbers that add up to target."""
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        s = arr[lo] + arr[hi]
        if s == target:
            return (lo + 1, hi + 1)
        elif s < target:
            lo += 1
        else:
            hi -= 1
    return (-1, -1)

print("Two Sum [2,7,11,15] target=9:", two_sum_sorted([2, 7, 11, 15], 9))  # (1,2)

# ---------------------------------------------
# 2. THREE SUM  O(n²)  — find all unique triplets summing to 0
# ---------------------------------------------
def three_sum(arr):
    arr.sort()
    result = []
    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue              # skip duplicates
        lo, hi = i + 1, len(arr) - 1
        while lo < hi:
            s = arr[i] + arr[lo] + arr[hi]
            if s == 0:
                result.append([arr[i], arr[lo], arr[hi]])
                while lo < hi and arr[lo] == arr[lo + 1]: lo += 1
                while lo < hi and arr[hi] == arr[hi - 1]: hi -= 1
                lo += 1; hi -= 1
            elif s < 0:
                lo += 1
            else:
                hi -= 1
    return result

print("\nThree Sum [-1,0,1,2,-1,-4]:", three_sum([-1, 0, 1, 2, -1, -4]))

# ---------------------------------------------
# 3. CONTAINER WITH MOST WATER  O(n)
# ---------------------------------------------
def max_water(height):
    lo, hi = 0, len(height) - 1
    max_area = 0
    while lo < hi:
        area = min(height[lo], height[hi]) * (hi - lo)
        max_area = max(max_area, area)
        if height[lo] < height[hi]:
            lo += 1
        else:
            hi -= 1
    return max_area

print("\nMax Water [1,8,6,2,5,4,8,3,7]:", max_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49

# ---------------------------------------------
# 4. MOVE ZEROES to end (preserve order)  O(n)
# ---------------------------------------------
def move_zeroes(arr):
    a = arr[:]
    slow = 0
    for fast in range(len(a)):
        if a[fast] != 0:
            a[slow], a[fast] = a[fast], a[slow]
            slow += 1
    return a

print("\nMove Zeroes [0,1,0,3,12]:", move_zeroes([0, 1, 0, 3, 12]))  # [1,3,12,0,0]

# ---------------------------------------------
# 5. REMOVE DUPLICATES from sorted array (in-place)  O(n)
# ---------------------------------------------
def remove_duplicates(arr):
    if not arr: return 0
    a = arr[:]
    slow = 0
    for fast in range(1, len(a)):
        if a[fast] != a[slow]:
            slow += 1
            a[slow] = a[fast]
    print("Deduped array:", a[:slow + 1])
    return slow + 1   # new length

remove_duplicates([1, 1, 2, 2, 3, 4, 4, 5])

# ---------------------------------------------
# 6. REVERSE ARRAY in-place  O(n)
# ---------------------------------------------
def reverse_array(arr):
    a = arr[:]
    lo, hi = 0, len(a) - 1
    while lo < hi:
        a[lo], a[hi] = a[hi], a[lo]
        lo += 1; hi -= 1
    return a

print("\nReverse [1,2,3,4,5]:", reverse_array([1, 2, 3, 4, 5]))

# ---------------------------------------------
# 7. MERGE TWO SORTED ARRAYS  O(m+n)
# ---------------------------------------------
def merge_sorted(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i]); i += 1
        else:
            result.append(b[j]); j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result

print("\nMerge [1,3,5] & [2,4,6]:", merge_sorted([1, 3, 5], [2, 4, 6]))

# ---------------------------------------------
# 8. DUTCH NATIONAL FLAG  O(n) — sort array of 0s,1s,2s
# ---------------------------------------------
def dutch_flag(arr):
    a = arr[:]
    low = mid = 0
    high = len(a) - 1
    while mid <= high:
        if a[mid] == 0:
            a[low], a[mid] = a[mid], a[low]
            low += 1; mid += 1
        elif a[mid] == 1:
            mid += 1
        else:   # a[mid] == 2
            a[mid], a[high] = a[high], a[mid]
            high -= 1
    return a

print("\nDutch Flag [2,0,2,1,1,0]:", dutch_flag([2, 0, 2, 1, 1, 0]))  # [0,0,1,1,2,2]

# ===================================================
#  SLIDING WINDOW TECHNIQUE
# ===================================================

# ---------------------------------------------
# 9. MAX SUM SUBARRAY of fixed size k  O(n)
# ---------------------------------------------
def max_sum_subarray_k(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]  # slide
        max_sum = max(max_sum, window_sum)
    return max_sum

print("\n\nMax sum subarray k=3 in [2,1,5,1,3,2]:",
      max_sum_subarray_k([2, 1, 5, 1, 3, 2], 3))   # 9

# ---------------------------------------------
# 10. SMALLEST SUBARRAY with sum >= S  O(n)
# ---------------------------------------------
def smallest_subarray_sum(arr, S):
    min_len = float('inf')
    window_sum = 0
    lo = 0
    for hi in range(len(arr)):
        window_sum += arr[hi]
        while window_sum >= S:
            min_len = min(min_len, hi - lo + 1)
            window_sum -= arr[lo]
            lo += 1
    return min_len if min_len != float('inf') else 0

print("Smallest subarray sum>=7 in [2,1,5,2,3,2]:",
      smallest_subarray_sum([2, 1, 5, 2, 3, 2], 7))  # 2

# ---------------------------------------------
# 11. LONGEST SUBSTRING without repeating chars  O(n)
# ---------------------------------------------
def length_of_longest_substring(s):
    char_map = {}
    lo = 0
    max_len = 0
    for hi, ch in enumerate(s):
        if ch in char_map and char_map[ch] >= lo:
            lo = char_map[ch] + 1
        char_map[ch] = hi
        max_len = max(max_len, hi - lo + 1)
    return max_len

print("\nLongest no-repeat 'abcabcbb':", length_of_longest_substring("abcabcbb"))  # 3
print("Longest no-repeat 'pwwkew':", length_of_longest_substring("pwwkew"))       # 3

# ---------------------------------------------
# 12. MAX CONSECUTIVE ONES with k flips  O(n)
#     (0s can be flipped to 1s at most k times)
# ---------------------------------------------
def max_ones_with_k_flips(arr, k):
    lo = 0
    zeros = 0
    max_len = 0
    for hi in range(len(arr)):
        if arr[hi] == 0:
            zeros += 1
        while zeros > k:
            if arr[lo] == 0:
                zeros -= 1
            lo += 1
        max_len = max(max_len, hi - lo + 1)
    return max_len

print("\nMax ones k=2 in [1,1,0,0,1,1,1,0,1,1]:",
      max_ones_with_k_flips([1,1,0,0,1,1,1,0,1,1], 2))   # 9 (flip positions 7,3)

# ---------------------------------------------
# 13. FRUIT INTO BASKETS (at most 2 distinct values)  O(n)
# ---------------------------------------------
def total_fruit(fruits):
    basket = defaultdict(int)
    lo = 0
    max_len = 0
    for hi in range(len(fruits)):
        basket[fruits[hi]] += 1
        while len(basket) > 2:
            basket[fruits[lo]] -= 1
            if basket[fruits[lo]] == 0:
                del basket[fruits[lo]]
            lo += 1
        max_len = max(max_len, hi - lo + 1)
    return max_len

print("\nFruits max 2 baskets [1,2,1,2,3]:", total_fruit([1, 2, 1, 2, 3]))  # 4

# ---------------------------------------------
# 14. MINIMUM WINDOW SUBSTRING  O(n + m)
# ---------------------------------------------
def min_window(s, t):
    need = defaultdict(int)
    for c in t:
        need[c] += 1
    missing = len(t)
    lo = 0
    best = (float('inf'), 0, 0)
    for hi, ch in enumerate(s, 1):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1
        if missing == 0:
            # shrink from left
            while need[s[lo]] < 0:
                need[s[lo]] += 1
                lo += 1
            if hi - lo < best[0]:
                best = (hi - lo, lo, hi)
            need[s[lo]] += 1
            missing += 1
            lo += 1
    return s[best[1]:best[2]] if best[0] != float('inf') else ""

print('\nMin window "ADOBECODEBANC" t="ABC":', min_window("ADOBECODEBANC", "ABC"))  # "BANC"

print("\n[Y] Two Pointers & Sliding Window Done!")
