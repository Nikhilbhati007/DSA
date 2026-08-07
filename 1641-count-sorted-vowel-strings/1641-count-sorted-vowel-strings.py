class Solution(object):
    def countVowelStrings(self, n):
        dp=[[0]*5 for _ in range(n+1)]
        for i in range(5):
            dp[1][i]+=1
        for i in range(2,n+1):
            for j in range(5):
                dp[i][j]=sum(dp[i-1][j:5])
        return sum(dp[n][0:5])

