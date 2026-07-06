class vector_subtraction:
    def subtract(self,v1:list,v2:list)->list:
        if len(v1) != len(v2):
            return "Vectors must be the same length to subtract"
        return [v1[i] - v2[i] for i in range(len(v1))]

v1 = [4, 5, 6]
v2 = [1, 2, 3]
result = vector_subtraction().subtract(v1, v2)
print(result)
