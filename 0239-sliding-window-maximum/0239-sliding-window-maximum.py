from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        dq = deque()
        n = len(nums)
        res = []
        for i in range(n):
            # Remove indices outside the current window
            if dq and dq[0] <= i - k:
                dq.popleft()
            # Remove smaller elements from the back
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            # Add current index
            dq.append(i)
            # Start recording answers when the first window is complete
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res
