class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        n=len(s)
        minlength=float('inf')
        l,r=0,0
        ans=""
        ones=0
        while r<n:
            if s[r]=='1':
                ones+=1
            if k==ones:
                while k == ones:
                    length = r - l + 1
                    if length < minlength:
                        minlength = length
                        ans = s[l:r+1]
                    elif length == minlength:
                        ans = min(ans, s[l:r+1])
                    if s[l] == '1':
                        ones -= 1
                    l+=1
            r+=1
        return ans

