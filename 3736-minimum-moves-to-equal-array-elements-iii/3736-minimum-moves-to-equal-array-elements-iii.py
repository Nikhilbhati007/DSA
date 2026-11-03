class Solution(object):
    def minMoves(self, nums):
        maxele=max(nums)
        n=len(nums)
        mov=0
        for i in range(n):
            mov+=(maxele-nums[i])
        return mov
            