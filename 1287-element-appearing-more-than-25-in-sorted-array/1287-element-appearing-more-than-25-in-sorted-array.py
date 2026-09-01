class Solution(object):
    def findSpecialInteger(self, arr):
        n = len(arr)

        for i in range(n):
            if arr[i] == arr[i + n // 4]:
                return arr[i]