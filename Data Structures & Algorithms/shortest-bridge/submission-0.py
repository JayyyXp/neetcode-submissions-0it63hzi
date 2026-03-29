class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        def dfs(r, c):
            if (
                r not in range(ROWS) or 
                c not in range(COLS) or 
                (r,c) in visited or
                grid[r][c] == 0
            ):
                return 
            visited.add((r,c))
            for dr,dc in [[1,0],[-1,0],[0,1], [0,-1]]:
                dfs(r+dr,c+dc)
        found = False
        for r in range(ROWS):
            if found:
                break
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs(r,c)
                    found = True
                    break
        #print(visited)
        visited2 = set() 
        q = deque(visited)
        d = 0
        while q:
            print(q)
            for _ in range(len(q)):
                r,c = q.popleft()
                if r not in range(ROWS) or c not in range(COLS) or (r,c) in visited2:
                    continue
                if grid[r][c] == 1 and (r,c) not in visited:
                    return d-1
                visited2.add((r,c))
                for dr,dc in [[1,0],[-1,0],[0,1], [0,-1]]:
                    q.append((r+dr,c+dc))
            d += 1