class GridPaths:
    """
    Counts the number of paths from the top-left to the bottom-right
    corner of a grid, moving only right or down, while avoiding
    obstacles. Backtracking explores both moves from each cell and lets
    the recursion naturally "undo" a dead-end by simply returning 0 and
    trying the other direction from the caller.

    count_paths() -> number of valid right/down paths avoiding obstacles
                     (grid cell value 1 = obstacle, 0 = open)
    Steps
        1. Out of bounds or an obstacle -> 0 paths from here.
        2. Reached the bottom-right corner -> 1 valid path found.
        3. Otherwise, total paths = paths(move right) + paths(move down).
    Time Complexity  : O(2^(rows+cols)) worst case without memoisation
    Space Complexity : O(rows + cols) — recursion depth
    """

    def __init__(self, grid: list):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if grid else 0

    def count_paths(self) -> int:
        return self._count(0, 0)

    def _count(self, r: int, c: int) -> int:
        if r >= self.rows or c >= self.cols or self.grid[r][c] == 1:
            return 0
        if r == self.rows - 1 and c == self.cols - 1:
            return 1
        return self._count(r + 1, c) + self._count(r, c + 1)


rows = int(input("Enter number of rows: "))
grid = [list(map(int, input(f"Enter row {i + 1} (0=open 1=obstacle) separated by space: ").split())) for i in range(rows)]
print("Total paths:", GridPaths(grid).count_paths())
