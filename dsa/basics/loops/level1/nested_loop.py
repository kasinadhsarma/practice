class NestedLoop:
    """
    Demonstrates a `for` loop inside another `for` loop.

    multiplication_table() -> n x n table as a list of rows : O(N²) time, O(N²) space
    """

    def __init__(self, n: int):
        self.n = n

    def multiplication_table(self) -> list:
        table = []
        for i in range(1, self.n + 1):
            row = []
            for j in range(1, self.n + 1):
                row.append(i * j)
            table.append(row)
        return table


n = int(input("Enter table size: "))
for row in NestedLoop(n).multiplication_table():
    print(" ".join(str(x) for x in row))
