class Solution(object):
    def maxSelectedElements(self, nums):
        nums.sort()
        dp = {}
        ans = 0
        for x in nums:
            prev = dp.get(x, 0)
            left = dp.get(x - 1, 0)
            dp[x] = max(dp.get(x, 0), left + 1, 1)
            dp[x + 1] = max(dp.get(x + 1, 0), prev + 1)
            ans = max(ans, dp[x], dp[x + 1])
        return ans