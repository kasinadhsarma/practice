"""
======================================================
  ARRAYS IN DSA — PART 10: SPECIAL ARRAY TYPES & PROBLEMS
======================================================
  1.  Jagged (Ragged) Arrays
  2.  Sparse Array
  3.  Circular Buffer / Ring Buffer
  4.  Prefix Maximum / Suffix Minimum Arrays
  5.  Subarray problems — all subarrays, print them
  6.  Kadane variants: min subarray sum, circular
  7.  Rearrange elements by sign
  8.  Find all pairs with given sum
  9.  Find pair with given difference
  10. Minimum swaps to sort
  11. Minimum number of platforms (trains)
  12. Activity Selection (Greedy)
  13. Stock span problem
"""

from collections import defaultdict

# ---------------------------------------------
# 1. JAGGED ARRAYS — rows of different lengths
# ---------------------------------------------
jagged = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]
print("Jagged Array:")
for row in jagged: print(row)

# Flatten jagged
flat = [v for row in jagged for v in row]
print("Flattened:", flat)

# ---------------------------------------------
# 2. SPARSE ARRAY (dictionary-based)
# ---------------------------------------------
class SparseArray:
    def __init__(self, size, default=0):
        self.size = size
        self.default = default
        self.data = {}

    def __setitem__(self, idx, val):
        if val != self.default:
            self.data[idx] = val
        elif idx in self.data:
            del self.data[idx]

    def __getitem__(self, idx):
        return self.data.get(idx, self.default)

    def __repr__(self):
        return f"SparseArray({self.size}, data={self.data})"

sa = SparseArray(10)
sa[0] = 5; sa[7] = 3; sa[9] = 8
print("\nSparse Array:", sa)
print("sa[0]:", sa[0], "  sa[5]:", sa[5])   # 5, 0

# ---------------------------------------------
# 3. CIRCULAR BUFFER / RING BUFFER  O(1) enqueue/dequeue
# ---------------------------------------------
class CircularBuffer:
    def __init__(self, capacity):
        self.cap = capacity
        self.buf = [None] * capacity
        self.head = 0           # read pointer
        self.tail = 0           # write pointer
        self.size = 0

    def enqueue(self, val):
        if self.size == self.cap:
            raise OverflowError("Buffer full")
        self.buf[self.tail] = val
        self.tail = (self.tail + 1) % self.cap
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise IndexError("Buffer empty")
        val = self.buf[self.head]
        self.head = (self.head + 1) % self.cap
        self.size -= 1
        return val

    def peek(self):
        if self.size == 0: raise IndexError("Buffer empty")
        return self.buf[self.head]

cb = CircularBuffer(3)
cb.enqueue(1); cb.enqueue(2); cb.enqueue(3)
print("\nCircular dequeue:", cb.dequeue(), cb.dequeue())   # 1 2
cb.enqueue(4)
print("Peek:", cb.peek())   # 3

# ---------------------------------------------
# 4. PREFIX MAXIMUM / SUFFIX MINIMUM
# ---------------------------------------------
arr = [3, 1, 4, 1, 5, 9, 2, 6]
n = len(arr)

prefix_max = arr[:]
for i in range(1, n): prefix_max[i] = max(prefix_max[i-1], arr[i])

suffix_min = arr[:]
for i in range(n-2, -1, -1): suffix_min[i] = min(suffix_min[i+1], arr[i])

print("\nArray:", arr)
print("Prefix Max:", prefix_max)
print("Suffix Min:", suffix_min)

# ---------------------------------------------
# 5. PRINT ALL SUBARRAYS  O(n³) / O(n²)
# ---------------------------------------------
def print_all_subarrays(arr):
    n = len(arr)
    subs = []
    for i in range(n):
        for j in range(i, n):
            subs.append(arr[i:j+1])
    return subs

print("\nAll subarrays of [1,2,3]:", print_all_subarrays([1,2,3]))
# [1],[2],[3],[1,2],[2,3],[1,2,3]

# Count subarrays: n*(n+1)//2
n_test = 5
print(f"Count of subarrays for n={n_test}: {n_test*(n_test+1)//2}")

# ---------------------------------------------
# 6. KADANE VARIANTS
# ---------------------------------------------

# Minimum subarray sum
def min_subarray_sum(arr):
    min_sum = cur_sum = arr[0]
    for v in arr[1:]:
        cur_sum = min(v, cur_sum + v)
        min_sum = min(min_sum, cur_sum)
    return min_sum

print("\nMin subarray sum [3,-4,2,-3,-1,7,-5]:",
      min_subarray_sum([3,-4,2,-3,-1,7,-5]))   # -7

# Maximum sum of non-adjacent elements  O(n)
def max_non_adjacent_sum(arr):
    if not arr: return 0
    if len(arr) == 1: return max(0, arr[0])
    incl = max(0, arr[0])
    excl = 0
    for v in arr[1:]:
        incl, excl = excl + max(0, v), max(incl, excl)
    return max(incl, excl)

print("Max non-adjacent [5,5,10,100,10,5]:",
      max_non_adjacent_sum([5,5,10,100,10,5]))   # 110

