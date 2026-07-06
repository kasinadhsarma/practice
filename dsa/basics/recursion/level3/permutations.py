class Permutations:
    """
    Generates every permutation of a list via backtracking: pick each
    remaining element to go next, recurse on what's left, then undo the
    choice (backtrack) and try the next candidate.

    generate() -> list of all N! permutations
    Steps
        1. If nothing remains to place, the current arrangement is complete.
        2. Otherwise, try each remaining element as the next pick.
        3. Recurse with that element removed from the remaining pool.
        4. Backtrack (implicit here since we pass new lists, not shared state).
    Time Complexity  : O(N! * N) — N! permutations, O(N) to build/copy each
    Space Complexity : O(N)      — recursion depth
    """

    def __init__(self, items: list):
        self.items = items

    def generate(self) -> list:
        if len(self.items) <= 1:
            return [self.items[:]]

        result = []
        for i, item in enumerate(self.items):
            remaining = self.items[:i] + self.items[i + 1:]
            for perm in Permutations(remaining).generate():
                result.append([item] + perm)
        return result


items = input("Enter items separated by space: ").split()
perms = Permutations(items).generate()
print(f"Total permutations: {len(perms)}")
for p in perms:
    print(p)
