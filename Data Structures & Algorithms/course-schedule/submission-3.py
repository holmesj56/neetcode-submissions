class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic={i:[] for i in range(numCourses)}
        curr=set()
        for crs,pre in prerequisites:
            dic[crs].append(pre)
        visited=set()
        def dfs(cur):
            if cur in visited:
                return False
            if dic[cur]==[]:
                return True
            visited.add(cur)
            for i in dic[cur]:
                if not dfs(i): 
                    return False
            visited.remove(cur)
            dic[cur]=[]
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
                
            
                

        
        
                
            