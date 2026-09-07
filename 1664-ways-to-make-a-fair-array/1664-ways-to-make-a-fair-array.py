class Solution(object):
    def waysToMakeFair(self, nums):
        n = len(nums)

        left_even = 0
        left_odd = 0

        # Initially, calculate sums on the right
        right_even = 0
        right_odd = 0

        for i in range(n):
            if i % 2 == 0:
                right_even += nums[i]
            else:
                right_odd += nums[i]

        ans = 0

        for i in range(n):

            # Remove current element from right side
            if i % 2 == 0:
                right_even -= nums[i]
            else:
                right_odd -= nums[i]

            # After removal:
            # right odd becomes even
            # right even becomes odd
            new_even = left_even + right_odd
            new_odd = left_odd + right_even

            if new_even == new_odd:
                ans += 1

            # Add current element to left side
            if i % 2 == 0:
                left_even += nums[i]
            else:
                left_odd += nums[i]

        return ans