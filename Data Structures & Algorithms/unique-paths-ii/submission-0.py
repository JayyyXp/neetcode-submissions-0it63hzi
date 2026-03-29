class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1:
            return 0

        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])
        memo = {}
        def dfs(i,j):
            if (i == ROWS-1) and (j == COLS - 1):
                return 1
            if i == ROWS or j == COLS:
                return 0
            if obstacleGrid[i][j] == 1:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            ret = 0
            ret += dfs(i+1, j)
            ret += dfs(i, j+1)
            memo[(i,j)] = ret
            return ret
        return dfs(0,0)