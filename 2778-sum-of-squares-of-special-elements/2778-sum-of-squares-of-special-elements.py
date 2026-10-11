class Solution(object):
    def sumOfSquares(self, nums):
        sqsum=0
        n=len(nums)
        for i in range(n):
            if n%(i+1)==0:
                sqsum+=(nums[i])**2
        return sqsum

        