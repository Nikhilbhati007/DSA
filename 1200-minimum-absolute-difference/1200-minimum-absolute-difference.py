class Solution(object):
    def minimumAbsDifference(self, arr):
        n=len(arr)
        arr.sort()
        res=[]
        diff=float('inf')
        for i in range(1,n):
            diff=min(diff,arr[i]-arr[i-1])
        for j in range(1,n):
            if arr[j] - arr[j-1] == diff:
                res.append([arr[j-1], arr[j]])
               
        return res