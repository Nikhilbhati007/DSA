class Solution:
    def countCommas(self, n):
        total = 0
        x = 1000

        while x <= n:
            total += n - x + 1
            x *= 1000

        return total