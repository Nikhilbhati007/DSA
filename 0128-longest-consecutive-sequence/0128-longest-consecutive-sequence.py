class Solution(object):
    def longestConsecutive(self, nums):
        st=set()
        for i in nums:
            st.add(i)
        maxlength=0
        for i in st:
            if (i-1) not in st:
                currnum=i
                currlength=1
                while (currnum+ 1) in st:
                    currnum+=1
                    currlength+=1
                maxlength=max(maxlength,currlength)
        return maxlength
                
        