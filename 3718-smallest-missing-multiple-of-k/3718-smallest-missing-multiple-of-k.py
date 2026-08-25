class Solution(object):
    def missingMultiple(self, nums, k):
        n=len(nums)
        for i in range(1,n+1):
            if i*k not in nums:
                return i*k
        return (n+1)*k