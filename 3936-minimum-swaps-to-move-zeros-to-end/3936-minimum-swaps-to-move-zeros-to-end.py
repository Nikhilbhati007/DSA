class Solution(object):
    def minimumSwaps(self, nums):
        n = len(nums)
        moves = 0
        i = 0
        j = n - 1

        while i < j:
            while i < j and nums[i] != 0:
                i += 1

            while i < j and nums[j] == 0:
                j -= 1

            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
                moves += 1
                i += 1
                j -= 1

        return moves