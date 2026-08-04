class Solution(object):
    def findMissingElements(self, nums):
        small=min(nums)
        large=max(nums)
        l=[]
        for i in range(small,large+1):
            if i not in nums:
                l.append(i)
        return l
