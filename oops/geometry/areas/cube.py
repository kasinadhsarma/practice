class cube:
    # here area of cube = 6*a*a
    # here time complexity is O(1) - constant time complexity
    # here space complexity is O(1) - constant space complexity
    
    def __init__(self,a):
        self.a = a
    def get_area(self):
        return 6*self.a*self.a


a = int(input("enter the side of the cube: "))
cube = cube(a)
print("the area of the cube is: ",cube.get_area())