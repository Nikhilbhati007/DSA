class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        # Step 1: Assign component IDs
        comp = [0] * n
        comp_id = 0
        comp[0] = comp_id
        
        for i in range(1, n):
            if nums[i] - nums[i-1] <= maxDiff:
                comp[i] = comp_id
            else:
                comp_id += 1
                comp[i] = comp_id
        
        # Step 2: Answer queries
        ans = []
        for u, v in queries:
            ans.append(comp[u] == comp[v])
        
        return ans
