class Solution(object):
    def mySqrt(self, n):
        
        # using binary search
        l=1
        h=n
        ans=0
        while  (l<=h):
            mid=(l+h)//2
            if mid*mid<=n:
                ans=mid
                l=mid+1
            else:
                h=mid-1
        return ans