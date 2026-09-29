class Solution:
    def findShortestSubArray(self, nums):
        freq = {}
        first = {}
        last = {}
        for i, num in enumerate(nums):
            freq[num] = freq.get(num, 0) + 1
            if num not in first:
                first[num] = i
            last[num] = i
        degree = max(freq.values())
        ans = len(nums)

        for num in freq:
            if freq[num] == degree:
                ans = min(ans, last[num] - first[num] + 1)
        return ans