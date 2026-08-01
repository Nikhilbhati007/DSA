class Solution(object):
    def winningPlayer(self, x, y):
        flag = 0

        while x >= 1 and y >= 4:
            x -= 1
            y -= 4
            flag ^= 1

        if flag == 1:
            return "Alice"
        return "Bob"