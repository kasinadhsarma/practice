"""
======================================================
  ARRAYS IN DSA -- PART 11: REMAINING TOPICS
======================================================
  1.  LIS -- Longest Increasing Subsequence  O(n log n)
  2.  Count Inversions (Merge Sort)           O(n log n)
  3.  Median of Two Sorted Arrays             O(log(min(m,n)))
  4.  Merge K Sorted Arrays (Min-Heap)        O(n log k)
  5.  Max Sum Rectangle in 2D Matrix          O(m^2 * n)
  6.  Wave / Zigzag Array                     O(n)
  7.  Cycle Sort (minimum array writes)       O(n)
  8.  Pancake Sorting                         O(n^2)
  9.  Elements Appearing > n/3 Times          O(n) O(1)
  10. Rearrange Array in Max-Min Form         O(n)
  11. Array Represents a Number (Add 1)       O(n)
  12. Longest Bitonic Subarray               O(n)
"""

import heapq
import bisect

# -------------------------------------------------
# 1. LONGEST INCREASING SUBSEQUENCE (LIS)
# -------------------------------------------------

# O(n^2) DP approach
def lis_dp(arr):
    """Returns length and the actual LIS."""
    n = len(arr)
    dp = [1] * n
    parent = [-1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j
    # reconstruct
    max_len = max(dp)
    idx = dp.index(max_len)
    lis = []
    while idx != -1:
        lis.append(arr[idx])
        idx = parent[idx]
    return max_len, lis[::-1]

# O(n log n) Patience Sorting approach
def lis_fast(arr):
    """Returns just the length in O(n log n)."""
    tails = []   # tails[i] = smallest tail of all IS of length i+1
    for v in arr:
        pos = bisect.bisect_left(tails, v)
        if pos == len(tails):
            tails.append(v)
        else:
            tails[pos] = v
    return len(tails)

arr = [10, 9, 2, 5, 3, 7, 101, 18]
length, seq = lis_dp(arr)
print("LIS DP  [10,9,2,5,3,7,101,18]: length=%d, seq=%s" % (length, seq))
print("LIS fast length:", lis_fast(arr))   # 4

# Longest Decreasing Subsequence = LIS of reversed array
def lds(arr): return lis_fast(arr[::-1])
print("LDS [10,9,2,5,3,7,101,18]:", lds(arr))

# Longest Bitonic Subsequence = LIS from left + LDS from right - 1
def longest_bitonic_subsequence(arr):
    n = len(arr)
    # LIS ending at each index
    lis = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                lis[i] = max(lis[i], lis[j] + 1)
    # LIS starting from each index (= LDS)
    lds = [1] * n
    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            if arr[j] < arr[i]:
                lds[i] = max(lds[i], lds[j] + 1)
    return max(lis[i] + lds[i] - 1 for i in range(n))

print("Longest Bitonic [1,11,2,10,4,5,2,1]:",
      longest_bitonic_subsequence([1,11,2,10,4,5,2,1]))   # 6

# -------------------------------------------------
# 2. COUNT INVERSIONS using Merge Sort   O(n log n)
#    Inversion: pair (i,j) where i<j but arr[i]>arr[j]
# -------------------------------------------------
def count_inversions(arr):
    if len(arr) <= 1:
        return arr[:], 0
    mid = len(arr) // 2
    left, left_inv  = count_inversions(arr[:mid])
    right, right_inv = count_inversions(arr[mid:])
    merged, split_inv = merge_count(left, right)
    return merged, left_inv + right_inv + split_inv

def merge_count(left, right):
    result = []
    inv = 0
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
            inv += len(left) - i   # all remaining left elements form inversions
    result.extend(left[i:])
    result.extend(right[j:])
    return result, inv

_, inv = count_inversions([8, 4, 2, 1])
print("\nInversions in [8,4,2,1]:", inv)   # 6

_, inv2 = count_inversions([1, 20, 6, 4, 5])
print("Inversions in [1,20,6,4,5]:", inv2)  # 5

# -------------------------------------------------
# 3. MEDIAN OF TWO SORTED ARRAYS   O(log(min(m,n)))
# -------------------------------------------------
def find_median_sorted(A, B):
    # ensure A is the smaller array
    if len(A) > len(B):
        A, B = B, A
    m, n = len(A), len(B)
    lo, hi = 0, m
    while lo <= hi:
        i = (lo + hi) // 2          # partition A
        j = (m + n + 1) // 2 - i   # partition B
        A_left  = A[i-1] if i > 0 else float('-inf')
        A_right = A[i]   if i < m else float('inf')
        B_left  = B[j-1] if j > 0 else float('-inf')
        B_right = B[j]   if j < n else float('inf')

        if A_left <= B_right and B_left <= A_right:
            if (m + n) % 2 == 1:
                return max(A_left, B_left)
            return (max(A_left, B_left) + min(A_right, B_right)) / 2
        elif A_left > B_right:
            hi = i - 1
        else:
            lo = i + 1

print("\nMedian [1,3] & [2]:", find_median_sorted([1,3], [2]))             # 2.0
print("Median [1,2] & [3,4]:", find_median_sorted([1,2], [3,4]))          # 2.5
print("Median [0,0] & [0,0]:", find_median_sorted([0,0], [0,0]))          # 0.0
print("Median [] & [1]:", find_median_sorted([], [1]))                     # 1.0

# -------------------------------------------------
# 4. MERGE K SORTED ARRAYS   O(n log k)
# -------------------------------------------------
def merge_k_sorted(arrays):
    heap = []
    # (value, array_index, element_index)
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))
    result = []
    while heap:
        val, i, j = heapq.heappop(heap)
        result.append(val)
        if j + 1 < len(arrays[i]):
            heapq.heappush(heap, (arrays[i][j+1], i, j+1))
    return result

