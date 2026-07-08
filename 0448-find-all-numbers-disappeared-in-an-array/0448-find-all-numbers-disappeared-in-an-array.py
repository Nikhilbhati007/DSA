class Solution(object):
    def findDisappearedNumbers(self, nums):
        n=len(nums)
        freq={}
        for i in range(1, n+1):
            freq[i] = 0
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        l=[]
        for i,j in freq.items():
            if j==0:
                l.append(i)
        return l