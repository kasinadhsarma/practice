class FactorialRecursive:
    """
    Demonstrates basic recursion: a function that calls itself on a
    smaller version of the same problem until it hits a base case.

    calculate() -> n! = n * (n-1) * ... * 1
    Base case  : 0! = 1! = 1
    Time Complexity  : O(N)
    Space Complexity : O(N) — recursion call stack, one frame per call
    """

    def __init__(self, n: int):
        self.n = n

    def calculate(self) -> int:
        if self.n <= 1:
            return 1
        return self.n * FactorialRecursive(self.n - 1).calculate()


n = int(input("Enter n: "))
print("Factorial:", FactorialRecursive(n).calculate())
