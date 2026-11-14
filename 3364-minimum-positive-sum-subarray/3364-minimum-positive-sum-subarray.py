from bisect import bisect_left

class Solution(object):
    def minimumSumSubarray(self, nums, l, r):

        n = len(nums)

        # Prefix sum
        pref = [0] * (n + 1)

        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        # Coordinate compression
        vals = sorted(set(pref))
        m = len(vals)

        def getRank(x):
            return bisect_left(vals, x) + 1

        # Fenwick Tree
        bit = [0] * (m + 1)

        def update(i, val):
            while i <= m:
                bit[i] += val
                i += i & -i

        def query(i):
            ans = 0

            while i > 0:
                ans += bit[i]
                i -= i & -i

            return ans

        # Find kth smallest element
        def findKth(k):
            idx = 0
            mask = 1 << (m.bit_length() - 1)

            while mask:
                nxt = idx + mask

                if nxt <= m and bit[nxt] < k:
                    idx = nxt
                    k -= bit[nxt]

                mask >>= 1

            return idx + 1

        ans = float('inf')

        for i in range(l, n + 1):

            # Add valid left prefix
            update(getRank(pref[i - l]), 1)

            # Remove expired prefix
            if i - r - 1 >= 0:
                update(getRank(pref[i - r - 1]), -1)

            # Find largest prefix strictly smaller than pref[i]
            rank = getRank(pref[i]) - 1

            cnt = query(rank)

            if cnt > 0:
                pos = findKth(cnt)

                best = vals[pos - 1]

                curr = pref[i] - best

                ans = min(ans, curr)

        return ans if ans != float('inf') else -1