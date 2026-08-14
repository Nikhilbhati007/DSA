class Solution(object):
    def countSubarrays(self, nums):
        n=len(nums)
        cnt=0
        for i in range(n-2):
            j=i+2
            if 2*(nums[i]+nums[j])==nums[i + 1]:
                cnt+=1
        return cnt
        
        