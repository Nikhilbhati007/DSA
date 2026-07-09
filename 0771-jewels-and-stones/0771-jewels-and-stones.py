class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        cnt=0
        for i in stones:
            if i in jewels:
                cnt+=1
        return cnt