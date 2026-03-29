class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        heap = [[grid[0][0], [0, 0]]]
        heapq.heapify(heap)
        ans = 0
        visited = set()
        while heap:
            
            #heapLen = len(heap)
            #for i in range(heapLen):
            currVal, (r, c) = heapq.heappop(heap)
            if (r,c) in visited:
                continue
            visited.add((r,c))
            ans = max(ans, currVal)
            if r == ROWS-1 and c == COLS-1:
                return ans 
            if (c+1) in range(COLS):
                heapq.heappush(heap, [grid[r][c+1], [r, c+1]])
            if (c-1) in range(COLS):
                heapq.heappush(heap, [grid[r][c-1], [r, c-1]])
            if (r+1) in range(ROWS):
                heapq.heappush(heap, [grid[r+1][c], [r+1, c]])
            if (r-1) in range(ROWS):
                heapq.heappush(heap, [grid[r-1][c], [r-1, c]])