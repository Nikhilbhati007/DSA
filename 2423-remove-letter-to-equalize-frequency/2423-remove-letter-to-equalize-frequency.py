class Solution(object):
    def equalFrequency(self, word):
        freq={}
        n=len(word)
        for i in word:
            freq[i]=freq.get(i,0)+1
        cnt=0
        for i,j in freq.items():
            freq[i]-=1 
            values=[v for v in freq.values() if v > 0] 
            if len(set(values))==1: 
                return True 
            freq[i]+=1 
        return False

        