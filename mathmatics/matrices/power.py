class power:
    def _multiply(self,a:list,b:list)->list:
        rows_a = len(a)
        cols_a = len(a[0])
        cols_b = len(b[0])
        result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
        for i in range(rows_a):
            for j in range(cols_b):
                for k in range(cols_a):
                    result[i][j] += a[i][k] * b[k][j]
        return result

    def calculate(self,matrix:list,n:int)->list:
        size = len(matrix)
        if n < 0:
            return "Only non-negative integer powers are supported"
        # any square matrix to the power of 0 is the identity matrix
        result = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
        for _ in range(n):
            result = self._multiply(result, matrix)
        return result

matrix = [[1, 1], [1, 0]]
n = 5
result = power().calculate(matrix, n)
print(result)
