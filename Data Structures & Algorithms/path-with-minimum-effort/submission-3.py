class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS = len(heights)
        COLS = len(heights[0])
        l = [[0, [0,0]]]
        heapq.heapify(l)
        visited = set()
        while True:
            diff, (r, c) = heapq.heappop(l)
            if (r,c) in visited:
                continue
            visited.add((r,c))
            if r == ROWS-1 and c == COLS-1:
                return diff
            if r + 1 in range(ROWS):
                heapq.heappush(
                    l,
                    [max(diff,abs(heights[r+1][c]- heights[r][c])), [r+1, c]]
                )
            if r - 1 in range(ROWS):
                heapq.heappush(
                    l,
                    [max(diff,abs(heights[r-1][c] - heights[r][c])), [r-1, c]]
                )
            if c + 1 in range(COLS):
                heapq.heappush(
                    l,
                    [max(diff,abs(heights[r][c+1]- heights[r][c])), [r, c+1]]
                )
            if c - 1 in range(COLS):
                heapq.heappush(
                    l,
                    [max(diff,abs(heights[r][c-1]- heights[r][c])), [r, c-1]]
                )
                
        