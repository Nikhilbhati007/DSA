class Solution(object):
    def maxAscendingSum(self, nums):
        n=len(nums)
        maxsum=nums[0]
        prev=nums[0]
        l=1
        currsum=nums[0]
        while(l<n):
            if nums[l]<=prev:
                currsum=0
            currsum+=nums[l]
            prev=nums[l]
            maxsum=max(maxsum,currsum)
            l+=1
        return maxsum

        