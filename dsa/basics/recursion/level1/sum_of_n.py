class SumOfN:
    """
    Recursively sums the first n natural numbers, reducing the problem
    to "n plus the sum of everything before it" until reaching 0.

    calculate() -> 1 + 2 + ... + n
    Base case  : sum(0) = 0
    Time Complexity  : O(N)
    Space Complexity : O(N) — recursion call stack
    """

    def __init__(self, n: int):
        self.n = n

    def calculate(self) -> int:
        if self.n <= 0:
            return 0
        return self.n + SumOfN(self.n - 1).calculate()


n = int(input("Enter n: "))
print("Sum 1..n:", SumOfN(n).calculate())
