"""
Longest Palindromic Subsequence
----------------------------------
Technique : Dynamic Programming (interval DP over substring ranges)
Idea      : Find the length of the longest subsequence of a string that
            reads the same forwards and backwards (characters don't need
            to be contiguous). Solve on shrinking substring ranges [i, j]:
            if the outer characters match, they can both join the answer
            found for the inner range; otherwise take the better of
            dropping one end or the other.

            Equivalent formulation: this equals the Longest Common
            Subsequence of the string with its own reverse.

Formula / Recurrence
    dp[i][j] = length of the longest palindromic subsequence in s[i..j]

    Base case  : dp[i][i] = 1  for every i           (single character)

    Recurrence (filling by increasing substring length):
        if s[i] == s[j]:  dp[i][j] = dp[i+1][j-1] + 2
        else            :  dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    Answer : dp[0][n-1]

Steps
    1. Every single character is a palindrome of length 1: dp[i][i] = 1.
    2. Process substrings by increasing length (2, 3, ..., n):
       For each start i (end j = i + length - 1):
       - If s[i] == s[j], extend the inner palindrome by both ends.
       - Otherwise, take the best of excluding the left or right character.
    3. dp[0][n-1] covers the whole string — the final answer.

Time  Complexity : O(N^2)  — all O(N^2) substring ranges filled once
Space Complexity : O(N^2)  — dp table over substring ranges
"""

class LongestPalindromicSubsequence:
    def __init__(self, s: str):
        self.s = s

    def length(self) -> int:
        s = self.s
        n = len(s)
        if n == 0:
            return 0

        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2 if length > 2 else 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]


s = input("enter a string: ")
print("longest palindromic subsequence length:", LongestPalindromicSubsequence(s).length())
