"""
Longest Increasing Subsequence (LIS)
--------------------------------------
Technique : Dynamic Programming (bottom-up tabulation)
Idea      : Find the length of the longest subsequence of an array where
            every element is strictly greater than the one before it (the
            elements don't need to be contiguous). For each position, look
            back at every earlier position that could precede it in an
            increasing run, and extend the best one found.

Formula / Recurrence
    dp[i] = length of the longest increasing subsequence ENDING at index i

    Base case  : dp[i] = 1 for all i  (every element is an LIS of length 1 alone)

    Recurrence :
        dp[i] = max(dp[i], dp[j] + 1)  for every j < i where arr[j] < arr[i]

    Answer : max(dp)  — the best ending position isn't necessarily the last one

Steps
    1. Initialise dp[i] = 1 for every index (each element alone is length 1).
    2. For each index i, look at every earlier index j:
       - If arr[j] < arr[i], this element could extend that subsequence.
       - Update dp[i] = max(dp[i], dp[j] + 1).
    3. The answer is the maximum value anywhere in dp.

Time  Complexity : O(N^2)  — the tabulation DP shown here (an O(N log N)
                    patience-sorting approach exists but isn't a DP technique)
Space Complexity : O(N)    — the dp array
"""

class LongestIncreasingSubsequence:
    def __init__(self, arr: list):
        self.arr = arr

    def length(self) -> int:
        n = len(self.arr)
        if n == 0:
            return 0
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if self.arr[j] < self.arr[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


arr = list(map(int, input("enter elements separated by space: ").split()))
print("LIS length:", LongestIncreasingSubsequence(arr).length())
