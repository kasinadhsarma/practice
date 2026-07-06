class DoWhileEmulator:
    """
    Python has no native `do...while` loop. This emulates "run the body at
    least once, then check the condition" using `while True` + `break`.

    collect_until_negative() -> consumes values in order, always processing
    at least the first one, stopping right after a negative value is seen.
    Time Complexity  : O(N)
    Space Complexity : O(N)
    """

    def __init__(self, values: list):
        self.values = values

    def collect_until_negative(self) -> list:
        collected = []
        i = 0
        while True:
            if i >= len(self.values):
                break
            value = self.values[i]
            collected.append(value)
            i += 1
            if value < 0:
                break
        return collected


raw = input("Enter numbers separated by spaces: ")
values = [int(x) for x in raw.split()]
print("Collected:", DoWhileEmulator(values).collect_until_negative())
