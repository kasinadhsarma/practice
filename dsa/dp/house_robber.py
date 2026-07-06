"""
House Robber
------------
Technique : Dynamic Programming (bottom-up tabulation)
Idea      : Given the amount of money in each house along a street, find
            the maximum total you can rob without ever robbing two directly
            adjacent houses (doing so triggers an alarm). At each house you
            choose: skip it (keep the best total so far) or rob it (best
            total from two houses back, plus this house's money).

Formula / Recurrence
    dp[i] = maximum money obtainable from the first i houses

    Base case  : dp[0] = 0, dp[1] = money[0]

    Recurrence :
        dp[i] = max(dp[i-1], dp[i-2] + money[i-1])
                       ^ skip house i        ^ rob house i

    Answer : dp[n]

Steps
    1. Handle the empty/one-house edge cases directly.
    2. dp[0] = 0 (no houses), dp[1] = money[0] (only one choice).
    3. For each house i (2 to n): dp[i] = max(skip it, rob it).
    4. dp[n] is the maximum amount obtainable.

Time  Complexity : O(N)  — one pass through the houses
Space Complexity : O(1)  — only the last two dp values are ever needed
"""

class HouseRobber:
    def __init__(self, money: list):
        self.money = money

    def max_amount(self) -> int:
        n = len(self.money)
        if n == 0:
            return 0
        if n == 1:
            return self.money[0]

        prev2, prev1 = 0, self.money[0]
        for i in range(1, n):
            current = max(prev1, prev2 + self.money[i])
            prev2, prev1 = prev1, current

        return prev1


money = list(map(int, input("enter money in each house separated by space: ").split()))
print("maximum amount robbable:", HouseRobber(money).max_amount())
