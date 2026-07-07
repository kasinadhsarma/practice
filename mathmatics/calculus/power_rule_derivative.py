class power_rule_derivative:
    # symbolic differentiation of a polynomial, coefficient list lowest
    # degree first: [c0, c1, c2, ...] means c0 + c1*x + c2*x^2 + ...
    # power rule: d/dx(c * x^n) = c*n * x^(n-1)
    # the constant term (degree 0) always vanishes
    # time complexity O(N), space O(N)
    def calculate(self,coefficients:list)->list:
        if len(coefficients) <= 1:
            return [0]
        return [coefficients[power] * power for power in range(1, len(coefficients))]

polynomial = [5, 3, 4, 2]  # 5 + 3x + 4x^2 + 2x^3
result = power_rule_derivative().calculate(polynomial)
print(result)  # 3 + 8x + 6x^2
