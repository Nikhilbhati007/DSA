class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        if arr[0]!=1 and 1 in arr:
            arr.sort()
        if arr[0]!=1 :
            arr[0]=1
        for i in range(1,len(arr)):
            if abs(arr[i-1] -arr[i])>1:
                arr[i]=arr[i-1]+1
        return max(arr)

        