class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited_nodes = [set()]
        ROWS = len(grid)
        COLS = len(grid[0])

        def island_search(r, c):
            print(r,c)
            if r < 0 or c < 0 or r == ROWS or c == COLS:
                return
            if grid[r][c] == '0':
                return
            if (r,c) in visited_nodes[0]:
                return 
            visited_nodes[0].add((r,c))
            island_search(r+1, c)
            island_search(r-1, c)
            island_search(r, c+1)
            island_search(r, c-1)

        ans = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and ((r,c) not in visited_nodes[0]):
                    print(visited_nodes[0])
                    island_search(r, c)
                    ans += 1

        return ans