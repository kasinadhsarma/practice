# 💡 DSA — Dynamic Programming (DP)

**Location:** [`dsa/dp/`](../dsa/dp/)

**Dynamic Programming** solves problems by breaking them into overlapping subproblems, storing the results of each subproblem to avoid redundant computation. This is the core difference from plain recursion.

> **Key Insight:** DP = Recursion + Memoization (top-down) or Tabulation (bottom-up).

---

## Core DP Concepts

| Concept | Description |
|:---|:---|
| **Optimal Substructure** | The optimal solution to the whole problem is built from optimal solutions to its subproblems |
| **Overlapping Subproblems** | The same subproblems are solved multiple times — DP caches their answers |
| **Memoization (Top-Down)** | Recursive solution + cache (dictionary/array) to store computed results |
| **Tabulation (Bottom-Up)** | Iteratively fill a table starting from base cases up to the final answer |

---

## Problems

---

### 🎒 0/1 Knapsack — `knapsack_01.py`

**Technique:** Dynamic Programming — bottom-up tabulation  
**Type:** 0/1 Choice (take an item or leave it — no fractions)

#### Problem Statement
Given $N$ items each with weight $w[i]$ and value $v[i]$, and a knapsack of capacity $W$:  
**Find the maximum total value you can carry.**

#### Recurrence
```
dp[i][w] = maximum value using first i items with capacity w

Base case:  dp[0][w] = 0   for all w   (no items → no value)

Recurrence:
  if w[i] > w :  dp[i][w] = dp[i-1][w]                     ← item too heavy, skip
  else         :  dp[i][w] = max(
                      dp[i-1][w],                            ← skip item i
                      dp[i-1][w - w[i]] + v[i]              ← take item i
                  )

Answer: dp[N][W]
```

#### Steps
1. Build a 2D table `dp` of size `(n+1) × (W+1)` initialised to `0`.
2. For each item `i` (1 to n), for each capacity `w` (0 to W): apply recurrence.
3. `dp[n][W]` is the answer.

#### Complexity
| | |
|:---|:---|
| **Time** | $\mathcal{O}(N \times W)$ — filling the DP table |
| **Space** | $\mathcal{O}(N \times W)$ — DP table *(reducible to $\mathcal{O}(W)$ with 1D rolling array)* |

#### Why not Greedy?
Greedy (pick by value/weight ratio) **fails** for 0/1 Knapsack because you cannot take fractions — taking the "best ratio" item may leave a gap in the bag that a combination of smaller items could fill better.

---

### 🎒 Fractional Knapsack — `knapsack_fractional.py`

**Technique:** Greedy — sort by value-to-weight ratio  
**Type:** Fractional Choice (can take any fraction of an item)

#### Problem Statement
Same as 0/1, but you **can take fractions of items**.

#### Greedy Criterion
```
ratio[i] = v[i] / w[i]    (value per unit weight)

Sort items by ratio descending.

For each item (sorted):
    take = min(w[i], remaining_capacity)
    profit += take × (v[i] / w[i])
    remaining_capacity -= take
```

#### Why Greedy is Optimal Here
The **exchange argument** proves it: swapping any fraction of a lower-ratio item for a fraction of the highest-ratio item never decreases total profit. This argument **does not hold** for 0/1 Knapsack because items can't be split.

#### Complexity
| | |
|:---|:---|
| **Time** | $\mathcal{O}(N \log N)$ — dominated by sorting |
| **Space** | $\mathcal{O}(N)$ — item list with ratios |

---

## 0/1 vs Fractional Knapsack — Comparison

| | 0/1 Knapsack | Fractional Knapsack |
|:---|:---|:---|
| **Item Choice** | Whole item only (0 or 1) | Any fraction allowed |
| **Technique** | Dynamic Programming | Greedy |
| **Time** | $O(N \times W)$ | $O(N \log N)$ |
| **Space** | $O(N \times W)$ | $O(N)$ |
| **Optimal Greedy?** | ❌ No — DP required | ✅ Yes |

---

