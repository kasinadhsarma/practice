class BreakDemo:
    """
    Demonstrates exiting a loop early with `break`.

    first_divisor() -> smallest divisor of n greater than 1, or n itself if prime
    Time Complexity  : O(N) worst case
    Space Complexity : O(1)
    """

    def __init__(self, n: int):
        self.n = n

    def first_divisor(self) -> int:
        result = self.n
        for i in range(2, self.n):
            if self.n % i == 0:
                result = i
                break
        return result


n = int(input("Enter n: "))
print("First divisor:", BreakDemo(n).first_divisor())
