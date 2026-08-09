class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        def binary_sum(nums,k):
            if k<0:
                return 0
            n=len(nums)
            l,r,cnt,bsum=0,0,0,0
            while(r<n):
                bsum+=nums[r]
                while bsum>k:
                    bsum-=nums[l]
                    l+=1
                cnt+=r-l+1
                r+=1
            return cnt
        ans=binary_sum(nums,goal)-binary_sum(nums,goal-1)
        return ans

        
        