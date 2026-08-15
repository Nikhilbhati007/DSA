class Solution(object):
    def longestSubsequence(self, nums):
        n = len(nums)
        xr = 0
        for x in nums:
            xr ^= x
        if xr != 0:
            return n
        for x in nums:
            if x != 0:
                return n - 1
        return 0