class cross_product:
    def calculate(self,v1:list,v2:list)->list:
        if len(v1) != 3 or len(v2) != 3:
            return "Cross product is only defined for 3D vectors"
        x = v1[1] * v2[2] - v1[2] * v2[1]
        y = v1[2] * v2[0] - v1[0] * v2[2]
        z = v1[0] * v2[1] - v1[1] * v2[0]
        return [x, y, z]

v1 = [1, 0, 0]
v2 = [0, 1, 0]
result = cross_product().calculate(v1, v2)
print(result)
