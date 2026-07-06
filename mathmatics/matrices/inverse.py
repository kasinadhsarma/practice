class inverse:
    def _minor(self,matrix:list,skip_row:int,skip_col:int)->list:
        # drop skip_row and skip_col to build the minor for cofactor expansion
        rows = [row[:skip_col] + row[skip_col + 1:] for i, row in enumerate(matrix) if i != skip_row]
        return rows

    def _determinant(self,matrix:list)->float:
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        if n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        total = 0
        for col in range(n):
            sign = 1 if col % 2 == 0 else -1
            total += sign * matrix[0][col] * self._determinant(self._minor(matrix, 0, col))
        return total

    def calculate(self,matrix:list):
        n = len(matrix)
        det = self._determinant(matrix)
        if det == 0:
            return "Matrix is singular and has no inverse"
        if n == 1:
            return [[1 / matrix[0][0]]]
        # build the cofactor matrix
        cofactors = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                sign = 1 if (i + j) % 2 == 0 else -1
                cofactors[i][j] = sign * self._determinant(self._minor(matrix, i, j))
        # adjugate is the transpose of the cofactor matrix
        adjugate = [[cofactors[j][i] for j in range(n)] for i in range(n)]
        # inverse = adjugate / determinant
        return [[adjugate[i][j] / det for j in range(n)] for i in range(n)]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 10]]
result = inverse().calculate(matrix)
print(result)
