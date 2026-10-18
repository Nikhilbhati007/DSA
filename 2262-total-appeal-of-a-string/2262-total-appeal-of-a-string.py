class Solution(object):
    def appealSum(self, s):
        n = len(s)
        ans = 0
        last = {}
        curr = 0 
        for i in range(n):
            ch = s[i]
            curr += i - last.get(ch, -1)
            last[ch] = i
            ans += curr
        return ans