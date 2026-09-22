class Solution:
    def shortestToChar(self, s,c):
        n = len(s)
        ans = [n] * n
        dist = n
        for i in range(n):
            if s[i] == c:
                dist = 0
            else:
                dist += 1
            ans[i] = dist
        dist = n
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                dist = 0
            else:
                dist += 1
            ans[i] = min(ans[i], dist)

        return ans