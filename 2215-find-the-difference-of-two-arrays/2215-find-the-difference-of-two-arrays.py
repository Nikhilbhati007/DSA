class Solution(object):
    def findDifference(self, nums1, nums2):
        ans=[]
        out1=[]
        out2=[]
        for i in nums1:
            if i not in nums2 and i not in out1:
                out1.append(i)
        for i in nums2:
            if i not in nums1 and i not in out2:
                out2.append(i)
        ans.append(out1)
        ans.append(out2)
        return ans      
        