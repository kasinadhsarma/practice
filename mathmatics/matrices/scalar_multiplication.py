class scalar_multiplication:
    def multiply(self,matrix:list,scalar:float)->list:
        # get the dimensions of the matrix
        rows = len(matrix)
        cols = len(matrix[0])
        # create the result matrix
        result = [[0 for _ in range(cols)] for _ in range(rows)]
        # scale every element
        for i in range(rows):
            for j in range(cols):
                result[i][j] = matrix[i][j] * scalar
        return result

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
scalar = 3
result = scalar_multiplication().multiply(matrix, scalar)
print(result)
