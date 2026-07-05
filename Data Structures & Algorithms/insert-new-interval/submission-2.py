class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l,r= newInterval[0],newInterval[1]
        
        included=[]
        for inter in intervals:
            if (l>=inter[0] and l<=inter[1]) or (r<=inter[1] and r>=inter[0]
                or l<=inter[0] and r>=inter[1]) or (r>=inter[1] and l<=inter[0] ):
                l=min(l,inter[0])
                r=max(r,inter[1])
                
            else:
                included.append(inter)
        included.append([l,r])
        included.sort()
        return included
                

