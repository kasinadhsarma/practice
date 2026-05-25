import math
class rightcircularcone:
    # here volume of right circular cone is (1/3) * pi * r^2 * h
    # time complexity is O(1) - constant time complexity
    # space complexity is O(1) - constant space complexity
    
    def __init__(self, r , h):
        self.r = r
        self.h = h
    def get_volume(self):
        return (1/3) * math.pi * self.r * self.r * self.h


r = int(input("enter the radius of the right circular cone: "))
h = int(input("enter the height of the right circular cone: "))
rightcircularcone = rightcircularcone(r,h)
print("the volume of the right circular cone is: ",rightcircularcone.get_volume())