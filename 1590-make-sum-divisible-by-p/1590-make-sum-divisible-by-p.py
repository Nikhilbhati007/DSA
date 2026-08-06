class Solution(object):
    def minSubarray(self, nums, p):
        total = sum(nums)
        rem = total % p
        if rem == 0:
            return 0
        n = len(nums)
        mp = {0: -1}
        prefix = 0
        ans = n
        for i in range(n):
            prefix = (prefix + nums[i]) % p
            target = (prefix - rem + p) % p

            if target in mp:
                ans = min(ans, i - mp[target])
            mp[prefix] = i
        return ans if ans < n else -1