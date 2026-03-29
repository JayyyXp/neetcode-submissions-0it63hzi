class Solution:
    def dfs(self, grid):
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()
        cache = {}
        def distToRotten(r, c):
            if (
                r == -1 or r == ROWS or
                c == -1 or c == COLS or 
                (r,c) in visited or
                grid[r][c] == 0
                ):
                return float('inf')
            if grid[r][c] == 2:
                return 0
            #if (r,c) in cache:
            #    return cache[(r,c)]
            visited.add((r,c))
            ret = min(
                distToRotten(r+1, c),
                distToRotten(r-1, c),
                distToRotten(r, c+1),
                distToRotten(r, c-1)
            ) + 1
            visited.remove((r,c))
            cache[(r,c)] = ret
            return ret

        ans = 0
        for r in range(ROWS): 
            for c in range(COLS):
                if grid[r][c] == 1:
                    ans = max(
                        ans,
                        distToRotten(r,c)
                    )
        return ans if ans != float('inf') else -1 

    def bfs(self, grid):
        ROWS = len(grid)
        COLS = len(grid[0])

        rotten = collections.deque()
        fresh = 0
        for r in range(ROWS): 
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotten.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        time = 0
        while len(rotten) != 0 and fresh > 0:

            # go through all the rotten oranges
            for i in range(len(rotten)):
                r, c = rotten.popleft()
                
                if r + 1 < ROWS:
                    if grid[r+1][c] == 1:
                        grid[r+1][c] = 2
                        rotten.append((r+1,c))
                        fresh -= 1
                if r - 1 >= 0:
                    if grid[r-1][c] == 1:
                        grid[r-1][c] = 2
                        rotten.append((r-1,c))
                        fresh -= 1
                if c + 1 < COLS:
                    if grid[r][c+1] == 1:
                        grid[r][c+1] = 2
                        rotten.append((r,c+1))
                        fresh -= 1
                if c - 1 >= 0:
                    if grid[r][c-1] == 1:
                        grid[r][c-1] = 2
                        rotten.append((r,c-1))
                        fresh -= 1
            time += 1            

        return -1 if fresh > 0 else time 

    def orangesRotting(self, grid: List[List[int]]) -> int:
        #return self.dfs(grid)
        return self.bfs(grid)
