class Solution(object):
    def largestInteger(self, nums, k):
        n = len(nums)
        m = n - k + 1
        pos = {}
        for i, x in enumerate(nums):
            if x not in pos:
                pos[x] = []
            pos[x].append(i)
        ans = -1
        for x, positions in pos.items():
            total = 0
            first = True
            for p in positions:
                L = max(0, p - k + 1)
                R = min(p, m - 1)

                if first:
                    curL = L
                    curR = R
                    first = False
                elif L <= curR + 1:
                    curR = max(curR, R)
                else:
                    total += curR - curL + 1
                    curL = L
                    curR = R

            if not first:
                total += curR - curL + 1
            if total == 1:
                ans = max(ans, x)

        return ans