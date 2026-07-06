class trace:
    def calculate(self,matrix:list)->float:
        # check the matrix is square
        rows = len(matrix)
        cols = len(matrix[0])
        if rows != cols:
            return "Trace is only defined for square matrices"
        # sum the diagonal elements
        total = 0
        for i in range(rows):
            total += matrix[i][i]
        return total

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = trace().calculate(matrix)
print(result)
