class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        comm = set()
        for r in range(ROWS):
            l = []
            for c in range(COLS):
                if grid[r][c] == 1:
                    l.append((r,c))
            if len(l) > 1:
                for s in l:
                    comm.add(s)
        for c in range(COLS):
            l = []
            for r in range(ROWS):
                if grid[r][c] == 1:
                    l.append((r,c))
            if len(l) > 1:
                for s in l:
                    comm.add(s)
        return len(comm)