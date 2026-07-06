class ZipDemo:
    """
    Demonstrates parallel iteration over multiple sequences with `zip`.

    pair_up()     -> list of tuples pairing elements from both lists : O(min(N,M))
    dot_product() -> sum of element-wise products                    : O(min(N,M))
    """

    def __init__(self, a: list, b: list):
        self.a = a
        self.b = b

    def pair_up(self) -> list:
        pairs = []
        for x, y in zip(self.a, self.b):
            pairs.append((x, y))
        return pairs

    def dot_product(self) -> int:
        total = 0
        for x, y in zip(self.a, self.b):
            total += x * y
        return total


a = [int(x) for x in input("Enter first list: ").split()]
b = [int(x) for x in input("Enter second list: ").split()]
demo = ZipDemo(a, b)
print("Pairs:", demo.pair_up())
print("Dot product:", demo.dot_product())
