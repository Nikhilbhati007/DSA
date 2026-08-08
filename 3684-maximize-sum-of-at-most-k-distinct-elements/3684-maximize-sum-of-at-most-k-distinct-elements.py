class Solution(object):
    def maxKDistinct(self, nums, k):
        n=len(nums)
        st=set()
        out=[]
        nums.sort(reverse=True)
        for i in range(n):
            if k==0:
                break
            if nums[i] not in st:
                out.append(nums[i])
                st.add(nums[i])
                k-=1
        return out                
