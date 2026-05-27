"""
======================================================
  ARRAYS IN DSA — PART 1: BASICS & FUNDAMENTALS
======================================================
  Topics:
    1. Array creation & types
    2. Memory layout (row-major / col-major)
    3. Basic operations: traverse, access, insert, delete, update, search
    4. Static vs Dynamic arrays
    5. Time & Space complexity cheat-sheet
"""

# ---------------------------------------------
# 1. ARRAY CREATION
# ---------------------------------------------

# 1D Array (Python list)
arr1d = [10, 20, 30, 40, 50]

# 2D Array (matrix)
arr2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 3D Array
arr3d = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

# Using array module (typed, fixed-type)
import array
typed_arr = array.array('i', [1, 2, 3, 4, 5])   # 'i' = signed int

# Using numpy (numerical arrays)
# import numpy as np
# np_arr = np.array([1, 2, 3, 4, 5])

print("1D:", arr1d)
print("2D:", arr2d)
print("3D:", arr3d)

# ---------------------------------------------
# 2. MEMORY LAYOUT
# ---------------------------------------------
# Row-major (C, Python):  row stored contiguously
#   arr[i][j] -> base + (i*cols + j) * size
#
# Col-major (Fortran, MATLAB):  column stored contiguously
#   arr[i][j] -> base + (j*rows + i) * size
#
# For 2D arr[3][3] (row-major):
#   Index formula: base + (r*3 + c) * element_size

rows, cols = 3, 3
def row_major_index(r, c, num_cols):
    return r * num_cols + c

print("\nRow-major index of [1][2]:", row_major_index(1, 2, cols))  # -> 5

# ---------------------------------------------
# 3. BASIC OPERATIONS
# ---------------------------------------------

arr = [10, 20, 30, 40, 50]

# 3a. TRAVERSE  O(n)
print("\n--- Traverse ---")
for elem in arr:
    print(elem, end=" ")
print()

# 3b. ACCESS  O(1)
print("\n--- Access ---")
print("arr[0] =", arr[0])
print("arr[-1] =", arr[-1])   # last element
print("arr[1:4] =", arr[1:4]) # slicing O(k)

# 3c. UPDATE  O(1)
arr[2] = 99
print("\n--- Update arr[2]=99 ---", arr)

# 3d. INSERT  O(n) worst-case (shift), O(1) amortized at end
arr.append(60)          # insert at end  O(1) amortized
arr.insert(0, 5)        # insert at index 0  O(n)
print("\n--- Insert ---", arr)

# 3e. DELETE  O(n) worst-case
arr.pop()               # remove last  O(1)
arr.pop(0)              # remove at index 0  O(n)
arr.remove(99)          # remove first occurrence of value  O(n)
print("\n--- Delete ---", arr)

# 3f. LINEAR SEARCH  O(n)
def linear_search(arr, target):
    for i, v in enumerate(arr):
        if v == target:
            return i
    return -1

print("\n--- Linear Search ---")
print("Found 40 at index:", linear_search(arr, 40))

# ---------------------------------------------
# 4. STATIC vs DYNAMIC ARRAYS
# ---------------------------------------------
# Static  : fixed size at compile time (e.g., C int arr[10])
# Dynamic : resize automatically (Python list, C++ vector)
#
# Python list is a DYNAMIC array:
#   - internally holds a pointer array
#   - when full, allocates ~2x space and copies  -> amortized O(1) append

import sys
dyn = []
for i in range(6):
    dyn.append(i)
    print(f"len={len(dyn)}, sys.getsizeof={sys.getsizeof(dyn)} bytes")

# ---------------------------------------------
# 5. TIME & SPACE COMPLEXITY CHEAT-SHEET
# ---------------------------------------------
complexity = """
Operation           | Time (avg)  | Time (worst) | Space
--------------------+-------------+--------------+-------
Access  arr[i]      | O(1)        | O(1)         | O(1)
Update  arr[i]=x    | O(1)        | O(1)         | O(1)
Append  (end)       | O(1)*       | O(n)         | O(1)
Insert  (middle)    | O(n)        | O(n)         | O(1)
Delete  (end)       | O(1)        | O(1)         | O(1)
Delete  (middle)    | O(n)        | O(n)         | O(1)
Linear Search       | O(n)        | O(n)         | O(1)
Binary Search       | O(log n)    | O(log n)     | O(1)
Traverse            | O(n)        | O(n)         | O(1)
Slice [l:r]         | O(k)        | O(n)         | O(k)

* amortized; individual append can be O(n) on resize
"""
print(complexity)
