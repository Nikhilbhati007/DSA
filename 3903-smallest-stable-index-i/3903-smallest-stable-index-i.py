class Solution(object):
    def firstStableIndex(self, nums, k):
        # O(n^2)
        '''
        n=len(nums)
        max_so_far=nums[0]
        for i in range(n):
            if max_so_far<nums[i]:
                max_so_far=nums[i]
            min_ele=min(nums[i:n])
            if max_so_far-min_ele<=k:
                return i
        return -1
        '''
        # O(N) solution and Sp-O(N)
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