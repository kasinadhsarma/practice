class slope_and_line_equation:
    # slope: rise over run — how steeply the line climbs between two points
    #   m = (y2 - y1) / (x2 - x1)
    # slope_intercept_form: once you know m and one point, y = mx + b lets
    # you solve for b (the y-intercept) by substitution
    # time complexity O(1), space O(1)
    def slope(self,point1:tuple,point2:tuple)->float:
        x1, y1 = point1
        x2, y2 = point2
        if x2 == x1:
            return None  # vertical line — slope is undefined
        return (y2 - y1) / (x2 - x1)

    def slope_intercept_form(self,point1:tuple,point2:tuple)->tuple:
        m = self.slope(point1, point2)
        if m is None:
            return None
        x1, y1 = point1
        b = y1 - m * x1
        return (m, b)  # y = m*x + b

point1 = (1, 2)
point2 = (4, 11)
sle = slope_and_line_equation()
result = (sle.slope(point1, point2), sle.slope_intercept_form(point1, point2))
print(result)
