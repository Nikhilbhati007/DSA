class Solution(object):
    def minimumRounds(self, tasks):
        freq={}
        for i in tasks:
            freq[i]=freq.get(i,0)+1
        ans = 0
        for i in freq.values():
            if i == 1:
                return -1
            ans += (i + 2) // 3
        return ans