import math

class pythagorean_identity:
    # the identity sin^2(theta) + cos^2(theta) = 1 holds for every angle —
    # it's just the Pythagorean theorem applied to the unit circle
    # time complexity O(1), space O(1)
    def verify(self,angle_degrees:float)->bool:
        radians = math.radians(angle_degrees)
        value = math.sin(radians) ** 2 + math.cos(radians) ** 2
        return math.isclose(value, 1.0, abs_tol=1e-9)

angle_degrees = 37
result = pythagorean_identity().verify(angle_degrees)
print(result)
