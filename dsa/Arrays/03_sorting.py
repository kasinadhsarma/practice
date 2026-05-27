"""
======================================================
  ARRAYS IN DSA — PART 3: SORTING ALGORITHMS
======================================================
  1.  Bubble Sort
  2.  Selection Sort
  3.  Insertion Sort
  4.  Shell Sort
  5.  Merge Sort
  6.  Quick Sort
  7.  Heap Sort
  8.  Counting Sort
  9.  Radix Sort
  10. Bucket Sort
  11. Tim Sort (Python built-in explanation)
"""

# ---------------------------------------------
# 1. BUBBLE SORT  O(n²) time | O(1) space
#    Repeatedly swap adjacent out-of-order pairs
# ---------------------------------------------
def bubble_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:           # already sorted — best case O(n)
            break
    return a

print("Bubble:", bubble_sort([64, 34, 25, 12, 22, 11, 90]))

# ---------------------------------------------
# 2. SELECTION SORT  O(n²) time | O(1) space
#    Find min in unsorted portion, place it first
# ---------------------------------------------
def selection_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

print("Selection:", selection_sort([64, 25, 12, 22, 11]))

# ---------------------------------------------
# 3. INSERTION SORT  O(n²) worst | O(n) best | O(1) space
#    Build sorted prefix one element at a time
# ---------------------------------------------
def insertion_sort(arr):
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

print("Insertion:", insertion_sort([12, 11, 13, 5, 6]))

# ---------------------------------------------
# 4. SHELL SORT  O(n log n) ~ O(n^1.5) | O(1) space
#    Insertion sort with diminishing gap sequences
# ---------------------------------------------
def shell_sort(arr):
    a = arr[:]
    n = len(a)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = a[i]
            j = i
            while j >= gap and a[j - gap] > temp:
                a[j] = a[j - gap]
                j -= gap
            a[j] = temp
        gap //= 2
    return a

print("Shell:", shell_sort([12, 34, 54, 2, 3]))

# ---------------------------------------------
# 5. MERGE SORT  O(n log n) all cases | O(n) space
#    Divide-and-conquer, stable
# ---------------------------------------------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left  = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

print("Merge:", merge_sort([38, 27, 43, 3, 9, 82, 10]))

# ---------------------------------------------
# 6. QUICK SORT  O(n log n) avg | O(n²) worst | O(log n) space
#    Divide-and-conquer, in-place
# ---------------------------------------------
def quick_sort(arr, lo=0, hi=None):
    if hi is None: hi = len(arr) - 1
    if lo < hi:
        pi = partition(arr, lo, hi)
        quick_sort(arr, lo, pi - 1)
        quick_sort(arr, pi + 1, hi)

def partition(arr, lo, hi):
    pivot = arr[hi]          # last element as pivot
    i = lo - 1
    for j in range(lo, hi):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
    return i + 1

qs = [10, 7, 8, 9, 1, 5]
quick_sort(qs)
print("Quick:", qs)

# Randomised Quick Sort (avoids worst-case on sorted input)
import random
def quick_sort_rand(arr, lo=0, hi=None):
    if hi is None: hi = len(arr) - 1
    if lo < hi:
        # swap random pivot with last element
        r = random.randint(lo, hi)
        arr[r], arr[hi] = arr[hi], arr[r]
        pi = partition(arr, lo, hi)
        quick_sort_rand(arr, lo, pi - 1)
        quick_sort_rand(arr, pi + 1, hi)

# ---------------------------------------------
# 7. HEAP SORT  O(n log n) all cases | O(1) space
#    Uses max-heap
# ---------------------------------------------
def heap_sort(arr):
    a = arr[:]
    n = len(a)
    # Build max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i)
    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]     # move current root (max) to end
        heapify(a, i, 0)
    return a

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1   # left child
    r = 2 * i + 2   # right child
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

print("Heap:", heap_sort([12, 11, 13, 5, 6, 7]))

# ---------------------------------------------
# 8. COUNTING SORT  O(n + k) | O(k) space
#    Only for non-negative integers with bounded range k
# ---------------------------------------------
def counting_sort(arr):
    if not arr: return arr
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for v in arr:
        count[v] += 1
    result = []
    for v, c in enumerate(count):
        result.extend([v] * c)
    return result

print("Counting:", counting_sort([4, 2, 2, 8, 3, 3, 1]))

# ---------------------------------------------
# 9. RADIX SORT  O(d*(n+k)) | O(n+k) space
#    Sort by individual digits using counting sort
# ---------------------------------------------
def radix_sort(arr):
    if not arr: return arr
    max_val = max(arr)
    exp = 1
    a = arr[:]
    while max_val // exp > 0:
        a = counting_sort_by_digit(a, exp)
        exp *= 10
    return a

def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count  = [0] * 10
    for i in arr:
        idx = (i // exp) % 10
        count[idx] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        idx = (arr[i] // exp) % 10
        output[count[idx] - 1] = arr[i]
        count[idx] -= 1
    return output

print("Radix:", radix_sort([170, 45, 75, 90, 802, 24, 2, 66]))

# ---------------------------------------------
# 10. BUCKET SORT  O(n + k) avg | O(n²) worst | O(n+k) space
#     Best for uniformly distributed floats in [0,1)
# ---------------------------------------------
def bucket_sort(arr):
    if not arr: return arr
    n = len(arr)
    buckets = [[] for _ in range(n)]
    for v in arr:
        idx = int(v * n)            # assumes 0 <= v < 1
        buckets[idx].append(v)
    for b in buckets:
        b.sort()                    # insertion sort inside each bucket
    return [v for b in buckets for v in b]

floats = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
print("Bucket:", bucket_sort(floats))

# ---------------------------------------------
# 11. TIM SORT (Python's built-in)  O(n log n) | O(n)
#     Hybrid of Merge Sort + Insertion Sort
#     Used by list.sort() and sorted()
# ---------------------------------------------
data = [5, 2, 4, 6, 1, 3]
print("Tim (sorted):", sorted(data))
data.sort()
print("Tim (in-place):", data)

# ---------------------------------------------
# COMPLEXITY SUMMARY
# ---------------------------------------------
print("""
Algorithm       | Best       | Avg        | Worst      | Space  | Stable
----------------+------------+------------+------------+--------+-------
Bubble          | O(n)       | O(n²)      | O(n²)      | O(1)   | [Y]
Selection       | O(n²)      | O(n²)      | O(n²)      | O(1)   | X
Insertion       | O(n)       | O(n²)      | O(n²)      | O(1)   | [Y]
Shell           | O(n log n) | ~O(n^1.5)  | O(n²)      | O(1)   | X
Merge           | O(n log n) | O(n log n) | O(n log n) | O(n)   | [Y]
Quick           | O(n log n) | O(n log n) | O(n²)      | O(logn)| X
Heap            | O(n log n) | O(n log n) | O(n log n) | O(1)   | X
Counting        | O(n+k)     | O(n+k)     | O(n+k)     | O(k)   | [Y]
Radix           | O(d*n)     | O(d*n)     | O(d*n)     | O(n+k) | [Y]
Bucket          | O(n+k)     | O(n+k)     | O(n²)      | O(n+k) | [Y]
Tim             | O(n)       | O(n log n) | O(n log n) | O(n)   | [Y]
""")
