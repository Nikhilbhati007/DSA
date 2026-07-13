class Solution(object):
    def countBeautifulPairs(self, nums):
        freq = [0] * 10
        ans = 0

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        for num in nums:
            last = num % 10

            # Count all previous first digits that are coprime with last
            for first in range(1, 10):
                if gcd(first, last) == 1:
                    ans += freq[first]

            # Find first digit of current number
            first = num
            while first >= 10:
                first //= 10

            freq[first] += 1

        return ans