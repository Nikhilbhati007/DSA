class Solution(object):
    def checkDivisibility(self, n):
        digsum=0
        digprod=1
        temp=n
        while temp!=0:
            rem=temp%10
            digsum+=rem
            digprod*=rem
            temp=temp//10
        div=digsum+digprod
        if n%div==0:
            return True
        else:
            return False
