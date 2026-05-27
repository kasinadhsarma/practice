"""
======================================================
  ARRAYS IN DSA — PART 9: 2D ARRAYS / MATRICES
======================================================
  1.  Matrix creation & traversal
  2.  Row / Column / Diagonal traversal
  3.  Matrix transpose
  4.  Rotate 90° CW and CCW
  5.  Spiral traversal
  6.  Diagonal traversal (anti & main)
  7.  Search in row-wise & col-wise sorted matrix  O(m+n)
  8.  Word search in matrix (DFS backtracking)
  9.  Matrix multiplication  O(n³)
  10. Count islands (DFS / BFS)
  11. Flood fill
  12. Shortest path in binary matrix (BFS)
"""

from collections import deque

# ---------------------------------------------
# 1. MATRIX CREATION & TRAVERSAL
# ---------------------------------------------
m, n = 3, 4
matrix = [[i * n + j + 1 for j in range(n)] for i in range(m)]
print("Matrix:")
for row in matrix: print(row)

# ---------------------------------------------
# 2. ROW / COLUMN / MAIN-DIAGONAL TRAVERSAL
# ---------------------------------------------
print("\nRow-major:", [matrix[i][j] for i in range(m) for j in range(n)])
print("Col-major:", [matrix[i][j] for j in range(n) for i in range(m)])
print("Main diagonal:", [matrix[i][i] for i in range(min(m, n))])
print("Anti-diagonal:", [matrix[i][min(m,n)-1-i] for i in range(min(m, n))])

