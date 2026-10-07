class Solution(object):
    def createTargetArray(self, nums, index):
        n = len(nums)
        target = []

        for i in range(n):
            target.insert(index[i], nums[i])

        return target