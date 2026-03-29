class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS = len(matrix)
        COLS = len(matrix[0])
        self.movingSum = [[0]*(COLS) for i in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                prev = 0
                if r > 0 and c > 0:
                    prev -= self.movingSum[r-1][c-1]
                if r > 0:
                    prev += self.movingSum[r-1][c]
                if c > 0:
                    prev += self.movingSum[r][c-1]
                self.movingSum[r][c] = matrix[r][c] + prev  

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.movingSum[row2][col2]
        if row1 > 0:
            ans -= self.movingSum[row1-1][col2]
        if col1 > 0:
            ans -= self.movingSum[row2][col1-1]
        if col1 > 0 and row1 > 0:
            ans += self.movingSum[row1-1][col1-1]
        return ans 


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)