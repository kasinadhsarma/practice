"""
======================================================
  ARRAYS IN DSA — PART 5: PREFIX SUM & DIFFERENCE ARRAY
======================================================
  Prefix Sum:
    1. Build prefix sum array
    2. Range sum query  O(1) after O(n) preprocessing
    3. Subarray sum equals k
    4. Maximum subarray sum (Kadane's)
    5. Find equilibrium index
    6. 2D prefix sum (matrix range sum)

  Difference Array:
    7. Range update in O(1)
    8. Car pooling / Meeting Rooms
"""

from collections import defaultdict

# ---------------------------------------------
# 1. BUILD PREFIX SUM ARRAY  O(n)
# ---------------------------------------------
def build_prefix_sum(arr):
    """prefix[i] = arr[0] + arr[1] + ... + arr[i-1]
       (1-indexed; prefix[0] = 0 for convenience)"""
    n = len(arr)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]
    return prefix

arr = [2, 4, 6, 8, 10]
prefix = build_prefix_sum(arr)
print("Array:", arr)
print("Prefix:", prefix)

# ---------------------------------------------
# 2. RANGE SUM QUERY [l, r] (0-indexed)  O(1)
# ---------------------------------------------
def range_sum(prefix, l, r):
    """Sum of arr[l..r] inclusive."""
    return prefix[r + 1] - prefix[l]

print("\nRange Sum [1..3]:", range_sum(prefix, 1, 3))  # 4+6+8 = 18
print("Range Sum [0..4]:", range_sum(prefix, 0, 4))   # 30

# ---------------------------------------------
# 3. SUBARRAY SUM EQUALS K  O(n)
# ---------------------------------------------
def subarray_sum_equals_k(arr, k):
    """Count subarrays whose sum == k using prefix sum + hash map."""
    count = 0
    cumsum = 0
    freq = defaultdict(int)
    freq[0] = 1          # empty prefix
    for v in arr:
        cumsum += v
        count += freq[cumsum - k]
        freq[cumsum] += 1
    return count

print("\nSubarray sum=3 in [1,1,1]:", subarray_sum_equals_k([1, 1, 1], 3))    # 1  -> [1,1,1]
print("Subarray sum=3 in [1,2,3]:", subarray_sum_equals_k([1, 2, 3], 3))       # 2  -> [1,2], [3]
print("Subarray sum=0 in [1,-1,2,-2]:", subarray_sum_equals_k([1,-1,2,-2], 0)) # 3

# ---------------------------------------------
# 4. KADANE'S ALGORITHM — Maximum Subarray Sum  O(n)
# ---------------------------------------------
def kadane(arr):
    """Returns (max_sum, start_idx, end_idx)."""
    max_sum = cur_sum = arr[0]
    start = end = 0
    temp_start = 0
    for i in range(1, len(arr)):
        if cur_sum + arr[i] < arr[i]:
            cur_sum = arr[i]
            temp_start = i
        else:
            cur_sum += arr[i]
        if cur_sum > max_sum:
            max_sum = cur_sum
            start = temp_start
            end = i
    return max_sum, start, end

arr_k = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
ms, s, e = kadane(arr_k)
print(f"\nKadane max sum={ms}, subarray={arr_k[s:e+1]}")   # 6, [4,-1,2,1]

# Variant: Maximum Circular Subarray Sum
def max_circular_subarray(arr):
    max_sum, _, _ = kadane(arr)
    if max_sum < 0:
        return max_sum   # all negative
    total = sum(arr)
    neg_arr = [-v for v in arr]
    min_sum, _, _ = kadane(neg_arr)
    min_sum = -min_sum
    return max(max_sum, total - min_sum)

print("Circular Kadane [5,-3,5]:", max_circular_subarray([5, -3, 5]))   # 10

