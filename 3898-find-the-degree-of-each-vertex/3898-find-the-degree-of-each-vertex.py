class Solution(object):
    def findDegrees(self, matrix):
        n=len(matrix)
        res=[]
        for i in range(n):
            cnt=0
            cnt=matrix[i].count(1)
            res.append(cnt)
        return res
            
        