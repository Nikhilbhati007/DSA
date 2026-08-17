class Solution(object):
    def transformArray(self, nums):
        n=len(nums)
        for i in range(n):
            if nums[i]%2==0:
                nums[i]=0
            else:
                nums[i]=1
        i = 0
        while i < n and nums[i] != 1:
            i += 1
        j = i + 1
        while j < n:
            if nums[j] != 1:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1

        return nums