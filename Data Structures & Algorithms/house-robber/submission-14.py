class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        [2,9,8,3,6]
        prev=2,cur=9
        2+8 or 9   10 ,9=> 
        9+3 or 10 
        """
        if len(nums)<3:
            return max(nums)
        prev,cur=nums[0],max(nums[0],nums[1])
        for i in range(2,len(nums)):
            prev,cur= cur,max(cur,prev+nums[i])  
        return cur
