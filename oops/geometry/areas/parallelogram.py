class areaofparallelogram:
    # formula of parallelogram is base * height
    # here time complexity is O(1) - constant time complexity
    # here space complexity is O(1) - constant time complexity
    
    def __init__(self,base , height):
        self.base = base
        self.height = height
    def get_area(self):
        return self.base * self.height


base = int(input("enter the base of the parallelogram: "))
height = int(input("enter the height of the parallelogram: "))
parallelogram = areaofparallelogram(base,height)
print("the area of the parallelogram is: ",parallelogram.get_area())
