"""
======================================================
  ARRAYS IN DSA — PART 7: CLASSIC ARRAY PROBLEMS
======================================================
  1.  Find missing number (1..n)
  2.  Find duplicate number (Floyd's / XOR)
  3.  Find all duplicates in array
  4.  Find missing and repeating
  5.  Best time to buy and sell stock (I, II, III)
  6.  Trapping Rain Water
  7.  Jump Game I & II
  8.  4-Sum problem
  9.  Subarray with given sum (positive)
  10. Longest consecutive sequence
  11. Spiral matrix traversal
  12. Matrix rotation 90°
  13. Set matrix zeroes
  14. Find kth largest / smallest element
"""

import heapq

# ---------------------------------------------
# 1. FIND MISSING NUMBER in [0..n]  O(n) O(1)
# ---------------------------------------------
def missing_number(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)

# XOR approach
def missing_number_xor(nums):
    xor = 0
    for i, v in enumerate(nums):
        xor ^= (i + 1) ^ v
    return xor

print("Missing in [3,0,1]:", missing_number([3, 0, 1]))         # 2
print("Missing XOR [9,6,4,2,3,5,7,0,1]:", missing_number_xor([9,6,4,2,3,5,7,0,1]))  # 8

# ---------------------------------------------
# 2. FIND DUPLICATE NUMBER (only one duplicate, n+1 array)
#    Floyd's cycle detection  O(n) O(1)
# ---------------------------------------------
def find_duplicate_floyd(nums):
    slow = fast = nums[0]
    # detect cycle
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    # find entrance
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow

print("\nDuplicate in [1,3,4,2,2]:", find_duplicate_floyd([1,3,4,2,2]))  # 2

# ---------------------------------------------
# 3. FIND ALL DUPLICATES  O(n) O(1) extra
#    Values are 1..n, array length n
# ---------------------------------------------
def find_all_duplicates(nums):
    result = []
    for v in nums:
        idx = abs(v) - 1
        if nums[idx] < 0:
            result.append(abs(v))
        else:
            nums[idx] = -nums[idx]
    # restore (optional)
    for i in range(len(nums)): nums[i] = abs(nums[i])
    return result

print("\nAll duplicates [4,3,2,7,8,2,3,1]:", find_all_duplicates([4,3,2,7,8,2,3,1]))

# ---------------------------------------------
# 4. FIND MISSING AND REPEATING  O(n) O(1) (math)
# ---------------------------------------------
def find_missing_repeating(arr):
    n = len(arr)
    S  = sum(arr)
    S2 = sum(v*v for v in arr)
    Sn  = n*(n+1)//2
    Sn2 = n*(n+1)*(2*n+1)//6
    # x - y = S - Sn          (x=repeat, y=missing)
    # x² - y² = S2 - Sn2
    diff = S - Sn
    sq_diff = S2 - Sn2
    x_plus_y = sq_diff // diff
    x = (diff + x_plus_y) // 2
    y = x - diff
    return x, y   # (repeated, missing)

print("\nMissing & Repeating [3,1,3]:", find_missing_repeating([3,1,3]))  # (3,2)

# ---------------------------------------------
# 5. BEST TIME TO BUY & SELL STOCK
# ---------------------------------------------

# I: at most one transaction  O(n)
def max_profit_I(prices):
    min_price = float('inf')
    max_profit = 0
    for p in prices:
        min_price = min(min_price, p)
        max_profit = max(max_profit, p - min_price)
    return max_profit

# II: unlimited transactions  O(n) (take every upslope)
def max_profit_II(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit

# III: at most two transactions  O(n)
def max_profit_III(prices):
    buy1 = buy2 = float('inf')
    profit1 = profit2 = 0
    for p in prices:
        buy1    = min(buy1, p)
        profit1 = max(profit1, p - buy1)
        buy2    = min(buy2, p - profit1)
        profit2 = max(profit2, p - buy2)
    return profit2

prices = [3, 3, 5, 0, 0, 3, 1, 4]
print("\nStock I:", max_profit_I(prices))    # 4
print("Stock II:", max_profit_II(prices))   # 6
print("Stock III:", max_profit_III(prices)) # 6

# ---------------------------------------------
# 6. TRAPPING RAIN WATER  O(n) O(1)
# ---------------------------------------------
def trap_water(height):
    lo, hi = 0, len(height) - 1
    left_max = right_max = water = 0
    while lo < hi:
        if height[lo] < height[hi]:
            if height[lo] >= left_max:
                left_max = height[lo]
            else:
                water += left_max - height[lo]
            lo += 1
        else:
            if height[hi] >= right_max:
                right_max = height[hi]
            else:
                water += right_max - height[hi]
            hi -= 1
    return water

print("\nTrapping water [0,1,0,2,1,0,1,3,2,1,2,1]:",
      trap_water([0,1,0,2,1,0,1,3,2,1,2,1]))   # 6

# ---------------------------------------------
# 7. JUMP GAME I & II
# ---------------------------------------------

# I: can reach last index?  O(n)
def can_jump(nums):
    max_reach = 0
    for i, v in enumerate(nums):
        if i > max_reach: return False
        max_reach = max(max_reach, i + v)
    return True

# II: minimum jumps to reach last index  O(n)
def jump_game_II(nums):
    jumps = cur_end = cur_farthest = 0
    for i in range(len(nums) - 1):
        cur_farthest = max(cur_farthest, i + nums[i])
        if i == cur_end:
            jumps += 1
            cur_end = cur_farthest
    return jumps

print("\nCan Jump [2,3,1,1,4]:", can_jump([2,3,1,1,4]))    # True
print("Can Jump [3,2,1,0,4]:", can_jump([3,2,1,0,4]))    # False
print("Min Jumps [2,3,1,1,4]:", jump_game_II([2,3,1,1,4]))  # 2

# ---------------------------------------------
# 8. 4-SUM (find all unique quadruplets summing to target)  O(n³)
# ---------------------------------------------
def four_sum(nums, target):
    nums.sort()
    result = []
    n = len(nums)
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i-1]: continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j-1]: continue
            lo, hi = j + 1, n - 1
            while lo < hi:
                s = nums[i] + nums[j] + nums[lo] + nums[hi]
                if s == target:
                    result.append([nums[i],nums[j],nums[lo],nums[hi]])
                    while lo < hi and nums[lo]==nums[lo+1]: lo += 1
                    while lo < hi and nums[hi]==nums[hi-1]: hi -= 1
                    lo += 1; hi -= 1
                elif s < target: lo += 1
                else: hi -= 1
    return result

