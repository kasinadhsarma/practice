"""
======================================================
  ARRAYS IN DSA — PART 8: ADVANCED TECHNIQUES
======================================================
  1.  Segment Tree (range sum + point update)
  2.  Segment Tree with Lazy Propagation (range update)
  3.  Fenwick Tree / BIT (Binary Indexed Tree)
  4.  Sparse Table (Range Minimum Query in O(1))
  5.  Monotonic Stack — Next Greater Element
  6.  Monotonic Queue — Sliding Window Maximum
  7.  Bitwise techniques on arrays
"""

import math

# ===================================================
# 1. SEGMENT TREE — Range Sum Query + Point Update
#    Build: O(n)  |  Query: O(log n)  |  Update: O(log n)
# ===================================================
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self._build(arr, 0, 0, self.n - 1)

    def _build(self, arr, node, lo, hi):
        if lo == hi:
            self.tree[node] = arr[lo]
            return
        mid = (lo + hi) // 2
        self._build(arr, 2*node+1, lo, mid)
        self._build(arr, 2*node+2, mid+1, hi)
        self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]

    def update(self, idx, val, node=0, lo=0, hi=None):
        if hi is None: hi = self.n - 1
        if lo == hi:
            self.tree[node] = val
            return
        mid = (lo + hi) // 2
        if idx <= mid:
            self.update(idx, val, 2*node+1, lo, mid)
        else:
            self.update(idx, val, 2*node+2, mid+1, hi)
        self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]

    def query(self, l, r, node=0, lo=0, hi=None):
        """Returns sum of arr[l..r]."""
        if hi is None: hi = self.n - 1
        if r < lo or hi < l:
            return 0             # out of range
        if l <= lo and hi <= r:
            return self.tree[node]  # fully inside
        mid = (lo + hi) // 2
        return (self.query(l, r, 2*node+1, lo, mid) +
                self.query(l, r, 2*node+2, mid+1, hi))

arr = [1, 3, 5, 7, 9, 11]
st = SegmentTree(arr)
print("Segment Tree sum [1..4]:", st.query(1, 4))   # 3+5+7+9 = 24
st.update(1, 10)                                     # arr[1] = 10
print("After update[1]=10, sum[1..4]:", st.query(1, 4))  # 31

# ===================================================
# 2. SEGMENT TREE WITH LAZY PROPAGATION
#    Range Update (add val to range) + Range Sum Query
# ===================================================
class LazySegTree:
    def __init__(self, arr):
        n = len(arr)
        self.n = n
        self.tree = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
        self._build(arr, 0, 0, n - 1)

    def _build(self, arr, node, lo, hi):
        if lo == hi:
            self.tree[node] = arr[lo]; return
        mid = (lo + hi) // 2
        self._build(arr, 2*node+1, lo, mid)
        self._build(arr, 2*node+2, mid+1, hi)
        self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]

    def _push_down(self, node, lo, hi):
        if self.lazy[node]:
            mid = (lo + hi) // 2
            self.tree[2*node+1] += self.lazy[node] * (mid - lo + 1)
            self.lazy[2*node+1] += self.lazy[node]
            self.tree[2*node+2] += self.lazy[node] * (hi - mid)
            self.lazy[2*node+2] += self.lazy[node]
            self.lazy[node] = 0

    def range_update(self, l, r, val, node=0, lo=0, hi=None):
        if hi is None: hi = self.n - 1
        if r < lo or hi < l: return
        if l <= lo and hi <= r:
            self.tree[node] += val * (hi - lo + 1)
            self.lazy[node] += val; return
        self._push_down(node, lo, hi)
        mid = (lo + hi) // 2
        self.range_update(l, r, val, 2*node+1, lo, mid)
        self.range_update(l, r, val, 2*node+2, mid+1, hi)
        self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]

    def range_query(self, l, r, node=0, lo=0, hi=None):
        if hi is None: hi = self.n - 1
        if r < lo or hi < l: return 0
        if l <= lo and hi <= r: return self.tree[node]
        self._push_down(node, lo, hi)
        mid = (lo + hi) // 2
        return (self.range_query(l, r, 2*node+1, lo, mid) +
                self.range_query(l, r, 2*node+2, mid+1, hi))

lazy_st = LazySegTree([1, 2, 3, 4, 5])
print("\nLazy ST sum[0..4]:", lazy_st.range_query(0, 4))   # 15
lazy_st.range_update(1, 3, 10)                             # add 10 to [1..3]
print("After +10 on [1..3], sum[0..4]:", lazy_st.range_query(0, 4))  # 45

# ===================================================
# 3. FENWICK TREE / BIT
#    Point Update + Prefix Sum Query  O(log n)
# ===================================================
class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, delta):
        """Add delta to position i (1-indexed)."""
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)           # move to next responsible node

    def prefix_sum(self, i):
        """Sum of arr[1..i] (1-indexed)."""
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)           # move to parent
        return s

    def range_sum(self, l, r):
        return self.prefix_sum(r) - self.prefix_sum(l - 1)

