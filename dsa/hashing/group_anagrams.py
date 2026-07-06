"""
Group Anagrams
--------------
Technique : Hashing — canonical-key grouping
Idea      : Two words are anagrams of each other if they contain exactly the
            same letters. Sorting a word's letters produces a canonical form
            that is identical for every anagram of that word, so it can be
            used as a hashmap key to bucket words together.

Formula / Property
    key(word) = "".join(sorted(word))
    All words sharing the same key are anagrams of one another.

Steps
    1. Create an empty hashmap (canonical key -> list of original words).
    2. For each word, compute its sorted-letters key.
    3. Append the word to the bucket for that key.
    4. Return all buckets (their values) as the grouped anagrams.

Time  Complexity : O(N * K log K)  — N words, each of length up to K, sorted
Space Complexity : O(N * K)        — every word is stored once, in some bucket
"""

class GroupAnagrams:
    def __init__(self, words: list):
        self.words = words

    def group(self) -> list:
        buckets = {}
        for word in self.words:
            key = "".join(sorted(word))
            buckets.setdefault(key, []).append(word)
        return list(buckets.values())


words = input("enter words separated by space: ").split()
result = GroupAnagrams(words).group()
print("grouped anagrams:", result)
