"""
Isomorphic Strings
------------------
Technique : Hashing — bijective (two-way) character mapping
Idea      : Two strings are isomorphic if every character in the first string
            can be replaced to get the second string, with a consistent
            one-to-one mapping in both directions (no two characters may map
            to the same target character).

Formula / Property
    s1 is isomorphic to s2  iff:
        len(s1) == len(s2), and
        there exist bijective maps f: s1 -> s2 and g: s2 -> s1 such that
        f(s1[i]) == s2[i] and g(s2[i]) == s1[i] for every index i.

    Example: "egg" ~ "add"   (e->a, g->d)
             "foo" !~ "bar"  (f->b, o->a, o->r  conflicts: o can't map to
                              both a and r)

Steps
    1. Reject immediately if lengths differ.
    2. Walk both strings in lockstep, maintaining two hashmaps:
       s1->s2 and s2->s1.
    3. At each position, if a character is already mapped to something
       different than its counterpart, the strings are not isomorphic.
    4. Otherwise record the mapping and continue.

Time  Complexity : O(N)      — one pass through the strings
Space Complexity : O(1)      — at most 26 (or alphabet-size) map entries
"""

class IsomorphicStrings:
    def is_isomorphic(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        map_s1_s2 = {}
        map_s2_s1 = {}

        for c1, c2 in zip(s1, s2):
            if c1 in map_s1_s2 and map_s1_s2[c1] != c2:
                return False
            if c2 in map_s2_s1 and map_s2_s1[c2] != c1:
                return False
            map_s1_s2[c1] = c2
            map_s2_s1[c2] = c1

        return True

    def count_matches(self, candidates: list, target: str) -> int:
        # counts how many strings in `candidates` are isomorphic to `target`
        return sum(1 for s in candidates if self.is_isomorphic(s, target))


n = int(input("enter number of candidate strings: "))
candidates = [input(f"candidate {i + 1}: ") for i in range(n)]
target = input("enter target string: ")
matcher = IsomorphicStrings()
print("isomorphic to target:", matcher.count_matches(candidates, target))
