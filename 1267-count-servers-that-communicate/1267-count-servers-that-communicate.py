class Solution(object):
    def countServers(self, grid):
        n = len(grid)
        m = len(grid[0])

        row = [0] * n
        col = [0] * m

        # Count servers in each row and column
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    row[i] += 1
                    col[j] += 1

        ans = 0

        # Count each communicating server once
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    if row[i] > 1 or col[j] > 1:
                        ans += 1

        return ans