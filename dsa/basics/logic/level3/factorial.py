class Factorial:
    # Factorial of N: product of all positive integers up to N
    # Formula: N! = N * (N-1) * (N-2) * ... * 1  ;  0! = 1
    # Iterative approach
    #   Time Complexity:  O(N)
    #   Space Complexity: O(1)
    # Recursive approach
    #   Time Complexity:  O(N)
    #   Space Complexity: O(N) — call stack depth

    def __init__(self, N: int):
        if N < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        self.N = N

    # ── Iterative ──────────────────────────────────────────────────────────────
    def iterative(self) -> int:
        result = 1
        for i in range(2, self.N + 1):
            result *= i
        return result

    # ── Recursive ──────────────────────────────────────────────────────────────
    def recursive(self, n: int = None) -> int:
        if n is None:
            n = self.N
        if n == 0 or n == 1:
            return 1
        return n * self.recursive(n - 1)

    # ── Trailing zeroes (bonus) ─────────────────────────────────────────────────
    def trailing_zeros(self) -> int:
        """Count trailing zeros in N! — each zero comes from a factor of 5."""
        count = 0
        power = 5
        while power <= self.N:
            count += self.N // power
            power *= 5
        return count


N = int(input("Enter the number: "))
f = Factorial(N)
print(f"{N}! (iterative) = {f.iterative()}")
print(f"{N}! (recursive) = {f.recursive()}")
print(f"Trailing zeros in {N}! = {f.trailing_zeros()}")
