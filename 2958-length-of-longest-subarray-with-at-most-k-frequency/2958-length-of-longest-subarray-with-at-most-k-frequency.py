class Solution(object):
    def maxSubarrayLength(self, nums, k):
        freq={}
        n=len(nums)
        maxlen=0
        l,r=0,0
        while(r<n):
            freq[nums[r]]=freq.get(nums[r],0)+1
            while freq[nums[r]]>k:
                freq[nums[l]]-=1
                l+=1
            maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen
        
        