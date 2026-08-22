class Solution(object):
    def isMiddleElementUnique(self, nums):
        n=len(nums)
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        j=n//2
        if freq[nums[j]]>1:
            return False
        else:
            return True 