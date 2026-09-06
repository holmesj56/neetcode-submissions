class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp=[0]*len(nums)
        dp[len(nums)-1]=-1
        for i in range(len(nums)-2,-1,-1):
            n=nums[i]
            for j in range(1,n+1):
                if dp[i+j]==-1:
                    dp[i]=-1
                    break
        return True if dp[0]==-1 else  False
        
                    

                



            

            


        