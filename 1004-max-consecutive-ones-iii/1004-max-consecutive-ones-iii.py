class Solution(object):
    def longestOnes(self, nums, k):
        freqone=0
        n=len(nums)
        l,r=0,0
        maxlength=-1
        while (r<n):
            if nums[r]==1:
                freqone+=1
            while (r-l+1)-freqone>k:
                if nums[l]==1:
                    freqone-=1
                l+=1
            maxlength=max(maxlength,r-l+1)
            r+=1
        return maxlength

