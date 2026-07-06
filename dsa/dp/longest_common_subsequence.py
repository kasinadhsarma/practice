"""
Longest Common Subsequence (LCS)
---------------------------------
Technique : Dynamic Programming (bottom-up tabulation)
Idea      : Given two strings, find the length of the longest sequence of
            characters that appears in both strings in the same relative
            order (not necessarily contiguous). Build the answer from the
            LCS of every pair of prefixes.

Formula / Recurrence
    dp[i][j] = length of LCS of s1[:i] and s2[:j]

    Base case  : dp[0][j] = dp[i][0] = 0  (an empty prefix has no LCS)

    Recurrence :
        if s1[i-1] == s2[j-1]:  dp[i][j] = dp[i-1][j-1] + 1
        else                 :  dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    Answer : dp[len(s1)][len(s2)]

Steps
    1. Build a 2D table dp of size (n+1) x (m+1) initialised to 0.
    2. For each pair of positions (i, j):
       - If the characters match, extend the diagonal LCS by 1.
       - Otherwise, carry forward the best of skipping a character from
         either string.
    3. dp[n][m] is the LCS length. Backtrack through the table to recover
       the actual subsequence.

Time  Complexity : O(N x M)  — filling the dp table
Space Complexity : O(N x M)  — dp table
"""

class LongestCommonSubsequence:
    def __init__(self, s1: str, s2: str):
        self.s1 = s1
        self.s2 = s2

    def length(self) -> int:
        n, m = len(self.s1), len(self.s2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if self.s1[i - 1] == self.s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[n][m]

    def sequence(self) -> str:
        n, m = len(self.s1), len(self.s2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if self.s1[i - 1] == self.s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # backtrack to reconstruct the actual subsequence
        i, j = n, m
        chars = []
        while i > 0 and j > 0:
            if self.s1[i - 1] == self.s2[j - 1]:
                chars.append(self.s1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] >= dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
        return "".join(reversed(chars))


s1 = input("enter first string: ")
s2 = input("enter second string: ")
lcs = LongestCommonSubsequence(s1, s2)
print("LCS length:", lcs.length())
print("LCS sequence:", lcs.sequence())
