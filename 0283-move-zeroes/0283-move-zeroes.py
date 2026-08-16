class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        i = 0
        while i < n and nums[i] != 0:
            i += 1
        j = i + 1
        while j < n:
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1