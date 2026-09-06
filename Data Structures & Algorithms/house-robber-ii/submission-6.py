class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<2:
            return max(nums)
        prev,cur=nums[0],max(nums[0],nums[1])
        for i in range(2,len(nums)-1):
            prev,cur= cur,max(cur,prev+nums[i])
        prev1,cur1=nums[-1],max(nums[-1],nums[-2])
        for i in range(len(nums)-3,0,-1):
            prev1,cur1= cur1,max(cur1,prev1+nums[i])
        return max(cur,cur1)