print("\n4-Sum [1,0,-1,0,-2,2] target=0:", four_sum([1,0,-1,0,-2,2], 0))

# ---------------------------------------------
# 9. SUBARRAY WITH GIVEN SUM (all positive)  O(n)
# ---------------------------------------------
def subarray_with_sum(arr, target):
    lo = 0
    cur_sum = 0
    for hi in range(len(arr)):
        cur_sum += arr[hi]
        while cur_sum > target and lo < hi:
            cur_sum -= arr[lo]; lo += 1
        if cur_sum == target:
            return (lo, hi)
    return (-1, -1)

print("\nSubarray sum=15 in [1,4,20,3,10,5]:",
      subarray_with_sum([1,4,20,3,10,5], 15))   # indices of [20,3,10] or similar

# ---------------------------------------------
# 10. LONGEST CONSECUTIVE SEQUENCE  O(n)
# ---------------------------------------------
def longest_consecutive(nums):
    num_set = set(nums)
    best = 0
    for v in num_set:
        if v - 1 not in num_set:   # start of a sequence
            length = 1
            while v + length in num_set:
                length += 1
            best = max(best, length)
    return best

print("\nLongest consecutive [100,4,200,1,3,2]:", longest_consecutive([100,4,200,1,3,2]))  # 4

# ---------------------------------------------
# 11. SPIRAL MATRIX TRAVERSAL  O(m*n)
# ---------------------------------------------
def spiral_order(matrix):
    result = []
    if not matrix: return result
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for c in range(left, right + 1):   result.append(matrix[top][c])
        top += 1
        for r in range(top, bottom + 1):   result.append(matrix[r][right])
        right -= 1
        if top <= bottom:
            for c in range(right, left - 1, -1): result.append(matrix[bottom][c])
            bottom -= 1
        if left <= right:
            for r in range(bottom, top - 1, -1): result.append(matrix[r][left])
            left += 1
    return result

mat = [[1,2,3],[4,5,6],[7,8,9]]
print("\nSpiral order:", spiral_order(mat))  # [1,2,3,6,9,8,7,4,5]

# ---------------------------------------------
# 12. ROTATE MATRIX 90° CLOCKWISE  O(n²) O(1)
#     Transpose then reverse each row
# ---------------------------------------------
def rotate_90(matrix):
    n = len(matrix)
    # transpose
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # reverse each row
    for row in matrix:
        row.reverse()
    return matrix

import copy
m = copy.deepcopy(mat)
print("Rotate 90°:", rotate_90(m))  # [[7,4,1],[8,5,2],[9,6,3]]

# ---------------------------------------------
# 13. SET MATRIX ZEROES  O(m*n) O(1) extra
#     If any cell is 0, set entire row & col to 0
# ---------------------------------------------
def set_zeroes(matrix):
    m, n = len(matrix), len(matrix[0])
    row0 = any(matrix[0][j] == 0 for j in range(n))
    col0 = any(matrix[i][0] == 0 for i in range(m))
    # use first row/col as markers
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    if row0:
        for j in range(n): matrix[0][j] = 0
    if col0:
        for i in range(m): matrix[i][0] = 0
    return matrix

zm = [[1,1,1],[1,0,1],[1,1,1]]
print("\nSet Zeroes:", set_zeroes(zm))  # [[1,0,1],[0,0,0],[1,0,1]]

# ---------------------------------------------
# 14. KTH LARGEST / SMALLEST ELEMENT
# ---------------------------------------------

# Using min-heap  O(n log k)
def kth_largest(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)
    for v in nums[k:]:
        if v > heap[0]:
            heapq.heapreplace(heap, v)
    return heap[0]

# Using QuickSelect  O(n) avg
def kth_smallest_quickselect(arr, k):
    a = arr[:]
    def quickselect(lo, hi, k):
        if lo == hi: return a[lo]
        pivot_idx = partition_qs(lo, hi)
        if pivot_idx == k:     return a[pivot_idx]
        elif pivot_idx < k:    return quickselect(pivot_idx+1, hi, k)
        else:                  return quickselect(lo, pivot_idx-1, k)

    def partition_qs(lo, hi):
        pivot = a[hi]; i = lo - 1
        for j in range(lo, hi):
            if a[j] <= pivot:
                i += 1; a[i], a[j] = a[j], a[i]
        a[i+1], a[hi] = a[hi], a[i+1]
        return i + 1

    return quickselect(0, len(a)-1, k-1)

nums = [3, 2, 1, 5, 6, 4]
print("\nKth largest (k=2) in [3,2,1,5,6,4]:", kth_largest(nums, 2))       # 5
print("Kth smallest (k=2) in [3,2,1,5,6,4]:", kth_smallest_quickselect(nums, 2)) # 2

print("\n[Y] Classic Array Problems Done!")
