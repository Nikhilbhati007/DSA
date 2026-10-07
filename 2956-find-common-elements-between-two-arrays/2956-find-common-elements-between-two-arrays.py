class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        ans1 = 0
        ans2 = 0

        freq1 = {}
        freq2 = {}

        for i in nums1:
            freq1[i] = freq1.get(i, 0) + 1

        for i in nums2:
            freq2[i] = freq2.get(i, 0) + 1

        for i in nums1:
            if i in freq2:
                ans1 += 1

        for j in nums2:
            if j in freq1:
                ans2 += 1

        return [ans1, ans2]