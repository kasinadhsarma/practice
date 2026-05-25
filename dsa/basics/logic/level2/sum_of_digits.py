class SumOfDigits:
    # Sum of digits: repeatedly extract last digit and accumulate
    # Formula: sum = d1 + d2 + d3 + ... + dk  (where d1..dk are digits of N)
    # Time Complexity:  O(log N) — one iteration per digit
    # Space Complexity: O(1)    — only scalar variables used

    def __init__(self, N: int):
        self.N = abs(N)  # handle negatives gracefully

    def get_sum(self) -> int:
        temp = self.N
        total = 0
        while temp > 0:
            total += temp % 10
            temp //= 10
        return total

    def get_digital_root(self) -> int:
        """Repeatedly sum digits until single digit (digital root)."""
        n = self.N
        while n >= 10:
            total = 0
            while n > 0:
                total += n % 10
                n //= 10
            n = total
        return n


N = int(input("Enter the number: "))
s = SumOfDigits(N)
print(f"Sum of digits of {N}       : {s.get_sum()}")
print(f"Digital root of {N}        : {s.get_digital_root()}")
