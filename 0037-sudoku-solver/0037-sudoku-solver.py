class Solution(object):
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    empty.append((i, j))
                else:
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[(i // 3) * 3 + j // 3].add(num)

        def solver(pos):
            if pos == len(empty):
                return True

            best = pos
            best_candidates = None

            for k in range(pos, len(empty)):
                r, c = empty[k]
                b = (r // 3) * 3 + c // 3

                candidates = [
                    num for num in "123456789"
                    if num not in rows[r]
                    and num not in cols[c]
                    and num not in boxes[b]
                ]

                if best_candidates is None or len(candidates) < len(best_candidates):
                    best = k
                    best_candidates = candidates

                if len(best_candidates) == 0:
                    return False

                if len(best_candidates) == 1:
                    break

            empty[pos], empty[best] = empty[best], empty[pos]

            r, c = empty[pos]
            b = (r // 3) * 3 + c // 3

            candidates = [
                num for num in "123456789"
                if num not in rows[r]
                and num not in cols[c]
                and num not in boxes[b]
            ]

            for num in candidates:
                board[r][c] = num
                rows[r].add(num)
                cols[c].add(num)
                boxes[b].add(num)

                if solver(pos + 1):
                    return True

                board[r][c] = "."
                rows[r].remove(num)
                cols[c].remove(num)
                boxes[b].remove(num)

            empty[pos], empty[best] = empty[best], empty[pos]
            return False

        solver(0)