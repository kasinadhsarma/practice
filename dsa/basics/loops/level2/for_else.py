class ForElseDemo:
    """
    Demonstrates the `for...else` construct: the `else` block runs only
    if the loop finishes normally, i.e. it never hits `break`.

    is_prime() -> True if n has no divisor in [2, n-1]
    Time Complexity  : O(N)
    Space Complexity : O(1)
    """

    def __init__(self, n: int):
        self.n = n

    def is_prime(self) -> bool:
        if self.n < 2:
            return False
        for i in range(2, self.n):
            if self.n % i == 0:
                break
        else:
            return True
        return False


n = int(input("Enter n: "))
print("Is prime:", ForElseDemo(n).is_prime())
