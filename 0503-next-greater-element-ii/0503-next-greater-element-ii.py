
class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        maxele = max(nums)
        res = []
        for i in range(n):
            if nums[i] == maxele:
                res.append(-1)
                continue
            k = (i + 1) % n
            count = 0
            while count < n - 1:
                if nums[k] > nums[i]:
                    res.append(nums[k])
                    break

                k = (k + 1) % n
                count += 1
            else:
                res.append(-1)

        return res