# ---------------------------------------------
# 3. TRANSPOSE (square matrix in-place)
# ---------------------------------------------
def transpose(mat):
    n = len(mat)
    for i in range(n):
        for j in range(i + 1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    return mat

sq = [[1,2,3],[4,5,6],[7,8,9]]
print("\nTranspose:", transpose([row[:] for row in sq]))

# ---------------------------------------------
# 4. ROTATE 90° CLOCKWISE & COUNTER-CLOCKWISE
# ---------------------------------------------
def rotate_cw(mat):
    """Transpose then reverse each row."""
    n = len(mat)
    a = [row[:] for row in mat]
    for i in range(n):
        for j in range(i+1, n):
            a[i][j], a[j][i] = a[j][i], a[i][j]
    for row in a: row.reverse()
    return a

def rotate_ccw(mat):
    """Transpose then reverse each column (reverse rows)."""
    n = len(mat)
    a = [row[:] for row in mat]
    for i in range(n):
        for j in range(i+1, n):
            a[i][j], a[j][i] = a[j][i], a[i][j]
    a.reverse()
    return a

print("\nRotate CW:", rotate_cw(sq))
print("Rotate CCW:", rotate_ccw(sq))

# ---------------------------------------------
# 5. SPIRAL TRAVERSAL  O(m*n)
# ---------------------------------------------
def spiral_order(matrix):
    result = []
    if not matrix: return result
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for c in range(left, right + 1):
            result.append(matrix[top][c])
        top += 1
        for r in range(top, bottom + 1):
            result.append(matrix[r][right])
        right -= 1
        if top <= bottom:
            for c in range(right, left - 1, -1):
                result.append(matrix[bottom][c])
            bottom -= 1
        if left <= right:
            for r in range(bottom, top - 1, -1):
                result.append(matrix[r][left])
            left += 1
    return result

mat5 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print("\nSpiral:", spiral_order(mat5))

# Generate n×n spiral matrix
def spiral_matrix_gen(n):
    mat = [[0]*n for _ in range(n)]
    top, bottom, left, right = 0, n-1, 0, n-1
    num = 1
    while top <= bottom and left <= right:
        for c in range(left, right+1):   mat[top][c] = num; num += 1
        top += 1
        for r in range(top, bottom+1):   mat[r][right] = num; num += 1
        right -= 1
        if top <= bottom:
            for c in range(right, left-1, -1): mat[bottom][c] = num; num += 1
            bottom -= 1
        if left <= right:
            for r in range(bottom, top-1, -1): mat[r][left] = num; num += 1
            left += 1
    return mat

print("Spiral 3×3:")
for row in spiral_matrix_gen(3): print(row)

# ---------------------------------------------
# 6. DIAGONAL TRAVERSAL (all diagonals)
# ---------------------------------------------
def diagonal_traverse(matrix):
    if not matrix: return []
    m, n = len(matrix), len(matrix[0])
    result = []
    diags = {}
    for i in range(m):
        for j in range(n):
            d = i + j
            if d not in diags: diags[d] = []
            diags[d].append(matrix[i][j])
    for d in sorted(diags):
        if d % 2 == 0: result.extend(reversed(diags[d]))
        else:          result.extend(diags[d])
    return result

print("\nDiagonal traverse [[1,2,3],[4,5,6],[7,8,9]]:",
      diagonal_traverse([[1,2,3],[4,5,6],[7,8,9]]))

# ---------------------------------------------
# 7. SEARCH IN ROW-WISE & COL-WISE SORTED MATRIX  O(m+n)
#    (staircase search — start top-right)
# ---------------------------------------------
def search_matrix(matrix, target):
    if not matrix: return False
    r, c = 0, len(matrix[0]) - 1
    while r < len(matrix) and c >= 0:
        if matrix[r][c] == target: return (r, c)
        elif matrix[r][c] > target: c -= 1
        else: r += 1
    return (-1, -1)

# Binary search in row+col sorted matrix where mat[i][j] < mat[i][j+1]
# and mat[m-1][j] < mat[m][0]  O(log(m*n))
def search_matrix_bs(matrix, target):
    m, n = len(matrix), len(matrix[0])
    lo, hi = 0, m * n - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        val = matrix[mid // n][mid % n]
        if val == target: return True
        elif val < target: lo = mid + 1
        else: hi = mid - 1
    return False

sorted_mat = [[1,4,7,11],[2,5,8,12],[3,6,9,16],[10,13,14,17]]
print("\nSearch 5 in sorted matrix:", search_matrix(sorted_mat, 5))
print("Search 20:", search_matrix(sorted_mat, 20))

# ---------------------------------------------
# 8. WORD SEARCH IN MATRIX (DFS + Backtrack)  O(m*n*4^L)
# ---------------------------------------------
def word_search(board, word):
    m, n = len(board), len(board[0])

    def dfs(r, c, idx):
        if idx == len(word): return True
        if r < 0 or r >= m or c < 0 or c >= n: return False
        if board[r][c] != word[idx]: return False
        tmp = board[r][c]
        board[r][c] = '#'          # mark visited
        found = (dfs(r+1,c,idx+1) or dfs(r-1,c,idx+1) or
                 dfs(r,c+1,idx+1) or dfs(r,c-1,idx+1))
        board[r][c] = tmp          # restore
        return found

    for i in range(m):
        for j in range(n):
            if dfs(i, j, 0): return True
    return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
print('\nWord search "ABCCED":', word_search(board, "ABCCED"))  # True
print('Word search "SEE":', word_search(board, "SEE"))          # True
print('Word search "ABCB":', word_search(board, "ABCB"))        # False

# ---------------------------------------------
# 9. MATRIX MULTIPLICATION  O(n³)
# ---------------------------------------------
def mat_mul(A, B):
    m, n, p = len(A), len(A[0]), len(B[0])
    C = [[0]*p for _ in range(m)]
    for i in range(m):
        for k in range(n):
            for j in range(p):
                C[i][j] += A[i][k] * B[k][j]
    return C

A = [[1,2],[3,4]]
B = [[5,6],[7,8]]
print("\nMatrix Multiply:", mat_mul(A, B))   # [[19,22],[43,50]]

# ---------------------------------------------
# 10. COUNT ISLANDS (DFS)  O(m*n)
# ---------------------------------------------
def count_islands(grid):
    if not grid: return 0
    m, n = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1':
            return
        grid[r][c] = '#'
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            dfs(r+dr, c+dc)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1
    return count

grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
print("\nCount Islands:", count_islands([row[:] for row in grid]))  # 3

# ---------------------------------------------
# 11. FLOOD FILL  O(m*n)
# ---------------------------------------------
def flood_fill(image, sr, sc, newColor):
    img = [row[:] for row in image]
    old = img[sr][sc]
    if old == newColor: return img
    def fill(r, c):
        if r < 0 or r >= len(img) or c < 0 or c >= len(img[0]): return
        if img[r][c] != old: return
        img[r][c] = newColor
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            fill(r+dr, c+dc)
    fill(sr, sc)
    return img

print("\nFlood Fill:")
for row in flood_fill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2): print(row)

# ---------------------------------------------
# 12. SHORTEST PATH IN BINARY MATRIX (BFS)  O(m*n)
#     0=open, 1=blocked; 8-directional
# ---------------------------------------------
def shortest_path_binary(grid):
    n = len(grid)
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1
    queue = deque([(0, 0, 1)])   # (row, col, dist)
    visited = set([(0, 0)])
    dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    while queue:
        r, c, dist = queue.popleft()
        if r == n-1 and c == n-1: return dist
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if 0 <= nr < n and 0 <= nc < n and (nr,nc) not in visited and grid[nr][nc] == 0:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
    return -1

g = [[0,0,0],[1,1,0],[1,1,0]]
print("\nShortest path:", shortest_path_binary(g))   # 4

print("\n[Y] 2D Arrays / Matrices Done!")
