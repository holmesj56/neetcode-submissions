class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited=set()
        def dfs(i,j,pos):
            if pos==len(word):
                return True
            if (i,j) in visited or  i>=len(board) or j>=len(board[0]) or i<0 or j<0:
                return False
            if board[i][j]!=word[pos]:
                return False
            visited.add((i,j))

            
            res= (dfs(i+1,j,pos+1) or dfs(i,j+1,pos+1) or dfs(i-1,j,pos+1) or dfs(i,j-1,pos+1))
            visited.remove((i,j))
            return res
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0):
                    visited.add((i,j))
                    return True
        return False