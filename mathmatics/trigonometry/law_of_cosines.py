import math

class law_of_cosines:
    # generalizes the Pythagorean theorem to any triangle:
    #   c^2 = a^2 + b^2 - 2ab * cos(C)
    # find_side:  solve for the side opposite a known angle
    # find_angle: rearrange to solve for the angle opposite a known side
    # time complexity O(1), space O(1)
    def find_side(self,a:float,b:float,angle_c_degrees:float)->float:
        angle_c = math.radians(angle_c_degrees)
        c_squared = a ** 2 + b ** 2 - 2 * a * b * math.cos(angle_c)
        return math.sqrt(c_squared)

    def find_angle(self,a:float,b:float,c:float)->float:
        cos_c = (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)
        return math.degrees(math.acos(cos_c))

a, b, angle_c_degrees = 7, 10, 60
loc = law_of_cosines()
side_c = loc.find_side(a, b, angle_c_degrees)
result = (side_c, loc.find_angle(a, b, side_c))
print(result)
