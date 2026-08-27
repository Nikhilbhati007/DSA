class Solution(object):
    def subArrayRanges(self, nums):
        #ans=abs(subarr_min(nums)-subarr_max(nums))
        #return ans
        n=len(nums)
        ans=0
        for i in range(n):
            mini=nums[i]
            maxi=nums[i]
            for j in range(i+1,n):
                mini=min(mini,nums[j])
                maxi=max(maxi,nums[j])
                ans+=abs(mini-maxi)
        return ans
        