import math

class Vector2D:
    # Represents a 2D Vector with x and y coordinates
    # Encapsulates physical/geometric attributes: Magnitude and Direction Angle
    # Time Complexity: O(1) constant time
    # Space Complexity: O(1) constant space
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_magnitude(self):
        # Magnitude (distance from origin) using Pythagorean Theorem: sqrt(x^2 + y^2)
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_direction_angle(self):
        # Calculates the angle in degrees relative to the positive X-axis
        # math.atan2(y, x) handles all quadrants correctly
        radian_angle = math.atan2(self.y, self.x)
        degree_angle = math.degrees(radian_angle)
        
        # Keep angle positive between 0 and 360 degrees
        if degree_angle < 0:
            degree_angle += 360
            
        return degree_angle


# Example Execution:
x_val = int(input("enter the X coordinate: "))
y_val = int(input("enter the Y coordinate: "))

vector = Vector2D(x_val, y_val)
print("Vector Magnitude (Length):", round(vector.get_magnitude(), 2))
print("Vector Direction (Angle in Degrees):", round(vector.get_direction_angle(), 2))
