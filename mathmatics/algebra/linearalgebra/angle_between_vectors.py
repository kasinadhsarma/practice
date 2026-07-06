import math

class angle_between_vectors:
    def calculate(self,v1:list,v2:list)->float:
        dot = sum(v1[i] * v2[i] for i in range(len(v1)))
        mag1 = sum(component ** 2 for component in v1) ** 0.5
        mag2 = sum(component ** 2 for component in v2) ** 0.5
        if mag1 == 0 or mag2 == 0:
            return "Angle is undefined for a zero vector"
        cos_theta = dot / (mag1 * mag2)
        # clamp to [-1, 1] to avoid a math domain error from float rounding
        cos_theta = max(-1.0, min(1.0, cos_theta))
        return math.degrees(math.acos(cos_theta))

v1 = [1, 0]
v2 = [0, 1]
result = angle_between_vectors().calculate(v1, v2)
print(result)
