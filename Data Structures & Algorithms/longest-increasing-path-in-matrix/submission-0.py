class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        self.maxLenght = 0

        def dfs(r, c, prevVal, lenght):
            if (
                r not in range(ROWS) or
                c not in range(COLS) or
                matrix[r][c] <= prevVal
            ):
                self.maxLenght = max(self.maxLenght, lenght)
                return


            dfs(r+1,c,matrix[r][c], lenght+1) 
            dfs(r-1,c,matrix[r][c], lenght+1) 
            dfs(r,c+1,matrix[r][c], lenght+1) 
            dfs(r,c-1,matrix[r][c], lenght+1) 

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c, -1, 0)
        return self.maxLenght