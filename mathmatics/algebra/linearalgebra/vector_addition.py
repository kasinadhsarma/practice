class vector_addition:
    def add(self,v1:list,v2:list)->list:
        if len(v1) != len(v2):
            return "Vectors must be the same length to add"
        return [v1[i] + v2[i] for i in range(len(v1))]

v1 = [1, 2, 3]
v2 = [4, 5, 6]
result = vector_addition().add(v1, v2)
print(result)
