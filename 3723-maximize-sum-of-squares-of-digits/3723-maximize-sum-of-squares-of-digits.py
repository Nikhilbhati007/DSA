class Solution(object):
    def maxSumOfSquares(self, num, sum):
        if sum > 9 * num:
            return ""

        ans = ""

        for i in range(num):
            digit = min(9, sum)
            ans += str(digit)
            sum -= digit

        return ans