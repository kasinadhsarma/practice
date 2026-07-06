class EnumerateDemo:
    """
    Demonstrates iterating with index and value together via `enumerate`.

    indexed_items()    -> list of (index, item) pairs : O(N) time, O(N) space
    find_index(target) -> index of first match, or -1 : O(N) time, O(1) space
    """

    def __init__(self, items: list):
        self.items = items

    def indexed_items(self) -> list:
        result = []
        for index, item in enumerate(self.items):
            result.append((index, item))
        return result

    def find_index(self, target) -> int:
        for index, item in enumerate(self.items):
            if item == target:
                return index
        return -1


raw = input("Enter items separated by spaces: ")
items = raw.split()
demo = EnumerateDemo(items)
print("Indexed:", demo.indexed_items())
