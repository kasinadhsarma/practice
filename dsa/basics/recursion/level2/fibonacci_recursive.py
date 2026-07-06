class FibonacciRecursive:
    """
    Naive recursive Fibonacci — the classic example of a recursion tree
    with overlapping subproblems (contrast with dsa/dp/'s memoised
    Fibonacci, which caches these repeated subcalls to avoid the
    exponential blowup seen here).

    calculate() -> F(n) = F(n-1) + F(n-2),  F(0)=0, F(1)=1
    Time Complexity  : O(2^N) — no memoisation, subproblems recomputed repeatedly
    Space Complexity : O(N)   — deepest recursion path
    """

    def __init__(self, n: int):
        self.n = n

    def calculate(self) -> int:
        if self.n <= 1:
            return self.n
        return FibonacciRecursive(self.n - 1).calculate() + FibonacciRecursive(self.n - 2).calculate()

    def call_count(self) -> int:
        """Counts how many recursive calls calculate() makes internally."""
        if self.n <= 1:
            return 1
        return 1 + FibonacciRecursive(self.n - 1).call_count() + FibonacciRecursive(self.n - 2).call_count()


n = int(input("Enter n: "))
fib = FibonacciRecursive(n)
print("Fibonacci(n):", fib.calculate())
print("Recursive calls made:", fib.call_count())
