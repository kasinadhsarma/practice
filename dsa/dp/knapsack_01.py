"""
0/1 Knapsack Problem
---------------------
Technique : Dynamic Programming (bottom-up tabulation)
Idea      : Given n items each with a weight w[i] and value v[i], and a
            knapsack of capacity W, find the maximum total value you can
            carry. Each item can be taken (1) or left (0) — no fractions.

Formula / Recurrence
    dp[i][w] = maximum value using first i items with capacity w

    Base case  : dp[0][w] = 0  for all w  (no items → no value)

    Recurrence :
        if w[i] > w:  dp[i][w] = dp[i-1][w]          ← item too heavy, skip
        else       :  dp[i][w] = max(
                            dp[i-1][w],                ← skip item i
                            dp[i-1][w - w[i]] + v[i]  ← take item i
                        )

    Answer : dp[n][W]

Steps
    1. Build a 2D table dp of size (n+1) × (W+1) initialised to 0.
    2. For each item i (1 to n):
       For each capacity w (0 to W):
         - If item i is too heavy for w: carry forward dp[i-1][w].
         - Else: take the max of skipping or taking item i.
    3. dp[n][W] is the answer.

Why DP and not Greedy?
    Greedy (pick by value/weight ratio) fails for 0/1 knapsack because you
    cannot take fractions — see knapsack_fractional.py for that version.

Time  Complexity : O(n × W)  — filling the dp table
Space Complexity : O(n × W)  — dp table  (can be reduced to O(W) with 1D array)
"""

class Knapsack01:
    def __init__(self, weights, values, capacity):
        self.weights  = weights
        self.values   = values
        self.capacity = capacity
        self.n        = len(weights)

    def max_value(self):
        n, W = self.n, self.capacity
        dp = [[0] * (W + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for w in range(W + 1):
                dp[i][w] = dp[i - 1][w]          # skip item i
                if self.weights[i - 1] <= w:
                    dp[i][w] = max(
                        dp[i][w],
                        dp[i - 1][w - self.weights[i - 1]] + self.values[i - 1]
                    )
        return dp[n][W]


n        = int(input("enter number of items: "))
weights  = list(map(int, input("enter weights separated by space: ").split()))
values   = list(map(int, input("enter values separated by space: ").split()))
capacity = int(input("enter knapsack capacity: "))
ks = Knapsack01(weights, values, capacity)
print("maximum value:", ks.max_value())
