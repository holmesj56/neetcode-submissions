from functools import cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        i,j=0,0
        self.res=0
        self.dp = [[-1] * len(text2) for _ in range(len(text1))]
        def dfs(i,j):
            if i>=len(text1) or j>=len(text2) :
                
                return 0
            if self.dp[i][j] != -1:
                return self.dp[i][j]
            if text1[i]==text2[j]:
                
                self.dp[i][j]=1+dfs(i+1,j+1)
            else:
                self.dp[i][j]= max(dfs(i+1,j) , dfs(i,j+1))
            return self.dp[i][j]
        
        return dfs(0,0)
            