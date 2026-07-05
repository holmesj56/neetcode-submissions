class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0 for _ in range(n)] for _ in range(m)]
        self.res=0
        def dfs(i,j):
            if i>=m or j>=n:
                return 0
            if (i,j)==(m-1,n-1):
                return 1
                
            if dp[i][j]!=0:
                return dp[i][j]
            dp[i][j]=dfs(i+1,j)+dfs(i,j+1)
            return dp[i][j]
        return dfs(0,0)
                
            