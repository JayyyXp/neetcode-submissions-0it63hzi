class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        houses = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    houses += 1
        print(houses)
        dist = [[0]*COLS for _ in range(ROWS)]
        times_visited = [[0]*COLS for _ in range(ROWS)]
        def bfs(r,c):
            q = deque([[r,c,0]]) 

            visited = set()
            while q:
                for _ in range(len(q)):
                    r,c,d = q.popleft()
                    if grid[r][c] == 0:
                        dist[r][c] += d
                        times_visited [r][c] += 1
                    for dr, dc in [[1,0], [-1,0], [0,1], [0,-1]]:
                        if (
                            r + dr in range(ROWS) and
                            c + dc in range(COLS) and
                            (r + dr, c + dc) not in visited and
                            grid[r + dr][c + dc] != 2 and 
                            grid[r + dr][c + dc] != 1
                        ): 
                            visited.add((r + dr,c + dc))
                            q.append([r + dr, c + dc, d + 1])

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    bfs(r,c)
        ans = float('inf')
        for r in range(ROWS):
            for c in range(COLS):
                if times_visited[r][c] == houses:
                    ans = min(ans,dist[r][c])
        if ans == float('inf'):
            return -1
        return ans
