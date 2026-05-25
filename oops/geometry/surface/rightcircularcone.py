class rightcircularcone:
    # s = root of r^2  + h^2
    # surface area = pi * r * r + pi * r * s
    # time complexity is O(1) - constant time complexity
    # space complexity is O(1) - constant space complexity
    
    def __init__(self, r , h):
        self.r = r
        self.h = h
    def get_surface_area(self):
        s = (self.r * self.r + self.h * self.h) ** 0.5
        return 3.14 * self.r * self.r + 3.14 * self.r * s  


r = int(input("enter the radius of the right circular cone: "))
h = int(input("enter the height of the right circular cone: "))
rightcircularcone = rightcircularcone(r,h)
print("the surface area of the right circular cone is: ",rightcircularcone.get_surface_area())
