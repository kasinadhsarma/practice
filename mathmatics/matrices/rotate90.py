class rotate90:
    def clockwise(self,matrix:list)->list:
        # get the dimensions of the matrix
        rows = len(matrix)
        cols = len(matrix[0])
        # rotated matrix has swapped dimensions
        result = [[0 for _ in range(rows)] for _ in range(cols)]
        # element at (i, j) moves to (j, rows - 1 - i)
        for i in range(rows):
            for j in range(cols):
                result[j][rows - 1 - i] = matrix[i][j]
        return result

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = rotate90().clockwise(matrix)
print(result)
