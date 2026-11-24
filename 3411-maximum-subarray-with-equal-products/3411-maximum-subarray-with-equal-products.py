class Solution:
    def maxLength(self, nums):

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        n = len(nums)

        if n == 1:
            return 1 if nums[0] == 1 else 0

        left = 0
        ans = 2

        for right in xrange(n):

            while any(gcd(nums[right], nums[i]) > 1
                      for i in xrange(left, right)):

                left += 1

            ans = max(ans, right - left + 1)

        return ans