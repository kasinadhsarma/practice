class determinant:
    def _minor(self,matrix:list,skip_col:int)->list:
        # drop row 0 and column skip_col to build the minor for cofactor expansion
        return [row[:skip_col] + row[skip_col + 1:] for row in matrix[1:]]

    def calculate(self,matrix:list)->float:
        n = len(matrix)
        # base case: 1x1 matrix
        if n == 1:
            return matrix[0][0]
        # base case: 2x2 matrix
        if n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        # recursive case: expand along the first row
        total = 0
        for col in range(n):
            sign = 1 if col % 2 == 0 else -1
            total += sign * matrix[0][col] * self.calculate(self._minor(matrix, col))
        return total

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 10]]
result = determinant().calculate(matrix)
print(result)
