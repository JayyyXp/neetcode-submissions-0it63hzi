class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        def traverse(i, j): 
            if (i == -1 or i == ROWS or
                j == -1 or j == COLS or
                (i,j) in visited or
                grid[i][j] == -1
            ): 
                return 2147483647 
            if grid[i][j] == 0:
                return 0
            visited.add((i,j))
            res = min(
                traverse(i+1, j) + 1,
                traverse(i-1, j) + 1,
                traverse(i, j+1) + 1,
                traverse(i, j-1) + 1,
                2147483647
            )
            visited.remove((i,j))
            return res
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647

        def bfs(r, c):
            q = deque([(r, c)])
            visit = [[False] * COLS for _ in range(ROWS)]
            visit[r][c] = True
            steps = 0
            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    if grid[row][col] == 0:
                        return steps
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if (0 <= nr < ROWS and 0 <= nc < COLS and 
                            not visit[nr][nc] and grid[nr][nc] != -1
                        ):
                            visit[nr][nc] = True
                            q.append((nr, nc))
                steps += 1
            return INF
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2147483647:
                    grid[i][j] = bfs(i,j)#traverse(i, j)



