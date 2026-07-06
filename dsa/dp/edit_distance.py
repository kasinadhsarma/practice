"""
Edit Distance (Levenshtein Distance)
--------------------------------------
Technique : Dynamic Programming (bottom-up tabulation)
Idea      : Find the minimum number of single-character insert, delete, or
            replace operations needed to transform one string into another.
            Build the answer from the edit distance of every pair of
            prefixes, the same way LCS does.

Formula / Recurrence
    dp[i][j] = edit distance between s1[:i] and s2[:j]

    Base case  : dp[i][0] = i   (delete all i characters of s1)
                 dp[0][j] = j   (insert all j characters of s2)

    Recurrence :
        if s1[i-1] == s2[j-1]:  dp[i][j] = dp[i-1][j-1]           (no edit needed)
        else                 :  dp[i][j] = 1 + min(
                                     dp[i-1][j],    # delete from s1
                                     dp[i][j-1],    # insert into s1
                                     dp[i-1][j-1],  # replace
                                 )

    Answer : dp[len(s1)][len(s2)]

Steps
    1. Build a 2D table dp of size (n+1) x (m+1).
    2. Fill row 0 and column 0 with the base cases (pure inserts/deletes).
    3. For each pair of positions (i, j):
       - If characters match, no new edit is needed — copy the diagonal.
       - Otherwise, take 1 + the cheapest of delete/insert/replace.
    4. dp[n][m] is the minimum edit distance.

Time  Complexity : O(N x M)  — filling the dp table
Space Complexity : O(N x M)  — dp table (can be reduced to O(min(N,M)))
"""

class EditDistance:
    def __init__(self, s1: str, s2: str):
        self.s1 = s1
        self.s2 = s2

    def calculate(self) -> int:
        n, m = len(self.s1), len(self.s2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = i
        for j in range(m + 1):
            dp[0][j] = j

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if self.s1[i - 1] == self.s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],      # delete
                        dp[i][j - 1],      # insert
                        dp[i - 1][j - 1],  # replace
                    )

        return dp[n][m]


s1 = input("enter first string: ")
s2 = input("enter second string: ")
print("edit distance:", EditDistance(s1, s2).calculate())
