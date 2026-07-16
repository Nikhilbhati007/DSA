class Solution(object):
    def totalMoney(self, n):
        ans = 0
        strt = 1

        for i in range(n):
            ans += strt + (i % 7)

            if (i + 1) % 7 == 0:
                strt += 1

        return ans