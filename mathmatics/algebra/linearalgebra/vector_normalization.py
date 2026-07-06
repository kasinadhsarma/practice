class vector_normalization:
    def normalize(self,vector:list)->list:
        magnitude = sum(component ** 2 for component in vector) ** 0.5
        if magnitude == 0:
            return "Cannot normalize the zero vector"
        return [component / magnitude for component in vector]

vector = [3, 4]
result = vector_normalization().normalize(vector)
print(result)
