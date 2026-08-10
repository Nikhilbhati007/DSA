class Solution(object):
    def minWindow(self, s, t):
        n=len(s)
        m=len(t)
        freq=[0]*256
        l,r=0,0
        s_idx=-1
        cnt=0
        minlength=float('inf')
        for i in range(m):
            freq[ord(t[i])] += 1
        while(r<n):
            if (freq[ord(s[r])]>0):
                cnt+=1
            freq[ord(s[r])]-=1
            while(cnt==m):
                if r - l + 1 < minlength:
                    minlength = r - l + 1
                    s_idx = l
                freq[ord(s[l])] += 1

                if freq[ord(s[l])] > 0:
                    cnt -= 1
                l+=1
            r+=1
        if s_idx == -1:
            return ""

        return s[s_idx:s_idx + minlength]
        