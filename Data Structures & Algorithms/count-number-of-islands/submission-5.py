class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return  0

        visited=set()

        def dfs(i,j):
            if (i,j) in visited or i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]=='0':
                return 0
            
            visited.add((i,j))
            dfs(i+1,j) 
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)
        res=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1' and (i,j) not in visited:
                    dfs(i,j)
                    res+=1
        return res

            