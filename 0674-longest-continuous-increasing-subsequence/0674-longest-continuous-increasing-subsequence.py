class Solution(object):
    def findLengthOfLCIS(self, nums):
        n=len(nums)
        #using two pointer
        n = len(nums)
        if n == 0:
            return 0
        i = 0
        j = 1
        ans = 1
        while j < n:
            if nums[j - 1] < nums[j]:
                ans = max(ans, j - i + 1)
            else:
                i = j
            j += 1

        return ans
        