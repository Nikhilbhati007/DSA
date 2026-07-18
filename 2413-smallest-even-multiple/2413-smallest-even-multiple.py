class Solution(object):
    def smallestEvenMultiple(self, n):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return (a * b) // gcd(a, b)
        return lcm(2,n)