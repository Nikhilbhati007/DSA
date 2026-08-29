class Solution(object):
    def matrixReshape(self, mat, r, c):
        n=len(mat)
        m=len(mat[0])
        if m*n != r*c:
            return mat
        new_mat=[[0]*c for i in range(r)]
        arr=[]
        for i in range(n):
            for j in range(m):
                arr.append(mat[i][j])
        i=0
        for k in range(r):
            for l in range(c):
                new_mat[k][l]=arr[i]
                i+=1
        return new_mat

            
