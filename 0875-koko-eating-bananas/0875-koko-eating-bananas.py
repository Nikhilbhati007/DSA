class Solution(object):
    def minEatingSpeed(self, piles, k):
        l=1
        h=max(piles)
        while l<=h:
            mid=(l+h)//2
            hrs=0
            for i in piles:
                hrs+=(i+mid-1)//mid
            if hrs<=k:
                h=mid-1
            else:
                l=mid+1
        return l



        