class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue=deque()
        row,col=len(grid),len(grid[0])
        visited=set()
        visited.add((0,0))
        queue.append((0,0))
        lenght=1
        while queue:
            for i in range(len(queue)):
                l,r=queue.popleft()
                if grid[l][r]==1:
                    continue
                if (l,r)==(row-1,col-1):
                    return lenght
                nei=([0,1],[1,0],[1,1],[-1,0],[0,-1])
                for [dl,dr] in nei:
                    if (dl+l)>=row or (dr+r)>=col or (dl+l)<0 or (dr+r)<0 or grid[dl+l][dr+r]==1 or (dl+l,dr+r) in visited:
                        continue
                    visited.add((dl+l,dr+r))
                    queue.append((dl+l,dr+r))
            lenght+=1
        return lenght if (row-1,col-1) in visited else -1
                    
                     


        