class Solution(object):
    def uniquePathsWithObstacles(self, grid):
        n = len(grid)
        m = len(grid[0])

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        if grid[0][0] == 0:
            dp[1][1] = 1

        for i in range(1, n + 1):
            for j in range(1, m + 1):

                if i == 1 and j == 1:
                    continue

                # From left
                if j > 1 and grid[i - 1][j - 1] == 0:
                    dp[i][j] += dp[i][j - 1]

                # From top
                if i > 1 and grid[i - 1][j - 1] == 0:
                    dp[i][j] += dp[i - 1][j]

        return dp[n][m]