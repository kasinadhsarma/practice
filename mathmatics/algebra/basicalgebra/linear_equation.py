class linear_equation:
    # solves ax + b = 0 for a single variable: x = -b / a
    # time complexity O(1), space O(1)
    def solve(self,a:float,b:float)->float:
        if a == 0:
            return None  # no unique solution — either no solution or infinite solutions
        return -b / a

a = 2
b = -10
result = linear_equation().solve(a, b)
print(result)
