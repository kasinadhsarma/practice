class ForLoop:
    """
    Demonstrates the basic `for` loop over a numeric range.

    sum_range()      -> sum of 1..n using a for loop           : O(N) time, O(1) space
    multiples_of(k)  -> multiples of k in [1, n]                : O(N) time, O(N) space
    """

    def __init__(self, n: int):
        self.n = n

    def sum_range(self) -> int:
        total = 0
        for i in range(1, self.n + 1):
            total += i
        return total

    def multiples_of(self, k: int) -> list:
        result = []
        for i in range(1, self.n + 1):
            if i % k == 0:
                result.append(i)
        return result


n = int(input("Enter n: "))
loop = ForLoop(n)
print("Sum 1..n:", loop.sum_range())
print("Multiples of 3:", loop.multiples_of(3))
