class Solution(object):
    def areOccurrencesEqual(self, s):
        freq={}
        for i in s:
            freq[i]=freq.get(i,0)+1
        cd=freq[s[0]]
        for i,j in freq.items():
            if j!=cd:
                return False
        return True
        
        