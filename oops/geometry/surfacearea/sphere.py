import math
class sphere:
    # here surface area of sphere is 4 * pi * r^2
    # time complexity is O(1) - constant time complexity
    # space complexity is O(1) - constant space complexity
    
    def __init__(self, r):
        self.r = r
    def get_surface_area(self):
        return 4 * math.pi * self.r * self.r


r = int(input("enter the radius of the sphere: "))
sphere = sphere(r)
print("the surface area of the sphere is: ",sphere.get_surface_area())