
class Solution(object):
    def getPermutation(self, n, k):
        nums = [str(i) for i in range(1, n + 1)]

        fact = [1] * n
        for i in range(1, n):
            fact[i] = fact[i - 1] * i

        k -= 1

        def solve(nums, k, n):
            if n == 0:
                return ""

            index = k // fact[n - 1]
            digit = nums.pop(index)
            k %= fact[n - 1]

            return digit + solve(nums, k, n - 1)

        return solve(nums, k, n)
