class Solution(object):
    def characterReplacement(self, s, k):
        #use sliding window
        freq=[0]*256
        n=len(s)
        l=0
        r=0
        maxlength=-1
        while(r<n):
            freq[ord(s[r])]+=1
            while (r-l+1)-max(freq)>k:
                freq[ord(s[l])]-=1
                l+=1
            maxlength=max(maxlength,r-l+1)
            r+=1
        return maxlength


