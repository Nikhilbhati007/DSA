class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        n = len(nums1)
        m = len(nums2)

        idx1 = (n + m) // 2
        idx2 = idx1 - 1

        i = j = 0
        cnt = 0
        ele1 = ele2 = -1

        while i < n and j < m:
            if nums1[i] < nums2[j]:
                if cnt == idx1:
                    ele1 = nums1[i]
                if cnt == idx2:
                    ele2 = nums1[i]
                i += 1
            else:
                if cnt == idx1:
                    ele1 = nums2[j]
                if cnt == idx2:
                    ele2 = nums2[j]
                j += 1
            cnt += 1

        while i < n:
            if cnt == idx1:
                ele1 = nums1[i]
            if cnt == idx2:
                ele2 = nums1[i]
            i += 1
            cnt += 1

        while j < m:
            if cnt == idx1:
                ele1 = nums2[j]
            if cnt == idx2:
                ele2 = nums2[j]
            j += 1
            cnt += 1

        if (n + m) % 2 == 1:
            return ele1

        return (ele1 + ele2) / 2.0