class summation_formulas:
    # closed-form shortcuts for three classic sums over 1..n, so the total
    # is computed in O(1) instead of actually looping n times:
    #   sum_natural_numbers: n(n+1)/2
    #   sum_of_squares:      n(n+1)(2n+1)/6
    #   sum_of_cubes:        (n(n+1)/2)^2   — notably, the square of the
    #                        sum of naturals
    # time complexity O(1), space O(1)
    def sum_natural_numbers(self,n:int)->int:
        return n * (n + 1) // 2

    def sum_of_squares(self,n:int)->int:
        return n * (n + 1) * (2 * n + 1) // 6

    def sum_of_cubes(self,n:int)->int:
        return (n * (n + 1) // 2) ** 2

n = 5
sf = summation_formulas()
result = (sf.sum_natural_numbers(n), sf.sum_of_squares(n), sf.sum_of_cubes(n))
print(result)
