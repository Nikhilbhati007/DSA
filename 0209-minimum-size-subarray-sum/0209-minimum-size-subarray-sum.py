class Solution(object):
    def minSubArrayLen(self, target, nums):
        n=len(nums)
        l,r=0,0
        minlength=float('inf')
        currsum=0
        while(r<n):
            currsum+=nums[r]
            while currsum>=target:
                minlength=min(minlength,r-l+1)
                currsum-=nums[l]
                l+=1
            r+=1
        if minlength==float('inf'):
            return 0
        return minlength
        