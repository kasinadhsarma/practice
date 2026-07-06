class vector_magnitude:
    def calculate(self,vector:list)->float:
        return sum(component ** 2 for component in vector) ** 0.5

vector = [3, 4]
result = vector_magnitude().calculate(vector)
print(result)
