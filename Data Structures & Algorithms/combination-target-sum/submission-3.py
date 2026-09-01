class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def combi(i,cursum,cur):
            if i>=len(nums) or cursum>target:
                return 
            if cursum==target:
                res.append(cur.copy())
                return
            cur.append(nums[i])
            combi(i,cursum+nums[i],cur)
            cur.pop()
            combi(i+1,cursum,cur)
        combi(0,0,[])
        return res