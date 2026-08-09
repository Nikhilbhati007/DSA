class Solution(object):
    def numberOfSubarrays(self, nums, k):
        bin_arr=[]
        for i in nums:
            if i%2==0:
                bin_arr.append(0)
            else:
                bin_arr.append(1)
        def binary_sum(nums,k):
            if k<0:
                return 0
            n=len(nums)
            l,r,cnt,bsum=0,0,0,0
            while(r<n):
                bsum+=nums[r]
                while bsum>k:
                    bsum-=nums[l]
                    l+=1
                cnt+=r-l+1
                r+=1
            return cnt
        ans=binary_sum(bin_arr,k)-binary_sum(bin_arr,k-1)
        return ans