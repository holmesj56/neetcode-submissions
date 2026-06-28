class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visited=set()
        res=0
        def dfs(i,j):
            if i>=len(grid) or j>=len(grid[0]) or i<0 or j<0 or grid[i][j]=='0' or (i,j) in visited:
                return
            
            visited.add((i,j))
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)
        for a in range(len(grid)):
            for b in range(len(grid[0])):
                if (a,b) not in visited and grid[a][b]=='1':
                    
                    dfs(a,b)
                    res+=1
        return res

                
                    
                

