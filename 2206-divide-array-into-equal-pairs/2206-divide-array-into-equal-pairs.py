class Solution(object):
    def divideArray(self, nums):
        n=len(nums)
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for j in freq.values():
            if  j%2!=0:
                return False
        return True             