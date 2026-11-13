class Solution(object):
    def countNonDecreasingSubarrays(self, nums, k):
        n = len(nums)

        # Prefix sum
        pref = [0] * (n + 1)

        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        # Next greater element
        nge = [n] * n
        st = []

        for i in range(n - 1, -1, -1):
            while st and nums[st[-1]] <= nums[i]:
                st.pop()

            if st:
                nge[i] = st[-1]

            st.append(i)

        # Binary lifting
        LOG = n.bit_length()

        up = [[n] * n for _ in range(LOG)]
        cost = [[0] * n for _ in range(LOG)]

        for i in range(n):
            up[0][i] = nge[i]

            j = nge[i]

            if j < n:
                cost[0][i] = (
                    nums[i] * (j - i)
                    - (pref[j] - pref[i])
                )

        for p in range(1, LOG):
            for i in range(n):
                mid = up[p - 1][i]

                if mid < n:
                    up[p][i] = up[p - 1][mid]
                    cost[p][i] = (
                        cost[p - 1][i]
                        + cost[p - 1][mid]
                    )

        # Calculate operations for [l, r]
        def getCost(l, r):
            ans = 0
            pos = l

            for p in range(LOG - 1, -1, -1):
                nxt = up[p][pos]

                if nxt <= r:
                    ans += cost[p][pos]
                    pos = nxt

            ans += (
                nums[pos] * (r - pos + 1)
                - (pref[r + 1] - pref[pos])
            )

            return ans

        # Two pointers
        ans = 0
        r = 0

        for l in range(n):
            while r + 1 < n and getCost(l, r + 1) <= k:
                r += 1

            ans += r - l + 1

        return ans