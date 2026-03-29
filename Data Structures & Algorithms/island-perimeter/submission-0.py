class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()
        def dfs(r,c):
            if (r,c) in visited:
                return 0
            if (
                r not in range(ROWS) or
                c not in range(COLS) or
                grid[r][c] == 0
            ): 
                return 1
            visited.add((r,c))
            return (
                dfs(r+1,c)+
                dfs(r-1,c)+
                dfs(r,c+1)+
                dfs(r,c-1)
            )

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return dfs(r,c)