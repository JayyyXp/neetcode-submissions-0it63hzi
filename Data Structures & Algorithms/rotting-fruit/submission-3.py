class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
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