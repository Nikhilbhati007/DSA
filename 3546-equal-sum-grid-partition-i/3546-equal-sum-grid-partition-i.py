class Solution(object):
    def canPartitionGrid(self, grid):
        m = len(grid)
        n = len(grid[0])
        
        total = 0
        for row in grid:
            total += sum(row)

        if total % 2:
            return False

        target = total // 2

        # Horizontal cuts
        curr = 0
        for i in range(m - 1):       # cut after row i
            curr += sum(grid[i])
            if curr == target:
                return True

        # Vertical cuts
        curr = 0
        for j in range(n - 1):       # cut after column j
            colSum = 0
            for i in range(m):
                colSum += grid[i][j]
            curr += colSum
            if curr == target:
                return True

        return False