class Fibonacci:
    # Fibonacci sequence: F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2) for n >= 2
    # Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    #
    # Iterative approach
    #   Time Complexity:  O(N)
    #   Space Complexity: O(1)
    #
    # Recursive approach (plain)
    #   Time Complexity:  O(2^N)  — exponential, due to repeated subproblems
    #   Space Complexity: O(N)    — call stack
    #
    # Memoised (top-down DP)
    #   Time Complexity:  O(N)
    #   Space Complexity: O(N)

    def __init__(self, N: int):
        if N < 0:
            raise ValueError("Index must be non-negative.")
        self.N = N
        self._memo = {}

    # ── Iterative ──────────────────────────────────────────────────────────────
    def iterative(self) -> int:
        if self.N <= 1:
            return self.N
        a, b = 0, 1
        for _ in range(2, self.N + 1):
            a, b = b, a + b
        return b

    # ── Recursive with memoisation ─────────────────────────────────────────────
    def memoised(self, n: int = None) -> int:
        if n is None:
            n = self.N
        if n <= 1:
            return n
        if n not in self._memo:
            self._memo[n] = self.memoised(n - 1) + self.memoised(n - 2)
        return self._memo[n]

    # ── Generate first N Fibonacci numbers ─────────────────────────────────────
    def generate_series(self) -> list:
        if self.N == 0:
            return [0]
        series = [0, 1]
        for i in range(2, self.N + 1):
            series.append(series[-1] + series[-2])
        return series

    # ── Check if a number is Fibonacci (bonus) ─────────────────────────────────
    @staticmethod
    def is_fibonacci(num: int) -> bool:
        """A number is Fibonacci iff one of (5*n²+4) or (5*n²-4) is a perfect square."""
        import math
        def is_perfect_square(x):
            s = int(math.isqrt(x))
            return s * s == x
        return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)


N = int(input("Enter N (find Nth Fibonacci number): "))
fib = Fibonacci(N)
print(f"F({N}) iterative   = {fib.iterative()}")
print(f"F({N}) memoised    = {fib.memoised()}")
print(f"Series 0..{N}     = {fib.generate_series()}")

num = int(input("Check if this number is a Fibonacci number: "))
print(f"{num} is {'a Fibonacci' if Fibonacci.is_fibonacci(num) else 'NOT a Fibonacci'} number")
