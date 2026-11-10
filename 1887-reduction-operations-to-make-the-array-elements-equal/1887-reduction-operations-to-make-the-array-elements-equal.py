class Solution(object):
    def reductionOperations(self, nums):
        nums.sort()
        ans = 0
        count = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                count += 1
            ans += count

        return ans