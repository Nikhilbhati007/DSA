class Solution(object):
    def minMoves2(self, nums):
        nums.sort()
        median = nums[len(nums) // 2]

        mov = 0
        for i in range(len(nums)):
            mov += abs(median - nums[i])

        return mov