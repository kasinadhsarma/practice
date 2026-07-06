"""
First Unique Character
------------------------
Technique : Hashing — frequency count + second pass
Idea      : Find the index of the first character in a string that appears
            exactly once. A single frequency-count pass tells you *which*
            characters are unique; a second pass finds the first one in
            original order.

Formula / Property
    freq[c] = number of occurrences of character c in the string.
    Answer  = min index i such that freq[s[i]] == 1  (or -1 if none exists).

Steps
    1. Count the frequency of every character in the string (hashmap).
    2. Walk the string again, in order, and return the index of the first
       character whose frequency is exactly 1.
    3. If no such character exists, return -1.

Time  Complexity : O(N)  — two linear passes over the string
Space Complexity : O(1)  — bounded alphabet size for the frequency map
"""

class FirstUniqueCharacter:
    def __init__(self, s: str):
        self.s = s

    def find_index(self) -> int:
        freq = {}
        for char in self.s:
            freq[char] = freq.get(char, 0) + 1

        for i, char in enumerate(self.s):
            if freq[char] == 1:
                return i
        return -1


s = input("enter a string: ")
index = FirstUniqueCharacter(s).find_index()
print("first unique character index:", index)
