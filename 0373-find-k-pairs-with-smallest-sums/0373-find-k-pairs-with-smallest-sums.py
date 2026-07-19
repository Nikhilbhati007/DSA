import heapq

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        if not nums1 or not nums2:
            return []

        heap = []

        # Push first element from each row
        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        ans = []

        while heap and len(ans) < k:
            s, i, j = heapq.heappop(heap)
            ans.append([nums1[i], nums2[j]])

            if j + 1 < len(nums2):
                heapq.heappush(heap,
                               (nums1[i] + nums2[j + 1], i, j + 1))

        return ans