class Solution(object):
    def applyOperations(self, nums):
        n=len(nums)
        for i in range(1,n):
            if nums[i-1]==nums[i]:
                nums[i-1]*=2
                nums[i]=0
        l=0
        while l<n and nums[l]!=0:
            l+=1
        r=l+1
        while r<n:
            if nums[r]!=0:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
            r+=1
        return nums

        