class Solution(object):
    def firstUniqueEven(self, nums):
        n=len(nums)
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for i in nums:
            if i%2==0 and freq[i]==1:
                return i
        return -1

        