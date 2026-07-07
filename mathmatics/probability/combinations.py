import math

class combinations:
    # nCr: number of UNORDERED selections of r items chosen from n
    # nCr = n! / (r! * (n - r)!)
    # time complexity O(N) for the factorials, space O(1)
    def calculate(self,n:int,r:int)->int:
        if r < 0 or r > n:
            return None
        return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

n = 5
r = 2
result = combinations().calculate(n, r)
print(result)
