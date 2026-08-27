class Solution(object):
    def sumSubarrayMins(self, arr):
        mod = 10**9 + 7
        n = len(arr)
        #previous smallest element 
        stack = []
        left = [0] * n
        for i in range(n):
            count = 1
            while stack and stack[-1][0] > arr[i]:
                count += stack.pop()[1]
            stack.append((arr[i], count))
            left[i] = count
        #next smallest element 
        stack = []
        right = [0] * n
        for i in range(n-1, -1, -1):
            count = 1
            while stack and stack[-1][0] >= arr[i]:
                count += stack.pop()[1]
            stack.append((arr[i], count))
            right[i] = count
        #final traversal
        res = 0
        for i in range(n):
            res = (res + arr[i] * left[i] * right[i]) % mod
        
        return res