import math

class unit_circle:
    # every angle maps to a point (cos(theta), sin(theta)) on the circle of
    # radius 1 centered at the origin — the definition that extends sin/cos
    # beyond right-triangle angles (0-90 degrees) to all angles
    # time complexity O(1), space O(1)
    def coordinates(self,angle_degrees:float)->tuple:
        radians = math.radians(angle_degrees)
        return (math.cos(radians), math.sin(radians))

angle_degrees = 60
result = unit_circle().coordinates(angle_degrees)
print(result)
