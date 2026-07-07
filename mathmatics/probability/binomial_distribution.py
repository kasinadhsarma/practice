import math

class binomial_distribution:
    # models the number of successes in n independent yes/no trials, each
    # with success probability p
    # pmf(k) = C(n,k) * p^k * (1-p)^(n-k)  — probability of exactly k successes
    # cdf(k) = sum of pmf(0..k)            — probability of AT MOST k successes
    # time complexity O(N) per pmf call, O(N^2) for cdf, space O(1)
    def pmf(self,n:int,k:int,p:float)->float:
        if k < 0 or k > n:
            return 0
        combos = math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
        return combos * (p ** k) * ((1 - p) ** (n - k))

    def cdf(self,n:int,k:int,p:float)->float:
        return sum(self.pmf(n, i, p) for i in range(k + 1))

n = 10
p = 0.5
k = 6
result = binomial_distribution().pmf(n, k, p)
print(result)
