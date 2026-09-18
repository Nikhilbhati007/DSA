class Solution(object):
    def isPerfectSquare(self, num):
        l=1
        h=num
        while (l<=h):
            mid=(l+h)//2
            if mid*mid==num:
                return True
            elif mid*mid>num:
                h=mid-1
            else:
                l=mid+1
        return False