### 🔤 Longest Common Subsequence (LCS) — `longest_common_subsequence.py`

Length (and actual reconstruction) of the longest subsequence common to two strings, characters not required to be contiguous.

| | |
|:---|:---|
| **Time** | $\mathcal{O}(N \times M)$ |
| **Space** | $\mathcal{O}(N \times M)$ |

---

### 📈 Longest Increasing Subsequence (LIS) — `longest_increasing_subsequence.py`

Length of the longest strictly-increasing subsequence, using the classic O(N²) tabulation (`dp[i]` = LIS ending at index `i`).

| | |
|:---|:---|
| **Time** | $\mathcal{O}(N^2)$ |
| **Space** | $\mathcal{O}(N)$ |

---

### 🪙 Coin Change — `coin_change.py`

Two related questions with unlimited coin supply: minimum coins to make an amount, and number of distinct combinations that make it.

| | |
|:---|:---|
| **Time** | $\mathcal{O}(\text{amount} \times \text{coins})$ |
| **Space** | $\mathcal{O}(\text{amount})$ |

---

### ✏️ Edit Distance (Levenshtein) — `edit_distance.py`

Minimum insert/delete/replace operations to transform one string into another.

| | |
|:---|:---|
| **Time** | $\mathcal{O}(N \times M)$ |
| **Space** | $\mathcal{O}(N \times M)$ |

---

### 🏠 House Robber — `house_robber.py`

Maximum sum obtainable without picking two adjacent elements — the O(1)-space rolling variant of a 1D DP.

| | |
|:---|:---|
| **Time** | $\mathcal{O}(N)$ |
| **Space** | $\mathcal{O}(1)$ |

---

### 🎯 Subset Sum — `subset_sum.py`

Whether any subset of a set of numbers sums to exactly a target — the reachability (boolean) variant of 0/1 knapsack.

| | |
|:---|:---|
| **Time** | $\mathcal{O}(N \times \text{target})$ |
| **Space** | $\mathcal{O}(N \times \text{target})$ |

---

### 🔁 Longest Palindromic Subsequence — `longest_palindromic_subsequence.py`

Length of the longest subsequence that reads the same forwards and backwards — interval DP over substring ranges.

| | |
|:---|:---|
| **Time** | $\mathcal{O}(N^2)$ |
| **Space** | $\mathcal{O}(N^2)$ |

---

### 🔗 Matrix Chain Multiplication — `matrix_chain_multiplication.py`

Minimum scalar multiplications to multiply a chain of matrices, by finding the optimal parenthesisation — interval DP trying every split point.

| | |
|:---|:---|
| **Time** | $\mathcal{O}(N^3)$ |
| **Space** | $\mathcal{O}(N^2)$ |

---

## How to Run

```bash
# 0/1 Knapsack
python ./dsa/dp/knapsack_01.py
# Enter: number of items, weights, values, capacity

# Fractional Knapsack
python ./dsa/dp/knapsack_fractional.py
# Enter: number of items, weights, values, capacity

# Longest Common Subsequence
python ./dsa/dp/longest_common_subsequence.py

# Longest Increasing Subsequence
python ./dsa/dp/longest_increasing_subsequence.py

# Coin Change
python ./dsa/dp/coin_change.py

# Edit Distance
python ./dsa/dp/edit_distance.py

# House Robber
python ./dsa/dp/house_robber.py

# Subset Sum
python ./dsa/dp/subset_sum.py

# Longest Palindromic Subsequence
python ./dsa/dp/longest_palindromic_subsequence.py

# Matrix Chain Multiplication
python ./dsa/dp/matrix_chain_multiplication.py
```

### Example (0/1 Knapsack)
```
enter number of items: 3
enter weights separated by space: 2 3 4
enter values separated by space: 3 4 5
enter knapsack capacity: 5
maximum value: 7
```

### Example (Fractional Knapsack)
```
enter number of items: 3
enter weights separated by space: 10 20 30
enter values separated by space: 60 100 120
enter knapsack capacity: 50
maximum value: 240.0
```
