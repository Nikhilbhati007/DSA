class Solution(object):
    def limitOccurrences(self, nums, k):
        freq = {}
        ans = []

        for i in nums:
            freq[i] = freq.get(i, 0) + 1

            if freq[i] <= k:
                ans.append(i)

        return ans
