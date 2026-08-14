class Solution(object):
    def largestInteger(self, n, s):
        if s>(n*9):
            return -1
        if s == 0:
            return 0

        ans = ""

        while n > 0:
            digit = min(9, s)
            ans += str(digit)
            s -= digit
            n -= 1

        return int(ans)