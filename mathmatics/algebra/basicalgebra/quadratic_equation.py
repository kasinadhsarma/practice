import cmath

class quadratic_equation:
    # solves ax^2 + bx + c = 0 via the quadratic formula:
    #   x = (-b +/- sqrt(b^2 - 4ac)) / 2a
    # uses cmath so complex roots (negative discriminant) come out naturally
    # instead of raising an error
    # time complexity O(1), space O(1)
    def solve(self,a:float,b:float,c:float)->tuple:
        if a == 0:
            return None  # not quadratic — degenerates to a linear equation
        discriminant = (b ** 2) - (4 * a * c)
        sqrt_disc = cmath.sqrt(discriminant)
        root1 = (-b + sqrt_disc) / (2 * a)
        root2 = (-b - sqrt_disc) / (2 * a)
        return (root1, root2)

a, b, c = 1, -3, 2
result = quadratic_equation().solve(a, b, c)
print(result)
