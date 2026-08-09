class Solution(object):
    def maximumSubarraySum(self, nums, k):
        n = len(nums)

        l = 0
        currsum = 0
        maxsum = 0
        freq = {}

        for r in range(n):
            currsum += nums[r]
            freq[nums[r]] = freq.get(nums[r], 0) + 1

            if r - l + 1 > k:
                freq[nums[l]] -= 1
                currsum -= nums[l]

                if freq[nums[l]] == 0:
                    del freq[nums[l]]

                l += 1

            if r - l + 1 == k and len(freq) == k:
                maxsum = max(maxsum, currsum)

        return maxsum