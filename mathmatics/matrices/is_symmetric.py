class is_symmetric:
    def check(self,matrix:list)->bool:
        # a symmetric matrix must be square
        rows = len(matrix)
        cols = len(matrix[0])
        if rows != cols:
            return False
        # a matrix is symmetric when it equals its own transpose
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] != matrix[j][i]:
                    return False
        return True

matrix = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]
result = is_symmetric().check(matrix)
print(result)
