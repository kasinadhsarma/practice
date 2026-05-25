import math
class sphere:
    # volume of sphere is (4/3) * pi * r^3
    # time complexity is O(1) - constant time complexity
    # space complexity is O(1) - constant space complexity
    
    def __init__(self, r):
        self.r = r
    def get_volume(self):
        return (4/3) * math.pi * self.r * self.r * self.r


r = int(input("enter the radius of the sphere: "))
sphere = sphere(r)
print("the volume of the sphere is: ",sphere.get_volume())