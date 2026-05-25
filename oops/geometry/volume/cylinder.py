import math
class cylinder:
    # volume of cylinder is 4/3 *pi*r^3
    # time complexity of the function is O(1) - constant time complexity
    # space complexity of the function is O(1) - constant space complexity
    
    def __init__(self, r):
        self.r = r
    def get_volume(self):
        return (4/3) * math.pi * self.r * self.r * self.r


r = int(input("enter the radius of the cylinder: "))
cylinder = cylinder(r)
print("the volume of the cylinder is: ",cylinder.get_volume())