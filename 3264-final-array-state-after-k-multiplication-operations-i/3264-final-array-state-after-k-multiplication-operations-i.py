class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        n = len(nums)

        while k > 0:
            min_idx = 0

            # Find the first occurrence of the minimum element
            for i in range(1, n):
                if nums[i] < nums[min_idx]:
                    min_idx = i

            # Multiply the minimum element
            nums[min_idx] *= multiplier
            k -= 1

        return nums