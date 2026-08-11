class Solution(object):
    def missingInteger(self, nums):
        n = len(nums)
        total = nums[0]
        i = 1
        while i < n and nums[i] == nums[i - 1] + 1:
            total += nums[i]
            i += 1
        s = set(nums)
        while total in s:
            total += 1
        return total