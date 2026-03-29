class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        # 10 000

        q = deque([[0,0]])
        seen = set([(0,0)])
        d = 0
        drs = [1, -1, 0]
        dcs = [1, -1, 0]
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if grid[r][c] == 1:
                    continue
                if (r,c) == (N-1, N-1):
                    return d+1
                for dr in drs:
                    for dc in dcs:
                        if (dr, dc) == (0,0):
                            continue
                        nr = dr + r
                        nc = dc + c
                        if (
                            0 <= nc < N and
                            0 <= nr < N and
                            (nr, nc) not in seen
                        ):
                            seen.add((nr, nc))
                            q.append([nr, nc])
            d += 1

        return -1
