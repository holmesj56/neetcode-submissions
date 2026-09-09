class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c=Counter(tasks)
        arr=[-cnt for cnt in c.values()]

        heapq.heapify(arr)

        q=deque()
        time=0
        while arr or q:
            time+=1
            if arr:
                l=heapq.heappop(arr)+1
                if l:
                    q.append([l,time+n])
            if q and q[0][1]==time:
                heapq.heappush(arr,q.popleft()[0])
        return time
        



                
        