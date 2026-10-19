class Solution(object):
    def solveNQueens(self, n):
        board = [["."] * n for i in range(n)]
        ans = []

        def isSafe(board, row, col, n):
            # Check horizontally to the left
            for j in range(col):
                if board[row][j] == "Q":
                    return False

            # Check upper-left diagonal
            i, j = row, col
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            # Check lower-left diagonal
            i, j = row, col
            while i < n and j >= 0:
                if board[i][j] == "Q":
                    return False
                i += 1
                j -= 1

            return True

        def solver(col, brd, ans, n):
            if col == n:
                ans.append(["".join(row) for row in brd])
                return

            for r in range(n):
                if isSafe(brd, r, col, n):
                    brd[r][col] = "Q"
                    solver(col + 1, brd, ans, n)
                    brd[r][col] = "."

        solver(0, board, ans, n)
        return ans