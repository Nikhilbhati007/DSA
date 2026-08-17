class Solution(object):
    def transformArray(self, nums):
        n=len(nums)
        for i in range(n):
            if nums[i]%2==0:
                nums[i]=0
            else:
                nums[i]=1
        nums.sort()
        return nums