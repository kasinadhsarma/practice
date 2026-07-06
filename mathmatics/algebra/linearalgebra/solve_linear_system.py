class solve_linear_system:
    def solve(self,coefficients:list,constants:list):
        n = len(coefficients)
        # build the augmented matrix [A | b]
        augmented = [row[:] + [constants[i]] for i, row in enumerate(coefficients)]

        # forward elimination with partial pivoting
        for col in range(n):
            pivot_row = None
            for r in range(col, n):
                if abs(augmented[r][col]) > 1e-9:
                    pivot_row = r
                    break
            if pivot_row is None:
                return "System has no unique solution"
            augmented[col], augmented[pivot_row] = augmented[pivot_row], augmented[col]
            for r in range(col + 1, n):
                factor = augmented[r][col] / augmented[col][col]
                for c in range(col, n + 1):
                    augmented[r][c] -= factor * augmented[col][c]

        # back substitution
        solution = [0] * n
        for i in range(n - 1, -1, -1):
            total = augmented[i][n]
            for j in range(i + 1, n):
                total -= augmented[i][j] * solution[j]
            solution[i] = total / augmented[i][i]
        return solution

coefficients = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
constants = [8, -11, -3]
result = solve_linear_system().solve(coefficients, constants)
print(result)
