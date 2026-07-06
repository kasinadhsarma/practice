class cramers_rule:
    def _determinant(self,matrix:list)->float:
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        if n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        total = 0
        for col in range(n):
            minor = [row[:col] + row[col + 1:] for row in matrix[1:]]
            sign = 1 if col % 2 == 0 else -1
            total += sign * matrix[0][col] * self._determinant(minor)
        return total

    def solve(self,coefficients:list,constants:list):
        n = len(coefficients)
        det = self._determinant(coefficients)
        if det == 0:
            return "System has no unique solution"
        solution = []
        for col in range(n):
            # replace column `col` with the constants vector
            modified = [row[:] for row in coefficients]
            for row in range(n):
                modified[row][col] = constants[row]
            solution.append(self._determinant(modified) / det)
        return solution

coefficients = [[2, 1], [1, 3]]
constants = [5, 10]
result = cramers_rule().solve(coefficients, constants)
print(result)
