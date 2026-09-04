class Solution(object):
    def firstStableIndex(self, nums, k):
        n=len(nums)
        max_so_far=nums[0]
        for i in range(n):
            if max_so_far<nums[i]:
                max_so_far=nums[i]
            min_ele=min(nums[i:n])
            if max_so_far-min_ele<=k:
                return i
                break
        return -1
        