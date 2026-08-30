class Solution(object):
    def minimumDeletions(self, nums):
        n = len(nums)
        min_i = nums.index(min(nums))
        max_i = nums.index(max(nums))
        left = min(min_i, max_i)
        right = max(min_i, max_i)
        front = right + 1
        back = n - left
        both = (left + 1) + (n - right)
        return min(front, back, both)