arrays = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
print("\nMerge K sorted:", merge_k_sorted(arrays))   # [1..9]

# -------------------------------------------------
# 5. MAXIMUM SUM RECTANGLE IN 2D MATRIX   O(m^2 * n)
#    Apply Kadane's along each pair of rows
# -------------------------------------------------
def max_sum_rectangle(matrix):
    m, n = len(matrix), len(matrix[0])
    max_sum = float('-inf')
    best = (0, 0, 0, 0)

    for top in range(m):
        col_sum = [0] * n
        for bottom in range(top, m):
            for c in range(n): col_sum[c] += matrix[bottom][c]
            # Kadane on col_sum
            cur = col_sum[0]
            cur_start = 0
            g_start = 0
            g_max = col_sum[0]
            g_end = 0
            for c in range(1, n):
                if col_sum[c] > cur + col_sum[c]:
                    cur = col_sum[c]; cur_start = c
                else:
                    cur += col_sum[c]
                if cur > g_max:
                    g_max = cur; g_end = c; g_start = cur_start
            if g_max > max_sum:
                max_sum = g_max
                best = (top, g_start, bottom, g_end)
    return max_sum, best

mat = [
    [ 1, -2, -1,  4],
    [-8,  3,  4,  2],
    [ 3,  8, 10, -8],
    [-4,  4, -6,  5]
]
ms, rect = max_sum_rectangle(mat)
print("\nMax sum rectangle: sum=%d, (top,left,bottom,right)=%s" % (ms, rect))  # 29

# -------------------------------------------------
# 6. WAVE ARRAY / ZIGZAG ARRAY   O(n)
#    arr[0] >= arr[1] <= arr[2] >= arr[3] ...
# -------------------------------------------------
def wave_array(arr):
    a = arr[:]
    for i in range(0, len(a) - 1, 2):
        if i > 0 and a[i] < a[i-1]:
            a[i], a[i-1] = a[i-1], a[i]
        if i+1 < len(a) and a[i] < a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
    return a

