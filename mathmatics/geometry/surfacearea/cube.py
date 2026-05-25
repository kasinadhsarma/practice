class cube:
    # here surface area of cube is 6 * s^2
    # time complexity is O(1) - constant time complexity
    # space complexity is O(1) - constant space complexity
    
    def __init__(self, s):
        self.s = s
    def get_surface_area(self):
        return 6 * self.s * self.s
        
s = int(input("enter the side of the cube: "))
cube = cube(s)
print("the surface area of the cube is: ",cube.get_surface_area())