# ---------------------------------------------
# 7. REARRANGE ELEMENTS BY SIGN (keep relative order)  O(n)
# ---------------------------------------------
def rearrange_by_sign(arr):
    """Positive at even indices, negative at odd indices."""
    pos = [v for v in arr if v >= 0]
    neg = [v for v in arr if v < 0]
    result = [0] * len(arr)
    for i in range(len(pos)): result[2*i] = pos[i]
    for i in range(len(neg)): result[2*i+1] = neg[i]
    return result

print("\nRearrange by sign [3,1,-2,-5,2,-4]:",
      rearrange_by_sign([3,1,-2,-5,2,-4]))

# ---------------------------------------------
# 8. FIND ALL PAIRS WITH GIVEN SUM  O(n)
# ---------------------------------------------
def find_pairs_with_sum(arr, target):
    seen = set()
    pairs = []
    for v in arr:
        complement = target - v
        if complement in seen:
            pairs.append((complement, v))
        seen.add(v)
    return pairs

print("\nPairs with sum=6 in [1,5,3,2,4,6,0]:",
      find_pairs_with_sum([1,5,3,2,4,6,0], 6))

# ---------------------------------------------
# 9. FIND PAIR WITH GIVEN DIFFERENCE  O(n log n)
# ---------------------------------------------
def find_pair_difference(arr, diff):
    arr_sorted = sorted(arr)
    lo, hi = 0, 1
    pairs = []
    n = len(arr_sorted)
    while lo < n and hi < n:
        if lo == hi:
            hi += 1
            continue
        d = arr_sorted[hi] - arr_sorted[lo]
        if d == diff:
            pairs.append((arr_sorted[lo], arr_sorted[hi]))
            lo += 1; hi += 1
        elif d < diff:
            hi += 1
        else:
            lo += 1
    return pairs

print("\nPairs with diff=3 in [1,5,3,4,2]:",
      find_pair_difference([1,5,3,4,2], 3))

# ---------------------------------------------
# 10. MINIMUM SWAPS TO SORT (0-indexed)  O(n log n)
# ---------------------------------------------
def min_swaps_to_sort(arr):
    indexed = sorted(enumerate(arr), key=lambda x: x[1])
    visited = [False] * len(arr)
    swaps = 0
    for i in range(len(arr)):
        if visited[i] or indexed[i][0] == i:
            continue
        cycle = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = indexed[j][0]
            cycle += 1
        swaps += cycle - 1
    return swaps

print("\nMin swaps to sort [4,3,2,1]:", min_swaps_to_sort([4,3,2,1]))   # 2

# ---------------------------------------------
# 11. MINIMUM PLATFORMS (Train schedule)  O(n log n)
#     Given arrival & departure times of trains,
#     find min platforms so no train waits
# ---------------------------------------------
def min_platforms(arrival, departure):
    arrival.sort()
    departure.sort()
    platforms = max_platforms = 0
    i = j = 0
    while i < len(arrival):
        if arrival[i] <= departure[j]:
            platforms += 1
            i += 1
        else:
            platforms -= 1
            j += 1
        max_platforms = max(max_platforms, platforms)
    return max_platforms

arr_t = [900, 940, 950, 1100, 1500, 1800]
dep_t = [910, 1200, 1120, 1130, 1900, 2000]
print("\nMin platforms:", min_platforms(arr_t, dep_t))   # 3

# ---------------------------------------------
# 12. ACTIVITY SELECTION (Greedy)  O(n log n)
#     Select max number of non-overlapping activities
# ---------------------------------------------
def activity_selection(start, finish):
    activities = sorted(zip(finish, start))
    selected = []
    last_finish = -1
    for f, s in activities:
        if s >= last_finish:
            selected.append((s, f))
            last_finish = f
    return selected

s = [1, 3, 0, 5, 8, 5]
f = [2, 4, 6, 7, 9, 9]
print("\nActivity Selection:", activity_selection(s, f))

# ---------------------------------------------
# 13. STOCK SPAN PROBLEM  O(n)
#     Span[i] = number of consecutive days before i where price <= price[i]
# ---------------------------------------------
def stock_span(prices):
    n = len(prices)
    span = [1] * n
    stack = []   # stores indices
    for i in range(n):
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()
        span[i] = i + 1 if not stack else i - stack[-1]
        stack.append(i)
    return span

print("\nStock Span [100,80,60,70,60,75,85]:",
      stock_span([100,80,60,70,60,75,85]))   # [1,1,1,2,1,4,6]

# ---------------------------------------------
# BONUS: Maximum of all subarrays of size k using Sparse Table
# ---------------------------------------------
def max_subarray_k_sparse(arr, k):
    """All maximum values of subarrays of size k."""
    from collections import deque
    dq = deque()
    result = []
    for i in range(len(arr)):
        while dq and dq[0] < i - k + 1: dq.popleft()
        while dq and arr[dq[-1]] < arr[i]: dq.pop()
        dq.append(i)
        if i >= k - 1: result.append(arr[dq[0]])
    return result

print("\nMax subarray k=3 in [1,2,3,1,4,5,2,3,6]:",
      max_subarray_k_sparse([1,2,3,1,4,5,2,3,6], 3))

print("\n[Y] Special Arrays & Classic Problems Done!")
