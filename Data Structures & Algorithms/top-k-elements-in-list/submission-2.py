class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for i in nums:
            dic[i]=dic.get(i,0)+1
        maxi=[]
        heapq.heapify(maxi)
        for key,values in dic.items():
            heapq.heappush(maxi,[values,key])
            if len(maxi)>k:
                heapq.heappop(maxi)
        res=[]
        for i,j in maxi:
            res.append(j)
        return res
            