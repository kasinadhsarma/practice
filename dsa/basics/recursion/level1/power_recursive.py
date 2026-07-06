class PowerRecursive:
    """
    Computes x^n recursively, plus the fast-exponentiation variant that
    halves the exponent each call instead of decrementing by 1.

    calculate()      -> x^n via n recursive multiplications : O(N) time
    calculate_fast()  -> x^n via repeated squaring            : O(log N) time
    Base case  : x^0 = 1
    Space Complexity : O(N) / O(log N) — recursion call stack
    """

    def __init__(self, x: float, n: int):
        self.x = x
        self.n = n

    def calculate(self) -> float:
        if self.n == 0:
            return 1
        return self.x * PowerRecursive(self.x, self.n - 1).calculate()

    def calculate_fast(self) -> float:
        if self.n == 0:
            return 1
        half = PowerRecursive(self.x, self.n // 2).calculate_fast()
        if self.n % 2 == 0:
            return half * half
        return half * half * self.x


x = float(input("Enter base x: "))
n = int(input("Enter exponent n: "))
power = PowerRecursive(x, n)
print("x^n (linear):", power.calculate())
print("x^n (fast):", power.calculate_fast())
