class Solution(object):
    def maxProduct(self, n):
        l=[]
        while n!=0:
            rem=n%10
            l.append(rem)
            n=n//10
        k=len(l)
        l.sort(reverse=True)
        return l[0]*l[1]