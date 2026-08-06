class Solution(object):
    def firstMissingPositive(self, nums):
        nums=list(set(nums))
        n=len(nums)
        nums.sort()
        res=[]
        count=0
        for i in range(n):
            if nums[i]<=0:
                count=count+1
        k=n-count
        if k==0:
            return 1
        for i in range(k):
            res.append(i+1)
        j=0
        for j in range(k):
            if res[j]!=nums[count+j]:
                return res[j]
                break
        return (res[j]+1)


        