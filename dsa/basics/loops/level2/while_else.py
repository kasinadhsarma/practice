class WhileElseDemo:
    """
    Demonstrates the `while...else` construct: the `else` block runs only
    if the loop's condition becomes False naturally, i.e. it never hits
    `break`. This is the `while` counterpart to `for...else`.

    has_factor_below(limit) -> True if a factor of n is found before limit
    is reached; the `else` clause marks the "searched everything, found
    nothing" case.
    Time Complexity  : O(N)
    Space Complexity : O(1)
    """

    def __init__(self, n: int):
        self.n = n

    def has_factor_below(self, limit: int) -> bool:
        i = 2
        while i < limit:
            if self.n % i == 0:
                break
            i += 1
        else:
            return False
        return True


n = int(input("Enter n: "))
limit = int(input("Enter search limit: "))
print("Has factor below limit:", WhileElseDemo(n).has_factor_below(limit))
