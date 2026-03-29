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
            for dr, dc in [[1,0],[-1,0],[0,1],[0,-1]]:
                if r + dr in range(ROWS) and c + dc in range(COLS):
                    heapq.heappush(
                        l,
                        [max(diff,abs(heights[r+dr][c+dc]- heights[r][c])), [r+dr, c+dc]]
                    )

        