class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        def dfs(r,c):
            if r not in range(ROWS) or c not in range(COLS):
                return float("inf")
            if (r,c) in visited:
                return 0
            if grid[r][c] == 0:
                return 0
            visited.add((r,c))
            ret = 1
            ret += dfs(r+1,c) 
            ret += dfs(r-1,c) 
            ret += dfs(r,c+1) 
            ret += dfs(r,c-1)

            return ret 
        ans = 0
        for r in range(1, ROWS-1):
            for c in range(1, COLS-1):
                if grid[r][c] == 1:
                    ret = dfs(r,c)
                    if ret != float("inf"):
                        ans += ret
        return ans