class circle_equation:
    # standard form: (x - h)^2 + (y - k)^2 = r^2, for a circle centered at
    # (h, k) with radius r. Plugging a point into the left-hand side and
    # comparing it to r^2 tells you where that point sits relative to the
    # circle: equal -> on it, less -> inside, greater -> outside.
    # time complexity O(1), space O(1)
    def classify_point(self,point:tuple,center:tuple,radius:float)->str:
        x, y = point
        h, k = center
        lhs = (x - h) ** 2 + (y - k) ** 2
        rhs = radius ** 2
        if lhs == rhs:
            return "on"
        return "inside" if lhs < rhs else "outside"

point = (3, 4)
center = (0, 0)
radius = 5
result = circle_equation().classify_point(point, center, radius)
print(result)