# Simpler: sort then swap adjacent pairs
def wave_array_v2(arr):
    a = sorted(arr)
    for i in range(0, len(a)-1, 2):
        a[i], a[i+1] = a[i+1], a[i]
    return a

print("\nWave array [3,6,5,10,7,20]:", wave_array_v2([3,6,5,10,7,20]))

# Verify wave property
def is_wave(arr):
    for i in range(len(arr)-1):
        if i % 2 == 0 and arr[i] < arr[i+1]: return False
        if i % 2 == 1 and arr[i] > arr[i+1]: return False
    return True

print("Is wave:", is_wave(wave_array_v2([3,6,5,10,7,20])))   # True

# -------------------------------------------------
# 7. CYCLE SORT   O(n) writes, O(n^2) time
#    Minimises total number of writes to the array
#    Only works when values are 1..n (or 0..n-1)
# -------------------------------------------------
def cycle_sort(arr):
    a = arr[:]
    writes = 0
    for cycle_start in range(len(a) - 1):
        item = a[cycle_start]
        pos = cycle_start
        for i in range(cycle_start + 1, len(a)):
            if a[i] < item:
                pos += 1
        if pos == cycle_start:
            continue
        while item == a[pos]:
            pos += 1
        a[pos], item = item, a[pos]
        writes += 1
        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start + 1, len(a)):
                if a[i] < item:
                    pos += 1
            while item == a[pos]:
                pos += 1
            a[pos], item = item, a[pos]
            writes += 1
    return a, writes

sorted_arr, w = cycle_sort([3, 1, 5, 4, 2])
print("\nCycle sort [3,1,5,4,2]:", sorted_arr, "writes:", w)

# -------------------------------------------------
# 8. PANCAKE SORTING   O(n^2) flips
#    Only operation allowed: flip(arr, k) reverses arr[0..k]
# -------------------------------------------------
def pancake_sort(arr):
    a = arr[:]
    result = []

    def flip(a, k):
        a[:k+1] = a[:k+1][::-1]

    n = len(a)
    for size in range(n, 1, -1):
        max_idx = a[:size].index(max(a[:size]))
        if max_idx == size - 1:
            continue
        if max_idx != 0:
            flip(a, max_idx)
            result.append(max_idx + 1)   # 1-indexed flip position
        flip(a, size - 1)
        result.append(size)
    return a, result

ps, flips = pancake_sort([3, 6, 2, 7, 4, 5, 1])
print("\nPancake sort [3,6,2,7,4,5,1]:", ps)
print("Flip sequence:", flips)

# -------------------------------------------------
# 9. ELEMENTS APPEARING MORE THAN n/3 TIMES   O(n) O(1)
#    Extended Boyer-Moore (at most 2 such elements)
# -------------------------------------------------
def majority_elements_n3(nums):
    c1 = c2 = None
    cnt1 = cnt2 = 0
    for v in nums:
        if v == c1:         cnt1 += 1
        elif v == c2:       cnt2 += 1
        elif cnt1 == 0:     c1, cnt1 = v, 1
        elif cnt2 == 0:     c2, cnt2 = v, 1
        else:               cnt1 -= 1; cnt2 -= 1
    threshold = len(nums) // 3
    return [v for v in (c1, c2) if v is not None and nums.count(v) > threshold]

print("\nMajority > n/3 in [3,2,3]:", majority_elements_n3([3,2,3]))          # [3]
print("Majority > n/3 in [1,1,1,3,3,2,2,2]:", majority_elements_n3([1,1,1,3,3,2,2,2]))  # [1,2]

