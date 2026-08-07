class Solution(object):
    def minOperations(self, nums, x):
        n=len(nums)
        Tsum=sum(nums)
        k=Tsum-x
        if k < 0:
            return -1
        if k == 0:
            return n
        l=0
        curr=0
        length=-1
        for i in range(n):
            curr+=nums[i]
            while curr>k:
                curr-=nums[l]
                l+=1
            if curr==k:
                length=max(length,i-l+1)
        if length==-1:
            return -1
        return n-length


            



        