import math

class permutations:
    # nPr: number of ORDERED arrangements of r items chosen from n
    # nPr = n! / (n - r)!
    # time complexity O(N) for the factorials, space O(1)
    def calculate(self,n:int,r:int)->int:
        if r < 0 or r > n:
            return None
        return math.factorial(n) // math.factorial(n - r)

n = 5
r = 2
result = permutations().calculate(n, r)
print(result)
