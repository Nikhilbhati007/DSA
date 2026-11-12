class Solution(object):
    def longestMonotonicSubarray(self, nums):
        n = len(nums)
        length = 1
        l = 0
        r = 1
        while (r<n):
            if nums[r] > nums[r-1]:
                while r < n and nums[r] > nums[r-1]:
                    length = max(length, r-l+1)
                    r += 1

            elif nums[r] < nums[r-1]:
                while r < n and nums[r] < nums[r-1]:
                    length = max(length, r-l+1)
                    r += 1
            else:
                r += 1

            l = r-1

        return length