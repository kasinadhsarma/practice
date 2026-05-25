class Square:
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side * self.side

# Get user input (a square only needs one side length)
side_input = int(input("enter the side length of the square: "))

# Create object (Object-Oriented approach)
sq = Square(side_input)

# Display result
print("the area of the square is:", sq.get_area())
