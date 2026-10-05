class Solution(object):
    def splitArray(self, nums,m):
        def no_students(nums,page):
            std=1
            pgstd=0
            for i in range(len(nums)):
                if pgstd+nums[i]<=page:
                    pgstd+=nums[i]
                else:
                    std+=1
                    pgstd=nums[i]
            return std
        l=max(nums)
        h=sum(nums)
        ans=0
        while (l<=h):
            mid=(l+h)//2
            students = no_students(nums, mid)
            if students <= m:                
                ans = mid
                h = mid - 1
            else:
                l=mid+1
        return ans