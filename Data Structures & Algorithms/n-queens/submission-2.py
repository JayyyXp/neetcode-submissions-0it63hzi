class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        col = set()
        posDiag = set()
        negDiag = set()
        board = [['.']*n for i in range(n)]

        ans = []
        def backtrack(r):
            print(board)
            if r == n:
                ans.append(
                    [''.join(row) for row in board]
                )
                return
            for c in range(n):
                
                if (
                    c not in col and
                    (r + c) not in negDiag and
                    (r-c) not in posDiag
                ):
                    board[r][c] = 'Q'

                    col.add(c)
                    negDiag.add(r+c)
                    posDiag.add(r-c)

                    backtrack(r+1)
                    board[r][c] = '.'

                    col.remove(c)
                    negDiag.remove(r+c)
                    posDiag.remove(r-c)
        backtrack(0)
        return ans 