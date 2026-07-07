class prime_sieve:
    # Sieve of Eratosthenes: mark every multiple of each prime as
    # composite, starting from 2; whatever survives unmarked is prime.
    # Far faster than trial-dividing every number individually when you
    # need ALL primes up to N, since each composite gets crossed out once.
    # time complexity O(N log log N), space O(N)
    def calculate(self,n:int)->list:
        if n < 2:
            return []
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for multiple in range(i * i, n + 1, i):
                    is_prime[multiple] = False
        return [i for i in range(2, n + 1) if is_prime[i]]

n = 50
result = prime_sieve().calculate(n)
print(result)
