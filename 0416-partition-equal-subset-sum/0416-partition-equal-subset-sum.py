class Solution(object):
    def canPartition(self, nums):
        total = sum(nums)

        # If total sum is odd, partition is impossible
        if total % 2 != 0:
            return False

        target = total // 2

        # dp[j] = True if sum j can be formed
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            # Traverse backwards for 0/1 Knapsack
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[target]