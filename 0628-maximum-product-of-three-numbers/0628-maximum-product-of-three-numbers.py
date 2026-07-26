class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        n = len(nums)
        prod1 = nums[n-1] * nums[n-2] * nums[n-3]
        prod2 = nums[0] * nums[1] * nums[n-1]

        return max(prod1, prod2)
