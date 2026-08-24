class Solution(object):
    def isBalanced(self, num):
        n=len(num)
        odd_sum=0
        even_sum=0
        for i in range(n):
            if i%2==0:
                even_sum+=int(num[i])
            else:
                odd_sum+=int(num[i])
        if even_sum==odd_sum:
            return True
        else:
            return False