class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        ans = 0
        visited = set()
        def islandCheck(i, j):
            if ((i, j) in visited or
                i < 0 or i == ROWS or
                j < 0 or j == COLS or
                grid[i][j] == 0):
                return 0
            visited.add((i,j))
            return (islandCheck(i+1, j) +
                islandCheck(i-1, j) +
                islandCheck(i, j-1) +
                islandCheck(i, j+1) +
                1)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    ans = max(ans, islandCheck(i, j))
        return ans