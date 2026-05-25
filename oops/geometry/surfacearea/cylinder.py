import math
class cylinder:
    # here surface area of cylinder is 2 * pi * r * (h + r)
    # time complexity is O(1) - constant time complexity
    # space complexity is O(1) - constant space complexity
    
    def __init__(self, r , h):
        self.r = r
        self.h = h
    def get_surface_area(self):
        return 2 * math.pi * self.r * (self.h + self.r)


r = int(input("enter the radius of the cylinder: "))
h = int(input("enter the height of the cylinder: "))
cylinder = cylinder(r,h)
print("the surface area of the cylinder is: ",cylinder.get_surface_area())