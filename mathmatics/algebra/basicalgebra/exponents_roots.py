class exponents_roots:
    # power: repeated multiplication generalized to any real exponent
    # nth_root: the inverse of raising to the nth power — x^(1/n)
    # time complexity O(1) (delegates to Python's built-in pow), space O(1)
    def power(self,base:float,exponent:float)->float:
        return base ** exponent

    def nth_root(self,x:float,n:int)->float:
        if x < 0 and n % 2 == 0:
            return None  # even root of a negative number isn't real
        if x < 0:
            return -((-x) ** (1 / n))
        return x ** (1 / n)

er = exponents_roots()
result = (er.power(2, 10), er.nth_root(27, 3))
print(result)
