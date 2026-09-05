class Solution(object):
    def pivotInteger(self, n):
        tsum=(n*(1+n))//2
        left_sum=0
        for i in range(1,n+1):
            left_sum+=i
            if left_sum==(tsum-left_sum+i):
                return i
        return -1