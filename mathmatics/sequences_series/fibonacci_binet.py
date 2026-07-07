import math

class fibonacci_binet:
    # Binet's formula gives the nth Fibonacci number directly, with no
    # recursion or loop, using the golden ratio phi = (1 + sqrt(5)) / 2:
    #   F(n) = (phi^n - psi^n) / sqrt(5),  where psi = (1 - sqrt(5)) / 2
    # psi^n shrinks toward 0 as n grows, so rounding the result recovers
    # the exact integer despite the floating-point irrational terms
    # time complexity O(1) (via pow), space O(1)
    def calculate(self,n:int)->int:
        sqrt5 = math.sqrt(5)
        phi = (1 + sqrt5) / 2
        psi = (1 - sqrt5) / 2
        return round((phi ** n - psi ** n) / sqrt5)

n = 10
result = fibonacci_binet().calculate(n)
print(result)
