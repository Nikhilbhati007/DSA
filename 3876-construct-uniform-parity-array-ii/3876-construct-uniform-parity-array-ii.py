class Solution(object):
    def uniformArray(self, nums1):
        n=len(nums1)
        cnt_even=0
        cnt_odd=0
        for i in nums1:
            if i%2==0:
                cnt_even+=1
            else:
                cnt_odd+=1
        if cnt_even==0 or cnt_odd==0:
            return True
        return min(nums1)%2==1