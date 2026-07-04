class Solution(object):
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])

        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]

        dp[0][1] = 0
        # You could also use dp[1][0] = 0 instead.

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i - 1][j - 1]

        return dp[m][n]