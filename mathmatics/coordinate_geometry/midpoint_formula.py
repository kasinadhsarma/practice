class midpoint_formula:
    # the point exactly halfway between two points — simply the average
    # of their x-coordinates and the average of their y-coordinates
    # time complexity O(1), space O(1)
    def calculate(self,point1:tuple,point2:tuple)->tuple:
        x1, y1 = point1
        x2, y2 = point2
        return ((x1 + x2) / 2, (y1 + y2) / 2)

point1 = (2, 3)
point2 = (8, 7)
result = midpoint_formula().calculate(point1, point2)
print(result)
