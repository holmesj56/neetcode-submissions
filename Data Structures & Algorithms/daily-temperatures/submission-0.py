class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        output=[0]*len(temperatures)
        for i,temp in enumerate(temperatures):
            while stack and stack[-1][0]<temp:
                item,ind=stack.pop()
                output[ind]=(i-ind)
            stack.append([temp,i])
        return output
        

            



        