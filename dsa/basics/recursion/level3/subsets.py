class Subsets:
    """
    Generates the power set (every possible subset, including the empty
    set and the full set) via backtracking: for each element, branch
    into "include it" and "exclude it", recursing on the rest.

    generate() -> list of all 2^N subsets
    Recurrence : subsets(items) = subsets(items[1:]) with item included
                                 + subsets(items[1:]) with item excluded
    Time Complexity  : O(2^N * N) — 2^N subsets, O(N) to build/copy each
    Space Complexity : O(N)       — recursion depth
    """

    def __init__(self, items: list):
        self.items = items

    def generate(self) -> list:
        if not self.items:
            return [[]]

        first, rest = self.items[0], self.items[1:]
        without_first = Subsets(rest).generate()
        with_first = [[first] + subset for subset in without_first]
        return without_first + with_first


items = input("Enter items separated by space: ").split()
subsets = Subsets(items).generate()
print(f"Total subsets: {len(subsets)}")
for s in subsets:
    print(s)
