class Solution(object):
    def smallestNumber(self, n, t):
        def checkdiv(n):
            temp=n
            prod=1
            while temp!=0:
                rem=temp%10
                prod*=rem
                temp=temp//10
            if prod%t==0:
                return True
            else:
                return False
        i=n
        while(True):
            if checkdiv(i):
                break
            i+=1
        return i
            