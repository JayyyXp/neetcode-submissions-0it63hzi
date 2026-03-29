class Solution:
    def totalNQueens(self, n: int) -> int:
        
        col = set()
        posDiag = set()
        negDiag = set()
        #board = [[0]*n for i in range(n)]
        ans = [0]
        def backtrack(r):
            if r == n:
                ans[0] += 1
                return
            for c in range(n):
                if (
                    c not in col and 
                    (r-c) not in posDiag and 
                    (r+c) not in negDiag 
                ):
                    col.add(c)
                    posDiag.add((r-c))
                    negDiag.add((r+c))
                    #board[r][c] = 1
                    backtrack(r+1)
                    col.remove(c)
                    posDiag.remove((r-c))
                    negDiag.remove((r+c))

        backtrack(0)
        return ans[0]