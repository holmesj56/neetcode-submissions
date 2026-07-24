class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c= Counter(tasks)
        time=0
        maxHeap=[-cnt for cnt in c.values()]
        heapq.heapify(maxHeap)
        q=deque()

        while maxHeap or q:
            time+=1
            if maxHeap:
                current=1+heapq.heappop(maxHeap)
                if current:
                    q.append([current,time+n])
            if q and q[0][1]==time:
                heapq.heappush(maxHeap,q.popleft()[0])
        return time
                
        