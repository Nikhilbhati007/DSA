class Solution(object):
    def subArrayRanges(self, nums):
        #for subarry minmun element sum

        def subarr_min(arr):
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
                res = (res + arr[i] * left[i] * right[i])
            
            return res

        
        #for subarry maximun element sum

        def subarr_max(arr):
            n = len(arr)
            #previous greatest element 
            stack = []
            left = [0] * n
            for i in range(n):
                count = 1
                while stack and stack[-1][0] < arr[i]:
                    count += stack.pop()[1]
                stack.append((arr[i], count))
                left[i] = count
            #next greatest element 
            stack = []
            right = [0] * n
            for i in range(n-1, -1, -1):
                count = 1
                while stack and stack[-1][0] <= arr[i]:
                    count += stack.pop()[1]
                stack.append((arr[i], count))
                right[i] = count
            #final traversal
            res = 0
            for i in range(n):
                res = (res + arr[i] * left[i] * right[i])
            
            return res


        #Final answer
        ans=abs(subarr_min(nums)-subarr_max(nums))
        return ans