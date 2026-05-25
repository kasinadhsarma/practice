class triangle:

    # formula of triangle is height * base / 2
    # here time complexity is O(1) - constant time complexity
    # here space complexity is O(1) - constant space complexity

    def __init__(self, base , height):
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5*self.base*self.height


base = int(input("enter the base of the triangle: "))
height = int(input("enter the height of the triangle: "))

tri = triangle(base,height)

print("the area of the triangle is: ",tri.get_area())