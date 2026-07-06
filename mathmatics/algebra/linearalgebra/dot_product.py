class dot_product:
    def calculate(self,v1:list,v2:list)->float:
        if len(v1) != len(v2):
            return "Vectors must be the same length for a dot product"
        total = 0
        for i in range(len(v1)):
            total += v1[i] * v2[i]
        return total

v1 = [1, 2, 3]
v2 = [4, 5, 6]
result = dot_product().calculate(v1, v2)
print(result)
