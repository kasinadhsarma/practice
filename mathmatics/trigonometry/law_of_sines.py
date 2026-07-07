import math

class law_of_sines:
    # in any triangle, each side's length is proportional to the sine of
    # its opposite angle:  a / sin(A) = b / sin(B) = c / sin(C)
    # given one full ratio (a, angle_A) plus another angle, this solves
    # for the side opposite that angle
    # time complexity O(1), space O(1)
    def find_side(self,known_side:float,known_angle_degrees:float,target_angle_degrees:float)->float:
        known_angle = math.radians(known_angle_degrees)
        target_angle = math.radians(target_angle_degrees)
        ratio = known_side / math.sin(known_angle)
        return ratio * math.sin(target_angle)

known_side = 10
known_angle_degrees = 30
target_angle_degrees = 45
result = law_of_sines().find_side(known_side, known_angle_degrees, target_angle_degrees)
print(result)
