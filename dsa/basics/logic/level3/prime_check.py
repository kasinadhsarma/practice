import math

class PrimeCheck:
    # A prime number has exactly two distinct factors: 1 and itself.
    # Key insight: if N has a factor > √N, it must also have one ≤ √N,
    # so we only need to check divisors up to √N.
    #
    # Single-number check
    #   Time Complexity:  O(√N)
    #   Space Complexity: O(1)
    #
    # Sieve of Eratosthenes (all primes up to limit)
    #   Time Complexity:  O(N log log N)
    #   Space Complexity: O(N)

    def __init__(self, N: int):
        self.N = N

    # ── Single check ───────────────────────────────────────────────────────────
    def is_prime(self) -> bool:
        n = self.N
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.isqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    # ── Prime factors ──────────────────────────────────────────────────────────
    def prime_factors(self) -> list:
        """Return all prime factors of N (with repetition)."""
        n = self.N
        factors = []
        # Extract factor 2
        while n % 2 == 0:
            factors.append(2)
            n //= 2
        # Extract odd factors
        for i in range(3, int(math.isqrt(n)) + 1, 2):
            while n % i == 0:
                factors.append(i)
                n //= i
        if n > 1:
            factors.append(n)
        return factors

    # ── Sieve of Eratosthenes ──────────────────────────────────────────────────
    @staticmethod
    def sieve(limit: int) -> list:
        """Return all primes up to `limit` using the Sieve of Eratosthenes."""
        if limit < 2:
            return []
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(math.isqrt(limit)) + 1):
            if is_prime[i]:
                for j in range(i * i, limit + 1, i):
                    is_prime[j] = False
        return [i for i, flag in enumerate(is_prime) if flag]

    # ── Next prime ─────────────────────────────────────────────────────────────
    def next_prime(self) -> int:
        """Return the smallest prime greater than N."""
        candidate = self.N + 1
        while True:
            pc = PrimeCheck(candidate)
            if pc.is_prime():
                return candidate
            candidate += 1


N = int(input("Enter the number: "))
pc = PrimeCheck(N)
print(f"{N} is {'a Prime' if pc.is_prime() else 'NOT a Prime'} number")
print(f"Prime factors of {N}    : {pc.prime_factors()}")
print(f"Next prime after {N}    : {pc.next_prime()}")

limit = int(input("List all primes up to: "))
print(f"Primes up to {limit}    : {PrimeCheck.sieve(limit)}")
