class ContinueDemo:
    """
    Demonstrates skipping the rest of an iteration with `continue`.

    sum_even() -> sum of only the even numbers in [1, n], skipping odd ones
    Time Complexity  : O(N)
    Space Complexity : O(1)
    """

    def __init__(self, n: int):
        self.n = n

    def sum_even(self) -> int:
        total = 0
        for i in range(1, self.n + 1):
            if i % 2 != 0:
                continue
            total += i
        return total


n = int(input("Enter n: "))
print("Sum of evens 1..n:", ContinueDemo(n).sum_even())
