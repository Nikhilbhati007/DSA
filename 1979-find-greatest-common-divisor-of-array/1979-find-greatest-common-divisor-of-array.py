class Solution(object):
    def findGCD(self, arr):
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a        
        max_ele=max(arr)
        min_ele=min(arr)
        return gcd(min_ele,max_ele)