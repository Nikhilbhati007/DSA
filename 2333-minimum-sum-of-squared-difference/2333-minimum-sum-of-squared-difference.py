class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diffarr = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diffarr) <= k:
            return 0

        low, high = 0, max(diffarr)

        while low < high:
            mid = (low + high) // 2
            operations = sum(max(0, x - mid) for x in diffarr)

            if operations <= k:
                high = mid
            else:
                low = mid + 1

        ans = 0
        for x in diffarr:
            ans += min(x, low) ** 2

        remaining = k - sum(max(0, x - low) for x in diffarr)

        for i in range(len(diffarr)):
            if remaining == 0:
                break
            if diffarr[i] >= low:
                ans -= low ** 2
                ans += (low - 1) ** 2
                remaining -= 1

        return ans