# -------------------------------------------------
# 10. REARRANGE ARRAY IN MAX-MIN FORM   O(n log n)
#     Result: max, min, 2nd-max, 2nd-min, ...
#     Sort first, then pick from both ends alternately
# -------------------------------------------------
def rearrange_max_min(arr):
    a = sorted(arr)
    n = len(a)
    result = [0] * n
    lo, hi = 0, n - 1
    for i in range(n):
        if i % 2 == 0:               # even positions get max
            result[i] = a[hi]; hi -= 1
        else:                        # odd positions get min
            result[i] = a[lo]; lo += 1
    return result

print("\nMax-Min form [1,2,3,4,5,6,7]:", rearrange_max_min([1,2,3,4,5,6,7]))
# Expected: [7,1,6,2,5,3,4]

# -------------------------------------------------
# 11. ARRAY REPRESENTS A NUMBER -- Add 1   O(n)
# -------------------------------------------------
def add_one(digits):
    d = digits[:]
    for i in range(len(d)-1, -1, -1):
        if d[i] < 9:
            d[i] += 1
            return d
        d[i] = 0
    return [1] + d    # overflow: [9,9,9] -> [1,0,0,0]

print("\nAdd 1 to [1,2,3]:", add_one([1,2,3]))     # [1,2,4]
print("Add 1 to [9,9,9]:", add_one([9,9,9]))       # [1,0,0,0]
print("Add 1 to [9]:", add_one([9]))               # [1,0]

# Multiply two numbers represented as arrays  O(m*n)
def multiply_arrays(num1, num2):
    m, n = len(num1), len(num2)
    result = [0] * (m + n)
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            mul = num1[i] * num2[j]
            p1, p2 = i + j, i + j + 1
            total = mul + result[p2]
            result[p2] = total % 10
            result[p1] += total // 10
    # remove leading zeros
    result = [str(d) for d in result]
    while len(result) > 1 and result[0] == '0':
        result.pop(0)
    return [int(d) for d in result]

print("Multiply [1,2,3] x [4,5,6]:", multiply_arrays([1,2,3],[4,5,6]))   # [5,6,0,8,8]

# -------------------------------------------------
# 12. LONGEST BITONIC SUBARRAY (contiguous)   O(n)
#     Different from Bitonic Subsequence --
#     elements must be contiguous
# -------------------------------------------------
def longest_bitonic_subarray(arr):
    n = len(arr)
    if n == 0: return 0

    # inc[i] = length of increasing run ending at i
    inc = [1] * n
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            inc[i] = inc[i-1] + 1

    # dec[i] = length of decreasing run starting at i
    dec = [1] * n
    for i in range(n-2, -1, -1):
        if arr[i] > arr[i+1]:
            dec[i] = dec[i+1] + 1

    # bitonic length at i = inc[i] + dec[i] - 1
    return max(inc[i] + dec[i] - 1 for i in range(n))

print("\nLongest Bitonic subarray [12,4,78,90,45,23]:",
      longest_bitonic_subarray([12,4,78,90,45,23]))   # 5  (4,78,90,45,23)

print("Longest Bitonic subarray [20,4,1,2,3,4,2,10]:",
      longest_bitonic_subarray([20,4,1,2,3,4,2,10]))  # 5  (1,2,3,4,2)

# -------------------------------------------------
# FINAL SUMMARY: All missing topics now covered
# -------------------------------------------------
print("""
[DONE] All remaining array topics covered:
  1.  LIS (O(n^2) DP  +  O(n log n) patience sort)
  2.  Count Inversions via Merge Sort  O(n log n)
  3.  Median of Two Sorted Arrays      O(log(min(m,n)))
  4.  Merge K Sorted Arrays            O(n log k)
  5.  Max Sum Rectangle 2D             O(m^2 * n)
  6.  Wave / Zigzag Array              O(n)
  7.  Cycle Sort (min writes)          O(n) writes
  8.  Pancake Sort                     O(n^2) flips
  9.  Majority Elements > n/3          O(n) O(1)
  10. Rearrange Max-Min Form           O(n)
  11. Array as Number (Add1, Multiply) O(n)
  12. Longest Bitonic Subarray         O(n)
""")
