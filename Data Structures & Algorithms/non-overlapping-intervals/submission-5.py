class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        res=0
        output=[]
        output.append(intervals[0])
        for i in range(1,len(intervals)):
            if intervals[i][0]<output[-1][1]:
                res+=1
                if intervals[i][1]<output[-1][1]:
                    output[-1]=intervals[i]
            else:
                output.append(intervals[i])

        return res