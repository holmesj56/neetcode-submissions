class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac_rech=set()
        visited=set()
        output=[]
        def flow(i,j,osc):
            nei=[(1,0),(0,-1),(-1,0),(0,1)]
            for a,b in nei:
                if i+a>=len(heights) or i+a<0 or j+b>=len(heights[0]) or j+b<0 or (i+a,j+b) in osc or heights[i][j]>heights[i+a][j+b]:
                    continue
                osc.add((i+a,j+b))
                flow(i+a,j+b,osc)

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i>0 and j>0:
                    continue
                
                if not (i,j) in pac_rech:
                    pac_rech.add((i,j))
                    flow(i,j,pac_rech)
        for i in range(len(heights)-1,-1,-1):
            for j in range(len(heights[0])-1,-1,-1):
                if i<len(heights)-1 and j<len(heights[0])-1:
                    continue
                
                if not (i,j) in visited:
                    visited.add((i,j))
                    flow(i,j,visited)
        for (i,j) in visited:
            if (i,j) in pac_rech:
                output.append((i,j))
        return output

        