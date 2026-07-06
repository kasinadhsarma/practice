class identity:
    def generate(self,n:int)->list:
        # build an n x n matrix with 1s on the diagonal and 0s elsewhere
        result = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            result[i][i] = 1
        return result

n = 4
result = identity().generate(n)
print(result)
