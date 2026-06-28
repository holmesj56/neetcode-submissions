class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        start=0
        r,c=len(board),len(board[0])
        w=len(word)
        path=set()
        def dfs(start,row,col):
            if start==len(word):
                    return True
            if row<0 or col<0 or row>=r or col>=c or start>=w or board[row][col]!=word[start] or (row,col) in path:
                return False
            path.add((row,col))
            res=(dfs(start + 1, row + 1, col) or 
                   dfs(start + 1, row - 1, col) or 
                   dfs(start + 1, row, col + 1) or 
                   dfs(start + 1, row, col - 1))
            path.remove((row,col))
            return res
        for i in range(r):
            for j in range(c):
                if dfs(0,i,j):
                    return True
        return  False
