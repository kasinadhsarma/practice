class euler_totient:
    # phi(n) counts the integers in [1, n] that are coprime to n
    # (share no common factor with n other than 1). Computed via the
    # product formula over n's distinct prime factors p:
    #   phi(n) = n * product((1 - 1/p) for each distinct prime p dividing n)
    # time complexity O(sqrt(N)), space O(1)
    def calculate(self,n:int)->int:
        result = n
        remaining = n
        p = 2
        while p * p <= remaining:
            if remaining % p == 0:
                while remaining % p == 0:
                    remaining //= p
                result -= result // p
            p += 1
        if remaining > 1:
            result -= result // remaining
        return result

n = 36
result = euler_totient().calculate(n)
print(result)
