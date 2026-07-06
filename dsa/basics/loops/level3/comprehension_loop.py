class ComprehensionDemo:
    """
    Demonstrates comprehensions as a compact form of a `for` loop.

    squares()          -> [i*i for i in range(1, n+1)]  : O(N) time, O(N) space
    evens(nums)        -> [x for x in nums if x % 2==0] : O(N) time, O(N) space
    length_map(words)  -> {w: len(w) for w in words}    : O(N) time, O(N) space
    """

    def __init__(self, n: int):
        self.n = n

    def squares(self) -> list:
        return [i * i for i in range(1, self.n + 1)]

    def evens(self, nums: list) -> list:
        return [x for x in nums if x % 2 == 0]

    def length_map(self, words: list) -> dict:
        return {w: len(w) for w in words}


n = int(input("Enter n: "))
print("Squares:", ComprehensionDemo(n).squares())