bit = FenwickTree(6)
for idx, v in enumerate([1, 3, 5, 7, 9, 11], start=1):
    bit.update(idx, v)

print("\nFenwick prefix sum [1..4]:", bit.range_sum(1, 4))   # 16
bit.update(1, 5)    # arr[1] += 5 -> arr[1] = 6
print("After update[1]+=5, range[1..4]:", bit.range_sum(1, 4))  # 21

# ===================================================
# 4. SPARSE TABLE — Range Minimum Query (RMQ)  O(1) query
#    Build: O(n log n)  |  Query: O(1)
# ===================================================
class SparseTable:
    def __init__(self, arr):
        n = len(arr)
        LOG = max(1, math.floor(math.log2(n)) + 1) if n > 0 else 1
        self.log = [0] * (n + 1)
        for i in range(2, n + 1):
            self.log[i] = self.log[i // 2] + 1
        # table[k][i] = min of arr[i .. i+2^k-1]
        self.table = [[float('inf')] * n for _ in range(LOG)]
        self.table[0] = arr[:]
        for k in range(1, LOG):
            for i in range(n - (1 << k) + 1):
                self.table[k][i] = min(self.table[k-1][i],
                                       self.table[k-1][i + (1 << (k-1))])

    def query_min(self, l, r):
        """Minimum of arr[l..r] (0-indexed)."""
        k = self.log[r - l + 1]
        return min(self.table[k][l], self.table[k][r - (1 << k) + 1])

sp = SparseTable([2, 4, 3, 1, 6, 7, 8, 9, 1, 7])
print("\nSparse Table RMQ [0..4]:", sp.query_min(0, 4))    # 1
print("Sparse Table RMQ [2..7]:", sp.query_min(2, 7))     # 1

# ===================================================
# 5. MONOTONIC STACK — Next Greater Element
# ===================================================

# Next Greater Element I  O(n)
def next_greater_element(arr):
    n = len(arr)
    result = [-1] * n
    stack = []   # stores indices
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)
    return result

print("\nNext Greater [4,5,2,25]:", next_greater_element([4,5,2,25]))   # [5,25,25,-1]

# Next Smaller Element  O(n)
def next_smaller_element(arr):
    n = len(arr)
    result = [-1] * n
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)
    return result

print("Next Smaller [4,5,2,10,8]:", next_smaller_element([4,5,2,10,8]))

# Largest Rectangle in Histogram  O(n) — uses monotonic stack
def largest_rectangle(heights):
    stack = [-1]
    max_area = 0
    for i, h in enumerate(heights):
        while stack[-1] != -1 and heights[stack[-1]] >= h:
            height = heights[stack.pop()]
            width = i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    while stack[-1] != -1:
        height = heights[stack.pop()]
        width = len(heights) - stack[-1] - 1
        max_area = max(max_area, height * width)
    return max_area

print("Largest Rectangle [2,1,5,6,2,3]:", largest_rectangle([2,1,5,6,2,3]))  # 10

# ===================================================
# 6. MONOTONIC DEQUE — Sliding Window Maximum  O(n)
# ===================================================
from collections import deque

def sliding_window_max(arr, k):
    dq = deque()   # stores indices; front = max
    result = []
    for i in range(len(arr)):
        # remove indices outside window
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        # remove smaller elements from back
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(arr[dq[0]])
    return result

print("\nSliding Window Max k=3 in [1,3,-1,-3,5,3,6,7]:",
      sliding_window_max([1,3,-1,-3,5,3,6,7], 3))   # [3,3,5,5,6,7]

# ===================================================
# 7. BITWISE TECHNIQUES ON ARRAYS
# ===================================================

# Find single number (all others appear twice)  O(n) O(1)
def single_number(nums):
    result = 0
    for v in nums:
        result ^= v
    return result

print("\nSingle number [2,2,1]:", single_number([2,2,1]))          # 1
print("Single number [4,1,2,1,2]:", single_number([4,1,2,1,2]))   # 4

# Find two non-repeating numbers (all others appear twice)  O(n) O(1)
def two_single_numbers(nums):
    xor = 0
    for v in nums: xor ^= v       # xor = a ^ b
    # rightmost set bit differentiates a and b
    diff_bit = xor & (-xor)
    a = b = 0
    for v in nums:
        if v & diff_bit: a ^= v
        else:            b ^= v
    return sorted([a, b])

print("Two singles [1,2,3,2,1,4]:", two_single_numbers([1,2,3,2,1,4]))  # [3,4]

# Count set bits in all numbers 0..n  O(n)
def count_bits(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)
    return dp

print("Count bits 0..5:", count_bits(5))   # [0,1,1,2,1,2]

print("\n[Y] Advanced Techniques Done!")
