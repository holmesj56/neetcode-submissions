class Solution:
    def climbStairs(self, n: int) -> int:
        [1,1]
        [1,1,1]
        [1,1,1,1]
        [0,1,2,3,5]
        if n==1:
            return 1
        prev,cur=0,1
        for i in range(1,n):
            prev,cur=cur,max(cur+1,prev+cur)
        return cur


