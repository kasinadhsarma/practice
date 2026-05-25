import math
class rightcurclularcode:
    # here surface area of right circular cone is pi * r^2 + pi * r * s
    # where s = slant height = sqrt(r^2 + h^2)
    # here time complexity is O(1) - constant time complexity
    # here space complexity is O(1) - constant space complexity

    def __init__(self, r , h):
        self.r = r
        self.h = h
        self.s = math.sqrt(self.r * self.r + self.h * self.h)   # slant height
    def get_surface_area(self):
        return math.pi * self.r * self.r + math.pi * self.r * self.s


r = int(input("enter the radius of the right circular cone: "))
h = int(input("enter the height of the right circular cone: "))
rightcurclularcode = rightcurclularcode(r,h)
print("the surface area of the right circular cone is: ",rightcurclularcode.get_surface_area())