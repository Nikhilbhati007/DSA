class Solution(object):
    def find132pattern(self, nums):
        #brute force O(n^3)
        '''
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i]<nums[k] and nums[k]<nums[j]:
                        return True
        return False
        '''
        stack = []
        second = float('-inf')

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < second:
                return True

            while stack and nums[i] > stack[-1]:
                second = stack.pop()

            stack.append(nums[i])

        return False