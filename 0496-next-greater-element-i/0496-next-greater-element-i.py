class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        n=len(nums2)
        res=[]
        freq={}
        for i in range(n):
            freq[nums2[i]]=i
        for i in nums1:
            j=freq[i]
            while j<n:
                if nums2[j]>i:
                    break
                j+=1
            if j==n:
                res.append(-1)
            else:
                res.append(nums2[j])
        return res


        
        