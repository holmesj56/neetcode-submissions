class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.total=[]
        def combi(i,curr,s):
            if i>=len(nums) or s>target:
                return
            if s==target:
                self.total.append(curr.copy())
                return

            curr.append(nums[i])    
            combi(i,curr,s+nums[i])
            curr.pop()
            combi(i+1,curr,s)
        combi(0,[],0)
        return self.total

            
