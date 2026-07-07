class derivative_numerical:
    # approximates f'(x) using the central difference formula:
    #   f'(x) ~= (f(x+h) - f(x-h)) / (2h)
    # centering the difference around x (rather than a one-sided
    # (f(x+h)-f(x))/h) cancels the first-order error term, giving a much
    # more accurate estimate for the same step size h
    # time complexity O(1) per call (two evaluations of f), space O(1)
    def calculate(self,f,x:float,h:float=1e-5)->float:
        return (f(x + h) - f(x - h)) / (2 * h)

f = lambda x: x ** 2  # f(x) = x^2, so f'(x) = 2x
x = 3
result = derivative_numerical().calculate(f, x)
print(result)
