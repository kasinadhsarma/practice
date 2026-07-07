class prime_factorization:
    # trial division: repeatedly divide out the smallest possible factor.
    # only needs to check divisors up to sqrt(n), since any factor larger
    # than that would need a matching factor smaller than sqrt(n).
    # time complexity O(sqrt(N)), space O(log N) — number of prime factors
    def calculate(self,n:int)->list:
        factors = []
        divisor = 2
        while divisor * divisor <= n:
            while n % divisor == 0:
                factors.append(divisor)
                n //= divisor
            divisor += 1
        if n > 1:
            factors.append(n)
        return factors

n = 360
result = prime_factorization().calculate(n)
print(result)
