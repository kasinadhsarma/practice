"""
Matrix Chain Multiplication
------------------------------
Technique : Dynamic Programming (interval DP over chain ranges)
Idea      : Given a chain of matrices to multiply together, matrix
            multiplication is associative but the total scalar-multiplication
            cost depends heavily on HOW they are grouped (parenthesised).
            Find the grouping that minimises total cost, by trying every
            possible split point for every sub-chain.

Formula / Recurrence
    Matrix i has dimensions dims[i-1] x dims[i]  (for i = 1..n)

    dp[i][j] = minimum cost to multiply matrices i through j

    Base case  : dp[i][i] = 0  (a single matrix needs no multiplication)

    Recurrence : try every split point k between i and j
        dp[i][j] = min over k in [i, j-1] of:
            dp[i][k] + dp[k+1][j] + dims[i-1] * dims[k] * dims[j]
                                     ^ cost of the final multiply at this split

    Answer : dp[1][n]

Steps
    1. Process sub-chains by increasing length (2, 3, ..., n matrices).
    2. For each sub-chain (i, j), try every split point k and keep the
       cheapest combination of (left cost + right cost + merge cost).
    3. dp[1][n] holds the minimum total scalar multiplications needed to
       multiply the entire chain, however it needs to be parenthesised.

Time  Complexity : O(N^3)  — O(N^2) sub-chains, each trying O(N) split points
Space Complexity : O(N^2)  — dp table over sub-chain ranges
"""

class MatrixChainMultiplication:
    def __init__(self, dims: list):
        # dims has n+1 entries for n matrices: matrix i is dims[i-1] x dims[i]
        self.dims = dims

    def min_cost(self) -> int:
        dims = self.dims
        n = len(dims) - 1   # number of matrices
        if n <= 1:
            return 0

        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for length in range(2, n + 1):
            for i in range(1, n - length + 2):
                j = i + length - 1
                dp[i][j] = float('inf')
                for k in range(i, j):
                    cost = dp[i][k] + dp[k + 1][j] + dims[i - 1] * dims[k] * dims[j]
                    dp[i][j] = min(dp[i][j], cost)

        return dp[1][n]


dims = list(map(int, input("enter matrix dimensions separated by space (n+1 values for n matrices): ").split()))
print("minimum scalar multiplications:", MatrixChainMultiplication(dims).min_cost())
