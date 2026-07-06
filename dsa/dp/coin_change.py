"""
Coin Change
-----------
Technique : Dynamic Programming (bottom-up tabulation, unbounded knapsack style)
Idea      : Given a set of coin denominations (unlimited supply of each) and
            a target amount, solve two related questions:
              1. Minimum number of coins needed to make the amount exactly.
              2. Number of distinct combinations of coins that make the
                 amount exactly (order doesn't matter).

Formula / Recurrence
    Minimum coins:
        dp_min[a] = fewest coins to make amount a
        dp_min[0] = 0
        dp_min[a] = min(dp_min[a - c] + 1  for every coin c <= a)
        If no combination works, dp_min[a] stays "impossible".

    Count combinations (order-independent — process coins one at a time
    on the OUTER loop to avoid counting permutations separately):
        dp_count[a] = number of ways to make amount a
        dp_count[0] = 1  (one way to make 0: use nothing)
        for each coin c:
            for a from c to target:
                dp_count[a] += dp_count[a - c]

Steps (minimum coins)
    1. dp_min[0] = 0; dp_min[a] = infinity for a > 0.
    2. For each amount a from 1 to target:
       For each coin c <= a: dp_min[a] = min(dp_min[a], dp_min[a-c] + 1).
    3. Return dp_min[target], or -1 if it's still infinity.

Steps (count combinations)
    1. dp_count[0] = 1; dp_count[a] = 0 for a > 0.
    2. For each coin (outer loop): for each amount from coin to target
       (inner loop): dp_count[a] += dp_count[a - coin].
    3. Return dp_count[target].

Time  Complexity : O(target x len(coins))  — for both variants
Space Complexity : O(target)               — the dp array
"""

class CoinChange:
    def __init__(self, coins: list, amount: int):
        self.coins = coins
        self.amount = amount

    def min_coins(self) -> int:
        target = self.amount
        dp = [float('inf')] * (target + 1)
        dp[0] = 0
        for a in range(1, target + 1):
            for coin in self.coins:
                if coin <= a:
                    dp[a] = min(dp[a], dp[a - coin] + 1)
        return dp[target] if dp[target] != float('inf') else -1

    def count_combinations(self) -> int:
        target = self.amount
        dp = [0] * (target + 1)
        dp[0] = 1
        for coin in self.coins:
            for a in range(coin, target + 1):
                dp[a] += dp[a - coin]
        return dp[target]


coins = list(map(int, input("enter coin denominations separated by space: ").split()))
amount = int(input("enter target amount: "))
cc = CoinChange(coins, amount)
print("minimum coins needed:", cc.min_coins())
print("number of combinations:", cc.count_combinations())
