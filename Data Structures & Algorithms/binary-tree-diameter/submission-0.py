# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result=0
        def dfs(cur):
            if not cur:
                return 0
            self.result=max(self.result,dfs(cur.left)+dfs(cur.right))    
            
            return 1+max(dfs(cur.left),dfs(cur.right))
        dfs(root)
        return self.result

