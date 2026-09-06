class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal=len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            n=nums[i]
            if i+n>=goal:
                goal=i
        return True if goal==0 else False
        
                    

                



            

            


        