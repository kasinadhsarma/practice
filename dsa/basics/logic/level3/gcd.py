class GCD:
    # GCD (Greatest Common Divisor) — largest integer that divides both a and b.
    # LCM (Least Common Multiple) — smallest positive integer divisible by both.
    #
    # Euclidean Algorithm:
    #   GCD(a, b) = GCD(b, a % b)   until b == 0
    #   GCD(a, 0) = a
    #
    # Key relationship:  LCM(a, b) = (a * b) // GCD(a, b)
    #
    # Time Complexity:  O(log(min(a, b)))  — Euclidean algorithm
    # Space Complexity: O(1) iterative  /  O(log(min(a,b))) recursive call-stack

    def __init__(self, a: int, b: int):
        self.a = abs(a)
        self.b = abs(b)

    # ── Iterative Euclidean GCD ────────────────────────────────────────────────
    def gcd_iterative(self) -> int:
        a, b = self.a, self.b
        while b:
            a, b = b, a % b
        return a

    # ── Recursive Euclidean GCD ───────────────────────────────────────────────
    def gcd_recursive(self, a: int = None, b: int = None) -> int:
        if a is None:
            a, b = self.a, self.b
        if b == 0:
            return a
        return self.gcd_recursive(b, a % b)

    # ── LCM using GCD ─────────────────────────────────────────────────────────
    def lcm(self) -> int:
        g = self.gcd_iterative()
        if g == 0:
            return 0
        return (self.a * self.b) // g

    # ── Extended Euclidean Algorithm (bonus) ──────────────────────────────────
    def extended_gcd(self, a: int = None, b: int = None):
        """
        Returns (gcd, x, y) such that  a*x + b*y = gcd(a, b).
        Useful for modular inverse and Bézout's identity.
        """
        if a is None:
            a, b = self.a, self.b
        if b == 0:
            return a, 1, 0
        g, x1, y1 = self.extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return g, x, y

    # ── GCD of a list ─────────────────────────────────────────────────────────
    @staticmethod
    def gcd_of_list(numbers: list) -> int:
        """Compute GCD of an entire list using the associative property."""
        from functools import reduce
        def _gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        return reduce(_gcd, numbers)


a = int(input("Enter first number  (a): "))
b = int(input("Enter second number (b): "))
calc = GCD(a, b)

print(f"GCD({a}, {b}) iterative = {calc.gcd_iterative()}")
print(f"GCD({a}, {b}) recursive = {calc.gcd_recursive()}")
print(f"LCM({a}, {b})           = {calc.lcm()}")

g, x, y = calc.extended_gcd()
print(f"Extended GCD: {a}*({x}) + {b}*({y}) = {g}")
