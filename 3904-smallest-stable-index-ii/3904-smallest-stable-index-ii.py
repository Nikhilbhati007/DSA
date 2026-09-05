class Solution(object):
    def firstStableIndex(self, nums, k):
        n=len(nums)
        max_so_far=nums[0]
        suff_min=[0]*n
        for i in range(n-1,-1,-1):
            if i==n-1:
                suff_min[i]=nums[i]
            else:
                suff_min[i]=min(nums[i],suff_min[i+1])
        for i in range(n):
            max_so_far=max(max_so_far,nums[i])
            min_ele=suff_min[i]
            if max_so_far-min_ele<=k:
                return i
        return -1