class Solution(object):
    def sumAndMultiply(self, n):
        digit_sum=0
        temp=n
        ans=0
        cnt=0
        while temp!=0:
            rem=temp%10
            digit_sum+=rem
            if rem != 0:
                ans+=rem*(10**cnt)
                cnt+=1
            temp=temp//10
        return ans*digit_sum
            
                 
