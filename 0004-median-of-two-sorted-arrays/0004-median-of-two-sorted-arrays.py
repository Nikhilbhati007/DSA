class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        L=nums1 + nums2
        L.sort()
        n=len(L)
        print(L)
        if n%2==0:
            k=n/2
            sum=L[k-1]+L[k]
            sum=float(sum)
            median=(sum)/2
        else:
            k=(n+1)/2
            median=(L[k-1])
        return median
        