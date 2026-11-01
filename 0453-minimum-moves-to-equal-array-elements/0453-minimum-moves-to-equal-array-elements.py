class Solution(object):
    def minMoves(self, nums):
        n=len(nums)
        minele=min(nums)
        mov=0
        for i in range(n):
            mov+=nums[i]-minele
        return mov
