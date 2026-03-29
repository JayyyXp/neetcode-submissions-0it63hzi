class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        self.maxLenght = 0
        dp = {}
        def dfs(r, c, prevVal):
            if (
                r not in range(ROWS) or
                c not in range(COLS) or
                matrix[r][c] <= prevVal
            ):
                #self.maxLenght = max(self.maxLenght, lenght)
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            res = max(
                1,
                dfs(r+1,c,matrix[r][c])+1,
                dfs(r-1,c,matrix[r][c])+1,
                dfs(r,c+1,matrix[r][c])+1,
                dfs(r,c-1,matrix[r][c])+1
            )
            dp[(r, c)] = res
            return res
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(dfs(r,c, -1), res)
        return res