class Solution(object):
    def smallestDivisor(self, nums,k):
        n=len(nums)
        if k<n:
            return -1
        l=1
        h=max(nums)
        out=0
        while(l<=h):
            mid=(l+h)//2
            ans=0
            for i in range(n):
                # ceil(a/b)=(a+b-1)//b
                ceil_val=(nums[i]+mid-1)//mid
                ans=ans+ceil_val
            if ans<=k:
                out=mid
                h=mid-1
            else:
                l=mid+1
        return out
    
            
