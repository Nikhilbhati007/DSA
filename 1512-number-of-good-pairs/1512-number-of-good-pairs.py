class Solution(object):
    def numIdenticalPairs(self, nums):
        freq = {}
        ans = 0

        for num in nums:
            ans += freq.get(num, 0)
            freq[num] = freq.get(num, 0) + 1

        return ans