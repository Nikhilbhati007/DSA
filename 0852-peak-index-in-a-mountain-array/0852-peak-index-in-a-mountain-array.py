class Solution(object):
    def peakIndexInMountainArray(self,nums):
        n=len(nums)
        if n==1:
            return 0
        if nums[0]>nums[1]:
            return 0
        if nums[n-1]>nums[n-2]:
            return n-1
        low=1
        high=n-2
        while(low<=high):
            mid= low + (high - low)//2
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            if nums[mid]<nums[mid+1]:
                low=mid+1
            else:
                high=mid-1