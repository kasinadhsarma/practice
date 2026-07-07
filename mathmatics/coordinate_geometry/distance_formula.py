import math

class distance_formula:
    # straight-line distance between two points — the Pythagorean theorem
    # applied to the horizontal and vertical legs between them:
    #   d = sqrt((x2-x1)^2 + (y2-y1)^2)
    # time complexity O(1), space O(1)
    def calculate(self,point1:tuple,point2:tuple)->float:
        x1, y1 = point1
        x2, y2 = point2
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

point1 = (0, 0)
point2 = (3, 4)
result = distance_formula().calculate(point1, point2)
print(result)
