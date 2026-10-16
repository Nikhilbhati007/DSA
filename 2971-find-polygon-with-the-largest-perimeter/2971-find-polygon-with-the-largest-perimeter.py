class Solution(object):
    def largestPerimeter(self, nums):
        n=len(nums)
        nums.sort()
        total=sum(nums)
        for i in range(n-1,1,-1):
            if total-nums[i]>nums[i]:
                return total
            total-=nums[i]
        return -1

        