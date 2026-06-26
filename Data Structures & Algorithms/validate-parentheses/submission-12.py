class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i in "{[(":
                stack.append(i)
            else:
                if stack==[]:
                    return False
                if i==']' and stack[-1]=="[":
                    stack.pop()
                elif i==')' and stack[-1]=="(":
                    stack.pop()
                elif i=='}' and stack[-1]=="{":
                    stack.pop()
                else:
                    return False
        return False if stack else True
        


