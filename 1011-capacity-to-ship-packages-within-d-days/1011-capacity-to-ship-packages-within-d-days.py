class Solution(object):
    def shipWithinDays(self,nums,k):
        n=len(nums)
        l=max(nums)
        h=sum(nums)
        min_cap=0
        while(l<=h):
            mid=(l+h)//2
            day=1
            load=0
            for i in range(n):
                if (load+nums[i])>mid:
                    day+=1
                    load=nums[i]
                else:
                    load+=nums[i]
            if day<=k:
                min_cap=mid
                h=mid-1
            else:
                l=mid+1
        return min_cap

