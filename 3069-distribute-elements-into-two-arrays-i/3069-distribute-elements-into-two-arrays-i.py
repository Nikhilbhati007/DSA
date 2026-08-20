class Solution(object):
    def resultArray(self, nums):
        n=len(nums)
        arr1=[]
        arr2=[]
        for i in range(n):
            if i>1:
                if arr1[-1]>arr2[-1]:
                    arr1.append(nums[i])
                else:
                    arr2.append(nums[i])
            else:
                if i==0:
                    arr1.append(nums[i])
                else:
                    arr2.append(nums[i])
        return arr1+arr2
