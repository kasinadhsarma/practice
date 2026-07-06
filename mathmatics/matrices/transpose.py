class transpose:
    def get_transpose(self,matrix:list)->list:
        # get the dimensions of the matrix
        rows = len(matrix)
        cols = len(matrix[0])
        # create the result matrix with swapped dimensions
        result = [[0 for _ in range(rows)] for _ in range(cols)]
        # flip rows and columns
        for i in range(rows):
            for j in range(cols):
                result[j][i] = matrix[i][j]
        return result

matrix = [[1, 2, 3], [4, 5, 6]]
result = transpose().get_transpose(matrix)
print(result)
