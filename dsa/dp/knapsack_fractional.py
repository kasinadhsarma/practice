"""
Fractional Knapsack Problem
----------------------------
Technique : Greedy — sort by value-to-weight ratio and take greedily
Idea      : Unlike 0/1 knapsack, here you can take fractions of an item.
            The optimal strategy is to always take as much as possible of
            the item with the highest value-per-unit-weight ratio.

Formula / Greedy Criterion
    Ratio for item i = v[i] / w[i]   (value per unit weight)

    Sort items by ratio in descending order.

    For each item (in sorted order):
        take = min(w[i], remaining_capacity)
        profit += take × (v[i] / w[i])
        remaining_capacity -= take

    This greedy choice is provably optimal:
        Exchange argument — swapping any fraction of a lower-ratio item
        for a fraction of the highest-ratio item never decreases profit.

Steps
    1. Compute ratio v[i]/w[i] for each item.
    2. Sort items by ratio descending.
    3. Iterate through sorted items:
       - If full item fits, take all of it.
       - Else take only as much as remaining capacity allows (fraction).
       - Update remaining capacity and total profit.
    4. Return total profit.

Why Greedy works here but NOT for 0/1 Knapsack?
    Fractional knapsack allows partial items → greedy exchange argument holds.
    0/1 knapsack forces binary choice → greedy may leave suboptimal gaps;
    DP must be used instead.

Time  Complexity : O(n log n)  — dominated by sorting
Space Complexity : O(n)        — item list with ratios
"""

class FractionalKnapsack:
    def __init__(self, weights, values, capacity):
        self.weights  = weights
        self.values   = values
        self.capacity = capacity

    def max_value(self):
        items = sorted(
            zip(self.values, self.weights),
            key=lambda x: x[0] / x[1],
            reverse=True
        )
        total     = 0.0
        remaining = self.capacity
        for value, weight in items:
            if remaining <= 0:
                break
            take   = min(weight, remaining)
            total += take * (value / weight)
            remaining -= take
        return round(total, 2)


n        = int(input("enter number of items: "))
weights  = list(map(int, input("enter weights separated by space: ").split()))
values   = list(map(int, input("enter values separated by space: ").split()))
capacity = int(input("enter knapsack capacity: "))
fk = FractionalKnapsack(weights, values, capacity)
print("maximum value:", fk.max_value())
