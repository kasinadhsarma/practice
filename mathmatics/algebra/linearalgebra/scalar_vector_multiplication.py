class scalar_vector_multiplication:
    def multiply(self,vector:list,scalar:float)->list:
        return [component * scalar for component in vector]

vector = [1, 2, 3]
scalar = 3
result = scalar_vector_multiplication().multiply(vector, scalar)
print(result)
