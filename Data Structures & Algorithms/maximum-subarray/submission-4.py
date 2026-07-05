class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = max(nums)
        cur=0
        for i in range(len(nums)):
            cur=cur+nums[i]
            if cur<0:
                cur=0
            if m>0:
                m=max(m,cur)
        return m
            