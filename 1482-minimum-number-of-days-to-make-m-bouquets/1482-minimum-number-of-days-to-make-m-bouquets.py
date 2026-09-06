class Solution(object):
    def minDays(self, bloomDay, m, k):
        n=len(bloomDay)
        if n<(m*k):
            return -1
        l=min(bloomDay)
        h=max(bloomDay)
        out=max(bloomDay)
        while (l<=h):
            mid=(l+h)//2
            cnt=0
            ans=0
            for i in range(n):
                if bloomDay[i]<=mid:
                    cnt+=1
                else:
                    ans=ans+cnt//k
                    cnt=0
            ans += cnt // k
            if ans>=m:
                out=mid
                h=mid-1
            else:
                l=mid+1
        return out