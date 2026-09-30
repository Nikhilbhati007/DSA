class Solution(object):
    def findPairs(self, nums, k):
        if k < 0:
            return 0

        freq = {}

        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        if k == 0:
            return sum(freq[x] > 1 for x in freq)

        cnt = 0

        for x in freq:
            if x + k in freq:
                cnt += 1

        return cnt