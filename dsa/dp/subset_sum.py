"""
Subset Sum
----------
Technique : Dynamic Programming (bottom-up tabulation, 0/1 knapsack style)
Idea      : Determine whether any subset of a given set of numbers adds up
            to exactly a target sum. For each number, you either include it
            in the running subset or skip it — the same include/skip
            decision structure as 0/1 knapsack, but tracking reachability
            (True/False) instead of value.

Formula / Recurrence
    dp[i][s] = True if some subset of the first i numbers sums to exactly s

    Base case  : dp[i][0] = True for all i   (the empty subset sums to 0)
                 dp[0][s] = False for all s > 0  (no numbers -> can't reach s>0)

    Recurrence :
        if nums[i-1] > s:  dp[i][s] = dp[i-1][s]                    (too big, skip)
        else            :  dp[i][s] = dp[i-1][s] OR dp[i-1][s - nums[i-1]]
                                        ^ skip it        ^ include it

    Answer : dp[n][target]

Steps
    1. Build a 2D boolean table dp of size (n+1) x (target+1).
    2. Set dp[i][0] = True for every i (sum 0 is always reachable).
    3. For each number i (1 to n), for each sum s (1 to target):
       - If the number is too big for s, carry forward dp[i-1][s].
       - Otherwise, it's reachable if it already was, OR if s minus this
         number was reachable using the earlier numbers.
    4. dp[n][target] answers whether the target sum is achievable.

Time  Complexity : O(N x Target)  — filling the dp table
Space Complexity : O(N x Target)  — dp table (can be reduced to O(Target))
"""

class SubsetSum:
    def __init__(self, nums: list):
        self.nums = nums

    def has_subset_with_sum(self, target: int) -> bool:
        n = len(self.nums)
        if target < 0:
            return False

        dp = [[False] * (target + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            for s in range(1, target + 1):
                if self.nums[i - 1] > s:
                    dp[i][s] = dp[i - 1][s]
                else:
                    dp[i][s] = dp[i - 1][s] or dp[i - 1][s - self.nums[i - 1]]

        return dp[n][target]


nums = list(map(int, input("enter numbers separated by space: ").split()))
target = int(input("enter target sum: "))
print("subset with target sum exists:", SubsetSum(nums).has_subset_with_sum(target))
