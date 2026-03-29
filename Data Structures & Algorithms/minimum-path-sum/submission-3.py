class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        memo = {}
        def dfs(r,c):
            if r == ROWS-1 and c == COLS-1:
                return grid[r][c]
            if (r,c) in memo:
                return memo[(r,c)]
            l = []
            if (r + 1) < ROWS:
                l.append(dfs(r+1, c))
            if (c + 1) < COLS:
                l.append(dfs(r, c+1))
            ret = grid[r][c] + min(l)
            memo[(r,c)] = ret
            return ret

        return dfs(0,0)