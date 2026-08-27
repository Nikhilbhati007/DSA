class Solution(object):
    def removeTrailingZeros(self, num):
        n=len(num)
        r=n-1
        while (num[r]=='0'):
            r-=1
        num=num[:r+1]
        return num