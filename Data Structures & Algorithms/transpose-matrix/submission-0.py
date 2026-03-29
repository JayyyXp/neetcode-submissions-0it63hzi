class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        matrixNew = [[0]*ROWS for _ in range(COLS)]
        for i in range(ROWS):
            for j in range(COLS):
                matrixNew[j][i] = matrix[i][j]
        return matrixNew