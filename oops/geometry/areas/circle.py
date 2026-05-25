import math
class areaofcircle:
    # here formula of area is pi*r*r
    # here time complexity is O(1) - constant time complexity
    # here space complexity is O(1) - constant space complexity
    def __init__(self,radius):
        self.radius = radius
    def get_area(self):
        return math.pi*self.radius*self.radius


radius = int(input("enter the radius of the circle: "))
circle = areaofcircle(radius)
print("the area of the circle is: ",circle.get_area())