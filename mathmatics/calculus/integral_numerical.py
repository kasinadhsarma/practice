class integral_numerical:
    # approximates the definite integral (area under the curve) using the
    # trapezoidal rule: split [a, b] into N slices and approximate each
    # slice as a trapezoid instead of a rectangle, which tracks a curving
    # function much more closely than a naive rectangle sum
    # time complexity O(N), space O(1)
    def calculate(self,f,a:float,b:float,n:int=1000)->float:
        h = (b - a) / n
        total = (f(a) + f(b)) / 2
        for i in range(1, n):
            total += f(a + i * h)
        return total * h

f = lambda x: x ** 2  # integral of x^2 from 0 to 3 = 9
a, b = 0, 3
result = integral_numerical().calculate(f, a, b)
print(result)
