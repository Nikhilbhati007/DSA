class Solution(object):
    def minSwaps(self, nums):
        n=len(nums)
        def sumdig(n):
            return sum(int(digit) for digit in str(n))
        # array ko sort karna hai on the basis of dig_sum and then num itself
        sort_nums=sorted(nums,key=lambda x:(sumdig(x),x))
        #cycle detection
        mp={}
        for i in range(n):
            mp[sort_nums[i]]=i
        targ_arr=[]
        for i in range(n):
            targ_arr.append(mp[nums[i]])
        visited = [False] * n 
        ans = 0 
        for i in range(n): 
            if visited[i] or targ_arr[i] == i: 
                continue 
            cycle = 0 
            j = i 
            while not visited[j]: 
                visited[j] = True 
                cycle += 1 
                j = targ_arr[j] 
            ans += cycle - 1 
        return ans


