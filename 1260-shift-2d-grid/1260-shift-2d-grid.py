class Solution(object):
    def shiftGrid(self, grid, k):
        n=len(grid)
        m=len(grid[0])
        def shift(grid, n, m):
            last = grid[n-1][m-1]

            for i in range(n-1, -1, -1):
                for j in range(m-1, -1, -1):
                    if i == 0 and j == 0:
                        grid[0][0] = last
                    elif j == 0:
                        grid[i][0] = grid[i-1][m-1]
                    else:
                        grid[i][j] = grid[i][j-1]
        for i in range(k):
            shift(grid,n,m)
        return grid