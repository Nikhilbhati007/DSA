class Solution(object):
    def removeCoveredIntervals(self, intv):
        n = len(intv)
        ans = n

        intv.sort(key=lambda x: (x[0], -x[1]))

        max_end = intv[0][1]

        for i in range(1, n):
            if intv[i][1] <= max_end:
                ans -= 1
            else:
                max_end = intv[i][1]

        return ans