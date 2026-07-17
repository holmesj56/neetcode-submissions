class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        pos=[[i,j] for i ,j in zip(position,speed)]

        for i,j in sorted(pos)[::-1]:
            stack.append((target-i)/j)
            if len(stack)>=2 and stack[-2]>=stack[-1]:
                stack.pop()
        return len(stack)