class circularring:
    # area of circular ring is pi * (R^2 - r^2)
    # here time complexity is O(1) - constant time complexity
    # here space complexity is O(1) - constant space complexity
    
    def __init__(self, R , r):
        self.R = R
        self.r = r
    def get_area(self):
        return 3.14 * (self.R * self.R - self.r * self.r)


R = int(input("enter the outer radius of the circular ring: "))
r = int(input("enter the inner radius of the circular ring: "))
ring = circularring(R,r)
print("the area of the circular ring is: ",ring.get_area())