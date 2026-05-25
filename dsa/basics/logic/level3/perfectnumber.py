class PerfectNumber:
    # A PERFECT number equals the sum of its proper divisors (all divisors except itself).
    # Example: 6  → proper divisors: 1, 2, 3  → 1+2+3 = 6   ✓
    #          28 → proper divisors: 1,2,4,7,14 → 28         ✓
    # Formula: sum_of_proper_divisors(N) == N
    #
    # Key optimisation: iterate only up to √N — every divisor d ≤ √N
    # pairs with N/d ≥ √N, so we collect both in one pass.
    #
    # Time Complexity:  O(√N)
    # Space Complexity: O(1)  (O(d(N)) if we store divisors list)

    def __init__(self, N: int):
        self.N = N

    def _sum_proper_divisors(self) -> int:
        n = self.N
        if n < 2:
            return 0
        total = 1  # 1 is always a proper divisor for n > 1
        i = 2
        while i * i <= n:
            if n % i == 0:
                total += i
                if i != n // i:          # avoid counting √N twice
                    total += n // i
            i += 1
        return total

    def is_perfect(self) -> bool:
        return self.N > 1 and self._sum_proper_divisors() == self.N

    def get_proper_divisors(self) -> list:
        """Return sorted list of proper divisors of N."""
        n = self.N
        if n < 2:
            return [1] if n == 1 else []
        divisors = {1}
        i = 2
        while i * i <= n:
            if n % i == 0:
                divisors.add(i)
                divisors.add(n // i)
            i += 1
        return sorted(divisors)

    # ── Classification (Abundant / Deficient / Perfect) ────────────────────────
    def classify(self) -> str:
        s = self._sum_proper_divisors()
        if s == self.N:
            return "Perfect"
        elif s > self.N:
            return "Abundant"
        else:
            return "Deficient"

    @staticmethod
    def find_perfect_numbers(limit: int) -> list:
        """Return all perfect numbers up to `limit`."""
        result = []
        for num in range(2, limit + 1):
            pn = PerfectNumber(num)
            if pn.is_perfect():
                result.append(num)
        return result


N = int(input("Enter the number: "))
pn = PerfectNumber(N)
print(f"{N} is a {pn.classify()} number")
print(f"Proper divisors of {N} : {pn.get_proper_divisors()}")

limit = int(input("Find perfect numbers up to: "))
print(f"Perfect numbers up to {limit}: {PerfectNumber.find_perfect_numbers(limit)}")
