class Solution(object):
    def gcdSum(self, nums):
        n=len(nums)
        def gcd(a,b):
            while b:
                a, b = b, a % b
            return a
        prefixgcd=[]
        mx=float('-inf')
        for i in range(n):
            mx=max(mx,nums[i])
            prefixgcd.append(gcd(mx,nums[i]))
        prefixgcd.sort()
        i=0
        j=n-1
        gcd_sum=0
        while i<j:
            gcd_sum+=gcd(prefixgcd[i],prefixgcd[j])
            i+=1
            j-=1
        return gcd_sum


