class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[]
        suf=collections.deque()
        preprod=1
        sufprod=1
        j=len(nums)-1
        for i in range(len(nums)):
            if i==0:
                pre.append(1)
                preprod*=nums[i]
                suf.appendleft(1)
                sufprod*=nums[j-i]
            else:
                pre.append(preprod)
                preprod*=nums[i]
                suf.appendleft(sufprod)
                sufprod*=nums[j-i]
        for i in range(len(nums)):
            pre[i]=pre[i]*suf[i]
        return pre
            
