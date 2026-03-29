class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        ans = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    if (
                        r+1 not in range(ROWS) or
                        grid[r+1][c] == 0
                    ):
                        ans += 1 
                    if (
                        r-1 not in range(ROWS) or
                        grid[r-1][c] == 0
                    ):
                        ans += 1 
                    if (
                        c+1 not in range(COLS) or
                        grid[r][c+1] == 0
                    ):
                        ans += 1 
                    if (
                        c-1 not in range(COLS)or 
                        grid[r][c-1] == 0
                    ):
                        ans += 1 
        return ans 
                    