class Solution(object):
    def minimumAddedInteger(self, nums1, nums2):
        nums1.sort()
        nums2.sort()

        def check(x):
            i = j = 0
            removed = 0

            while i < len(nums1) and j < len(nums2):
                if nums1[i] + x == nums2[j]:
                    i += 1
                    j += 1
                else:
                    removed += 1
                    i += 1
                    if removed > 2:
                        return False

            removed += len(nums1) - i
            return removed == 2

        ans = float('inf')

        for i in range(3):
            x = nums2[0] - nums1[i]
            if check(x):
                ans = min(ans, x)

        return ans