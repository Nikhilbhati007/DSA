class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        def subarray(nums,k):
            n=len(nums)
            freq={}
            l,r=0,0
            cnt=0
            while r<n:
                freq[nums[r]]=freq.get(nums[r],0)+1
                while len(freq)>k:
                    freq[nums[l]]-=1
                    if freq[nums[l]]==0:
                        del freq[nums[l]]
                    l+=1
                cnt+=r-l+1
                r+=1
            return cnt
        ans=subarray(nums,k)-subarray(nums,k-1)
        return ans