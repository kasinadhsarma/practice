class NQueens:
    """
    Places N queens on an N x N chessboard so that no two attack each
    other (no shared row, column, or diagonal). Classic backtracking:
    place a queen in the current row, recurse to the next row, and
    backtrack (try the next column) whenever a placement leads nowhere.

    solve() -> list of solutions, each a list where index = row and
               value = column of that row's queen
    Steps
        1. Try each column in the current row.
        2. If safe (no conflict with queens already placed), place it
           and recurse to the next row.
        3. If a full board is filled, record the solution.
        4. Backtrack: remove the queen and try the next column.
    Time Complexity  : O(N!) worst case — pruned by the safety check
    Space Complexity : O(N)  — recursion depth + one row of placements
    """

    def __init__(self, n: int):
        self.n = n

    def _is_safe(self, placements: list, row: int, col: int) -> bool:
        for r, c in enumerate(placements):
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def solve(self) -> list:
        solutions = []
        self._backtrack([], 0, solutions)
        return solutions

    def _backtrack(self, placements: list, row: int, solutions: list):
        if row == self.n:
            solutions.append(placements[:])
            return
        for col in range(self.n):
            if self._is_safe(placements, row, col):
                placements.append(col)
                self._backtrack(placements, row + 1, solutions)
                placements.pop()

    def count_solutions(self) -> int:
        return len(self.solve())


n = int(input("Enter board size N: "))
nq = NQueens(n)
solutions = nq.solve()
print(f"Total solutions for N={n}: {len(solutions)}")
if solutions:
    print("First solution (row -> column):", solutions[0])
