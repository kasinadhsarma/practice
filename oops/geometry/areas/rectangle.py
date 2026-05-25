class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def get_area(self):
        return self.length * self.breadth

# Get user input
length_input = int(input("enter the length of the rectangle: "))
breadth_input = int(input("enter the bredth of the rectangle: "))

# Create object (Object-Oriented approach)
rect = Rectangle(length_input, breadth_input)

# Display result
print("the area of the rectangle is:", rect.get_area())
