class RangeStepDemo:
    """
    Demonstrates `range()` with a custom start/stop/step, including
    reverse iteration via a negative step.

    step_range(start, stop, step) -> list(range(start, stop, step)) : O(N)
    reverse_range()                -> n down to 1                   : O(N)
    """

    def __init__(self, n: int):
        self.n = n

    def step_range(self, start: int, stop: int, step: int) -> list:
        return list(range(start, stop, step))

    def reverse_range(self) -> list:
        return list(range(self.n, 0, -1))


n = int(input("Enter n: "))
print("Reverse range:", RangeStepDemo(n).reverse_range())
