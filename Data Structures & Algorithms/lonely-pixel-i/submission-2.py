class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        
        ROWS = len(picture)
        COLS = len(picture[0])

        rowBlacks = [0]*ROWS
        colBlacks = [0]*COLS
        blacks = []

        for r in range(ROWS):
            for c in range(COLS):
                if picture[r][c] == 'B':
                    rowBlacks[r] += 1 
                    colBlacks[c] += 1 
                    blacks.append([r,c])
        ans = 0 
        for r,c in blacks:
            if rowBlacks[r] == colBlacks[c] == 1:
                ans += 1
        return ans