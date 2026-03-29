class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        def rowColZero(r, c):
            for i in range(COLS):
                if matrix[r][i] != 0:
                    matrix[r][i] = "ph"
            for i in range(ROWS):
                if matrix[i][c] != 0:
                    matrix[i][c] = "ph"

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    rowColZero(r, c)
                    
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == "ph":
                    matrix[r][c] = 0
                    