# ---------------------------------------------
# 5. FIND EQUILIBRIUM INDEX  O(n)
#    Index i where sum(arr[0..i-1]) == sum(arr[i+1..n-1])
# ---------------------------------------------
def equilibrium_index(arr):
    total = sum(arr)
    left_sum = 0
    for i, v in enumerate(arr):
        total -= v
        if left_sum == total:
            return i
        left_sum += v
    return -1

print("\nEquilibrium index of [-7,1,5,2,-4,3,0]:",
      equilibrium_index([-7, 1, 5, 2, -4, 3, 0]))   # 3

# ---------------------------------------------
# 6. 2D PREFIX SUM (Matrix Range Sum Query)  O(1) after O(m*n)
# ---------------------------------------------
def build_2d_prefix(matrix):
    if not matrix: return []
    m, n = len(matrix), len(matrix[0])
    P = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            P[i][j] = (matrix[i-1][j-1]
                       + P[i-1][j]
                       + P[i][j-1]
                       - P[i-1][j-1])
    return P

def matrix_range_sum(P, r1, c1, r2, c2):
    """Sum of matrix[r1..r2][c1..c2] (0-indexed)."""
    return (P[r2+1][c2+1] - P[r1][c2+1]
                           - P[r2+1][c1] + P[r1][c1])

mat = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]
P2 = build_2d_prefix(mat)
print("\n2D prefix sum query (2,1)-(4,3):", matrix_range_sum(P2, 2, 1, 4, 3))  # 8

# ===================================================
#  DIFFERENCE ARRAY
# ===================================================

# ---------------------------------------------
# 7. RANGE UPDATE in O(1) — Difference Array
#    Apply many range-add operations, then compute final array in O(n)
# ---------------------------------------------
def range_update_demo():
    """
    Given arr = [0]*n, apply q range-add operations:
        add val to arr[l..r]
    Difference array D:
        D[l]   += val
        D[r+1] -= val
    Final arr = prefix sum of D
    """
    n = 6
    D = [0] * (n + 1)

    def add(l, r, val):
        D[l]   += val
        D[r+1] -= val

    add(1, 3, 10)   # arr[1..3] += 10
    add(2, 5, 5)    # arr[2..5] += 5
    add(0, 2, 3)    # arr[0..2] += 3

    # reconstruct
    arr = [0] * n
    cur = 0
    for i in range(n):
        cur += D[i]
        arr[i] = cur
    return arr

print("\nDifference Array result:", range_update_demo())
# index:       0   1   2   3   4   5
# +3 on 0-2:   3   3   3
# +10 on 1-3:  3  13  13  10
# +5 on 2-5:   3  13  18  15   5   5
# Expected:   [3, 13, 18, 15, 5, 5]

# ---------------------------------------------
# 8. CAR POOLING using Difference Array  O(n + stops)
#    trips[i] = [num_passengers, from_stop, to_stop]
#    Can all passengers be carried if capacity = C?
# ---------------------------------------------
def car_pooling(trips, capacity):
    stops = [0] * 1001   # max stop index
    for passengers, start, end in trips:
        stops[start] += passengers
        stops[end]   -= passengers
    current = 0
    for passengers in stops:
        current += passengers
        if current > capacity:
            return False
    return True

print("\nCar Pooling [[2,1,5],[3,3,7]] cap=4:",
      car_pooling([[2,1,5],[3,3,7]], 4))   # False
print("Car Pooling [[2,1,5],[3,3,7]] cap=5:",
      car_pooling([[2,1,5],[3,3,7]], 5))   # True

# ---------------------------------------------
# BONUS: Product of Array Except Self  O(n) no division
# ---------------------------------------------
def product_except_self(arr):
    n = len(arr)
    out = [1] * n
    prefix = 1
    for i in range(n):
        out[i] = prefix
        prefix *= arr[i]
    suffix = 1
    for i in range(n - 1, -1, -1):
        out[i] *= suffix
        suffix *= arr[i]
    return out

print("\nProduct except self [1,2,3,4]:", product_except_self([1, 2, 3, 4]))  # [24,12,8,6]

print("\n[Y] Prefix Sum & Difference Array Done!")
