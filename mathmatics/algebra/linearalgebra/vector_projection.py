class vector_projection:
    def project(self,a:list,b:list)->list:
        # projects vector a onto vector b
        dot = sum(a[i] * b[i] for i in range(len(a)))
        b_mag_sq = sum(component ** 2 for component in b)
        if b_mag_sq == 0:
            return "Cannot project onto the zero vector"
        scalar = dot / b_mag_sq
        return [scalar * component for component in b]

a = [3, 4]
b = [1, 0]
result = vector_projection().project(a, b)
print(result)
