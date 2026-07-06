"""
Character Frequency Deficit
----------------------------
Technique : Hashing — fixed-size frequency array (26 lowercase letters)
Idea      : Given a source string S and a reference string R, find the
            minimum number of characters in S that must be replaced so that
            every character S needs is available in R's letter supply.

Formula / Property
    deficit = sum over each letter c of  max(0, freq_S[c] - freq_R[c])

    Only surpluses count — if R has *more* of a letter than S needs, that
    extra supply is simply unused, not subtracted anywhere.

Steps
    1. Build a 26-slot frequency array for S and for R.
    2. For each letter, compute how much more S needs than R supplies.
    3. Sum the positive deficits — that is the minimum replacement count.

Time  Complexity : O(N + M)   — one pass each over S and R (N = len(S), M = len(R))
Space Complexity : O(1)       — fixed 26-slot arrays regardless of input size
"""

class CharFrequencyDeficit:
    def calculate(self, s: str, r: str) -> int:
        freq_s = [0] * 26
        freq_r = [0] * 26

        for char in s:
            freq_s[ord(char) - ord('a')] += 1
        for char in r:
            freq_r[ord(char) - ord('a')] += 1

        mismatches = 0
        for i in range(26):
            if freq_s[i] > freq_r[i]:
                mismatches += freq_s[i] - freq_r[i]
        return mismatches


s = input("enter string S: ")
r = input("enter string R: ")
print("minimum replacements:", CharFrequencyDeficit().calculate(s, r))
